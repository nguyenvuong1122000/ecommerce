import openpyxl

data = openpyxl.load_workbook("maytinhbang.xlsx")
for (i, wordsheet) in enumerate(data):
