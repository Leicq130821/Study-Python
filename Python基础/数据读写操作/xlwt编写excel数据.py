import xlwt

# 创建excel对象。
excel=xlwt.Workbook(encoding='utf-8')
# 创建sheet工作表。
sheet=excel.add_sheet('工作表1')
# 往sheet中写入数据。
sheet.write(4,5,'中国')
# 生成excel文件。
excel.save(r'D:\自动化测试\xlwt.xlsx')