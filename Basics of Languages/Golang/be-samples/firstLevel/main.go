package main

import (
	"fmt"
	"net/http"
)

func main() {
	fmt.Println("Backend is Working: http://localhost:8080")
	http.ListenAndServe(":8080", nil)
}
