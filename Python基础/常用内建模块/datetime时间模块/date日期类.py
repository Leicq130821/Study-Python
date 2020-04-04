from datetime import date

# 最大日期、最小日期。
print(date.max)
print(date.min)
# 当前系统日期。
print(date.today())
# 实例化日期对象，Date=date(year，month，day)。
# year的范围为[1,9999]，month的范围为[1,12]，day的范围为[1,31]。
Date=date(2020,4,4)
print(Date)
print(Date.year)
print(Date.month)
print(Date.day)
# 生成并返回一个日期对象，原日期对象不变。
print(Date.replace(2020,1,1))
print(Date)
# 返回日期对应的time.struct_time对象，对象信息包括年、月、日、时、分、秒、星期（0表示星期一）、一年中的第几天、是否夏令时。
print(Date.timetuple())
# 返回日期是是自 0001-01-01 开始的第多少天。
print(Date.toordinal())
# 返回当前日期对应的星期数（[0-6]）0表示星期一。
print(Date.weekday())
# 返回当前日期对应的星期数（[1-7]）1表示星期一。
print(Date.isoweekday())
# 返回一个元组：（年份，这一天是这一年的第几个星期，星期几）。
print(Date.isocalendar())
# 返回‘YYYY-MM-DD'格式的日期字符串。
print(Date.isoformat())
# 返回指定格式的日期。
print(Date.strftime('%Y年%m月%d日'))