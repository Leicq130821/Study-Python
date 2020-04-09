from itertools import cycle

# cycle(iterable):可以把iterable变成无限循环迭代的迭代器。
Iterable=('ab','cd','ef')
Cycle=cycle(Iterable)
count=len(Iterable)*2
i=0
for iter in Cycle:
    i+=1
    print(iter)
    if i==count:
        break