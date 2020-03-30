# map(function,Iterable)function是函数，Iterable是可以进行迭代的对象，返回的是以迭代对象作为参数计算的函数结果并封装成一个Iterator迭代器。
# 迭代器是惰性序列，可以通过list()或者tuple()函数返回一个list或者tuple
def test(x):
    return x*x
print(map(test,range(10)))