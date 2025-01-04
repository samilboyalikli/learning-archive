
while True:
    y_h_s_ = input("Yüzdesi Hesaplanacak Sayı: ")
    y_ = input("Hesaplanmak istenen Yüzde: ")

    yuzdesi_hesaplanacak_sayi = float(y_h_s_)
    yuzdesi = float(y_)

    sonuc = yuzdesi_hesaplanacak_sayi * yuzdesi / 100
    print(sonuc)

    q_button = input("Programı Kapatmak İçin 'y' Devam Etmek İçin 'n' Tuşuna Basınız: ")
    if q_button.lower() == 'y':
        break
    elif q_button.lower() == 'n':
        continue
