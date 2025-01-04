import time

with open("a-ab.txt", "r") as dosya:
    metin = dosya.read()

kelimeler = metin.split()

quotes = ['"' + kelime + '"' for kelime in kelimeler]

yeni_metin = " ".join(quotes)

with open("tirnakli_dosya.txt", "w") as dosya:
    dosya.write(yeni_metin)

time.sleep(3)

with open("tirnakli_dosya.txt", "r") as dosya2:
    metin2 = dosya2.read()

kelimeler2 = metin2.split()

kelimeler_virgullu = ', '.join(kelimeler2)

yeni_metin2 = f"{kelimeler_virgullu}"

with open("virgullu_dosya.txt", "w") as dosya2:
    dosya2.write(yeni_metin2)
