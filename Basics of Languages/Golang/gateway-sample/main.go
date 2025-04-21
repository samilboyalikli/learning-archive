package main

import (
	"log"
	"net/http"
	"net/http/httputil"
	"net/url"
	"strings"
)

const firstServiceRoute = "http://localhost:8081"
const secondServiceRoute = "http://localhost:8082"

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
		// TODO - key/value çiftleriyle path ve reverseProxy'nin parametresini tekte atayabilirim
		// TODO - bu key/value çiftlerini de bir array yapıp, tek if bloğunda tüm else if'leri çalıştırabilirim.
		if strings.HasPrefix(r.URL.Path, "/service1") {
			log.Printf("This req is for first service.")
			reverseProxy(firstServiceRoute).ServeHTTP(w, r)	
		} else if strings.HasPrefix(r.URL.Path, "/service2") {
			log.Printf("This req is for second service.")
			reverseProxy(secondServiceRoute).ServeHTTP(w, r)
		}
	}

	http.HandleFunc("/", handler)
	log.Println("API Gateway çalışıyor: http://localhost:8080")
	
	err := http.ListenAndServe(":8080", nil)
	if err != nil {
		log.Fatalf("Sunucu başlatılamadı: %v", err)
	}
}
