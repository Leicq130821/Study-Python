# 切片根据索引可以取出列表元组指定范围的数,例如list[0:3]，取出列表索引0到3的数，但不包括3。
# 如果从第1个开始，0 可以省略list[:3]，想要从列表元组中的第n个开始取到最后一个，则直接写list[n:]
yuanzu=('a','b','c','d')
print(yuanzu[0:3])
print(yuanzu[1:])
# 切片支持取后面几个数，例如list[-3:]取出列表最后三个数。
print(yuanzu[-3:])
# 切片的其他操作：
liebiao=list(range(100))
print(liebiao)
print(liebiao[:10:2]) #前十个中每两个取一个
print(liebiao[::5]) #每五个取一个
# 切片还可以对字符串进行操作
str='abcdefg'
print(str[1:4])
print(str[:5:2])