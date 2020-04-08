from collections import Counter

# Count(iterable)返回一个计数器对象，统计每个元素出现的次数，并且将结果按从大到小生成一个字典，相同的统计次数先出现的元素在前。
# 计数器对象可以使用字典对应的方法。
count=Counter('abddcaeabe')
print(count)
# 结果可以进行遍历
for key,value in count.items():
    print(key,':',value)
# count.most_common(n):返回前n个重复次数最多的键值对，次数相同的取前一个。
print(count.most_common(1))
print(count.most_common(2))
# count.update()：增加元素的重复次数。
count.update('aaa')
print(count)
count.update({'a':1,'b':2})
print(count)
# count.subtract()：减少元素的重复次数。
count.subtract('aa')
print(count)
count.subtract({'a':1,'e':1})
print(count)