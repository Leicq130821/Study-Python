# eval(expression, globals=None, locals=None)：执行一个表达式，或字符串作为运算，也可以把字符串转换为列表、元组、字典、集合等，只能执行单个运算表达式，不能是复杂的代码逻辑。
# expression：必选参数，可以是字符串。
# globals：可选参数，表示全局命名空间（存放全局变量），如果被提供，则必须是一个字典对象。
# locals：可选参数，表示当前局部命名空间（存放局部变量），如果被提供，可以是任何映射对象。如果该参数被忽略，那么它将会取与globals相同的值。
print(eval('1+1'))
print(eval("'a'+'b'+'c'"))
print(eval("['a','b','c']"))
print(eval("('a','b','c')"))
print(eval("{'a':1,'b':2,'c':3}"))
print(eval("{'a','b','c'}"))
a=1
b=2
c=3
print(eval('a+b+c'))
print(eval('a+b+c',{'a':2,'b':3},{'b':5,'c':6}))
# exec(expression, globals=None, locals=None)：动态执行Python代码。
# exec可以执行复杂的Python代码，而不像eval函数那样只能计算一个表达式的值，而且与eval相比，exec()函数返回值永远都是None。
expression='''c=3
sum=a+b+c
print(sum)'''
exec(expression,{'a':1,'b':2,'c':4},{'a':3})