# reduce(function,Iterable)传给reduce中的函数function（有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用function函数运算，以此类推最后得到一个结果。
from functools import reduce
def test1(x,y):
    return x*y
print(reduce(test1,range(1,6)))