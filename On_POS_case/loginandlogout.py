#coding=utf-8
_author__ = 'Junior'
#APP的登陆与登出
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
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',self.desired_caps)#默认写法
        def timewait(int):
            self.driver.implicitly_wait(int)

        timewait(50)
        self.driver.switch_to_alert()

        self.driver.find_element_by_id('com.shishike.calm:id/negative_button').click()
        timewait(1)
        #下面就开始找元素找点了
        self.driver.find_element_by_name('admin').click()
        timewait(1)
        x=1
        for x in range(6):
            self.driver.find_element_by_id('com.shishike.calm:id/eight').click()
            timewait(1)
            x=x+1

        self.driver.find_element_by_xpath("//android.widget.GridView[1]/android.widget.LinearLayout[2]/android.widget.ImageView[1]").click()

        timewait(1)

        # try:
            # self.driver.find_element_by_xpath("//android.view.View[1]/android.widget.LinearLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.GridView[1]/android.widget.FrameLayout[9]").click()
        self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'麻婆豆腐')]").click()
        timewait(10)
        # except:
        #     pass

        self.driver.find_element_by_id('com.shishike.calm:id/btn_order_dish_right_cash').click()
        timewait(10)

        self.driver.find_element_by_name('扫码').click()
        timewait(10)
        self.driver.find_element_by_name('二维码').click()
        timewait(20)

        self.driver.find_element_by_id('com.shishike.calm:id/pay_back').click()
        timewait(3)

        self.driver.find_element_by_id('com.shishike.calm:id/cashier_title_bar_menu_btn').click()
        timewait(3)

        self.driver.find_element_by_id('com.shishike.calm:id/ordercenter').click()
        timewait(3)

        self.driver.find_element_by_id('com.shishike.calm:id/un_payment').click()
        timewait(3)

        self.driver.find_element_by_id('com.shishike.calm:id/unpay_order_detail_un_use').click()
        timewait(3)


        self.driver.switch_to_alert()
        timewait(3)

        self.driver.find_element_by_name('作废').click()
        timewait(3)


        self.driver.find_element_by_id('com.shishike.calm:id/cashier_title_bar_menu_btn').click()
        timewait(3)

        self.driver.find_element_by_id('com.shishike.calm:id/orderdishes').click()
        timewait(3)

    def tearDown(self):
        self.driver.quit()
#添加用例执行脚本
if __name__ == "__main__":
    unittest.main()