package main

import (
	"fmt"
)

// 13 - CREATING MAP WITHOUT JSON DECODER
func main() {
		il_nufus := map[string]int{
			"Bilecik": 210000,
			"İstanbul": 15000000,
			"Sakarya": 1000000,
		}
		for anahtar, deger := range il_nufus {
			fmt.Printf("İl: %s, Nüfus: %d\n", anahtar, deger)
		}
}

// 12 - MAP METHOD WITH JSON
// REQ: "encoding/json"
// func main() {
// 		sozluk := make(map[string]string)
// 		sozluk["IP"] = "Internet Protocol"
// 		sozluk["LAMP"] = "Linux Apache MySQL PHP"
// 		sozluk["GNU"] = "GNU is Not Unix"
// 		sozluk["WWW"] = "World Wide Web"
// 		sozluk["IMAP"] = "Internet Message Access Protocol"
// 		tum_elemanlar, _ := json.MarshalIndent(sozluk, "", " ")
// 		fmt.Println(string(tum_elemanlar))
// }

// 11 - USING MAP
// func main() {
// 		il_nufus := make(map[string]int)
// 		il_nufus["Bilecik"] = 210000
// 		il_nufus["İstanbul"] = 15000000
// 		il_nufus["Sakarya"] = 1000000
// 		fmt.Println(il_nufus["Bilecik"])
// 		fmt.Println(il_nufus)
// }

// 10 - COPY METHOD
// func main() {
// 		kaynak := []int{1,2,9,9}
// 		hedef := make([]int, 2)
// 		fmt.Println(kaynak, hedef)
// 		sayi := copy(hedef, kaynak)
// 		fmt.Println("Kopyalanan Eleman Sayısı:", sayi)
// 		fmt.Println(kaynak, hedef)
// }

// 9 - USING APPEND FUNC WITH TWO SLICE
// func main() {
// 		ilk := []int{1, 4}
// 		son := []int{5, 3}
// 		butun := append(ilk, son...)
// 		fmt.Printf("%v\n", butun)
// }

// 8 - USING SLICE WITH LEN AND CAP FUNCS
// There is a point: Slice format different between Golang and Python. Here first index include in process but last index not.
// func main() {
// 		dizi := [4]string{"a","b","c","d"}
// 		kesit := dizi[:3]
// 		fmt.Printf("1) Eleman Sayısı: %d, Kapasite: %d, %v\n", len(kesit), cap(kesit), kesit)
// 		kesit = append(kesit, "x")
// 		fmt.Printf("1) Eleman Sayısı: %d, Kapasite: %d, %v\n", len(kesit), cap(kesit), kesit)
// 		kesit = append(kesit, "y")
// 		fmt.Printf("1) Eleman Sayısı: %d, Kapasite: %d, %v\n", len(kesit), cap(kesit), kesit)
// 		kesit = kesit[2:]
// 		fmt.Printf("1) Eleman Sayısı: %d, Kapasite: %d, %v\n", len(kesit), cap(kesit), kesit)
// }

// 7 - USING SLICE WITH TURKISH CHARS
// func main() {
// 		slice := []int{1,0,7,1}
// 		for i, değer := range slice {
// 			fmt.Printf("İndeks: %d Değer: %d\n", i, değer)
// 		}
// }

// 6 - CODING A MATRIX WITH 2D ARRAY
// func main() {
// 		nokta := [3][2]int{{11, 12},{21, 22},{31, 32}}
// 		fmt.Println("Dizinin Tamamı:", nokta)
// 		fmt.Println("\n3x2 Matris Biçiminde:")
// 		for satir := 0; satir < 3; satir++ {
// 			for sutun := 0; sutun < 2; sutun++ {
// 				fmt.Print(nokta[satir][sutun], " ")
// 			}
// 			fmt.Println()
// 		}
// }

// 5 - RANGE USING WITHOUT FOR PARAMETER
// func main() {
// 		aday := [5]int{81, 100, 27, 95, 45}
// 		basarili := 0
// 		for _, puan := range aday {
// 			if puan >= 50 {
// 				basarili += 1
// 			}
// 		}
// 		fmt.Println("Başarılı Aday Sayısı:", basarili)
// }

// 4 - INSERTING DATAS ON THE ARRAY WITH RANGE
// func main() {
// 		aday:= [5]int{ 81, 100, 27, 95, 45 }
// 		for i, puan := range aday {
// 			if puan < 50 {
// 				fmt.Println(i, ". aday başarısız oldu:", puan)
// 			}
// 		}
// }

// 3 - INSERTING DATAS ON THE ARRAY DIRECTLY
// func main() {
// 		aday := [5]int {
// 			81,
// 			100,
// 			27,
// 			95,
// 			45,
// 		}
// 		var adaysayisi int = len(aday)
// 		for i := 0; i < adaysayisi; i++ {
// 			if aday[i] < 50 {
// 				fmt.Println(i, ". aday başarısız oldu:",  aday[i])
// 			}
// 		}
// }

// 2 - EXAMPLE OF FOR LOOP WITH ARRAYS
// func main() {
// 		var aday [5]float32
// 		var toplam float32
// 		aday[0] = 81
// 		aday[1] = 100
// 		aday[2] = 65
// 		aday[3] = 95
// 		aday[4] = 45
// 		for i := 0; i <= 4; i++ {
// 			toplam += aday[i]
// 		}
// 		fmt.Println("Toplam Aday Sayısı:", len(aday))
// 		fmt.Println("Ortalama:", toplam/5)
// }

// 1 - ARRAY
// func main() {
// 		var il [82]string
// 		il[1] = "Adana"
// 		il[54] = "Sakarya"
// 		il[16] = "Bursa"
// 		il[47] = "Mardin"
// 		fmt.Println(il[])
// 		fmt.Println(il[54])
// }
