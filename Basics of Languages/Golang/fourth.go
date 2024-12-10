package main

import (
	"fmt"
)

func main() {
	isim:=isim_al()
	yaş:=yaş_al()
	fmt.Println("\nHoşgeldiniz %s, Yaşınız: %d. ",isim,yaş)
	kontrol_et(yaş)
}
func isim_al() (isim string) {
	fmt.Print("İsminiz: ")
	fmt.scanln(&isim)
	return
}
func yaş_al() (yaş int) {
	fmt.Print("Yaşınız: ")
	fmt.scanln(&yaş)
	return
}
func kontrol_et(yaş int) {
	switch {
	case yaş < 18:
		fmt.Println("Sisteme giriş için yaşınız müsait değil. ")
	case yaş < 120:
		fmt.Println("Sisteme başarılı olarak giriş yaptınız. ")
		oturum_aç()
	default:
		fmt.Println("Şaka yapıyorsunuz değil mi?")
	}
}
func oturum_aç() {fmt.Println("İşiniz bitince oturumunuzu kapatmayı unutmayın.")}

// 8.
// func main() {
// 		a:=5
// 		b:=2
// 		fmt.Println("Bölüm =",böl(a,b))
// }
// func böl(a,b int) int {
// 		return a/b
// }

// 7.
// func main() {
// 		var a,b int=1,2
// 		fmt.Println(a,b)
// 		a,b=b,a
// 		fmt.Println(a,b)
// }

// 6.
// func değiştir(x,y int) (int,int) {
// 		return y,x
// }
// func main() {
// 		a:=1
// 		b:=2
// 		fmt.Println(a,b)
// 		a,b=değiştir(a,b)
// 		fmt.Println(a,b)
// }

// 5.
// var a, b int = 1, 2
// func değiştir() {
// 		gecici := a
// 		a = b
// 		b = gecici
// }
//func main() {
//		fmt.Println(a,b)
//		değiştir()
//		fmt.Println(a,b)
//}

// 4.
// func main() {
// 		aday := []int{40,100,15,70,45}
// 		fmt.Println("Ortalama =", ort(aday))
// }
//func ort(elemanlar []int) int {
//		var toplam int
//		for _, puan := range elemanlar {
//			toplam += puan
//		}
//		return toplam/len(elemanlar)
//}

// 3. 
// func main() {
// 		// Third Function
// 		var toplam_for_third int
// 		aday := [5]int{40,100,15,70,45}
// 		for i := 0; i <= 4; i++ {
// 			toplam_for_third += aday[i]
// 		}
// 		fmt.Println("toplam aday sayısı =", len(aday))
// 		fmt.Println("ortalama =", toplam_for_third/5)
// }

// 2.
// func main() {
// 		a := 5
// 		b := 4
// 		-> Second Function
// 		result_of_topla_with_return := topla_with_return(a,b)
// 		fmt.Println("Toplam (fonksiyonun cevabı):", result_of_topla_with_return)
// }
// -> This function can sum two integer. We are using this func with return.
// func topla_with_return(a, b int) int {
// 		return a + b
// }

// 1.
// func main() {
// 		a := 5
// 		b := 4
// 		-> First Function
// 		topla_without_return(a,b)
// }
// -> This function can sum two integer. We can use this func without return as you see.
// func topla_without_return(m, n int) {
// 		fmt.Println("sayıların toplamı =", m+n)
// }
