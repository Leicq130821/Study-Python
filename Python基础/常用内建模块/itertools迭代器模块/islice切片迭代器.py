from itertools import islice

# islice(iterable,start,end,step):切片迭代器可以对iterable进行切片，start是开始索引，end是结束索引，step是间隔，start闭end开。
List=list(islice(range(20),1,19,2))
print(List)