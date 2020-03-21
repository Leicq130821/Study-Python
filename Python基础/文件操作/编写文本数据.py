# 写入数据
file=open(r'D:\Python\write.txt','w')
file.write('第一行')
file.close()
# 换行写入
file=open(r'D:\Python\write.txt','w')
file.write('第一行')
file.write('\n')
file.write('第二行')
file.write('\n第三行\n')
file.write('第四行')
file.close()