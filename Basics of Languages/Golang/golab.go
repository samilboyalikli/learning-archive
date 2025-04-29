package main

import (
    "fmt"
)

func helloWorld() {
    fmt.Println("hello world")
}

func basicCalculator() string {
    var (
        firstTarget     int
        secondTarget    int
        process         string
    )   

    fmt.Print("First Target: ")
    fmt.Scanln(&firstTarget)
    fmt.Print("Second Target: ")
    fmt.Scanln(&secondTarget)
    fmt.Print("Process: ")
    fmt.Scanln(&process)

    switch process {
    case "+":
        var result int
        result = firstTarget + secondTarget
        return fmt.Sprintf("Result: %d", result)
    case "-":
        var result int
        result = firstTarget - secondTarget
        return fmt.Sprintf("Result: %d", result)
    case "*":
        var result float64
        result = float64(firstTarget) * float64(secondTarget)
        return fmt.Sprintf("Result: %f", result)
    case "/":
        var result float64
        result = float64(firstTarget) / float64(secondTarget)
        return fmt.Sprintf("Result: %f", result)
    default:
        return "invalid act :/"
    }
}

func main() {
    // --> Level 1
    // helloWorld()
    result := basicCalculator()
    fmt.Println(result)
} 