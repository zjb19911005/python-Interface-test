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

import unittest
import time
import HTMLTestRunner
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class testQSRtrade_here(unittest.TestCase):
	def setUp(self):
		self.x=random.randint(1,2)
		self.m=1
	def test001(self):
		for m in range(self.x):
			self.i = random.randint(1461726490000, 1561726497979)
			self.y = random.randint(100, 999)
			timestr = time.strftime('%Y%m%d%H%M%d', time.localtime(time.time()))
			print '当前系统时间是：' + timestr
			print '下单时间传参数是:%d' % (self.i)
			print '订单UUID传参数是:%d' % (self.y)
			tradedata={
	"appType": "5",
	"brandID": 4881,
	"content": {
		"payment": {
			"paymentType": 1,
			"payments": [{
				"paymentItems": [{
					"changeAmount": 0.0,
					"creatorId": 88888904893,
					"creatorName": "admin",
					"faceAmount": 6.1,
					"payModeId": -3,
					"payModeName": "现金",
					"payModelGroup": 2,
					"paySource": 1,
					"paymentUuid": "%s%d"%('b663b8067b9349919252dcda9f987',self.y),
					"refundWay": 1,
					"usefulAmount": 6.1,
					"brandIdenty": 4881,
					"clientCreateTime": self.i,
					"clientUpdateTime": self.i,
					"deviceIdenty": "94:a1:a2:30:8f:7f",
					"shopIdenty": 810002790,
					"statusFlag": 1,
					"uuid":"%s%d"%("d2e6d05624dc4b7fac1bd2c280074",self.y),
					"changed": "true"
				}],
				"actualAmount": 6.1,
				"creatorId": 88888904893,
				"creatorName": "admin",
				"exemptAmount": 0.0,
				"isPaid": 1,
				"paymentType": 1,
				"receivableAmount": 6.10,
				"relateUuid": "%s%d"%("3d154e6981cf4d629e1e646aae7c1",self.y),
				"updatorId": 88888904893,
				"updatorName": "admin",
				"brandIdenty": 4881,
				"clientCreateTime": self.i,
				"clientUpdateTime": self.i,
				"deviceIdenty": "94:a1:a2:30:8f:7f",
				"shopIdenty": 810002790,
				"statusFlag": 1,
				"uuid":"%s%d"%("b663b8067b9349919252dcda9f987",self.y),
				"changed": "true"
			}],
			"relateUuid":"%s%d"% ("3d154e6981cf4d629e1e646aae7c1",self.y),
			"tradePayForm": 1,
			"updatorId": 88888904893,
			"updatorName": "admin"
		},
		"trade": {
			"tradeExtra": {
				"creatorId": 88888904893,
				"creatorName": "admin",
				"deliveryPlatform": 1,
				"serialNumber": "008",
				"tradeUuid":"%s%d"%("3d154e6981cf4d629e1e646aae7c1",self.y),
				"updatorId": 88888904893,
				"updatorName": "admin",
				"brandIdenty": 4881,
				"clientCreateTime": self.i,
				"clientUpdateTime": self.i,
				"deviceIdenty": "94:a1:a2:30:8f:7f",
				"shopIdenty": 810002790,
				"statusFlag": 1,
				"uuid":"%s%d"%("3951e49c6e7e4c9899709e89a173c",self.y),
				"changed": "true"
			},
			"tradeItems": [{
				"actualAmount": 1.00,
				"amount": 1.00,
				"creatorId": 88888904893,
				"creatorName": "admin",
				"enableWholePrivilege": 1,
				"feedsAmount": 0,
				"guestPrinted": 1,
				"isChangePrice": 2,
				"issueStatus": 2,
				"price": 1.00,
				"propertyAmount": 0,
				"quantity": 1,
				"saleType": 2,
				"skuId": 296763,
				"skuName": "测试导入127",
				"skuUuid":"%s%d"%("43b9067e34f848fbbae1dbd523c77",self.y),
				"sort": 0,
				"tradeUuid":"%s%d"%("3d154e6981cf4d629e1e646aae7c1",self.y),
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
				"uuid":"%s%d"%("b52cc023e332411194f05cb285812",self.y),
				"changed": "true"
			}],
			"tradePrivileges": [{
				"creatorId": 88888904893,
				"creatorName": "admin",
				"privilegeAmount": 0.01,
				"privilegeName": "测试小数位数",
				"privilegeType": 12,
				"privilegeValue": 1.11,
				"promoId": 16431,
				"tradeUuid":"%s%d"%("3d154e6981cf4d629e1e646aae7c1",self.y),
				"updatorId": 88888904893,
				"updatorName": "admin",
				"brandIdenty": 4881,
				"clientCreateTime": self.i,
				"clientUpdateTime": self.i,
				"deviceIdenty": "94:a1:a2:30:8f:7f",
				"shopIdenty": 810002790,
				"statusFlag": 1,
				"uuid":"%s%d"%("d7a1223d1e224d89a4a63397bb5a3",self.y),
				"changed": "true"
			}, {
				"creatorId": 88888904893,
				"creatorName": "admin",
				"privilegeAmount": 0.07,
				"privilegeName": "配送费",
				"privilegeType": 12,
				"privilegeValue": 0.07,
				"promoId": 16548,
				"tradeUuid":"%s%d"%("3d154e6981cf4d629e1e646aae7c1",self.y),
				"updatorId": 88888904893,
				"updatorName": "admin",
				"brandIdenty": 4881,
				"clientCreateTime": self.i,
				"clientUpdateTime": self.i,
				"deviceIdenty": "94:a1:a2:30:8f:7f",
				"shopIdenty": 810002790,
				"statusFlag": 1,
				"uuid":"%s%d"%("2a091f451602425d9fa8e363d087c",self.y),
				"changed": "true"
			}, {
				"creatorId": 88888904893,
				"creatorName": "admin",
				"privilegeAmount": 2.00,
				"privilegeName": "WWWW",
				"privilegeType": 12,
				"privilegeValue": 2.00,
				"promoId": 16427,
				"tradeUuid":"%s%d"%("3d154e6981cf4d629e1e646aae7c1",self.y),
				"updatorId": 88888904893,
				"updatorName": "admin",
				"brandIdenty": 4881,
				"clientCreateTime": self.i,
				"clientUpdateTime": self.i,
				"deviceIdenty": "94:a1:a2:30:8f:7f",
				"shopIdenty": 810002790,
				"statusFlag": 1,
				"uuid":"%s%d"%("2b58d27e66614c509789b4f58e680",self.y),
				"changed": "true"
			}, {
				"creatorId": 88888904893,
				"creatorName": "admin",
				"privilegeAmount": 0.02,
				"privilegeName": "测试费用1",
				"privilegeType": 12,
				"privilegeValue": 2.00,
				"promoId": 16408,
				"tradeUuid":"%s%d"%("3d154e6981cf4d629e1e646aae7c1",self.y),
				"updatorId": 88888904893,
				"updatorName": "admin",
				"brandIdenty": 4881,
				"clientCreateTime": self.i,
				"clientUpdateTime": self.i,
				"deviceIdenty": "94:a1:a2:30:8f:7f",
				"shopIdenty": 810002790,
				"statusFlag": 1,
				"uuid":"%s%d"%("da58277cc2e0466b8abbf4609a04a",self.y),
				"changed": "true"
			}, {
				"creatorId": 88888904893,
				"creatorName": "admin",
				"privilegeAmount": 3.00,
				"privilegeName": "餐盒费",
				"privilegeType": 12,
				"privilegeValue": 3.00,
				"promoId": 6404,
				"tradeUuid":"%s%d"%("3d154e6981cf4d629e1e646aae7c1",self.y),
				"updatorId": 88888904893,
				"updatorName": "admin",
				"brandIdenty": 4881,
				"clientCreateTime": self.i,
				"clientUpdateTime": 1461742758002,
				"deviceIdenty": "94:a1:a2:30:8f:7f",
				"shopIdenty": 810002790,
				"statusFlag": 1,
				"uuid":"%s%d"%("f9aabbaa1d21451d8e2c56077c843",self.y),
				"changed": "true"
			}],
			"businessType": 1,
			"creatorId": 88888904893,
			"creatorName": "admin",
			"deliveryType": 1,
			"domainType": 1,
			"privilegeAmount": 0.00,
			"saleAmount": 6.10,
			"skuKindCount": 1,
			"source": 10,
			"sourceChild": 1,
			"tradeAmount": 6.10,
			"tradeAmountBefore": 6.10,
			"tradeNo": "101160427153540123%d"%self.y,
			"tradePayForm": 1,
			"tradePayStatus": 1,
			"tradePeopleCount": 1,
			"tradeStatus": 3,
			"tradeTime": 1461742540547,
			"tradeType": 1,
			"updatorId": 88888904893,
			"updatorName": "admin",
			"brandIdenty": 4881,
			"clientCreateTime": self.i,
			"clientUpdateTime": self.i,
			"deviceIdenty": "94:a1:a2:30:8f:7f",
			"shopIdenty": 810002790,
			"statusFlag": 1,
			"uuid":"%s%d"%("3d154e6981cf4d629e1e646aae7c1",self.y),
			"changed": "true"
				}
			},
	"deviceID": "94:a1:a2:30:8f:7f",
	"shopID": 810002790,
	"systemType": "android",
	"versionCode": "2110060701",
	"versionName": "6.7.1"
				}
			jdata=json.dumps(tradedata)
			head={'Content-Type':'application/json'}

			self.re=requests.post("http://test.calm.shishike.com/CalmRouter/v1/trade/create+cash",data=jdata,headers=head)
			m=m+1,
			s='操作成功'
			# if self.re.text.find(s)>=0:
			# 	print '第%d次测试通过' % m
			# else:
			# 	print '第%d次测试失败' % m
			# 	print self.re.text
			if s in self.re.text :
				print '第%d次测试通过' % m
			else:
				print '第%d次测试失败' % m
				print self.re.text

# if __name__=='__main__':
# 	unittest.main()
