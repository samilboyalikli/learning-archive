y_h_s_ = input("Zam Eklenecek Fiyat: ")
y_ = input("Eklenmek İstenen Zam Yüzdesi: ")

yuzdesi_hesaplanacak_sayi = float(y_h_s_)
yuzdesi = float(y_)
sonuc = yuzdesi_hesaplanacak_sayi * yuzdesi / 100

son_sayi = yuzdesi_hesaplanacak_sayi + sonuc
print("Son Tutar: ", son_sayi)
