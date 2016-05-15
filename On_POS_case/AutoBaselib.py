#coding=utf-8
_author__ = 'Junior'
#APP的登陆与登出
import unittest

from appium import webdriver

def setUp(self):
    self.desired_caps = {}#这里其实也可以把下面的参数,放到caps里面,通过字典的结构模式
    self.desired_caps['platformName'] = 'Android'
    self.desired_caps['platformVersion'] = '4.4.2'

    # self.desired_caps['deviceName'] = '1509a9d4e315e2b5'#设备名字可以通过adb devices查看
    self.desired_caps['deviceName'] ='127.0.0.1:62001'#夜神模拟器
    self.desired_caps['appPackage'] = 'com.shishike.calm'
    self.desired_caps['appActivity'] = '.calmlauncher.CalmHomeActivity_'
    self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
    self.driver.implicitly_wait(20)