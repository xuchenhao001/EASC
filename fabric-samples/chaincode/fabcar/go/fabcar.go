package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"github.com/hyperledger/fabric-contract-api-go/contractapi"
	"math"
	"net/http"
	"os"
	"strconv"
	"strings"
)

const url = "http://172.17.0.1:8888/messages"
var myuuid string
var userNum int
var negotiateRound = 10

type SmartContract struct {
	contractapi.Contract
}

type HttpMessage struct {
	Message string `json:"message"`
	Data interface{} `json:"data"`
	Uuid string `json:"uuid"`
	Epochs int `json:"epochs"`
}

type HttpAccAlphaMessage struct {
	Message string `json:"message"`
	Data AccAlpha `json:"data"`
	Uuid string `json:"uuid"`
	Epochs int `json:"epochs"`
}

type AccAlpha struct {
	AccTest []float64 `json:"acc_test"`
	Alpha []float64 `json:"alpha"`
}

type OutliersMap struct {
	OutlierIds []int `json:"outlier_ids"`
}

func (s *SmartContract) InitLedger(ctx contractapi.TransactionContextInterface) error {
	// generate a new uuid for each user
	var localMSPID string = os.Getenv("CORE_PEER_LOCALMSPID")
	println("LOCALMSPID: " + localMSPID)
	myuuid = strings.Trim(localMSPID, "OrgMSP")
	println("Init finished. My uuid: " + myuuid)
	return nil
}

// STEP #2
func (s *SmartContract) Prepare(ctx contractapi.TransactionContextInterface, receiveMsg string) error {
	fmt.Println("[PREPARE MSG] Received")
	receiveMsgBytes := []byte(receiveMsg)

	recMsg := new(HttpMessage)
	_ = json.Unmarshal(receiveMsgBytes, recMsg)

	// unmarshal to read user number
	dataMap := make(map[string]interface{})
	dataJson, err := json.Marshal(recMsg.Data)
	if err != nil {
		return fmt.Errorf("failed to marshal recMsg.Data interface: %s", err.Error())
	}
	err = json.Unmarshal(dataJson, &dataMap)
	if err != nil {
		return fmt.Errorf("failed to unmarshal dataJson to dataMap: %s", err.Error())
	}
	userNum = int(dataMap["user_number"].(float64))
	fmt.Println("Successfully loaded user number: ", userNum)

	recMsg.Uuid = myuuid
	sendMsgAsBytes, _ := json.Marshal(recMsg)

	go sendPostRequest(sendMsgAsBytes, "PREPARE")

	return nil
}

func saveAsMap(ctx contractapi.TransactionContextInterface, keyType string, epochs int, myUUID string,
	value interface{}) error {
	epochsString := strconv.Itoa(epochs)
	fmt.Println("save [" + keyType + "] map to DB in epoch [" + epochsString  + "] for uuid: [" + myUUID + "]")

	key, err := ctx.GetStub().CreateCompositeKey(keyType, []string{epochsString, myUUID})
	if err !=nil {
		return fmt.Errorf("failed to composite key: %s", err.Error())
	}

	jsonAsBytes, _ := json.Marshal(value)
	err = ctx.GetStub().PutState(key, jsonAsBytes)
	if err != nil {
		return fmt.Errorf("failed to save map into state: %s", err.Error())
	}
	return nil
}

func readAsMap(ctx contractapi.TransactionContextInterface,
	keyType string, epochs int) (map[string]interface{}, error) {

	epochsString := strconv.Itoa(epochs)
	fmt.Println("read [" + keyType + "] map from DB in epoch [" + epochsString  + "]")

	mapIter, err := ctx.GetStub().GetStateByPartialCompositeKey(keyType, []string{epochsString})
	if err != nil {
		return nil, fmt.Errorf("failed to read map from state by partial composite key: %s", err.Error())
	}
	defer mapIter.Close()

	resultMap := make(map[string]interface{})

	for mapIter.HasNext() {
		mapItem, err := mapIter.Next()
		if err != nil {
			return nil, fmt.Errorf("failed to read next map item from state: %s", err.Error())
		}

		var compositeKeyAttri []string
		_, compositeKeyAttri, err = ctx.GetStub().SplitCompositeKey(mapItem.Key)
		if err != nil {
			return nil, fmt.Errorf("failed to split composite key: %s", err.Error())
		}
		var myUUID string
		myUUID = compositeKeyAttri[1]
		valueMap := make(map[string]interface{})
		_ = json.Unmarshal(mapItem.Value, &valueMap)
		resultMap[myUUID] = valueMap
	}

	return resultMap, nil
}

// STEP #4
func (s *SmartContract) Train(ctx contractapi.TransactionContextInterface, receiveMsg string) error {
	fmt.Println("[TRAIN MSG] Received")
	receiveMsgBytes := []byte(receiveMsg)
	recMsg := new(HttpMessage)
	_ = json.Unmarshal(receiveMsgBytes, recMsg)

	// store w map into blockchain
	err := saveAsMap(ctx, "wMap", recMsg.Epochs, recMsg.Uuid, recMsg.Data)
	if err != nil {
		return fmt.Errorf("failed to update w map into state. %s", err.Error())
	}

	return nil
}

func (s *SmartContract) CheckTrainRead(ctx contractapi.TransactionContextInterface, receiveMsg string) error {
	fmt.Println("[CHECK TRAIN READ MSG] Received")
	receiveMsgBytes := []byte(receiveMsg)
	recMsg := new(HttpMessage)
	_ = json.Unmarshal(receiveMsgBytes, recMsg)

	// try to read wMap, if all good, then can go on "train ready".
	wMap, err := readAsMap(ctx, "wMap", recMsg.Epochs)
	if err != nil {
		return fmt.Errorf("failed to read w map from state. %s", err.Error())
	}
	if len(wMap) == userNum {
		fmt.Println("gathered enough w map [" + strconv.Itoa(len(wMap)) + "], can go on to train ready now.")
	} else {
		fmt.Println("not gathered enough w map [" + strconv.Itoa(len(wMap)) + "], do nothing.")
	}
	return nil
}

func (s *SmartContract) TrainReady(ctx contractapi.TransactionContextInterface, receiveMsg string) error {
	fmt.Println("[TRAIN READY MSG] Received")
	receiveMsgBytes := []byte(receiveMsg)
	recMsg := new(HttpMessage)
	_ = json.Unmarshal(receiveMsgBytes, recMsg)

	// count w map length. If gathered all of the w, average them and get global_w, release global_w
	wMap, err := readAsMap(ctx, "wMap", recMsg.Epochs)
	if err != nil {
		return fmt.Errorf("failed to read w map from state. %s", err.Error())
	}
	sendMsg := new(HttpMessage)
	sendMsg.Message = "security_poll"
	sendMsg.Data = wMap // send back a w map, the keys are uuids of users
	sendMsg.Uuid = myuuid
	sendMsg.Epochs = recMsg.Epochs
	sendMsgAsBytes, _ := json.Marshal(sendMsg)
	go sendPostRequest(sendMsgAsBytes, "SECURITY_POLL")
	return nil
}

// Security part
func (s *SmartContract) OutlierRecord(ctx contractapi.TransactionContextInterface, receiveMsg string) error {
	fmt.Println("[OUTLIER RECORD MSG] Received")
	receiveMsgBytes := []byte(receiveMsg)
	recMsg := new(HttpMessage)
	_ = json.Unmarshal(receiveMsgBytes, recMsg)

	// store outlier map into blockchain
	err := saveAsMap(ctx, "outlierMap", recMsg.Epochs, recMsg.Uuid, recMsg.Data)
	if err != nil {
		return fmt.Errorf("failed to update outlier map into state. %s", err.Error())
	}

	return nil
}

func (s *SmartContract) CheckPollRead(ctx contractapi.TransactionContextInterface, receiveMsg string) error {
	fmt.Println("[CHECK POLL READ MSG] Received")
	receiveMsgBytes := []byte(receiveMsg)
	recMsg := new(HttpMessage)
	_ = json.Unmarshal(receiveMsgBytes, recMsg)

	// try to read outlierMap, if all good, then can go on "poll ready".
	outlierMap, err := readAsMap(ctx, "outlierMap", recMsg.Epochs)
	if err != nil {
		return fmt.Errorf("failed to read outlier map from state. %s", err.Error())
	}
	if len(outlierMap) == userNum {
		fmt.Println("gathered enough outlier map [" + strconv.Itoa(len(outlierMap)) +
			"], can go on to poll ready now.")
	} else {
		fmt.Println("not gathered enough outlier map [" + strconv.Itoa(len(outlierMap)) + "], do nothing.")
	}
	return nil
}

func (s *SmartContract) PollReady(ctx contractapi.TransactionContextInterface, receiveMsg string) ([]int, error) {
	fmt.Println("[POLL READY MSG] Received")
	receiveMsgBytes := []byte(receiveMsg)
	recMsg := new(HttpMessage)
	_ = json.Unmarshal(receiveMsgBytes, recMsg)

	allOutlierMap, err := readAsMap(ctx, "outlierMap", recMsg.Epochs)
	if err != nil {
		return nil, fmt.Errorf("failed to read outlier map from state. %s", err.Error())
	}

	// calculate outlier poll number
	outlierPollResults := make(map[int]int)
	for _, value := range allOutlierMap {
		jsonString, _ := json.Marshal(value)
		outliers := new(OutliersMap)
		_ = json.Unmarshal(jsonString, &outliers)
		for _, outlier := range outliers.OutlierIds {
			if val, ok := outlierPollResults[outlier]; ok {
				outlierPollResults[outlier] = val + 1
			} else {
				outlierPollResults[outlier] = 1
			}
		}
	}
	var outlierJudgeResults []int
	for k, v := range outlierPollResults {
		fmt.Println("[Security] After calculate, outlier vote results for userid: " +
			strconv.Itoa(k) + " is: " + strconv.Itoa(v))
		outlierUserNum := userNum / 2
		if v > outlierUserNum {
			fmt.Println("[Security] Due to more than " + strconv.Itoa(outlierUserNum) + " vote, user: " +
				strconv.Itoa(k) + "is treated as malicious user.")
			outlierJudgeResults = append(outlierJudgeResults, k)
		}
	}

	return outlierJudgeResults, nil
}

// STEP #4 part: save w_glob onto distributed ledger
func (s *SmartContract) WGlob(ctx contractapi.TransactionContextInterface, receiveMsg string) error {
	fmt.Println("[WGLOB MSG] Received")
	receiveMsgBytes := []byte(receiveMsg)
	recMsg := new(HttpMessage)
	_ = json.Unmarshal(receiveMsgBytes, recMsg)
	// save w_glob to wGlobMap
	err := saveAsMap(ctx, "wGlobMap", recMsg.Epochs, recMsg.Uuid, recMsg.Data)
	if err != nil {
		return fmt.Errorf("failed to update w_glob map into state. %s", err.Error())
	}
	return nil
}

// STEP #6
// Gather data structure from python:
// UserA {acc_test: [acc_test1, acc_test2, ...]
//        alpha: [alpha1, alpha2, ...]}
// UserB {acc_test: [acc_test1, acc_test2, ...]
//        alpha: [alpha1, alpha2, ...]}
func (s *SmartContract) Negotiate(ctx contractapi.TransactionContextInterface, receiveMsg string) error {
	fmt.Println("[NEGOTIATE MSG] Received")
	receiveMsgBytes := []byte(receiveMsg)
	recMsg := new(HttpAccAlphaMessage)
	_ = json.Unmarshal(receiveMsgBytes, recMsg)

	// store acc_test and alpha map into blockchain
	err := saveAsMap(ctx, "accAlphaMap", recMsg.Epochs, recMsg.Uuid, recMsg.Data)
	if err != nil {
		return fmt.Errorf("failed to update acc_test and alpha map into state. %s", err.Error())
	}

	return nil
}

func (s *SmartContract) CheckNegotiateRead(ctx contractapi.TransactionContextInterface, receiveMsg string) error {
	fmt.Println("[CHECK NEGOTIATE READ MSG] Received")
	receiveMsgBytes := []byte(receiveMsg)
	recMsg := new(HttpAccAlphaMessage)
	_ = json.Unmarshal(receiveMsgBytes, recMsg)

	// try to read accAlphaMap, if all good, then can go on "negotiate ready".
	var accAlphaMap = map[string]AccAlpha{}
	accAlphaInterface, err := readAsMap(ctx, "accAlphaMap", recMsg.Epochs)
	if err != nil {
		return fmt.Errorf("failed to read acc_test and alpha map from state. %s", err.Error())
	}
	accAlphaString, err := json.Marshal(accAlphaInterface)
	if err != nil {
		return fmt.Errorf("failed to marshal accAlpha interface: %s", err.Error())
	}
	err = json.Unmarshal(accAlphaString, &accAlphaMap)
	if err != nil {
		return fmt.Errorf("failed to unmarshal accAlpha interface to accAlphaMap: %s", err.Error())
	}
	if len(accAlphaMap) == userNum {
		fmt.Println("gathered enough acc_test and alpha map [" + strconv.Itoa(len(accAlphaMap)) +
			"], can go on to negotiate ready now.")
	} else {
		fmt.Println("not gathered enough acc_test and alpha map [" + strconv.Itoa(len(accAlphaMap)) +
			"], do nothing.")
	}
	return nil
}

func (s *SmartContract) NegotiateReady(ctx contractapi.TransactionContextInterface, receiveMsg string) error {
	fmt.Println("[NEGOTIATE READY MSG] Received")
	receiveMsgBytes := []byte(receiveMsg)
	recMsg := new(HttpAccAlphaMessage)
	_ = json.Unmarshal(receiveMsgBytes, recMsg)

	var accAlphaMap = map[string]AccAlpha{}
	accAlphaInterface, err := readAsMap(ctx, "accAlphaMap", recMsg.Epochs)
	if err != nil {
		return fmt.Errorf("failed to read acc_test and alpha map from state. %s", err.Error())
	}
	accAlphaString, err := json.Marshal(accAlphaInterface)
	if err != nil {
		return fmt.Errorf("failed to marshal accAlpha interface: %s", err.Error())
	}
	err = json.Unmarshal(accAlphaString, &accAlphaMap)
	if err != nil {
		return fmt.Errorf("failed to unmarshal accAlpha interface to accAlphaMap: %s", err.Error())
	}
	// count accAlpha map length. If gathered all of the acc_test, choose the best alpha according to the policy
	// (findMaxAccAvg or findMinAccVar), release alpha and w
	if len(accAlphaMap) == userNum {
		fmt.Println("gathered enough acc_test and alpha, choose the best alpha according to the policy")
		alpha, acc := findMaxAccAvg(accAlphaMap)
		// load w from db
		wMap, err := readAsMap(ctx, "wMap", recMsg.Epochs)
		if err != nil {
			return fmt.Errorf("failed to read wMap from state. %s", err.Error())
		}
		// load wGlobMap from db
		wGlobMap, err := readAsMap(ctx, "wGlobMap", recMsg.Epochs)
		if err != nil {
			return fmt.Errorf("failed to read wGlobMap from state. %s", err.Error())
		}
		// release alpha and w
		data := make(map[string]interface{})
		data["alpha"] = alpha // alpha is included in data
		data["accuracy"] = acc // accuracy for alpha is included in data
		data["wMap"] = wMap // w map is included in data, the keys are uuids of users
		data["wGlobMap"] = wGlobMap // w_glob map is also included in data, the keys are uuids of users
		sendMsg := new(HttpMessage)
		sendMsg.Message = "alpha"
		sendMsg.Data = data
		sendMsg.Uuid = myuuid
		sendMsg.Epochs = recMsg.Epochs
		sendMsgAsBytes, _ := json.Marshal(sendMsg)

		go sendPostRequest(sendMsgAsBytes, "NEGOTIATE")
	} else {
		fmt.Println("not gathered enough acc_test and alpha [" + strconv.Itoa(len(accAlphaMap)) + "], do nothing")
	}

	return nil
}

// sub-functions for STEP#6: find out the max acc_test average
func findMaxAccAvg(accAlphaMap map[string]AccAlpha) (float64, float64) {
	fmt.Println("[Find Alpha] According to max acc_test average policy")
	accTestSum :=make([]float64, negotiateRound)
	var randomUuid string
	// calculate sum acc_test for all users into array `accTestSum`
	for id, accAlpha := range accAlphaMap {
		for k, v := range accAlpha.AccTest {
			accTestSum[k] += v
		}
		randomUuid = id
	}
	// find out the max value in `accTestSum`, return the alpha of that value.
	var max float64
	var maxIndex = 0
	for i, v := range accTestSum {
		if i==0 || v > max {
			max = v
			maxIndex = i
		}
	}
	alpha := accAlphaMap[randomUuid].Alpha[maxIndex]
	acc := max/float64(userNum)
	fmt.Println("Found the max acc_test: ", acc, " with alpha: ", alpha)
	return alpha, acc
}

// sub-functions for STEP#6: find out the min acc_test variance
func findMinAccVar(accAlphaMap map[string]AccAlpha) float64 {
	fmt.Println("[Find Alpha] According to min acc_test variance policy")
	accTestAvg :=make([]float64, negotiateRound)
	var randomUuid string
	// calculate sum acc_test for all users into array `accTestSum`
	for id, accAlpha := range accAlphaMap {
		for k, accTest := range accAlpha.AccTest {
			accTestAvg[k] += accTest / float64(userNum)
		}
		randomUuid = id
	}
	accTestVar :=make([]float64, negotiateRound)
	// calculate the variance value of acc_test
	for k, accAvg := range accTestAvg {
		nVariance := 0.0
		for _, accAlpha := range accAlphaMap {
			nVariance += math.Pow(accAlpha.AccTest[k] - accAvg, 2)
		}
		accTestVar[k] = nVariance / float64(userNum)
	}
	// find out the min variance value in accTestVar
	var min float64
	var minIndex = 0
	for i, v := range accTestVar {
		if i==0 || v < min {
			min = v
			minIndex = i
		}
	}
	alpha := accAlphaMap[randomUuid].Alpha[minIndex]
	fmt.Println("Found the min acc_test variance: ", min, " with alpha: ", alpha)
	return alpha
}

func sendPostRequest(buf []byte, requestType string) {
	fmt.Println("SEND REQUEST [" + requestType + "]")
	resp, err := http.Post(url, "application/json", bytes.NewBuffer(buf))
	if err != nil {
		fmt.Printf("[Error] failed to send post request to server. %s\n", err.Error())
		return
	}
	defer resp.Body.Close()
	if resp != nil {
		fmt.Println("SEND REQUEST [" + requestType + "]: " + resp.Status)
	} else {
		fmt.Println("SEND REQUEST [" + requestType + "]: No reply")
	}

}

func main() {

	chaincode, err := contractapi.NewChaincode(new(SmartContract))

	if err != nil {
		fmt.Printf("Error create chaincode: %s", err.Error())
		return
	}

	if err := chaincode.Start(); err != nil {
		fmt.Printf("Error starting chaincode: %s", err.Error())
	}
}
