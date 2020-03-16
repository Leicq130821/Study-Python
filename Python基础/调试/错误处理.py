# try...except...finally处理错误机制,try来执行语句，遇到错误后面的代码将不会执行。
# 然后跳转到错误处理部分:except,如果捕捉到相对应的异常,则执行except模块内容,异常信息还可以进行输出。
# 如果有finally模块,最后会执行finally模块,不管try模块里面的语句是否执行错误finally都会执行。
try:
    print('执行10除以0')
    print(10/0)
    print('执行10除以字符串5')
    print(10/'5')
except TypeError as E:
    print('被除数只能是数值')
    print(E)
except ZeroDivisionError as E:
    print('0不能作为除数！')
    print(E)
finally:
    print('我最后执行，且一定会执行！')

try:
    print('执行10除以字符串5')
    print(10/'5')
    print('执行10除以0')
    print(10/0)
except ZeroDivisionError as E:
    print('0不能作为除数！')
    print(E)
except TypeError as E:
    print('被除数只能是数值！')
    print(E)
finally:
    print('我最后执行，且一定会执行！')
# python判断错误的类型有很多，可以使用通用的Exception方法来判断。
try:
    print('执行10除以字符串5')
    print(10/'5')
    print('执行10除以0')
    print(10/0)
except Exception as E:
    print(E)
except ZeroDivisionError as E:
    print('0不能作为除数！')
    print(E)
except TypeError as E:
    print('被除数只能是数值！')
    print(E)
finally:
    print('我最后执行，且一定会执行！')