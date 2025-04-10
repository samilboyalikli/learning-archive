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
    var process string
    fmt.Print("Process: ")
    fmt.Scanln(&process)
    switch process {
    case "+":
        var result int
        result = firstTarget + secondTarget
        return fmt.Sprintf("Sonuç: %d", result)
    case "-":
        var result int
        result = firstTarget - secondTarget
        return fmt.Sprintf("Sonuç: %d", result)
    case "*":
        var result float64
        result = float64(firstTarget) * float64(secondTarget)
        return fmt.Sprintf("Sonuç: %f", result)
    case "/":
        var result float64
        result = float64(firstTarget) / float64(secondTarget)
        return fmt.Sprintf("Sonuç: %f", result)
    default:
        return "Geçersiz işlem!"
    }
}

func main() {
    // --> Level 1
    // helloWorld()
    result := basicCalculator()
    fmt.Println(result)
}
