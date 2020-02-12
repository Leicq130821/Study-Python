#input()函数返回的是str类型，如果输入值作为数值型参数，需要进行强制转换。
length=float(input('请输入正方形的边长：'))
print('正方形的面积为：',length*length)