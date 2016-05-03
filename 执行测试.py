#coding=utf-8
import HTMLTestRunner
import unittest
from keruyun_case import QSRTrade_for_takeout_in_TEST,QSR_Trade_for_here_in_TEST,QSRTrade_for_takeout_in_GLD

testunit = unittest.TestSuite()
testunit.addTest(QSR_Trade_for_here_in_TEST("test001"))
testunit.addTest(QSRTrade_for_takeout_in_GLD('test001'))
testunit.addTest(QSRTrade_for_takeout_in_TEST('test001'))
timestr = time.strftime('%Y%m%d%H%M%d', time.localtime(time.time()))

filename = 'D:\\result' + timestr + '.html'
fp = file(filename, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'快餐下单测试报告',description=u'快餐下单压力测试结果')
runner.run(testunit)
time