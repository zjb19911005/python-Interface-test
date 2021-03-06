#coding=utf-8
import HTMLTestRunner
import unittest
import doctest
import time
import sys
import os
import math

from ON_Interface_Case import *#导入客如云文件的用例
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
#将用例组建成数组
allcase = 'D:\PycharmProjects\python-Interface-test\On_Interface_Case'#给出执行用例py文件的路径

class run_interface_case():
    def creatSuite(self):#产生测试套件
        testunit=unittest.TestSuite()
    #使用discovery找到文件夹下的所有用例
        discovery=unittest.defaultTestLoader.discover(allcase,pattern='QSR_*.py',top_level_dir=None)#测试用例的名字是以QSR开头, top的意思是测试模块的顶层目录，即测试用例不是放在多级目录下，设置为none
        for suite in discovery:
            for case in suite:
                testunit.addTest(case)
                print testunit
            return discovery

    allcasenames=creatSuite()

    now = time.strftime('%Y-%m-%d-%H:%M:%d', time.localtime(time.time()))

    filename = 'C:\Users\Administrator.XYZ-PC\Desktop\TestReport\\'+now+"TestReport.html"
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'快餐下单压力测试报告',description=u'快餐下单压力测试结果数据')
    runner.run(allcasenames)
    fp.close()

#在跟一个发送邮件的代码，就完美了，但是保密