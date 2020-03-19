# 执行多层语句、嵌套语句或者引用模块时出现错误，那么错误会就会一直往上抛。
# 直到出现错误最根本的地方，打印出一个错误信息，那么追溯错误原因需要从上往下进行分析。
def bar(x):
    return 10/x
def foo(x):
    return bar(x)*2
def main(x):
    foo(x)+2
main(0)