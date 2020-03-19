# 可以通过assert断言的方式来检查错误，assert的基本语法为：assert 表达式,"断言语句"。
# 如果表达式返回的结果是False时，则抛出AssertionError并抛出断言语句。
age=int(input('请输入年龄：'))
assert 100>age>2,'年龄必须大于2小于100'
if age<7:
    print('你的年龄是儿童')
elif age<18:
    print('你的年龄是少年')
elif age<45:
    print('你的年龄是青年')
elif age<60:
    print('你的年龄是中年')
else:
    print('你的年龄是老年')