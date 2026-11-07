package main

// Khaos Forge - High-Speed Concurrent Probe Engine
// Author: dj

import (
	"encoding/json"
	"flag"
	"fmt"
	"net"
	"sync"
	"time"
)

type ScanResult struct {
	Target string `json:"target"`
	Port   int    `json:"port"`
	State  string `json:"state"`
}

func probePort(target string, port int, timeout time.Duration, wg *sync.WaitGroup, results chan<- ScanResult) {
	defer wg.Done()
	addr := fmt.Sprintf("%s:%d", target, port)
	conn, err := net.DialTimeout("tcp", addr, timeout)
	if err == nil {
		conn.Close()
		results <- ScanResult{Target: target, Port: port, State: "OPEN"}
	}
}

func main() {
	target := flag.String("target", "127.0.0.1", "Target IP or hostname")
	timeoutMs := flag.Int("timeout", 400, "Timeout in milliseconds")
	flag.Parse()

	commonPorts := []int{21, 22, 23, 25, 53, 80, 88, 110, 139, 443, 445, 1433, 3306, 3389, 5432, 8080, 8443}

	var wg sync.WaitGroup
	results := make(chan ScanResult, len(commonPorts))
	timeout := time.Duration(*timeoutMs) * time.Millisecond

	for _, port := range commonPorts {
		wg.Add(1)
		go probePort(*target, port, timeout, &wg, results)
	}

	wg.Wait()
	close(results)

	var output []ScanResult
	for r := range results {
		output = append(output, r)
	}

	data, _ := json.MarshalIndent(output, "", "  ")
	fmt.Println(string(data))
}
