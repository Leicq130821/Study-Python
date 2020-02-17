# sorted(Iterable, key=None, reverse=False)排序函数，用来排序可迭代的对象。
# Key：主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
# reverse：排序规则，reverse = True 降序，reverse = False 升序（默认）。
list=[9,5,2,8,6]
print(sorted(list))
# 可以对字典的key、value、items进行排序。
dict={'a':9,'h':2,'c':7,'e':5,'g':10}
print(sorted(dict.keys()))
print(sorted(dict.values()))
print(sorted(dict.items(),key=lambda x:x[1],reverse=True))
# sort()是list自带的方法，只能应用在list，sorted()可以对所有可迭代的对象进行排序操作。
# sort()是对已经存在的列表进行操作，无返回值，而sorted()方法返回的是一个新的list，不会对传入的list产生影响。
list=[10,3,5,7,1,12]
print(sorted(list))
print(list)
print(list.sort())
print(list)