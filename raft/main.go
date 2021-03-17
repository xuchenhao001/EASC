package main

import (
	"flag"
	"fmt"
	"log"
	"os"
	"os/signal"

	"github.com/otoolep/hraftd/http"
	"github.com/otoolep/hraftd/store"
)

// Command line defaults
const (
	DefaultHTTPAddr = ":7150"
	DefaultRaftAddr = ":7151"
)

// Command line parameters
var inmem bool
var httpAddr string
var raftAddr string
//var joinAddr string
var nodeID string

func init() {
	flag.BoolVar(&inmem, "inmem", true, "Use in-memory storage for Raft")
	flag.StringVar(&httpAddr, "haddr", DefaultHTTPAddr, "Set the HTTP bind address")
	flag.StringVar(&raftAddr, "raddr", DefaultRaftAddr, "Set Raft bind address")
	//flag.StringVar(&joinAddr, "join", "", "Set join address, if any")
	flag.StringVar(&nodeID, "id", "", "Node ID")
	flag.Usage = func() {
		fmt.Fprintf(os.Stderr, "Usage: %s [options] <raft-data-path> \n", os.Args[0])
		flag.PrintDefaults()
	}
}

func main() {
	flag.Parse()

	if flag.NArg() == 0 {
		fmt.Fprintf(os.Stderr, "No Raft storage directory specified\n")
		os.Exit(1)
	}

	// Ensure Raft storage exists.
	raftDir := flag.Arg(0)
	if raftDir == "" {
		fmt.Fprintf(os.Stderr, "No Raft storage directory specified\n")
		os.Exit(1)
	}
	os.MkdirAll(raftDir, 0700)

	s := store.New(inmem)
	s.RaftDir = raftDir
	s.RaftBind = raftAddr
	//if err := s.Open(joinAddr == "", nodeID); err != nil {
	//	log.Fatalf("failed to open store: %s", err.Error())
	//}

	h := httpd.New(httpAddr, nodeID, s)
	if err := h.Start(); err != nil {
		log.Fatalf("failed to start HTTP service: %s", err.Error())
	}

	// If join was specified, make the join request.
	//if joinAddr != "" {
	//	if err := join(joinAddr, raftAddr, nodeID); err != nil {
	//		log.Fatalf("failed to join node at %s: %s", joinAddr, err.Error())
	//	}
	//}

	log.Println("hraftd started successfully at: " + httpAddr)

	terminate := make(chan os.Signal, 1)
	signal.Notify(terminate, os.Interrupt)
	<-terminate
	log.Println("hraftd exiting")
}
