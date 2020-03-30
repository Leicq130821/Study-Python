# 函数可以赋值给变量
function=abs
print(function(-10))
function=pow
print(function(2,3))
# 函数的参数可以接收变量
a=10
def test(x,y):
    print(x*y)
test(10,a)
# 当函数的变量为函数时，这种函数就称之为高阶函数。
f=pow
def test1(x,y,function):
    print(function(x,y))
test1(2,4,f)