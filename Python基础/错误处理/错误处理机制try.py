# try...except...finally处理错误机制,try模块来执行语句如果遇到错误，try模块错误后面的代码将不会执行。
# 然后跳转到错误处理部分:except,except如果捕捉到相对应的异常,则执行except模块内容,异常信息还可以进行输出。
# 如果有finally模块,最后会执行finally模块,不管try模块里面的语句是否执行错误finally都会执行。
try:
    print('执行10除以0')
    print(10/0)
    print('出现了错误，后面的将不会执行')
    print('执行10除以字符串5')
    print(10/'5')
except TypeError as E:
    print('被除数只能是数值')
    print(E)
except ZeroDivisionError as E:
    print('捕捉到相应的错误，我将会执行')
    print('0不能作为除数！')
    print(E)
finally:
    print('不管try模块是否发生错误，我都会执行，且最后执行！')
# python判断错误的类型有很多，可以使用通用的Exception方法来判断。
try:
    print('执行10除以字符串5')
    print(10/'5')
    print('执行10除以0')
    print(10/0)
except Exception as E:
    print(E)
# 可以在except语句块后面加一个else，如果没有错误发生时，会执行else语句。
try:
    print('执行10除以2')
    print(10/2)
    print('执行5乘以2')
    print(5*2)
except Exception as E:
    print(E)
else:
    print('try模块中没有发生错误，将会执行else模块。')
# 使用try...except捕获错误还有一个好处是可以跨越多层调用。
def bar(x):
    return 10/x
def foo(x):
    return bar(x)*2
def main(x):
    try:
        return foo(x)+2
    except Exception as E:
        print(E)
    finally:
        print('我最后执行')
main(0)