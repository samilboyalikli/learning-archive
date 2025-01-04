
y_f_ = input("Ürünün Şimdiki Fiyatını Giriniz: ")
e_f_ = input("Ürünün Eski Fiyatını Giriniz: ")

y_f = float(y_f_)
e_f = float(e_f_)

zam = y_f - e_f
print(f"Ürüne {zam} tl zam yapılmıştır")

zam_yuzdesi = zam * 100 / e_f
print(f"Ürüne %{zam_yuzdesi} zam yapılmıştır.")
