# Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，
# 然后，在缩进块中编写函数体，函数的返回值用return语句返回
def test(x):
    if x>=0:
        return x
    else:
        return -x
print(test(-10))
# 如果想定义一个什么事也不做的空函数，可以用pass语句。
# pass作为占位符，比如没有想好的的函数代码可以先放一个pass，这样子不会影响到程序的执行。
def PASS(x):
    pass
PASS(10)
# 函数可以有多个返回值，返回值其实是一个tuple元组。
def tests(x,y):
    return x+y,x*y
a,b=tests(4,5)
print(a,b)
print(tests(4,5)[0])
print(tests(4,5)[1])
# 定义函数参数值可以给默认值，在调用这种类型的函数，有默认值的参数可以不用给，但要注意默认值参数的位置都是在没默认值参数的后面。
def function(x,y,z=10):
    print(x+y+z)
function(1,2)
function(1,2,3)
# 可变参数的函数
def test(*number):
  sum=0
  for i in number:
    sum=sum+pow(i,2)
  print(sum)
test(1,2,3,4)
set={1,2,3,4}
tuple=(1,2,3,4)
list=[1,2,3,4]
test(*set)
test(*tuple)
test(*list)