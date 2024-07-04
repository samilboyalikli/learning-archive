"""EXCEL DOSYASINDA BOŞ HÜCREYE VERİ YAZMA"""

import openpyxl

workbook = openpyxl.load_workbook("deneme0.xlsx")
sheet = workbook.active

empty_cell = None
for cell in sheet["A"]:
    if cell.value is None:
        empty_cell = cell
        break

if empty_cell:
    empty_cell.value = "Veri Eklenecek"
else:
    print("boş hücre bulunamadı")

workbook.save("deneme1.xlsx")
