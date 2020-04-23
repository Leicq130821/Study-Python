import os
#getcwd()：获取执行该函数的文件所在目录的绝对路径。
print(os.getcwd())
# os.path.realpath(__file__):获取当前文件的绝对路径。
print(os.path.realpath(__file__))
# mkdir(path)：创建单级目录，需要保证path里父级目录必须存在且创建的目录不存在,否则将会报错。
# rmdir(path)：删除单级目录，需要保证目录必须存在且为空目录，否则将会报错。
os.mkdir(r'D:\Python\mkdir\dir')
os.rmdir(r'D:\Python\mkdir\dir')
# makedirs(path)：如果path里父级目录不存在，则会一起创建，需要保证创建的最底层目录不存在，否则将会报错。
# removedirs(path)：如果path里有多级目录，则会删除多级目录，顺序是先删除子目录，然后再删除父目录，且目录为空时才能删除。
os.makedirs(r'D:\Python\makedirs\dirs')
os.removedirs(r'D:\Python\makedirs\dirs')
# chdir(path)：改变当前文件目录
# os.rename(oldpath,newpath)：重命名文件或者路径。
os.rename(r'D:\Python\TEST\test.txt',r'D:\Python\TEST\TEST.txt')
# os.path.join(path,filename)：目录与文件名称合成绝对路径。
print(os.path.join(r'D:\TEST','TEST.txt'))
# os.path.split(path)：拆分路径信息，返回两个元素的元组，后面一个元素为末级目录或者是文件名。
print(os.path.split(r'D:\Python\mkdir'))
print(os.path.split(r'D:\Python\TEST\TEST.txt'))
# os.path.splitext(path)：拆分路径信息，返回两个元素的元组，后面一个元素为文件扩展名。
print(os.path.splitext(r'D:\Python\mkdir'))
print(os.path.splitext(r'D:\Python\TEST\TEST.txt'))