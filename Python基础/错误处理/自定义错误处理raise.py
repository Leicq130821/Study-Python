# raise可以自定义抛出异常信息，当抛出异常时，异常后面的语句将不会执行。
try:
    num=10/2
    if num!=4:
        raise ValueError('数值错误')
    print('raise抛出异常，后面的语句将不会执行')
except Exception as E:
    print('raise抛出的异常可以被捕获')
    print(E)