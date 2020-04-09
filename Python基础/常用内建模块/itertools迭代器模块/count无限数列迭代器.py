from itertools import count

# count(start,step=none):可以生成一个以start开始每次增长step的无限数列迭代器。
Iterable=count(1,3)
for i in Iterable:
    if i>20:
        break
    print(i)