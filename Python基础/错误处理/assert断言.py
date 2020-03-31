# 可以通过assert断言的方式来检查错误，assert的基本语法为：assert 表达式,"断言语句"。
# 如果表达式返回的结果是False时，则抛出AssertionError并抛出断言语句，断言异常可以被except捕获。
def Diomod(x,y):
    try:
        assert isinstance(x,(int,float)) and isinstance(y,(int,float)),'被除数与除数类型不正确'
        assert y!=0,'除数不能为0'
    except Exception as E:
        print('输入错误：',E)
    else:
        print('输入正确，结果为：',x/y)
if __name__ == '__main__':
    Diomod(10,0)
    Diomod('a',1)
    Diomod(10,2)