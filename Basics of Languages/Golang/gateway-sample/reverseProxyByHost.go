package main

import (
	"log"
	"net/http"
	"net/http/httputil"
	"net/url"
	"strings"
	"time"
	"sync"
)

const (
	infoLogParameter int = 50
	warnLogParameter int = 75
	tooManyReqParameter int = 100
	resetStoreParameter int = 10
)

var routes = map[string]string {
	"subdomain1": "http://localhost:8081",
	"subdomain2": "http://localhost:8082",
}

var (
    ipStore = make(map[string][]time.Time)
    mu      sync.Mutex
)

func parseURL(route string) *url.URL {
    parsedURL, err := url.Parse(route)
    if err != nil {
        log.Fatalf("Invalid URL provided: %v", err)
    }
    return parsedURL
}

func reverseProxy(route string) *httputil.ReverseProxy {
	url := parseURL(route)
	proxy := httputil.NewSingleHostReverseProxy(url)
	proxy.Director = func(req *http.Request) {
		req.URL.Scheme = url.Scheme
		req.Host = url.Host
		req.URL.Host = url.Host
		req.URL.Path = url.Path
	}
	return proxy
}

func checkStore(ip string) {
	mu.Lock()
	defer mu.Unlock()

	now := time.Now()
	requests := ipStore[ip]

	count := 0
	for _, timeOfRequest := range requests {
		if now.Sub(timeOfRequest) <= time.Minute {
			count++
		}
	}

	switch {
	case count >= tooManyReqParameter:
		log.Printf("[WARNING] IP %s sent more than %d requests in the last minute.", ip, tooManyReqParameter)
	case count >= warnLogParameter:
		log.Printf("[WARNING] IP %s sent more than %d requests in the last minute.", ip, warnLogParameter)
	case count >= infoLogParameter:
		log.Printf("[INFO] IP %s sent more than %d requests in the last minute.", ip, infoLogParameter)
	}	
}

func addIP(ip string) {
	mu.Lock()
	defer mu.Unlock()
	ipStore[ip] = append(ipStore[ip], time.Now())
}

func resetStore() {
	mu.Lock()
	defer mu.Unlock()
	ipStore = make(map[string][]time.Time)
}

func periodicReset(interval time.Duration) {
	for {
		time.Sleep(interval)
		resetStore()
		log.Println("[INFO] IP Store reset")
	}
}

func main() {
	go periodicReset(time.Duration(resetStoreParameter) * time.Minute)
	handler := func(w http.ResponseWriter, r *http.Request) {
		for hostOfClient, hostOfServer := range routes {
			if strings.HasPrefix(r.Host, hostOfClient) {
				var address string
				address = hostOfServer+r.URL.Path
				clientIP := r.RemoteAddr
				checkStore(clientIP)
				addIP(clientIP)
				log.Printf("[INFO] IP: '%s'", clientIP)
				log.Printf("[INFO] Redirecting request...")
				log.Printf("[INFO] Method: '%s'", r.Method)
				log.Printf("[INFO] Adress: '%s'", address)
				reverseProxy(address).ServeHTTP(w, r)
			}	
		}
	}

	http.HandleFunc("/", handler)
	log.Println("[INFO] API Gateway is running (Port: 8080).")
	
	err := http.ListenAndServe(":8080", nil)
	if err != nil {
		log.Fatalf("Server failed to start (Port: 8080). Error:  %v", err)
	}
}
