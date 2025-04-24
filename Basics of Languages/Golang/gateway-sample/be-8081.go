package main

import (
    "fmt"
    "net/http"
)

func main() {
    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintf(w, "First Service Avaible...\n")
        fmt.Fprintf(w, "Method: '%s'\n", r.Method)
        fmt.Fprintf(w, "Host: '%s'\n", r.Host)
        fmt.Fprintf(w, "Path: '%s'\n", r.URL.Path)
        })

    fmt.Println("First Backend is Working: http://localhost:8081")
    http.ListenAndServe(":8081", nil)
}
