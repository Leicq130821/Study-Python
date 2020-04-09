from urllib import request,parse

info=request.Request(method='GET',url='http://192.168.100.233:7005')
response1=request.urlopen(info)
Dict={'username':'admin','password':'000000'}
data=bytes(parse.urlencode(Dict).encode('utf-8'))
response2=request.urlopen('http://192.168.100.233:7005/index_zt.jsp',data=data)
print(response1.status)
print(response1.msg)
print(response1.reason)
print(response1.info())
print(response1.getheaders())
for key,value in response1.getheaders():
    print(key,':',value)
request.Request()