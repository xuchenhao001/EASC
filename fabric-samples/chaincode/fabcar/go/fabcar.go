package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"github.com/google/uuid"
	"github.com/hyperledger/fabric-contract-api-go/contractapi"
	"math"
	"net/http"
	"strconv"
	"strings"
)

const url = "http://172.17.0.1:8888/messages"
var myuuid string
var userNum = 2
var negotiateRound = 10
var emptyLen = 2

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

func (s *SmartContract) InitLedger(ctx contractapi.TransactionContextInterface) error {
	// generate a new uuid for each user
	myuuid = uuid.Must(uuid.NewRandom()).String()
	println("Init finished. My uuid: " + myuuid)
	return nil
}

// STEP #2
func (s *SmartContract) Prepare(ctx contractapi.TransactionContextInterface, receiveMsg string) error {
	fmt.Println("[PREPARE MSG] Received")
	receiveMsgBytes := []byte(receiveMsg)

	recMsg := new(HttpMessage)
	_ = json.Unmarshal(receiveMsgBytes, recMsg)
	recMsg.Uuid = myuuid
	sendMsgAsBytes, _ := json.Marshal(recMsg)

	// clean wMap and accAlphaMap, prepare for train.
	//fmt.Println("clean wMap, accAlphaMap and wGlobMap, prepare for train.")
	//for epoch := recMsg.Epochs; epoch >= 1; epoch++ {
	//	_ = ctx.GetStub().PutState("wMap" + strconv.Itoa(epoch), []byte(" "))
	//	_ = ctx.GetStub().PutState("accAlphaMap" + strconv.Itoa(epoch), []byte(" "))
	//	_ = ctx.GetStub().PutState("wGlobMap" + strconv.Itoa(epoch), []byte(" "))
	//}

	sendPostRequest(sendMsgAsBytes, "PREPARE")

	return nil
}

// STEP #4
func (s *SmartContract) Train(ctx contractapi.TransactionContextInterface, receiveMsg string) error {
	fmt.Println("[TRAIN MSG] Received")
	receiveMsgBytes := []byte(receiveMsg)
	recMsg := new(HttpMessage)
	_ = json.Unmarshal(receiveMsgBytes, recMsg)

	wMap := make(map[string]interface{})
	wMapAsBytes, _ := ctx.GetStub().GetState("wMap" + strconv.Itoa(recMsg.Epochs))
	println("Exist wMapAsBytes len: ", len(wMapAsBytes))
	if wMapAsBytes == nil || len(wMapAsBytes) < emptyLen {
		fmt.Println("wMap doesn't exist, create a new one for: " + recMsg.Uuid)
		wMap[recMsg.Uuid] = recMsg.Data
	} else {
		fmt.Println("wMap exist, update it for: " + recMsg.Uuid)
		_ = json.Unmarshal(wMapAsBytes, &wMap)
		wMap[recMsg.Uuid] = recMsg.Data
	}
	// check all of the keys
	keys := make([]string, 0, len(wMap))
	for key := range wMap {
		keys = append(keys, key)
	}
	fmt.Println("wMap keys: " + strings.Join(keys, ", "))

	// store w map into blockchain
	jsonAsBytes, _ := json.Marshal(wMap)
	fmt.Println("update w map to DB")
	println("Update wMapAsBytes len: ", len(jsonAsBytes))
	err := ctx.GetStub().PutState("wMap" + strconv.Itoa(recMsg.Epochs), jsonAsBytes)
	if err !=nil {
		return fmt.Errorf("failed to update w map into state. %s", err.Error())
	}

	// count w map length. If gathered all of the w, average them and get global_w, release global_w
	if len(wMap) == userNum {
		fmt.Println("gathered enough w map, send for global_w")
		// average them, get global_w
		sendMsg := new(HttpMessage)
		sendMsg.Message = "average"
		sendMsg.Data = wMap // send back a w map, the keys are uuids of users
		sendMsg.Uuid = myuuid
		sendMsg.Epochs = recMsg.Epochs
		sendMsgAsBytes, _ := json.Marshal(sendMsg)

		go sendPostRequest(sendMsgAsBytes, "TRAIN")
	}
	return nil
}

// STEP #4 part: save w_glob onto distributed ledger
func (s *SmartContract) WGlob(ctx contractapi.TransactionContextInterface, receiveMsg string) error {
	fmt.Println("[WGLOB MSG] Received")
	receiveMsgBytes := []byte(receiveMsg)
	recMsg := new(HttpMessage)
	_ = json.Unmarshal(receiveMsgBytes, recMsg)
	// save w_glob to wGlobMap
	wGlobMap := make(map[string]interface{})
	wGlobMapAsBytes, _ := ctx.GetStub().GetState("wGlobMap" + strconv.Itoa(recMsg.Epochs))
	if wGlobMapAsBytes == nil || len(wGlobMapAsBytes) < emptyLen {
		fmt.Println("wGlobMap doesn't exist, create a new one for: " + recMsg.Uuid)
		wGlobMap[recMsg.Uuid] = recMsg.Data
	} else {
		fmt.Println("wGlobMap exist, update it for: " + recMsg.Uuid)
		_ = json.Unmarshal(wGlobMapAsBytes, &wGlobMap)
		wGlobMap[recMsg.Uuid] = recMsg.Data
	}
	jsonAsBytes, _ := json.Marshal(wGlobMap)
	fmt.Println("update w_glob map to DB")
	err := ctx.GetStub().PutState("wGlobMap" + strconv.Itoa(recMsg.Epochs), jsonAsBytes)
	if err !=nil {
		return fmt.Errorf("failed to put w_glob map into state. %s", err.Error())
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

	// save accAlpha to accAlphaMap
	accAlphaMap := make(map[string]AccAlpha)
	accAlphaMapAsBytes, _ := ctx.GetStub().GetState("accAlphaMap" + strconv.Itoa(recMsg.Epochs))
	if accAlphaMapAsBytes == nil || len(accAlphaMapAsBytes) < emptyLen {
		fmt.Println("accAlphaMap doesn't exist, create a new one for: " + recMsg.Uuid)
		accAlphaMap[recMsg.Uuid] = recMsg.Data
	} else {
		fmt.Println("accAlphaMap exist, update it for: " + recMsg.Uuid)
		_ = json.Unmarshal(accAlphaMapAsBytes, &accAlphaMap)
		accAlphaMap[recMsg.Uuid] = recMsg.Data
	}
	// check all of the keys
	keys := make([]string, 0, len(accAlphaMap))
	for key := range accAlphaMap {
		keys = append(keys, key)
	}
	fmt.Println("accAlphaMap keys: " + strings.Join(keys, ", "))

	// store accAlpha map into blockchain
	jsonAsBytes, _ := json.Marshal(accAlphaMap)
	fmt.Println("update accAlphaMap to DB")
	err := ctx.GetStub().PutState("accAlphaMap" + strconv.Itoa(recMsg.Epochs), jsonAsBytes)
	if err !=nil {
		return fmt.Errorf("failed to put accAlphaMap into state. %s", err.Error())
	}

	// count accAlpha map length. If gathered all of the acc_test, choose the best alpha according to the policy
	// (findMaxAccAvg or findMinAccVar), release alpha and w
	if len(accAlphaMap) == userNum {
		fmt.Println("gathered enough acc_test and alpha, choose the best alpha according to the policy")
		alpha := findMaxAccAvg(accAlphaMap)
		// load w from db
		wMap := make(map[string]interface{})
		wMapAsBytes, _ := ctx.GetStub().GetState("wMap" + strconv.Itoa(recMsg.Epochs))
		_ = json.Unmarshal(wMapAsBytes, &wMap)
		wGlobMap := make(map[string]interface{})
		wGlobMapAsBytes, _ := ctx.GetStub().GetState("wGlobMap" + strconv.Itoa(recMsg.Epochs))
		_ = json.Unmarshal(wGlobMapAsBytes, &wGlobMap)
		// release alpha and w
		data := make(map[string]interface{})
		data["alpha"] = alpha // alpha is included in data
		data["wMap"] = wMap // w map is included in data, the keys are uuids of users
		data["wGlobMap"] = wGlobMap // w_glob map is also included in data, the keys are uuids of users
		sendMsg := new(HttpMessage)
		sendMsg.Message = "alpha"
		sendMsg.Data = data
		sendMsg.Uuid = myuuid
		sendMsg.Epochs = recMsg.Epochs
		sendMsgAsBytes, _ := json.Marshal(sendMsg)

		go sendPostRequest(sendMsgAsBytes, "NEGOTIATE")
	}
	return nil
}

// sub-functions for STEP#6: find out the max acc_test average
func findMaxAccAvg(accAlphaMap map[string]AccAlpha) float64 {
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
	fmt.Println("Found the max acc_test: ", max/2, " with alpha: ", alpha)
	return alpha
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
	resp, err2 := http.Post(url, "application/json", bytes.NewBuffer(buf))
	if err2 != nil {
		fmt.Printf("[Error] failed to send post request to server. %s\n", err2.Error())
	}
	if resp != nil {
		fmt.Println(requestType + ": " + resp.Status)
	} else {
		fmt.Println(requestType + ": No reply")
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
