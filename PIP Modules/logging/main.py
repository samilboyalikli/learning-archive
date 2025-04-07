import logging


def logging_without_setting_handlers():
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


def logging_setting_handlers():
    
    # basicConfig() kullanamıyoruz çünkü sınırlı bir yapı kuruluyor.
    # getLogger() || addHandler() gibi metotlarla daha esnek bir yapı kurabiliriz.
    
    # logging modülünden getLogger() metoduyla bir logger oluşturduk:
    logger = logging.getLogger()
    
    # oluşturduğumuz logger'ın seviyesini belirledik:
    logger.setLevel(logging.DEBUG)
   
    # logging modülünden FileHandler() sınıfını çekerek logları dosyaya yazıyoruz:
    file_handler = logging.FileHandler("app.log")

    # oluşturduğumuz file_handler'ın hangi seviyedeki logları yazacağını belirliyoruz:
    file_handler.setLevel(logging.DEBUG)

    # logging modülünden StreamHandler() çekerek logları console'a yazıyoruz:
    stream_handler = logging.StreamHandler()

    # oluşturduğumuz stream_handler'ın hangi seviyedeki logları yazacağını belirliyoruz:.
    stream_handler.setLevel(logging.INFO)

    # addFilter() metodu için bir nesne oluşuruyoruz, çünkü addFilter(); .filter(record) nesnesi bekler:
    class InfoFilter(logging.Filter):
        def filter(self, record):
            return record.levelno == logging.INFO
    
    # addFilter() - handlerları filtreleme metodumuz bu sanırım.
    stream_handler.addFilter(InfoFilter())
 
    # burada ekleyeceğimiz handler'ların formatlarını ayarlıyoruz:
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    # anladığı kadarıyla burada handler ekliyoruz:
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)


if __name__ == "__main__":
    
    logging_setting_handlers()
    
    sayilar = [10,5,0,20,-5]
    for sayi in sayilar:
        try:
            sonuc = 100 / sayi
            logging.info(f"100 / {sayi} = {sonuc}")
        except ZeroDivisionError:
            logging.error(f"Hata! 100 sayısı {sayi}'ya bölünemez!")



