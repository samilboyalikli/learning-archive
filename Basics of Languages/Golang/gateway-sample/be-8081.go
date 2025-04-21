package main

import (
    "fmt"
    "net/http"
)

func main() {
    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintf(w, "First Service: %s %s", r.Method, r.URL.Path)
    })

    fmt.Println("First Backend is Working: http://localhost:8081")
    http.ListenAndServe(":8081", nil)
}
