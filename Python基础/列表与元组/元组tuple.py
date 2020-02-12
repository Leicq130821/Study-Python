# tuple和list非常类似，但是tuple一旦初始化就不能修改
classmates=('小明','小红')
print(classmates)
# 通过索引来访问元组的元素
print(classmates[0])
print(classmates[-1])
# 当元组中只有一个元素时需要在元素后面加上逗号来区分小括号
classmates=('小明',)
print(classmates)
# 当元组中元素包含列表时，可以对列表进行操作
classmates=('小明',['小红','小蓝'],'小刚')
classmates[1][1]='小白'
print(classmates)
classmates[1].insert(1,'小蓝')
print(classmates)
classmates[1].append('小林')
print(classmates)
classmates[1].pop(1)
print(classmates)