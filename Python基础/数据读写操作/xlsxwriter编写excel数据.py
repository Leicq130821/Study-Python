import xlsxwriter

# 实例化excel对象。
excel=xlsxwriter.Workbook(r'D:\自动化测试\xlsxwriter.xlsx')
# 添加sheet。
sheet=excel.add_worksheet('工作表1')
# 写入数据。
sheet.write(2,3,10000)
sheet.write_string(3,4,'中国')
sheet.write('F6','浙江省杭州市余杭区')
# 关闭文件（必须执行这一步）
excel.close()