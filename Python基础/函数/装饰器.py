# 给函数增加装饰器只需要在函数前加@装饰器函数，装饰器函数以函数作为参数必须要返回函数。
def zhuangshi(func):
    print('增加其他功能！')
    return func
@zhuangshi
def foo(name):
    print('my nane is',name)
foo('boy')