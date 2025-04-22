package main

import (
	"fmt"
)

var routes = map[string]string {
	"/service1": "http://localhost:8081",
	"/service2": "http://localhost:8082",
}

func main() {
	for path, domain := range routes {
		fmt.Printf("Key: %v, Value: %v\n", path, domain)
	}
}
