from datetime import datetime


# 返回一个表示当前本期日期时间的datetime对象。
print(datetime.today())
# 返回指定时区日期时间的datetime对象，如果不指定tz参数则结果同Datetime.today()。
print(datetime.now())
# 实例化
Datetime=datetime(2020,1,1,1,1,1,1)
print(Datetime)
# 日期时间的日期、时间对象
print(Datetime.date())
print(Datetime.time())
# 字符串时间转换为时间对象
print(datetime.strptime('2020-4-4 20:40:01','%Y-%m-%d %H:%M:%S'))