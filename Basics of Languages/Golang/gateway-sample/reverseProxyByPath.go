package main

import (
	"log"
	"net/http"
	"net/http/httputil"
	"net/url"
	"strings"
)

var routes = map[string]string {
	"/service1": "http://localhost:8081",
	"/service2": "http://localhost:8082",
}

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

func main() {
	handler := func(w http.ResponseWriter, r *http.Request) {
		for servicePath, domain := range routes {
			if strings.HasPrefix(r.URL.Path, servicePath) {
				var address string
				address = domain+r.URL.Path
				clientIP := r.RemoteAddr
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
