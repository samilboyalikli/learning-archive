package main

import (
	"fmt"
	"net/http"
    "database/sql"
    _ "modernc.org/sqlite"
)

func main() {
    db, err := sql.Open("sqlite", "database.db")
    if err != nil {
        panic(err)
    }
    defer db.Close()
    http.HandleFunc("/submit", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintf(w, "Service available...\n")
    })
	fmt.Println("Backend is Working: http://localhost:8080/home.html")
    page := http.FileServer(http.Dir("templates"))
    http.Handle("/", page)
    if err := http.ListenAndServe(":8080", nil); err != nil {
        panic(err)
    }
}

// TODOS
// 1. wordsaving component in home.html (checked)
// 2. main.go will be connected with home.html (checked)
// 3. creating sqlite database
// 4. database structure

// BUGS
// 1. no required module provides package modernc.org/sqlite; to add it: go get modernc.org/sqlite
// 2. 