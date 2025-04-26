package main

import (
	"log"
	"net/http"
	"net/http/httputil"
	"net/url"
	"strings"
)

var routes = map[string]string {
	"subdomain1": "http://localhost:8081",
	"subdomain2": "http://localhost:8082",
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
		for hostOfClient, hostOfServer := range routes {
			if strings.HasPrefix(r.Host, hostOfClient) {
				var address string
				address = hostOfServer+r.URL.Path
				clientIP := r.RemoteAddr
				// TODO - Should be saved IP with timestamp.
				// TODO - If same IP send message with same timestamp, rate limiter will write an info log.
				// TODO - If same IP send mesage with same timestamp, rate limiter will write a warn log.
				// TODO - The structure which IP's saved there, will reset all 15 min.
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
