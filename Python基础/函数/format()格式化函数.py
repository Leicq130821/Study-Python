# str.format():字符串格式化函数，基本语法是通过{}和:来代替以前的%。
# format()函数可以接受不限个参数，位置可以不按顺序。

# 不设置指定位置，按默认顺序。
print('{}{}'.format('Hello','World'))
# 设置指定位置
print('{1}{0}'.format('World','Hello','!!!'))
# 通过参数设置
print('姓名：{name} 年龄：{age} 住址：{address}'.format(name='李明',age=20,address='浙江省杭州市余杭区'))
# 通过字典设置
Dict={'name':'李明','address':'浙江省杭州市余杭区','age':20}
print('姓名：{name} 年龄：{age} 住址：{address}'.format(**Dict))
# 通过索引
Tuple=('李明',20,'浙江省杭州市余杭区')
List=['李明',20,'浙江省杭州市余杭区']
print('姓名：{0[0]} 年龄：{0[1]} 住址：{0[2]}'.format(Tuple))
print('姓名：{0[0]} 年龄：{0[1]} 住址：{0[2]}'.format(List))
# 数值格式化
# 保留两位小数（四舍五入）
print('{:.2f}'.format(9.87654321))
# 不保留小数（四舍五入）
print('{:.0f}'.format(9.87654321))
# 百分比格式
print('{:.2%}'.format(1.23456789))