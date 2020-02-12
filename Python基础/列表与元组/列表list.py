# 定义一个列表
classmates=['小红','小明','小刚']
# len()函数获取列表的元素个数
print(len(classmates))
# 使用索引访问列表元素
print(classmates[0])
print(classmates[len(classmates)-1])
# -1，-2，-3可以访问列表倒数几位的元素
print(classmates[-1])
print(classmates[-2])
print(classmates[-3])
# 往列表最后插入一个元素
classmates.append('小黄')
print(classmates)
# 往列表指定位置插入一个元素
classmates.insert(1,'小蓝')
print(classmates)
# 删除列表最后一个元素
classmates.pop()
print(classmates)
# 删除列表指定位置的元素
classmates.pop(1)
print(classmates)
# 替换列表的元素
classmates[0]='小白'
print(classmates)
# 列表中包含列表
classmates.insert(1,['小红','小蓝'])
print(classmates)
print(classmates[1][1])