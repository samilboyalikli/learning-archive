import logging

log_format = "%(asctime)s - %(levelname)s - %(message)s"
log_file = "app.log"

logging.basicConfig(
    level = logging.DEBUG,
    format = log_format,
    handlers = [
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

sayilar = [10,5,0,20,-5]

for sayi in sayilar:
    try:
        sonuc = 100 / sayi
        logging.info(f"100 / {sayi} = {sonuc}")
    except ZeroDivisionError:
        logging.error(f"Hata! 100 sayısı {sayi}'ya bölünemez!")

