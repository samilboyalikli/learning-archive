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

func logicalOperators() {
	value := 10
	fmt.Println(value > 50 && value < 100)
	fmt.Println(value > 50 || value < 100)
	fmt.Println(!(value < 50))
}

func conditionalStatement() {
	var grade int
	fmt.Print("What is your grade? ")
	fmt.Scan(&grade)

	if grade >= 50 {
		fmt.Println("Congratulation. You succeeded.")
	} else if grade <= 50 {
		fmt.Println("Unfortunately. You must try again.")
	} else {
		fmt.Println("There is no grade like you wrote.")
	}
}

func keywords() {
	var keywords string
	keywords = `break
case
chan
const
continue
default
defer
else
fallthrough
for
func
go
goto
if
import
interface
map
package
range
return
select
struct
switch
type
var`
	fmt.Println(keywords)
}

func bmi_index() {
	var weight float64
	fmt.Print("Weight: ")
	fmt.Scan(&weight)
	var height float64
	fmt.Print("Height: ")
	fmt.Scan(&height)
	var bmi float64
	bmi = weight/float64(math.Pow(float64(height),2))
	rounded_bmi := math.Round(bmi*100)/100
	
	if rounded_bmi < 18.5 {
		fmt.Println("Underweight")
	} else if 18.5 <= rounded_bmi && rounded_bmi < 25.0 {
		fmt.Println("Normal Weight")
	} else if 25.0 <= rounded_bmi && rounded_bmi < 30.0 {
		fmt.Println("Overweight")
	} else if 30.0 <= rounded_bmi && rounded_bmi < 40.0 {
		fmt.Println("Obese")
	} else if 40.0 <= rounded_bmi {
		fmt.Println("Morbidly Obese")
	} else {
		fmt.Println("There is a problem.")
	}
}

func main() {
	//prints()
	//variables()
	//received_input()
	//dataTypeConversion()
	//stringOperations()
	//arithmetic_operators()
	//comparisonOperators()
	//logicalOperators()
	//conditionalStatement()
	//keywords()
	bmi_index()
}

