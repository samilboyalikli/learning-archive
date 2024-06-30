from pypdf import PdfReader
# pypdf API'ndan PdfReader modülünü aktarıyoruz

reader = PdfReader("GeoBase_NHNC1_Data_Model_UML_EN.pdf")
page = reader.pages[3]

parts = []
# daha sonra kullanılmak üzere verilerin depolanacağı boş bir liste oluşturuyoruz
def visitor_body(text, cm, tm, font_dict, font_size):
# hangi bölümleri seçeceğimizi tanımlıyoruz
    y = tm[5]
    # almak istediğimiz verinin bulunduğu sayfanın dikey eksenindeki konumunu girdik
    if y > 50 and y < 720:
        # almak istediğimiz değerin y eksenindeki konumunu girdik
        parts.append(text)
#       parts listesindeki satırları birleştirip tek metin haline getirmesini istedik

page.extract_text(visitor_text=visitor_body)
# visitor_body fonksiyonuna uygun olan verileri çekmesini istedik
text_body = "".join(parts)
# çektiği verileri boşluk bırakmayacak nitelikte sunmasını istedik
print(text_body)
