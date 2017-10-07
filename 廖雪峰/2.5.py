# -*- coding: utf-8 -*-
#　IO读写
import pickle
import json
from urllib import request
from pprint import pprint
from collections import OrderedDict

d=dict(name='Bob', age=20, score=88)
jsonstr='[{"action_type":0,"action_url":"http:\/\/www.kymjs.com","start_time":"2017-10-07 00:00:00","description":"\u706b\u661f\u4e0a\u7684\u5ce1\u8c37\u7cfb\u7edf-\u6c34\u624b\u53f7\u5ce1\u8c37\u5730\u533a\u4e0a\u7684\u5c0f\u884c\u661f (\u00a9 Detlev van Ravenswaay\/Getty Images)","image_url":"http:\/\/cn.bing.com\/az\/hprichbg\/rb\/VallesMarineris_ZH-CN10598461085_1366x768.jpg","order_index":"20171007","scheme":""},{"action_type":0,"action_url":"http:\/\/www.kymjs.com","start_time":"2017-10-06 00:00:00","description":"\u5815\u843d\u7684\u751c\u6817\u5b50\u548c\u7d2b\u8721\u8611\uff0c\u82f1\u56fd\u8bfa\u798f\u514b  (\u00a9 Gary K. Smith\/Minden Pictures)","image_url":"http:\/\/cn.bing.com\/az\/hprichbg\/rb\/SweetChestnut_ZH-CN10220364928_1366x768.jpg","order_index":"20171006","scheme":""}]'

''' 序列化内容存储到文件中 '''
def writeObject():
   
    # f=open('dump.txt','wb')   ＃普通
    # pickle.dump(d,f)
    # f.close()

    #pythoner  
    with open('dump.txt','wb') as f:
        pickle.dump(d,f)
''' 读取文件内容进行反序列化 '''
def readObject():
    with open('dump.txt','rb') as f:
        d=pickle.load(f)
        print(d)

class Student(object):
    def __init__(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city
    

def writeObjectForJson():
    pass

def readObjectForJson():
    pass
def student2dict(std):
        return {
        'name': std.name,
        'age': std.age,
        'city': std.city
    }

class Weather(object):
    def __init__(self,action_type,action_url,start_time,description,image_url,order_index,scheme):
        self.action_type=action_type
        self.action_url=action_url
        self.start_time=start_time
        self.description=description
        self.image_url=image_url
        self.order_index=order_index
        self.scheme=scheme
class JSONObject:
    def __init__(self,d):
        self.__dict__=d
def readNetJson():
    with request.urlopen('http://openapi.kymjs.com:8081/splash') as f:
        data=f.read()
        print('states',f.status,f.reason)
        strjson=data.decode('utf-8')
        d=json.loads(strjson,object_pairs_hook=OrderedDict)
        return d

if __name__ == '__main__':
    # writeObject()
    # readObject()

    s=Student('lsl',24,'gz')
    print(json.dumps(s,default=student2dict))  #转换为json数据需要一个转换函数（student2dict），要不然会出现报错

    print(json.dumps(s,default=lambda obj:obj.__dict__))


    strjson=readNetJson()
    pprint(strjson)