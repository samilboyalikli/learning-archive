import pandas as pd

XLSX_YOLU = "xlsx_path"
OUTPUT_TXT_YOLU = "txt_path"

timecode_list = []

try:
    df = pd.read_excel(XLSX_YOLU, header=None)
    E_SUTUN_INDEKSI = 4

    if E_SUTUN_INDEKSI in df.columns:
        secilen_aralik = df[E_SUTUN_INDEKSI].iloc[2:]
        timecode_list = secilen_aralik.dropna().astype(str).tolist() # NaN ögeleri temizleme satırı
        timecode_list = [tc.strip() for tc in timecode_list] # boşluk temizleme satırı
    else:
        print("Mevcut Sütunlar:", list(df.columns))

    if timecode_list:
        print(f"Excel'den {len(timecode_list)} adet timecode başarıyla çekildi.")
        with open(OUTPUT_TXT_YOLU, mode='w', encoding='utf-8') as txt_file:
            txt_file.write(f"timecode_list = {str(timecode_list)}\n\n")
        print(f"Başarılı! Kullanıcılar için hazırlanan TXT dosyası burada oluşturuldu:\n{OUTPUT_TXT_YOLU}")
        
except Exception as e:
    print("Excel veya TXT işlemi sırasında bir hata oluştu:", str(e))
