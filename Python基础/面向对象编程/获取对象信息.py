from Python基础.面向对象编程.class类 import Classname

instance=Classname()
# type()函数可以返回对象的基本属性。
print(type(instance))
# dir()函数可以返回对象的所有属性及方法。
print(dir(instance))
# hasattr()函数可以判断对象是否含有属性，返回的是布尔型。
print(hasattr(instance,'shuxing'))
print(hasattr(instance,'mult'))
print(hasattr(instance,'sum'))
# getattr()函数可以返回属性的值，如果属性是函数则返回函数本身。
print(getattr(instance,'shuxing'))
print(getattr(instance,'mult'))
print(getattr(instance,'sum'))
# setattr()函数给对象的属性赋值，如果属性不存在则添加属性，如果存在则改变属性的值。
setattr(instance,'name','增加对象属性name')
setattr(instance,'shuxing','改变了属性的值')
print(getattr(instance,'name'))
print(getattr(instance,'shuxing'))