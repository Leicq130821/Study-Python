import requests

# 通过参数headers可以设置请求头信息。
response1=requests.post('http://localhost:7005/',headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},data={'username':'admin','password':'000000'})
print(response1.headers)
List=response1.headers['Set-Cookie'].split('=',1)
Data={'book_code':1,'product_id':855,'proj_id':'TZ_451','checker_empno':6393,'checker_empno_name':6393,'proj_check_seq':'1111','proj_check_comnt':'1111','checker_mem_role':'1111','checker_mem_check_comnt':'1111','reg_person':'1111','reg_org':'1111','reg_tm_picker':'2020-04-11','reg_tm':20200411,'checker_mem_name':'陈立群'}
Cookie={List[0]:List[1]}
response2=requests.post('http://localhost:7005/jtinfo/tproj_check_info_update.jsp?book_code=1&product_id=855',headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},cookies=Cookie,data=Data)
print(response2.headers)