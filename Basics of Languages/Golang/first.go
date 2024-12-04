package main

import (
	"fmt"
)

// 9.
func main() {
	isim := "Ayşe"
	isim = "Sare"
	memleket := "Sakarya"
	fmt.Println(isim + memleket)
}

// 8. 
//import (
//		"fmt"
//		"reflect"
//)
// func main() {
// 		var a = 3
// 		var b = 5
// 		var c = "go"
// 		fmt.Println("Toplam: ", a+b)
// 		fmt.Println(reflect.TypeOf(a), reflect.TypeOf(c))
// }

// 7.
// func main() {
// 		const sakarya int = 54
// 		const ülke string = "TR"
// 		fmt.Println(sakarya, ülke)
// }

// 6.
// func main() {
// 		var isim, parola, eposta bool
// 		isim = true
// 		parola = true
// 		eposta = false
// 		fmt.Println(isim && parola)
// 		fmt.Println(eposta || isim)
// 		fmt.Println(!isim)
// 		fmt.Println("Sakarya" == "Adapazarı")
// }


// 5.
// func main() {
// 		var ad, soyad string
// 		ad = "Sait\tFaik"
// 		soyad = "\nAbasıyanık"
// 		fmt.Println(ad+soyad)
// }

// 4.
// func main() {
// 		fmt.Println("Sakarya\tBilecik\tBursa\nİzmir\tVan\tBayburt\nTürkiye")
// }

// 3.
// func main()  {
// 		var bolum float32
// 		bolum = 8.0 / 25.0
// 		fmt.Println("Bölüm: ", bolum)
// }
// -> kullanacağımız float veri türünün daha hassas olmasını istiyorsak float32 yerine float64 kullanabiliriz.

// 2.
// func main() {
// 		var sayi1, sayi2 int
// 		sayi1 = 3
// 		sayi2 = sayi1 + 5
// 		fmt.Println("Sayıların Toplamı: ", sayi1+sayi2)
// }

// 1.
// func main() {
// 		fmt.Println("Hello, World!")
// }