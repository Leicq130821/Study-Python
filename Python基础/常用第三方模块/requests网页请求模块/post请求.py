from urllib.parse import urlencode

import requests

response=requests.post(url='http://192.168.100.233:7003/jtinfo/jtconfig.jsp?',data={'system_id':1,'company':'金谷信托','company_jc':'金谷信托111','company_id':'JG01','coa_id':'COA01','belong_corp':'金谷子公司'},headers={'Cookie':'JSESSIONID=sJJ4pvbGQMpJQFPXR7MWFSJ7wj1Hjkn8tyCQJkDs5y0xLQvY5Pnz!-84757755'
    ,'Content-Type':'text/html; charset=gbk'})
print(response.headers)
print(response.reason)
print(response.status_code)
print(response.encoding)
print(response.text)