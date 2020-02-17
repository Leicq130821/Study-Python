# exec(expression, globals=None, locals=None)：动态执行Python代码。
# exec可以执行复杂的Python代码，而不像eval函数那样只能计算一个表达式的值，而且与eval相比，exec()函数返回值永远都是None。
expression='''c=3
sum=a+b+c
print(sum)'''
exec(expression,{'a':1,'b':2,'c':4},{'a':3})