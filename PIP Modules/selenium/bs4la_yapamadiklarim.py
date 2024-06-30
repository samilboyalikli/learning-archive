import requests
# requests modülünü içe aktarıyoruz
from bs4 import BeautifulSoup
# beatifulsoup modülünü içe aktarıyoruz
def migros_fiyati():
    # fiyat çıkaracağımız bir fonksiyon yazıyoruz
    URL = 'https://www.migros.com.tr/sofra-ekmek-adet-p-4e2000'
    # url tanımlıyoruz
    Headers = {"user_agent": "buraya user agent'ınızı giriyorsunuz, onu google'dan bulabilirsiniz"}
    # user_agentımız siteye giriş kimliğimiz gibi, kimliksiz almıyorlar
    sayfa = requests.get(URL, headers=Headers)
    # sayfayı requests modülüyle user agent'ımızı kullanarak getiriyoruz
    icerik = BeautifulSoup(sayfa.content, 'html.parser')
    # BeautifulSoup modülüyle sayfanın içeriğini çekiyoruz, BS html'i parse ediyor
    fiyat_span = icerik.select_one('span._ngcontent-gmg-c272')
    # içeriklerin içinden çıkartmak istediğimiz locator'ı giriyoruz
    return fiyat_span.text.strip() if fiyat_span else "Fiyat bulunamadı"
# locator'un programı götürdüğü yerdeki metni çekiyoruz, strip() fonksiyonuyla boşlukları kesiyoruz
# bulunamama ihtimaline karşı küçük bir if else giriyoruz
print("Migros'ta Ekmek Fiyatı: ", migros_fiyati())
# veee fiyat...
# ne yazık ki karşımızda değil, çünkü javascript kodları dinamik biçimde kodlanmış
# program source kodlarında locator'ımızı bulamıyor
