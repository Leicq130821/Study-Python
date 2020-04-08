from collections import namedtuple

List=[('张三',40,'北京市朝阳区'),('李四',35,'上海市浦东区'),('王五',30,'杭州市余杭区')]
TEST=namedtuple('个人信息',['name','age','address'])
for info in List:
    Tuple=TEST(*info)
    print(Tuple)
    print('name=',Tuple.name,'age=',Tuple.age,'address=',Tuple.address)
    print('name=',Tuple[0],'age=',Tuple[1],'address=',Tuple[2])