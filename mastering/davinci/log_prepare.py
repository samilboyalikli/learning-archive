import pandas as pd

XLSX_YOLU = "xlsx_path"
OUTPUT_TXT_YOLU = "txt_path"

try:
    df = pd.read_excel(XLSX_YOLU, header=None)
    timecode_column = 4      # E Sütunu
    problem_column = 5       # F Sütunu
    subject_column = 6       # G Sütunu
    explanation_column = 7   # H Sütunu
    gerekli_sutunlar = [timecode_column, problem_column, subject_column, explanation_column]
    
    if all(col in df.columns for col in gerekli_sutunlar):
        secilen_data = df.iloc[2:]
        with open(OUTPUT_TXT_YOLU, mode='w', encoding='utf-8') as txt_file:
            log_sayaci = 0
            for index, row in secilen_data.iterrows():
                if pd.isna(row[timecode_column]):
                    continue
                tc = str(row[timecode_column]).strip()
                problem = str(row[problem_column]).strip() if pd.notna(row[problem_column]) else "Belirtilmedi"
                subject = str(row[subject_column]).strip() if pd.notna(row[subject_column]) else "Belirtilmedi"
                explanation = str(row[explanation_column]).strip() if pd.notna(row[explanation_column]) else "Açıklama yok"
                txt_file.write(f"TIMECODE: {tc}\n")
                txt_file.write(f"PROBLEM TYPE: {problem}\n")
                txt_file.write(f"SUBJECT: {subject}\n")
                txt_file.write(f"EXPLANATION: {explanation}\n")
                txt_file.write("-" * 40 + "\n")
                log_sayaci += 1

        if log_sayaci > 0:
            print(f"Başarılı! Toplam {log_sayaci} adet QC kaydı '{OUTPUT_TXT_YOLU}' dosyasına yazıldı.")
        else:
            print("Excel dosyasında işlenecek geçerli bir timecode satırı bulunamadı.")

    else:
        print("Hata: Excel dosyasında hedef sütunlardan (E, F, G, H) biri veya birkaçı eksik!")
        print("Mevcut Sütunlar:", list(df.columns))
except Exception as e:
    print("Excel veya TXT işlemi sırasında bir hata oluştu:", str(e))
