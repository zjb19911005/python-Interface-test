#coding=utf-8
from django.conf.locale import te

_author__ = 'Junior'

#用python来做接口测试
import requests

def shishike(url):
    headers={}
    params={}
    req=requests.post(url,headers,params=params)
    #设置编码
    req.encoding='utf-8'
    print(req,text)




if __name__=='__main__':
    url='http://www.baidu.com'
    shishike(url)

