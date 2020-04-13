import pymssql
# 创建数据库链接
sqlserver=pymssql.connect('127.0.0.1:1433','sa','000000','TEST')
# 创建游标
Cursor=sqlserver.cursor()
# 执行数据库数据库语句
Cursor.execute('''
    if not exists(select 1 from sysobjects where name='Student')begin
        create table Student(
            Serial_no integer not null identity,
            Name nvarchar(6),
            Age integer,
            Address nvarchar(30)
        )
    end
''')
Cursor.execute('''
    if not exists(select 1 from Student where Name in('小明','小红','小刚'))begin
        insert into Student(Name,Age,Address)
        values('小明',20,'北京市朝阳区'),
              ('小红',21,'上海市徐汇区'),
              ('小刚',22,'杭州市余杭区')
    end
''')
# 提交事务
sqlserver.commit()
# 查询信息
Cursor.execute('select * from Student')
student=Cursor.fetchone()
while student:
    print(student)
    student = Cursor.fetchone()
# 关闭游标与数据库连接
Cursor.close()
sqlserver.close()