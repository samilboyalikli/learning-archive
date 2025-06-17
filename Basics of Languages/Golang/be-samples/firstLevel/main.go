package main

import (
	"fmt"
	"net/http"
)

func main() {
    http.HandleFunc("/submit", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintf(w, "Service available...\n")
    })
	fmt.Println("Backend is Working: http://localhost:8080/home.html")
    page := http.FileServer(http.Dir("templates"))
    http.Handle("/", page)
    err := http.ListenAndServe(":8080", nil)
	if err != nil {
        panic(err)
    }
}

// TODOS
// 1. wordsaving component in home.html (checked)
// 2. main.go will be connected with home.html 
// 3. creating sqlite database
// 4. database structure
