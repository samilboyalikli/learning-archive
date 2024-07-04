import openpyxl

ana_excel_dosyasi = openpyxl.load_workbook('main_file.xlsx')
# load_workbook(file.xlsx) = belirtilen excel dosyasını çalışmaya hazır hale getirir
ana_sayfa = ana_excel_dosyasi.active
# active özelliği workbooktaki hangi sayfayı aktif olarak kullanacağımızı belirtir:
        # örneğin: "second_sheet = workbook["Sheet2"]
        #           workbook.active = second_sheet"

hedef_excel_dosyasi = openpyxl.load_workbook('target_file.xlsx')
hedef_sayfa = hedef_excel_dosyasi.active

founded = set()
unfounded = set()

for satir in ana_sayfa.iter_rows(min_row=2, values_only=True):
# iter_rows() fonksiyonu belirtilen sayfayı satır bazında dolaşır
# ana_sayfa'nın ikinci satırından itibaren tüm değerleri "satir" olarak niteliyoruz
    kelime = satir[0]
    # iter.rows() fonksiyonuyla "satir" isimli dataları elde ettik, bunlar satırlar
    # şimdi de bunların ilk sütunlarındaki datayı çekiyoruz ve "kelime" adıyla niteliyoruz
    bulundu = False
    # bulundu bool'unu false değeriyle başlatıyoruz for döngüsüyle değişebilirliğini belirleyeceğiz
    for hedef_satir in hedef_sayfa.iter_rows(values_only=True):
    # hedef_sayfa'daki tüm değerleri hedef_satir olarak niteliyoruz
        if kelime in hedef_satir:
        # "kelime" değerini "hedef_satır" değerinin içinde bul
            bulundu = True
            # "bulundu" bool'unu True olarak değiştir, bu işleme bulunduğu taktirde geçilecek
            break
            # eğer "bulundu" ise aramaya devam etme
    if bulundu: # kelime eğer bulundu ise founded setine ekle
        founded.add(kelime)
    else: # kelime eğer bulunmadı ise unfounded setine ekle
        unfounded.add(kelime)

print(
len(founded),"""adet data bulundu, bulunanlar: 

""", sorted(founded),
"""

""",
len(unfounded),"""adet data bulunamadı, bulunamayanlar:

""", sorted(unfounded))
