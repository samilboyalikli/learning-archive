import openpyxl

workbook = openpyxl.load_workbook("deneme.xlsx")
sheet = workbook.active
a_list = []

a = 1 + 0
a_list.append(a)

b = a + 1
a_list.append(b)

c = b + 1
a_list.append(c)

# eğer böyle olursa datalar farklı satırlara kaydedilir
data_to_insert = a_list
for row in data_to_insert:
    sheet.append([row])

# eğer böyle olursa datalar farklı sütunlara kaydedilir
data_to_insert = [a_list]
for row in data_to_insert:
    sheet.append(row)

workbook.save("deneme.xlsx")
