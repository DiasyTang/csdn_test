import os
import sys

from xlrd import open_workbook


class ReadExcel:
    def get_xls(self, xls_name, sheet_name):
        cls = []
        # 获取用例文件路径
        xlsPath = os.path.join(os.path.abspath("."), "data", xls_name)
        with open_workbook(xlsPath) as f:  # 打开用例Excel
            sheet = f.sheet_by_name(sheet_name)  # 获得打开Excel的sheet
            # 获取这个sheet的内容行数
            nrows = sheet.nrows
            for i in range(nrows):
                if sheet.row_values(i)[0] != u"case_name":
                    cls.append(sheet.row_values(i))
            return cls


if __name__ == "__main__":
    readexcel = ReadExcel()
    print(readexcel.get_xls("userCase.xlsx", "login"))
    print(readexcel.get_xls("userCase.xlsx", "login")[0][1])
    print(readexcel.get_xls("userCase.xlsx", "login")[1][2])

