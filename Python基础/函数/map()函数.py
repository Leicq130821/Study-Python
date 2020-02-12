# map(function,iterable,...)：map是python内置函数，会根据提供的函数对指定的序列做映射。
# 第一个参数为函数名，后面的参数一个多个可迭代的序列，返回的是一个集合。
result=map(lambda x:pow(x,2),[1,2,3])
print(list(result))
result2=map(lambda x,y:(x+y,x*y),[1,2,3],[4,5,6])
print(list(result2))