#coding=utf-8


import requests as requests

_author__ = 'Junior'

#用python来做接口测试
import json
import requests
import random
import json
import requests
import random
import speedtest_cli
import unittest
import time
import HTMLTestRunner
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class testQSRtrade_Baiduwaimai(unittest.TestCase):
	def setUp(self):#初始化文件
		self.x=random.randint(100,200)
		self.m=1
	def test001(self):
		for self.m in range(self.x):
			self.i = random.randint(1561832868730, 1562026497979)#服务器时间随机传参
			self.y = random.randint(10000000, 99999999)#订单UUID随机传参
			#传参数据
			tradedata={
	"appType": "5",
	"brandID": 4881,
	"content": {
		"tradeCustomers": [{
			"creatorId": 88888904893,
			"creatorName": "admin",
			"customerId": 2103896268,
			"customerName": "                    ",
			"customerPhone": "18608061005",
			"customerSex": 1,
			"customerType": 1,
			"tradeUuid": "%s%d"%("ed23e66787a341da8f721511",self.y),
			"updatorId": 88888904893,
			"updatorName": "admin",
			"brandIdenty": 4881,
			"clientCreateTime": self.i,
			"clientUpdateTime": self.i,
			"deviceIdenty": "94:a1:a2:30:8f:7f",
			"shopIdenty": 810002790,
			"statusFlag": 1,
			"uuid": "%s%d"%("97221e428f744d769db9f01e",self.y),
			"changed": 'true'
		}],
		"tradeExtra": {
			"creatorId": 88888904893,
			"creatorName": "admin",
			"deliveryAddress": "天府软件园",
			"deliveryAddressId": 129189,
			"deliveryPlatform": 1,
			"invoiceTitle": "",
			"receiverName": "                    ",
			"receiverPhone": "18608061005",
			"receiverSex": 1,
			"serialNumber": "",
			"tradeUuid": "%s%d"%("ed23e66787a341da8f721511",self.y),
			"updatorId": 88888904893,
			"updatorName": "admin",
			"brandIdenty": 4881,
			"clientCreateTime": self.i,
			"clientUpdateTime": self.i,
			"deviceIdenty": "94:a1:a2:30:8f:7f",
			"shopIdenty": 810002790,
			"statusFlag": 1,
			"uuid": "%s%d"%("69fa589fa19f4594bd40d92e",self.y),
			"delivery_platform":1,
			"changed": 'true'
		},
		"tradeItemProperties": [{
			"amount": 0.00,
			"creatorId": 88888904893,
			"creatorName": "admin",
			"price": 0.00,
			"propertyName": "碟",
			"propertyType": 4,
			"propertyUuid":"%s%d"%("f5a6deb2ae0e4700982b1ffa",self.y),
			"quantity": 1,
			"tradeItemUuid":"%s%d"%("a2c6109b834847f2b69b5a0e",self.y),
			"updatorId": 88888904893,
			"updatorName": "admin",
			"brandIdenty": 4881,
			"clientCreateTime": self.i,
			"clientUpdateTime": self.i,
			"deviceIdenty": "94:a1:a2:30:8f:7f",
			"shopIdenty": 810002790,
			"statusFlag": 1,
			"uuid": "%s%d"%("d059ee040d5f420cb7b05dd3",self.y),
			"changed": 'true'
		}],
		"tradeItems": [{
			"actualAmount": 50.00,
			"amount": 50.00,
			"creatorId": 88888904893,
			"creatorName": "admin",
			"enableWholePrivilege": 1,
			"feedsAmount": 0,
			"guestPrinted": 1,
			"isChangePrice": 2,
			"issueStatus": 2,
			"price": 50.00,
			"propertyAmount": 0.00,
			"quantity": 1,
			"saleType": 2,
			"skuId": 20,
			"skuName": "雪花啤酒",
			"skuUuid": "%s%d"%("eb831a4afd844b66aec8031b",self.y),
			"sort": 0,
			"tradeUuid": "%s%d"%("ed23e66787a341da8f721511",self.y),
			"type": 0,
			"unitName": "份",
			"updatorId": 88888904893,
			"updatorName": "admin",
			"brandIdenty": 4881,
			"clientCreateTime": self.i,
			"clientUpdateTime": self.i,
			"deviceIdenty": "94:a1:a2:30:8f:7f",
			"shopIdenty": 810002790,
			"statusFlag": 1,
			"uuid": "%s%d"%("a2c6109b834847f2b69b5a0e",self.y),
			"changed": 'true'
		}],
		"tradePrivileges": [{
			"creatorId": 88888904893,
			"creatorName": "admin",
			"privilegeAmount":self.y,
			"privilegeName": "餐盒费",
			"privilegeType": 12,
			"privilegeValue": 0.00,
			"promoId": 6914,
			"tradeUuid":"%s%d"%("ed23e66787a341da8f721511",self.y),
			"updatorId": 88888904893,
			"updatorName": "admin",
			"brandIdenty": 4881,
			"clientCreateTime": self.i,
			"clientUpdateTime": self.i,
			"deviceIdenty": "94:a1:a2:30:8f:7f",
			"shopIdenty": 810002790,
			"statusFlag": 1,
			"uuid": "%s%d"%("ed5172f4871743a4b2c61313",self.y),
			"changed": 'true'
		}],
		"businessType": 1,
		"creatorId": 88888904893,
		"creatorName": "admin",
		"deliveryType": 2,
		"domainType": 2,
		"privilegeAmount": 0.00,
		"saleAmount": 50.00,
		"skuKindCount": 1,
		"source": 4,
		"sourceChild": 41,
		"tradeAmount": 50.00,
		"tradeAmountBefore": 50.00,
		"tradeNo": "1011604281640%d" % self.y,
		"tradePayForm": 1,
		"tradePayStatus": 3,
		"tradePeopleCount": 3,
		"tradeStatus": 1,
		"tradeTime": 1461832845726,
		"tradeType": 1,
		"updatorId": 88888904893,
		"updatorName": "admin",
		"brandIdenty": 4881,
		"clientCreateTime": self.i,
		"clientUpdateTime": self.i,
		"deviceIdenty": "94:a1:a2:30:8f:7f",
		"shopIdenty": 810002790,
		"statusFlag": 1,
		"uuid": "%s%d"%("ed23e66787a341da8f721511",self.y),
		"changed": 'true'
	},
	"deviceID": "94:a1:a2:30:8f:7f",
	"shopID": 810002790,
	"systemType": "android",
	"versionCode": "2110060701",
	"versionName": "6.7.1"
}
			jdata=json.dumps(tradedata)#传参json格式化处理
			head={'Content-Type':'application/json'}#json请求头
			url="http://test.calm.shishike.com/CalmRouter/v1/trade/submit"
			# self.re=requests.post("https://testcalm.shishike.com/CalmRouter/v1/trade/submit",data=jdata,headers=head)
			self.re = requests.post(url, data=jdata,headers=head)
			self.m=self.m+1,
			s = '操作成功'
			#添加返回判断语句
			# if self.re.text.find(s)>=0:
			# 	print '第%d次测试通过' % m
			# else:
			# 	print '第%d次测试失败' % m
			# 	print self.re.text
			timestr = time.strftime('%Y-%m-%d/%H：%M：%d', time.localtime(time.time()))
			print "第%d次下单的系统时间是:" % (self.m) + timestr
			print '第%s次下单时间传参值是:%d' % (self.m,self.i)
			print '第%s次订单UUID传参值是:%d' % (self.m,self.y)
			if s in self.re.text:
				print '第%d次测试通过' % self.m
			else:
				print '第%d次测试失败,返回的错误信息如下:' % self.m
				print self.re.text
if __name__=='__main__':
	unittest.main()
