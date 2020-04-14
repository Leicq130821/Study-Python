import pymssql

try:
    SQL=pymssql.connect('127.0.0.1:1433','sa','000000','TEST')
    CURSOR=SQL.cursor()
    CURSOR.execute("update Student set Name='小蓝' where Serial_no=1")
    CURSOR.execute("update Student set Address='广州市天河区' where Serial_no=2")
    CURSOR.execute("update Student set Age=50 where Serial_no=3")
except Exception as E:
    print(E)
    SQL.rollback()
else:
    SQL.commit()
CURSOR.execute('select * from Student')
STUDENT=CURSOR.fetchall()
print(STUDENT)
CURSOR.close()
SQL.close()