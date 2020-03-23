import os
#getcwd()函数：获取当前目录的绝对路径。
print(os.getcwd())
# mkdir(path)函数：创建一级目录，需要保证path里父级目录必须存在且创建的目录不存在,否则将会报错。
# rmdir(path)函数：删除一级目录，需要保证目录必须存在且为空目录，否则将会报错。
os.mkdir(r'D:\mkdir\dir')
os.rmdir(r'D:\mkdir\dir')
# makedirs(path)函数：创建多级目录。
# removedirs(path)函数：删除多级目录。
os.makedirs(r'D:\makedirs\dirs\dir')
os.removedirs(r'D:\makedirs\dirs\dir')