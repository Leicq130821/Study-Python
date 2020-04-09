from itertools import repeat
# repeat(object,times=None):生成一个重复times次object的迭代器，若times=None则无限次重复。
Repeat=repeat((1,2,3),2)
for i in Repeat:
    print(i)