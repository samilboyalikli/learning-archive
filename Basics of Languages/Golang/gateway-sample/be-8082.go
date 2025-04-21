package main

import (
    "fmt"
    "net/http"
)

func main() {
    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintf(w, "Second Service: %s %s", r.Method, r.URL.Path)
    })

    fmt.Println("Second Backend is Working: http://localhost:8082")
    http.ListenAndServe(":8082", nil)
}
