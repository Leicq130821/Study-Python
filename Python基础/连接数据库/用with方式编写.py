import pymssql

with pymssql.connect('127.0.0.1:1433','sa','000000','TEST') as SQL:
    with SQL.cursor() as CURSOR:
        CURSOR.execute('select * from Student')
        Student=CURSOR.fetchall()
        print(Student)