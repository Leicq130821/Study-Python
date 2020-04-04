from datetime import time

# 最大时间、最小时间
print(time.max)
print(time.min)
# 实例化时间对象：Time=time(hour,minute,second,microsecond)
# hour范围为[0,24]，minute范围为[0,59]，second范围为[0,59]，microsecond范围为[0, 1000000]。
Time=time(10,10,10)
# 时间的属性
print(Time.hour)
print(Time.minute)
print(Time.second)
print(Time.microsecond)
# 返回一个新的时间对象，原时间对象不变。
print(Time.replace(12,12,12))
print(Time)
# 返回一个HH:MM:SS.%f格式的时间字符串。
print(Time.isoformat())
# 返回指定格式的时间字符串。
print(Time.strftime('%H点%M分%S秒'))