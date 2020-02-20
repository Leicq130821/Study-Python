# 使用模块前，需要导入模块，导入的时候需要注意如果引用的模块在不在包里面，那么导入不能使用相对路径的导入（例如：from ..test import Test），否则会报找不到父包的错误信息。
# 同时需要注意，如果导入的模块中有执行语句，那么一定要将执行语句写在if __name__ == '__main__':判断语句里面，否则引用这个模块时，去执行将会执行引用模块中的执行语句。
from Python基础.模块.创建模块 import Moudle

test1=Moudle.func1
test2=Moudle.func2

print(test1(5,2))
print(test2(5,2))