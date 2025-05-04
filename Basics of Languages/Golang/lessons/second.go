package main

import (
	"fmt"
)

// 9 - LOGICAL PROBLEM
func main() {
	sayi := 0
	switch {
	case sayi > 0:
		fmt.Println("Pozitive")
	default:
		fmt.Println("Negative")
	}
}

// 8 - SWITCH USING AS A IF BLOCK
func main() {
	sinav_notu := 50
	switch {
	case sinav_notu < 40:
		fmt.Println("Çok düşük!")
	case sinav_notu < 55:
		fmt.Println("İyi değil...")
	case sinav_notu < 70:
		fmt.Println("İdare eder...")
	case sinav_notu < 80:
		fmt.Println("Güzel...")
	default:
		fmt.Println("Çok güzel, tebrikler.")
	}
}

// 7 - SWITCH BLOCK SAMPLE
func main() {
	plaka_no := 16
	switch plaka_no {
	case 53:
		fmt.Println("Rize")
	case 54:
		fmt.Println("Sakarya")
	case 55:
		fmt.Println("Samsun")
	default:
		fmt.Println("Bilinmeyen Kod")
	}
}

// 6 - CORRECTED IF BLOCK (with many if)
func main() {
	var i, b2, b3, b4 int
	for i = 1; i <= 100; i++ {
		if i%2 == 0 {
			b2++
		}
		if i%3 == 0 {
			b3++
		}
		if i%4 == 0 {
			b4++
		}
	}
	fmt.Printf("2:%d, 3:%d, 4:%d\n", b2, b3, b4)
}

// 5 - IF ELSE CONTRUCT WITH A SIMPLE ERROR
func main() {
	var i, b2, b3, b4 int
	for i = 1; i <= 100; i++ {
		if i%2 == 0 {
			b2++
		} else if i%3 == 0 {
			b3++
		} else if i%4 == 0 {
			b4++
		}
	}
	fmt.Println("2:%d, 3:%d, 4:%d", b2, b3, b4)
}

// 4 - IF BLOCK SAMPLE WIHTOUT ELSE
func main() {
		for i := 1; i <= 10; i++ {
			if i%2 == 0 {
				fmt.Println(i)
			}
		}
}

// 3 - ETERNAL LOOP
func main() {
		for {
	
		}
}

// 2 - FOR LOOP REPLACING WHILE (without init and iter)
func main() {
		i := 1
		toplam := 0
		for i <= 5 {
			i++
			toplam = toplam+i
		}
		fmt.Println("Toplam: ", toplam)
}

// 1 - CANONICAL FOR LOOP (initialization, condition, iteration)
func main() {
		for i := 1; i <= 4; i++ {
			fmt.Println(i)
		}
}
