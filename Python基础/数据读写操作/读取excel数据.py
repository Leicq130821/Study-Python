import xlrd

# 实例化excel对象。
excel=xlrd.open_workbook(r'D:\自动化测试\data.xlsx')
# 实例化sheet对象。
sheet=excel.sheets()[1]
sheet=excel.sheet_by_index(1)
sheet=excel.sheet_by_name('Sheet1')
# 获取sheet行数。
print(sheet.nrows)
# 获取sheet列数。
print(sheet.ncols)
# 获取sheet某行数据。
row=sheet.row(1)
print(row)
# 获取sheet某列数据。
col=sheet.col(0)
print(col)
# 获取某行的某列值。
print(row[1].value)
# 获取某列的某行值。
print(col[0].value)
# 获取sheet某行某列值。
print(sheet.cell(2,0).value)