# Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，
# 然后，在缩进块中编写函数体，函数的返回值用return语句返回
def test1(x):
    if x>=0:
        return x
    else:
        return -x
print(test1(-10))
# 如果想定义一个什么事也不做的空函数，可以用pass语句。
# pass作为占位符，比如没有想好的的函数代码可以先放一个pass，这样子不会影响到程序的执行。
def PASS(x):
    pass
PASS(10)
# 函数可以有多个返回值，返回值其实是一个tuple元组。
def test2(x,y):
    return x+y,x*y
a,b=test2(4,5)
print(a,b)
print(test2(4,5)[0])
print(test2(4,5)[1])
# 当函数执行到return时，函数就执行完毕，并将结果返回，如果没有写返回值则返回None。
def test3(a):
    sum=0
    i=0
    while i<=a:
        i+=1
        sum=sum+i
        if i>3:
            return sum
print(test3(10))