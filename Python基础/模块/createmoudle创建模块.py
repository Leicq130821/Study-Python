# -*- coding: utf-8 -*-
# 创建模块其实就是建一个.py文件，通常情况下会把类似的功能代码写在同一个.py文件中
# -*- coding: utf-8 -*-
class Moudle():
    def func1(x,y):
        return x*y-(x+y)
    def func2(x,y):
        return pow(x,y)-(x+y)
if __name__ == '__main__':
    print(Moudle.func1(4,2))
    print(Moudle.func2(4,2))