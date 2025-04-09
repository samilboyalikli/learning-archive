package main

import (
    "fmt"
)

func helloWorld() {
    fmt.Println("hello world")
}

func basicCalculator() string {
    var firstTarget int
    fmt.Print("First Target: ")
    fmt.Scanln(&firstTarget)
    var secondTarget int
    fmt.Print("Second Target: ")
    fmt.Scanln(&secondTarget)
    return fmt.Sprintf("%d + %d", firstTarget, secondTarget)
}

func main() {
    // --> Level 1
    // helloWorld()
    fmt.Println(basicCalculator())
}
