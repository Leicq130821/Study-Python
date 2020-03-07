# 创建类通过关键字class，后面紧跟着类的名称，紧接着就是括号，括号里面放着父类列表，表示这个类从哪里继承的。
# 每个类都会继承object类，object可以省略不写。
class Classname(object):
    def mult(self,x,y):
        print(x*y)
    def sum(self,x,y):
        print(x+y)
