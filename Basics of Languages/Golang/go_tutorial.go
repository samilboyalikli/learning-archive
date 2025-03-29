// The file includes basics of golang.

package main

import (
	"fmt"
	"math"
	"strconv"
	"strings"
)

func prints() {
	fmt.Println("Hello, World!")
	fmt.Println(1+2)
}

func variables() {
	// With := operator:
	name := "Samil"
	surname := "Boyalikli"
	age := 27
	fmt.Println(name + ", " + surname + ", " + fmt.Sprint(age))
	fmt.Println(fmt.Sprintf("%s, %s, %d", name, surname, age))
}

func received_input() {	
	var name string
	fmt.Print("What is your name?")
	fmt.Scanln(&name)
	fmt.Println("Hello,", name, ".")
}

func dataTypeConversion() {
	var year string
	fmt.Print("What year were you born?")
	fmt.Scanln(&year)
	birthyear, err := strconv.Atoi(year)
	if err != nil {
		fmt.Println("Invalid input. Please enter a valid year.")
		return
	}
	var age int
	age = 2025 - birthyear
	fmt.Printf("Your age in 2025 will be: %d\n", age)
}

func stringOperations() {
	var word string
	word = "Golang is so easy."
	fmt.Println(strings.ToUpper(word))
	fmt.Println(strings.ToLower(word))
	fmt.Println(strings.Index(word,"G"))
	fmt.Println(strings.Index(word,"Golang"))
	fmt.Println(strings.Replace(word, "Golang", "Python", -1))
	fmt.Println(strings.Contains(word, "Golang"))
	fmt.Println(strings.Contains(word, "Python"))
}

func arithmetic_operators() {
	fmt.Println(10+3)
	fmt.Println(10-3)
	fmt.Println(10*3)
	fmt.Println(10/3)
	fmt.Println(10.0/3.0)
	fmt.Println(10%3)
	fmt.Println(math.Pow(10, 3))
	number := 10
	fmt.Println(number)
	number += 3
	fmt.Println(number)	
}

func comparisonOperators() {
	fmt.Println("x=10>3")
	x:=10>3
	fmt.Println(x)
	fmt.Println(10>3)
	fmt.Println(10<3)
	fmt.Println(10>=3)
	fmt.Println(10<=3)
	fmt.Println(10==10)
	fmt.Println(10!=10)
}

func main() {
	//prints()
	//variables()
	//received_input()
	//dataTypeConversion()
	//stringOperations()
	//arithmetic_operators()
	comparisonOperators()
}

