# dict字典采用key-value方式的储存，可以根据key值快速得到其value值
chengji={'小明':99,'小红':92,'小刚':95}
print(chengji['小明'])
# 将数据存入字典也可以通过key放入
chengji['小蓝']=90
print(chengji)
# 由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉
chengji['小红']=96
print(chengji)
# 通过in方法来判断key值是否存在在字典中，返回的结果是布尔型。
print('小蓝' in chengji)
# 通过字典的get方法来获取字典值
print(chengji.get('小黑',-1))
# 通过字典的pop(key)方法删除字典值并返回其values值
print(chengji.pop('小刚'))
print(chengji)
# 通过字典的items()方法可以返回字典的键值对列表
print(chengji.items())
# 通过字典的keys()方法可以返回字典的键列表
print(chengji.keys())
# 通过字典的values()方法可以返回字典的值列表
print(chengji.values())
# 通过字典的clear()方法可以删除所有元素，但不能返回其键与值
#chengji.clear()
# del函数可以删除指定的字典值,但不能返回其values值
del(chengji['小红'])
print(chengji)
# setdefault往字典中增加条目，如果存在则添加失败
chengji.setdefault('小红',95)
print(chengji)