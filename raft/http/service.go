// Package httpd provides the HTTP server for accessing the distributed key-value store.
// It also provides the endpoint for other nodes to join an existing cluster.
package httpd

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net"
	"net/http"
	"strings"
	"time"
)

type SetupRequest struct {
	LeaderAddr   string `json:"leaderAddr"`
	LeaderRaftAddr  string `json:"leaderRaftAddr"`
	LeaderId   string `json:"leaderId"`
	ClientAddrs  []string `json:"clientAddrs"`
	ClientRaftAddrs  []string `json:"clientRaftAddrs"`
	ClientIds  []string `json:"clientIds"`
}

// Store is the interface Raft-backed key-value stores must implement.
type Store interface {
	// Get returns the value for the given key.
	Get(key string) (string, error)

	// Set sets the value for the given key, via distributed consensus.
	Set(key, value string) error

	// Delete removes the given key, via distributed consensus.
	Delete(key string) error

	// Join joins the node, identitifed by nodeID and reachable at addr, to the cluster.
	Join(nodeID string, addr string) error

	// Open start up the first node of cluster.
	Open(enableSingle bool, localID string) error

	// GetLeader return the leader information. It may return empty string if there is no current leader.
	GetLeader() string
}

// Service provides HTTP service.
type Service struct {
	addr string
	nodeId string
	ln   net.Listener

	store Store
}

// New returns an uninitialized HTTP service.
func New(addr string, nodeId string, store Store) *Service {
	return &Service{
		addr:  addr,
		store: store,
		nodeId: nodeId,
	}
}

// Start starts the service.
func (s *Service) Start() error {
	server := http.Server{
		Handler: s,
	}

	ln, err := net.Listen("tcp", s.addr)
	if err != nil {
		return err
	}
	s.ln = ln

	http.Handle("/", s)

	go func() {
		err := server.Serve(s.ln)
		if err != nil {
			log.Fatalf("HTTP serve: %s", err)
		}
	}()

	return nil
}

// ServeHTTP allows Service to serve HTTP requests.
func (s *Service) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	if strings.HasPrefix(r.URL.Path, "/key") {
		s.handleKeyRequest(w, r)
	} else if r.URL.Path == "/join" {
		s.handleJoin(w, r)
	} else if r.URL.Path == "/setup" {
		s.handleSetup(w, r)
	} else if r.URL.Path == "/init" {
		s.handleInit(w, r)
	} else if r.URL.Path == "/info" {
		s.handleInfo(w, r)
	} else {
		log.Printf("Error: unknown URL path: " + r.URL.Path)
		w.WriteHeader(http.StatusNotFound)
	}
}

func (s *Service) handleSetup(w http.ResponseWriter, r *http.Request) {
	var m SetupRequest
	if err := json.NewDecoder(r.Body).Decode(&m); err != nil {
		w.WriteHeader(http.StatusBadRequest)
		return
	}

	// when setup, setup leader and then setup clients
	// setup the leader first
	if err := s.store.Open(true, m.LeaderId); err != nil {
		log.Fatalf("failed to open leader store: %s", err.Error())
	}

	// wait for the leader to be successfully elected
	for wait := true; wait; {
		log.Printf("[Leader] wait leader to be setup...")
		time.Sleep( 1*time.Second )
		getInfoURL := "http://" + m.LeaderAddr + "/info"
		res, err := sendRequest(getInfoURL, []byte(""))
		if err != nil {
			log.Fatalf("failed to get leader info: %s", err.Error())
		}
		var body map[string]string
		if err := json.Unmarshal(res, &body); err != nil {
			log.Fatalf("failed to unmarshal leader info: %s", err.Error())
		}
		log.Printf("[Leader] acquired leader address: %s", body["leaderAddr"])
		if body["leaderAddr"] == m.LeaderRaftAddr {
			log.Printf("[Leader] leader setting finished!")
			wait = false
		}
	}

	// setup clients
	for i := range m.ClientAddrs {
		// reset clients first
		resetURL := "http://" + m.ClientAddrs[i] + "/init"
		if _, err := sendRequest(resetURL, []byte("")); err != nil {
			log.Fatalf("failed to reset client: %s", err.Error())
		}

		if err := s.store.Join(m.ClientIds[i], m.ClientRaftAddrs[i]); err != nil {
			log.Fatalf("failed to join the client to the cluster: %s", err.Error())
		}
	}
}

// Do init to clients before let them join into the raft cluster
func (s *Service) handleInit(w http.ResponseWriter, r *http.Request) {
	if err := s.store.Open(false, s.nodeId); err != nil {
		log.Fatalf("failed to open client store: %s", err.Error())
	}
}

// return leader information
func (s *Service) handleInfo(w http.ResponseWriter, r *http.Request) {
	leaderAddr := s.store.GetLeader()
	b, err := json.Marshal(map[string]string{"leaderAddr": leaderAddr})
	if err != nil {
		log.Fatalf("failed to marshal leader address: %s", err.Error())
	}
	w.Header().Set("Content-Type", "application/json")
	w.Write(b)
	return
}

func sendRequest(url string, requestBody []byte) ([]byte,error) {
	req, err := http.NewRequest("POST", url, bytes.NewBuffer(requestBody))
	if req == nil {
		return nil, err
	}
	req.Header.Set("Content-Type", "application/json")
	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	fmt.Println("request response Status:", resp.Status)
	//fmt.Println("response Headers:", resp.Header)
	body, _ := ioutil.ReadAll(resp.Body)
	//fmt.Println("response Body:", string(body))
	return body, nil
}

func (s *Service) handleJoin(w http.ResponseWriter, r *http.Request) {
	var m SetupRequest
	if err := json.NewDecoder(r.Body).Decode(&m); err != nil {
		w.WriteHeader(http.StatusBadRequest)
		return
	}

	if m.LeaderAddr == s.addr {
		// if the leader address is the same as current node, set up cluster.
		if err := s.store.Open(true, s.nodeId); err != nil {
			log.Fatalf("failed to open leader store: %s", err.Error())
		}
	} else {
		// otherwise, join the node into the cluster
		if err := s.store.Open(false, s.nodeId); err != nil {
			log.Fatalf("failed to open client store: %s", err.Error())
		}
		if err := s.store.Join(s.nodeId, m.LeaderAddr); err != nil {
			log.Fatalf("failed to join the client to the cluster: %s", err.Error())
		}
	}
}

func (s *Service) handleKeyRequest(w http.ResponseWriter, r *http.Request) {
	getKey := func() string {
		parts := strings.Split(r.URL.Path, "/")
		if len(parts) != 3 {
			return ""
		}
		return parts[2]
	}

	switch r.Method {
	case "GET":
		k := getKey()
		if k == "" {
			w.WriteHeader(http.StatusBadRequest)
		}
		v, err := s.store.Get(k)
		if err != nil {
			w.WriteHeader(http.StatusInternalServerError)
			return
		}

		b, err := json.Marshal(map[string]string{k: v})
		if err != nil {
			w.WriteHeader(http.StatusInternalServerError)
			return
		}

		w.Header().Set("Content-Type", "application/json")
		w.Write(b)

	case "POST":
		// Read the value from the POST body.
		m := map[string]string{}
		if err := json.NewDecoder(r.Body).Decode(&m); err != nil {
			w.WriteHeader(http.StatusBadRequest)
			return
		}
		for k, v := range m {
			if err := s.store.Set(k, v); err != nil {
				w.WriteHeader(http.StatusInternalServerError)
				return
			}
		}

	case "DELETE":
		k := getKey()
		if k == "" {
			w.WriteHeader(http.StatusBadRequest)
			return
		}
		if err := s.store.Delete(k); err != nil {
			w.WriteHeader(http.StatusInternalServerError)
			return
		}
		s.store.Delete(k)

	default:
		w.WriteHeader(http.StatusMethodNotAllowed)
	}
	return
}

// Addr returns the address on which the Service is listening
func (s *Service) Addr() net.Addr {
	return s.ln.Addr()
}
