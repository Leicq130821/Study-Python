from collections import OrderedDict

# OrderDict()：可以提供一个有序字典。
Dict=OrderedDict()
Dict['name']='李明'
Dict['age']=20
Dict['address']='浙江省杭州市余杭区'
for key in Dict:
    print(key,':',Dict[key])
for key,value in Dict.items():
    print(key,':',value)