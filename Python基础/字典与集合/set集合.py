# 创建集合可以使用{}与set()方法，创建空的集合必须使用set()方法
# 使用set(str)方法的方法创建集合会把每字符串每一个字符拆分成元素
jihe=set('123456')
print(jihe)
# set()方法里面也通过列表的方式来定义元素
jihe=set(['a','b','c'])
print(jihe)
# 通过{}来创建集合
jihe={'d','e','f'}
print(jihe)
# add(key)方法可以往集合中添加元素
jihe.add('a')
print(jihe)
# update(x)方法,x可以多个用逗号隔开且x可以时元组、列表等
jihe.update(['g','h'],('i','j'))
print(jihe)
# remove(key)方法删除集合中的元素，若元素不存在则会报错
jihe.remove('d')
print(jihe)
# discard(key)方法删除集合中的元素，元素不存也不会报错
jihe.discard('c')
# 集合之间的运算
set1=set('abcdefg')
set2=set('efghijk')
# 集合1中含有的元素且集合2中不含有
set3=set1-set2
print(set3)
# 集合1、集合2所有元素
set4=set1|set2
print(set4)
# 集合1、集合2都含有的元素
set5=set1&set2
print(set5)
# 集合1、集合2不同时包含的元素
set6=set1^set2
print(set6)
# 清空集合
jihe.clear()