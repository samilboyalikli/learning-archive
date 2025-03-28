// The file includes basics of golang.

package main

import (
	"fmt"
	"math"
	"strconv"
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
	var age int
	age = 2025 - 
	//<<<<<<<<<<<<---------------------------------------------------------------------------------------------------------
	
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

func main() {
	//prints()
	//variables()
	//received_input()
	dataTypeConversion()
	//arithmetic_operators()
}

