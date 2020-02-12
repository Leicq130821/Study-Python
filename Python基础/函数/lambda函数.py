# lambda函数：lambda argument_list:expression。
# argument_list是参数列表，它的结构与Python中函数(function)的参数列表是一样的（输入）。
# expression是一个关于参数的表达式，表达式中出现的参数需要在argument_list中有定义，并且表达式只能是单行的（输出）。
# lambda函数：又称“匿名函数”，lambda函数有输入和输出：输入是传入到参数列表argument_list的值，输出是根据表达式expression计算得到的值。
# lambda函数功能简单：单行expression决定了lambda函数不可能完成复杂的逻辑。
exper=lambda x,y,z:x+y+z
print(exper(1,2,3))