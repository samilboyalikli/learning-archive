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

var routes = map[string]string {
	"subdomain1": "http://localhost:8081",
	"subdomain2": "http://localhost:8082",
}

type IPData struct {
	IP        		string
	Timestamp 		time.Time
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

	if count == 2 {
		log.Printf("[INFO] IP %s sent two requests in the same second.", ip)
	} else if count == 3 {
		log.Printf("[WARNING] IP %s sent three requests in the same second.", ip)
	} else if count > 3 {
		log.Printf("[WARNING] IP %s sent more than three requests in the same second.", ip)
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
	go periodicReset(15 * time.Minute)
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
