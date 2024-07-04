import m_excel_comparator

comparator = m_excel_comparator.ExcelComparator()
comparator.main_file("main_file")
comparator.target_file("target_file")
comparator.compare()

print(len(comparator.found), "adet daha bulundu, bulunanlar:")
print(sorted(comparator.found))
print(len(comparator.unfound), "adet data bulunamadı, bulunamayanlar:")
print(sorted(comparator.unfound))
