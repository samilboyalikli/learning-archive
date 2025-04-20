package main

import (
	"log"
	"net/http"
	"net/http/httputil"
	"net/url"
)

// Yönlendirmek istediğimiz backend servisin adresi
const backendURL = "http://localhost:8081"

func main() {
	// Backend URL'sini parse ediyoruz
	url, err := url.Parse(backendURL)
	if err != nil {
		log.Fatalf("URL çözümlenemedi: %v", err)
	}

	// Reverse proxy oluşturuyoruz
	proxy := httputil.NewSingleHostReverseProxy(url)

	// Gelen isteği işleyen handler
	handler := func(w http.ResponseWriter, r *http.Request) {
		log.Printf("İstek yönlendiriliyor: %s %s", r.Method, r.URL.Path)
		proxy.ServeHTTP(w, r)
	}

	http.HandleFunc("/", handler)
	
	log.Println("API Gateway çalışıyor: http://localhost:8080")
	err = http.ListenAndServe(":8080", nil)
	if err != nil {
		log.Fatalf("Sunucu başlatılamadı: %v", err)
	}
}
