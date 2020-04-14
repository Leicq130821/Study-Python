import pymysql

# 创建数据库连接(mysql与mssql连接方法的参数位置不一样)
MYSQL=pymysql.connect('127.0.0.1','root','000000','TEST',3306)
# 创建索引
Cursor=MYSQL.cursor()
# 执行语句
try:
    Cursor.execute('''
        create table if not exists Student(
            Serial_no int not null auto_increment primary key,
            Name varchar(20),
            Age int,
            Address varchar(30)
            )
''')
    Cursor.execute('''
        insert into Student(Name,Age,Address)
        values('小明',20,'北京市朝阳区'),
              ('小红',21,'上海市徐汇区'),
              ('小刚',22,'杭州市余杭区')
''')
    # 提交事务
    MYSQL.commit()
except Exception as E:
    print(E)
    MYSQL.rollback()
# 查询信息
Cursor.execute('select * from Student')
student=Cursor.fetchall()
print(student)
# 关闭游标
Cursor.close()
# 关闭连接
MYSQL.close()