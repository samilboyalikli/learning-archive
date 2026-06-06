import os

TARGET_FOLDER = "target_folder"

try:
    if os.path.exists(TARGET_FOLDER):
        silinen_dosya_sayisi = 0
        for dosya_adi in os.listdir(TARGET_FOLDER):
            if dosya_adi.lower().endswith('.drx'):
                tam_yol = os.path.join(TARGET_FOLDER, dosya_adi)
                os.remove(tam_yol)
                silinen_dosya_sayisi += 1
                print(f"Silindi: {dosya_adi}")
        if silinen_dosya_sayisi > 0:
            print(f"\nİşlem başarıyla tamamlandı! Toplam {silinen_dosya_sayisi} adet .drx dosyası temizlendi.")
        else:
            print("\nKlasörde silinecek herhangi bir .drx uzantılı dosya bulunamadı.")
    else:
        print(f"Hata: Belirtilen klasör yolu bulunamadı: {TARGET_FOLDER}")
except Exception as e:
    print(f"Dosyalar silinirken bir hata meydana geldi: {str(e)}")
    
