1. ilgili bölümün qc.xlsx dosyası bu projenin dizinine kopyalanır.
2. da vinci resolve'da mxf dosyası açılır.
3. da vinci resolve'da f6 ile python console açılır.
4. timecode_list ile xlsx dosyasından timecode'lar çekilir.
5. timecode listesi add_marker'a verilir.
6. add_marker'daki fonksiyon python console'a kopyalanır.
7. python console'da `add_marker(resolve)` metodu artık çalıştırılabilir.
> Bu sayede ilgili framelere marker eklenmiş oldu.
8. grap_still metodu python console'a kopyalanır.
9. python console'da `grap_still(resolve)` metodu çalıştırılır.
> Böylece markered frameler da vinci'nin local galerisine çekilmiş olur.
10. zaten galeri açılmış olacak ve oradan ctrl+a ile tüm galeri seçilir.
11. jpg olarak export edilebilir.
> Böylece artık jpg'leri elde etmiş olduk. Galeri temizlenmelidir.
12. jpg'leri kaydettiğimiz dosyada görseller üzerinde sorunları gösteririz.
13. log_prepare ile problem görsellerine gireceğimi logları txt olarak alırız.
14. görselleri notion'a yollayıp log.txt'teki ilgili hata logunu üstüne kopyalarız.
15. ardından sonradan oluşan eklenen tüm dosyaları sileriz.