import time

# dosyayı okutup metni alıyoruz
with open("a-ab.txt", "r") as dosya:
    metin = dosya.read()

# metni kelimelere bölüyoruz
kelimeler = metin.split()

# kelimelerin başına ve sonuna tırnak işareti ekliyoruz
kelimeler_tirnakli = ['"' + kelime + '"' for kelime in kelimeler]

# tırnak işareti eklenmiş kelimeleri birleştiyoruz
yeni_metin = " ".join(kelimeler_tirnakli)

# yeni metni bir dosyaya aktarıyoruz
with open("tirnakli_dosya.txt", "w") as dosya:
    dosya.write(yeni_metin)

# dosyanın kaydedilmesi için zaman tanıyoruz
time.sleep(3)

# kaydedilen dosyasını okutuyoruz
with open("tirnakli_dosya.txt", "r") as dosya2:
    metin2 = dosya2.read()

# metni kelimelere ayırıyoruz
kelimeler2 = metin2.split()

# kelimeleri virgülle birleştirtiyoruz
kelimeler_virgullu = ', '.join(kelimeler2)

# yeni metin oluşturuyoruz
yeni_metin2 = f"{kelimeler_virgullu}"

# yeni metni bir dosyaya yazıyoruz
with open("virgullu_dosya.txt", "w") as dosya2:
    dosya2.write(yeni_metin2)
