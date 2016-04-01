#coding=utf-8
from django.conf.locale import te

_author__ = 'Junior'

#用python来做接口测试
import urllib2,urllib
import json
import unittest, time, re

class APITest():
    '''
    接口测试类
    '''
    def apicall(self,method,url,getparams,postparams):
        str1=''
        #GET方法调用
        if method=='GET':
            if getparams!="":
                for k in getparams:
                    str1=str1+k+'='+urllib2.quote(str(getparams.get(k)))
                    if len(getparams)>2:
                        str1=str1+"&"
                url=url+"&"+str1;
            result = urllib2.urlopen(url).read()
        #POST方法调用
        if method=='POST':
            if postparams!="":
                data = urllib.urlencode(postparams)
                req = urllib2.Request(url, data)
            response = urllib2.urlopen(req)
            result = response.read()
        jsdata=json.loads(result)
        return jsdata

class APIGetAdList(unittest.TestCase):
    def test_call(self):
        api=APITest()
        getparams={'keyword':"测试"}
        postparams=''
        data=api.apicall('GET','http://api.zhongchou.cn/deal/list?v=1',getparams,postparams)
        print data
        if(data['errno']!=""):
                self.assertEqual(0, data['errno'])
                print "接口 deal/list ------------OK！"
        else:
                print "接口 deal/list ------------Failure！"
                self.assertEqual(0, data['errno'])


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
