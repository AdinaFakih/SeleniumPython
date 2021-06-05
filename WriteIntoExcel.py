import openpyxl
path = "C://Users//addyf//Downloads//MnS.xlsx"
workbook = openpyxl.load_workbook(path)
sheet = workbook.active  #workbook.get_sheet_by_name("MnS.xlsx")
for r in range(1,6):
    for c in range(1,4):
        sheet.cell(row=r, column=c).value = "welcome"

workbook.save(path)