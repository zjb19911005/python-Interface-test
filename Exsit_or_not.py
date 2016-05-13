#coding=utf-8
_author__ = 'Junior'
#建立一个多线程去监控自动化页面的状态
import threading
import time
import unittest
from appium import webdriver


class loginandlogout(unittest.TestCase):
    def setUp(self):
        self.desired_caps = {}#这里其实也可以把下面的参数,放到caps里面,通过字典的结构模式
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['platformVersion'] = '4.4.2'

        # self.desired_caps['deviceName'] = '1509a9d4e315e2b5'#设备名字可以通过adb devices查看
        self.desired_caps['deviceName'] ='127.0.0.1:62001'#夜神模拟器
        self.desired_caps['appPackage'] = 'com.shishike.calm'
        self.desired_caps['appActivity'] = '.calmlauncher.CalmHomeActivity_'


    def test_login(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)  # 默认写法

        self.driver.implicitly_wait(20)
        # 下面就开始找元素找点了
        try:
            self.driver.find_element_by_name('admin').click()
        except:
            return catcterror.is_update()

        x = 1
        for x in range(6):
            self.driver.find_element_by_id('com.shishike.calm:id/eight').click()
            self.driver.implicitly_wait(1)
            x = x + 1
        self.driver.find_element_by_xpath("//android.widget.GridView[1]/android.widget.LinearLayout[2]/android.widget.ImageView[1]").click()
        self.driver.implicitly_wait(1)

# 为多线程定义一个函数
class catcterror():
    def is_update(self):
        try:
            self.driver.find_element_by_name('admin').click()
        except:
            self.driver.find_element_by_id('com.shishike.calm:id/negative_button').click()
            self.driver.implicitly_wait(1)
            self.driver.find_element_by_name('admin').click()
thread=[]
t1=threading.Thread(target=loginandlogout)
thread.append(t1)
t2=threading.Thread(target=catcterror.is_update)
thread.append(t2)

if __name__=="__main__":
    for t in thread:
      t.SetDeaamon(True)
      t.start()
    t.join()







