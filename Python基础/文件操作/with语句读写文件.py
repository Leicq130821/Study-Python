# with语句读取文件
with open(r'D:\Python\read.txt','r') as file:
    print(file.read())
# with语句编写文本数据
with open(r'D:\Python\write.txt','w') as file:
    file.write('with语句编写文本数据')