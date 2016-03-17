#coding=utf-8
from django.conf.locale import te

_author__ = 'Junior'

#用python来做接口测试
import requests
import datetime
import time
import threading
import unittest



def shishike(url):
    header={'content-type':'application/json'}
    data={"id": 123,
            "brandId": 4881,
            "commercialId": 810002790,
            "orderSource": 2,
            "creatorId": 123,
            "serverCreateTime": 1234567890,
            "updaterId": 123,
            "serverUpdateTime": 1234567890,
            "status": 0
            }
    req=requests.post(url,header,data)
    #设置编码
    req.encoding='utf-8'
    print(req.text)


if __name__=='__main__':
    url='http://gitlab.shishike.com/sync/api/wikis/sync/commercial_order_setting'
    shishike(url)
    testunit = unittest.TestSuite()
    testunit.addTest(shishike)
    timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))

filename = 'D:\\result' + timestr + '.html'
fp = file(filename, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(
     stream=fp,
     title=u'自动化测试报告',
     description=u'自动化测试结果'
     )
runner.run(testunit)
