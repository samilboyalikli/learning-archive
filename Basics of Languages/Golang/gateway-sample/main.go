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
        log.Fatalf("URL çözümlenemedi: %v", err)
    }
    return parsedURL
}

func reverseProxy(route string) *httputil.ReverseProxy {
	url := parseURL(route)
	proxy := httputil.NewSingleHostReverseProxy(url)
	return proxy
}

func main() {
	handler := func(w http.ResponseWriter, r *http.Request) {
		log.Printf("İstek yönlendiriliyor: %s %s", r.Method, r.URL.Path)
		for servicePath, domain := range routes {
			if strings.HasPrefix(r.URL.Path, servicePath) {
				log.Printf("This req for %v.", servicePath)
				reverseProxy(domain).ServeHTTP(w, r) 
			}
		}
	}

	http.HandleFunc("/", handler)
	log.Println("API Gateway çalışıyor: http://localhost:8080")
	
	err := http.ListenAndServe(":8080", nil)
	if err != nil {
		log.Fatalf("Sunucu başlatılamadı: %v", err)
	}
}
