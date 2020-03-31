class Classname():
    name='类的名称'
    def mult(self,x,y):
        return x*y
    def sum(self,x,y):
        return x+y
    def pow(self,x,y):
        return pow(x,y)
Instance=Classname()
# type(object)：获取对象的基本属性
print(type(Instance))
# dir(object)：获取对象的所有属性及方法
print(dir(Instance))
# hasattr(object,name)：判断对象是否有属性name，返回的结果是布尔型。
print(hasattr(Instance,'name'))
print(hasattr(Instance,'mult'))
print(hasattr(Instance,'sum'))
print(hasattr(Instance,'pow'))
print(hasattr(Instance,'average'))
# getattr(object,name,defaultvalue)：获取对象属性name的值，如果不存在属性name，则返回默认值。
print(getattr(Instance,'mult',1))
print(getattr(Instance,'name',1))
# setattr(object,name,value)：设置对象的属性，如果对象不存在属性name则增加属性name，如果存在则更改属性name的值。
setattr(Instance,'age',20)
print(getattr(Instance,'age',10))