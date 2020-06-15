# 读取全部数据。
file=open(r'D:\Python\read.txt','r')
print(file.read())
file.close()
# 每次读取一行数据。
file=open(r'D:\Python\read.txt','r')
print(file.readlines())
print(file.readline())
print(file.readline())
print(file.readline())
file.close()
# 读取全部数据，并返回以行为元素的列表。
file=open(r'D:\Python\read.txt','r')
lines=file.readlines()
print(lines)
for line in lines:
    print(line.strip())
file.close()