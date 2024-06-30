
# pypdf modülünü indirmek için:
# pip install pypdf

from pypdf import PdfReader
# pypdf API'ndan PdfReader modülünü çekiyoruz

reader = PdfReader("sozluk.pdf")
# programı yazdığımız .py dosyasıyla programın okuyacağı .pdf dosyası aynı dizinde olmak zorunda
# aksi halde .pdf dosyasının dizinini programa tarif etmek zorundayız
# örneğin:
# reader = PdfReader("C:\\Users\\Kullanıcı\\Belgeler\\sozluk.pdf")
page = reader.pages[1]
# hangi sayfayı yazdıracağımızı burada tanımlıyoruz
print(page.extract_text())
# tanımlı sayfayı yazdırıyoruz
