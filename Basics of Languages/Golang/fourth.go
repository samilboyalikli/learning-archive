package main

import (
	"fmt"
)

func main() {
	// a := 5
	// b := 4
	// first function
	// >> topla_without_return(a,b)
	// second function
	// >> result_of_topla_with_return := topla_with_return(a,b)
	// >> fmt.Println("Toplam (fonksiyonun cevabı):", result_of_topla_with_return)

	// third function
	var toplam_for_third int
	aday := [5]int{40,100,15,70,45}
	for i := 0; i <= 4; i++ {
		toplam_for_third += aday[i]
	}
	fmt.Println("toplam aday sayısı =", len(aday))
	fmt.Println("ortalama =", toplam_for_third/5)
}

// This function can sum two integer. We can use this func without return as you see.
func topla_without_return(m, n int) {
	fmt.Println("sayıların toplamı =", m+n)
}

// This function can sum two integer. We are using this func with return.
func topla_with_return(a, b int) int {
	return a + b
}

