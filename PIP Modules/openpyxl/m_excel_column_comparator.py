# moduler version of my excel_comparator tool
import openpyxl


class ExcelComparator:
    def __init__(self, m_file_name=None, t_file_name=None):
        self.m_file_name = m_file_name
        self.t_file_name = t_file_name
        self.found = set()
        self.unfound = set()

    def main_file(self, m_file_name):
        self.m_file_name = m_file_name

    def target_file(self, t_file_name):
        self.t_file_name = t_file_name

    def compare(self):
        if not self.m_file_name or not self.t_file_name:
            raise ValueError("Main file and target file names are required.")

        main_excel = openpyxl.load_workbook(f'{self.m_file_name}.xlsx')
        target_excel = openpyxl.load_workbook(f'{self.t_file_name}.xlsx')

        main_sheet = main_excel.active
        target_sheet = target_excel.active

        for row in main_sheet.iter_rows(values_only=True):
            data = row[0]
            found_ = False
            for target_row in target_sheet.iter_rows(values_only=True):
                if data in target_row:
                    found_ = True
                    break
            if found_:
                self.found.add(data)
            else:
                self.unfound.add(data)
