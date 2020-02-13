# 必选参数是函数中最常用的参数类型，在调用含有必选参数函数时，参数必须传入，且参数对应的值有且仅有一个。
def test1(x,y):
    print(x*y)
test1(4,5)
# 定义函数参数值可以给默认值，在调用这种类型的函数，有默认值的参数可以不用给，但要注意默认值参数的位置都是在没默认值参数的后面。
def test2(x,y,z=10):
    print(x+y+z)
test2(1,2)
test2(1,2,3)
# 可变参数的函数，传入的参数个数是可以变的，函数接受到的参数是一个tuple元组，定义时只需要在参数名称前加*。
# 可变参数的函数可以使用列表、元组、集合来作为参数，使用时只需要在列表元组集合前也加*即可。
def test3(*number):
  sum=0
  for i in number:
    sum=sum+pow(i,2)
  print(sum)
test3(1,2,3,4)
set={1,2,3,4}
tuple=(1,2,3,4)
list=[1,2,3,4]
test3(*set)
test3(*tuple)
test3(*list)
# 关键字参数也允许传入任意个参数，这些参数在函数内部自动组装为一个dict字典,定义时只需要在参数名称前加**。
# 关键字参数的函数可以使用字典作为参数，使用时只需要在字典前也加**即可。
def test4(**number):
    print(number)
    for num in number:
        print(num,':',number[num])
test4(a=1,b=2)
dict={'a':1,'b':2,'c':3}
test4(**dict)
# 关键字参数可以传入任意个参数，如果想要限制关键字参数的名字以及个数的话，则可以通过命名关键字参数的形式，命名关键字用*与位置参数分隔。
def test5(a,b,*,c,d):
    sum=a+b
    sum=sum+c+d
    print(sum)
test5(1,2,c=3,d=4)
# 如果函数以及包含可变函数，那么*可以省略,但调用函数时一定传入关键字参数，否则会报错。
def test6(a,b,*numbers,d,e):
    sum=a+b
    for num in numbers:
        sum=sum+num
    sum=sum+d+e
    print(sum)
test6(1,2,3,4,5,6,d=7,e=8)
# 定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但需要注意参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数、关键字参数。
def test7(a,b=2,*c,d,**e):
    print('a=',a,'b=',b,'c=',c,'d=',d,'e=',e)
    sum=a+b+d
    for num in c:
        sum=sum+num
    for num in e:
        print(num)
        sum=sum+e[num]
    print(sum)
test7(1,2,3,4,5,d=6,f=7,g=8)