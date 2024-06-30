from selenium.webdriver.support.ui import WebDriverWait
# tarayıcının açılması için programa süre tanıyorum
from selenium.webdriver.support import expected_conditions as EC
# tarayıcının açılması, web sayfasının görülmesi gibi parametrelerde programın sürprizle karşılaşmasını bu paketle önlüyorum
from selenium import webdriver
# webdriver'ı içeri aktarıyorum
from selenium.webdriver.common.by import By
# xpath'i okuturken kullanacağım bazı komutlar için By modülünü aktif ediyorum
from selenium.webdriver.chrome.service import Service
service = Service()
driver = webdriver.Chrome(service=service)
driver.get("https://www.migros.com.tr/sofra-ekmek-adet-p-4e2000")
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "(//span[@class='amount'])[1]"))
)
# eklediğim nesnelere göre XPATH girişini revize ettim
print(element.text)
