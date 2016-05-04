#coding=utf-8
import HTMLTestRunner
import unittest
import doctest
import time
import sys
import os
import math
sys.path.append("/D:\PycharmProjects\python-Interface-test\keruyun_case")
from keruyun_case import *#导入客如云文件的用例
#将用例组建成数组
alltestnames=[
    'keruyun_case.QSR_Trade_for_here_in_TEST'
]
suite =unittest.TestSuite()
if __name__ == '__main__':
    for test in alltestnames:#循环用例
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName(test))
    print 'Runining...'

timestr = time.strftime('%Y%m%d%H%M%d', time.localtime(time.time()))

filename = 'D:\\result' + timestr + '.html'
fp = file(filename, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'快餐下单测试报告',description=u'快餐下单压力测试结果')
runner.run(suite)
