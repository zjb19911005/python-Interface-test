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
import MySQLdb
import re


class testFSR_here(unittest.TestCase):
	def setUp(self):#初始化文件
		self.x=random.randint(1,2)
		self.m=1
		self.i = random.randint(146250530000, 1462503359999)  # 服务器时间随机传参
		self.y = random.randint(1000, 9999)  # 订单UUID随机传参
	def test001_dinnerSubmit(self):
		# for self.m in range(self.x):
			#传参数据
		tradedata={
	"appType": "5",
	"brandID": 4881,
	"content": {
		"tables": [{
			"id": 4000181879,
			"modifyDateTime": 1461661519000,
			"tableStatus": 1
		}],
		"tradeExtra": {
			"creatorId": 88888930971,
			"creatorName": "zhujb",
			"deliveryPlatform": 1,
			"tradeUuid": "%s%d"%("e7bf82d54146450b98070d027f3f",self.y),
			"updatorId": 88888930971,
			"updatorName": "zhujb",
			"brandIdenty": 4881,
			"clientCreateTime": self.i,
			"clientUpdateTime": self.i,
			"deviceIdenty": "94:a1:a2:30:65:af",
			"shopIdenty": 810002790,
			"statusFlag": 1,
			"uuid":"%s%d"%( "464bad2502b747ea9776867645e6",self.y),
			"changed": 'true'
		},
		"tradeItems": [],
		"tradeTables": [{
			"creatorId": 88888930971,
			"creatorName": "zhujb",
			"memo": "无",
			"selfTableStatus": 1,
			"tableId": 4000162905,
			"tableName": "4",
			"tablePeopleCount": 8,
			"tradeUuid":"%s%d"%( "e7bf82d54146450b98070d027f3f",self.y),
			"updatorId": 88888930971,
			"updatorName": "zhujb",
			"waiterId": 0,
			"waiterName": "zhujb",
			"brandIdenty": 4881,
			"clientCreateTime": self.i,
			"clientUpdateTime": self.i,
			"deviceIdenty": "94:a1:a2:30:65:af",
			"shopIdenty": 810002790,
			"statusFlag": 1,
			"uuid": "%s%d"%("511edc9d1f85435ca56ae48e5a3a",self.y),
			"changed": 'true'
		}],
		"businessType": 2,
		"creatorId": 88888930971,
		"creatorName": "zhujb",
		"deliveryType": 1,
		"domainType": 1,
		"privilegeAmount": 0,
		"saleAmount": 0,
		"skuKindCount": 0,
		"source": 10,
		"sourceChild": 1,
		"tradeAmount": 0,
		"tradeNo": "10116050611282000%d"%self.y,
		"tradePayForm": 1,
		"tradePayStatus": 1,
		"tradePeopleCount": 8,
		"tradeStatus": 3,
		"tradeTime": 1462505300721,
		"tradeType": 1,
		"updatorId": 88888930971,
		"updatorName": "zhujb",
		"brandIdenty": 4881,
		"clientCreateTime": self.i,
		"clientUpdateTime": self.i,
		"deviceIdenty": "94:a1:a2:30:65:af",
		"shopIdenty": 810002790,
		"statusFlag": 1,
		"uuid": "%s%d"%("e7bf82d54146450b98070d027f3f",self.y),
		"changed": 'true'
	},
	"deviceID": "94:a1:a2:30:65:af",
	"shopID": 810002790,
	"systemType": "android",
	"versionCode": "2110060800",
	"versionName": "6.8.0"
}
		jdata=json.dumps(tradedata)#传参json格式化处理
		head={'Content-Type':'application/json'}#json请求头
		url="http://test.calm.shishike.com/CalmRouter/v1/trade/dinnerSubmit"
		# self.re=requests.post("https://testcalm.shishike.com/CalmRouter/v1/trade/submit",data=jdata,headers=head)
		re1 = requests.post(url, data=jdata,headers=head)
		# self.m=self.m+1,
		s = '操作成功'
		timestr = time.strftime('%Y-%m-%d/%H：%M：%d', time.localtime(time.time()))
		print "第%d次开台的系统时间是:" % (self.m) + timestr
		print '.'
		if '操作成功' in re1.text:
			print '第%d次开台通过' % self.m
			print '.'
			self.uuid = '%s%d ' % ("e7bf82d54146450b98070d027f3f", self.y),
			print '本次交易的UUID是:%s' % self.uuid
			print '本次交易的流水号是：%d'%self.y
			self.suttime=re.search('serverCreateTime":\d{12}',str(re1.text)).group()[18:]#正则表达式查询后切片读取数据
			print '订单改单收银前服务器最新更新时间是：%s'% self.suttime
		else:
			print '第%d次开台失败,返回的错误信息如下:' % self.m
			print re1.text

		# 传参数据
		tradedata ={
	"appType": "5",
	"brandID": 4881,
	"content": {
		"payment": {
			"updatorName": "zhujb",
			"paymentType": 1,
			"payments": [{
				"paymentItems": [{
					"changeAmount": 0.0,
					"creatorId": 88888930971,
					"creatorName": "zhujb",
					"faceAmount": 27.18,
					"payModeId": -3,
					"payModeName": "现金",
					"payModelGroup": 2,
					"paySource": 1,
					"paymentUuid": "%s%d"%("2fe88f007f5243808a852a45298b",self.y),
					"refundWay": 1,
					"usefulAmount": 27.18,
					"brandIdenty": 4881,
					"clientCreateTime": 826193664692,
					"clientUpdateTime": 826193664692,
					"deviceIdenty": "94:a1:a2:30:65:af",
					"shopIdenty": 810002790,
					"statusFlag": 1,
					"uuid": "%s%d"%("64e2e1ef8e294b1787c5f660ae2c",self.y),
					"changed": 'true'
				}],
				"actualAmount": 27.18,
				"creatorId": 88888930971,
				"creatorName": "zhujb",
				"exemptAmount": 0.0,
				"isPaid": 1,
				"paymentType": 1,
				"receivableAmount": 27.18,
				"relateId": 3354394,
				"relateUuid": "%s%d"%("e7bf82d54146450b98070d027f3f",self.y),
				"updatorId": 88888930971,
				"updatorName": "zhujb",
				"brandIdenty": 4881,
				"clientCreateTime": 826193664692,
				"clientUpdateTime": 826193664692,
				"deviceIdenty": "94:a1:a2:30:65:af",
				"shopIdenty": 810002790,
				"statusFlag": 1,
				"uuid": "%s%d"%("2fe88f007f5243808a852a45298b",self.y),
				"changed": 'true'
			}],
			"relateUuid": "%s%d"%("e7bf82d54146450b98070d027f3f",self.y),
			"updatorId": 88888930971,
			"paymentTime": 1462505329363
		},
		"trade": {
			"tradeExtra": {
				"callDishStatus": 0,
				"creatorId": 88888930971,
				"creatorName": "zhujb",
				"deliveryPlatform": 1,
				"deliveryStatus": 0,
				"serialNumber": "%d" %self.y,
				"tradeId": 3354394,
				"tradeUuid": "%s%d"%("e7bf82d54146450b98070d027f3f",self.y),
				"updatorId": 88888930971,
				"updatorName": "zhujb",
				"brandIdenty": 4881,
				"clientCreateTime":826193664692 ,
				"clientUpdateTime": 826193664692,
				"deviceIdenty": "94:a1:a2:30:65:af",
				"id": 3261230,
				"serverCreateTime": self.suttime,
				"serverUpdateTime": self.suttime,
				"shopIdenty": 810002790,
				"statusFlag": 1,
				"uuid": "%s%d"%("464bad2502b747ea9776867645e6",self.y),
				"changed": 'false'
			},
			"tradeItemProperties": [{
				"amount": 0.00,
				"creatorId": 88888930971,
				"creatorName": "zhujb",
				"price": 0.00,
				"propertyName": "份",
				"propertyType": 4,
				"propertyUuid": "d5d937e9ecec4c5088a7c5c705aab55e",
				"quantity": 1,
				"tradeItemUuid": "%s%d"%("3c7968cddb07404e8ee08578b984",self.y),
				"updatorId": 88888930971,
				"updatorName": "zhujb",
				"brandIdenty": 4881,
				"clientCreateTime": 826193664692,
				"clientUpdateTime": 826193664692,
				"deviceIdenty": "94:a1:a2:30:65:af",
				"shopIdenty": 810002790,
				"statusFlag": 1,
				"uuid":"%s%d"%( "ded24a4330fb46fe95461ef2450d",self.y),
				"changed": 'true'
			}, {
				"amount": 0.00,
				"creatorId": 88888930971,
				"creatorName": "zhujb",
				"price": 0.00,
				"propertyName": "中杯",
				"propertyType": 4,
				"propertyUuid": "930bcaab1ff74c099c6dfdc442ffc381",
				"quantity": 1,
				"tradeItemUuid": "%s%d"%("3c7968cddb07404e8ee08578b984",self.y),
				"updatorId": 88888930971,
				"updatorName": "zhujb",
				"brandIdenty": 4881,
				"clientCreateTime": 826193664692,
				"clientUpdateTime": 826193664692,
				"deviceIdenty": "94:a1:a2:30:65:af",
				"shopIdenty": 810002790,
				"statusFlag": 1,
				"uuid": "%s%d"%("6ee95b1b94984e24b9cb34b1e743",self.y),
				"changed": 'true'
			}],
			"tradeItems": [{
				"actualAmount": 10.77,
				"amount": 10.77,
				"creatorId": 88888930971,
				"creatorName": "zhujb",
				"enableWholePrivilege": 1,
				"feedsAmount": 0,
				"guestPrinted": 1,
				"isChangePrice": 2,
				"issueStatus": 2,
				"price": 10.77,
				"propertyAmount": 0.00,
				"quantity": 1,
				"saleType": 2,
				"skuId": 13,
				"skuName": "糖醋排骨",
				"skuUuid": "4f9cdc3c05bf41d0b6bf4dfd3889031a",
				"sort": 0,
				"tradeId": 3354394,
				"tradeTableId": 1047823,
				"tradeTableUuid": "%s%d"%("511edc9d1f85435ca56ae48e5a3a",self.y),
				"tradeUuid": "%s%d"%("e7bf82d54146450b98070d027f3f",self.y),
				"type": 0,
				"unitName": "盘",
				"updatorId": 88888930971,
				"updatorName": "zhujb",
				"brandIdenty": 4881,
				"clientCreateTime": self.i,
				"clientUpdateTime": self.i,
				"deviceIdenty": "94:a1:a2:30:65:af",
				"shopIdenty": 810002790,
				"statusFlag": 1,
				"uuid": "%s%d"%("3c7968cddb07404e8ee08578b984",self.y),
				"changed": 'true'
			}],
			"tradePrivileges": [{
				"creatorId": 88888930971,
				"creatorName": "zhujb",
				"privilegeAmount": 16.00,
				"privilegeName": "WWWW",
				"privilegeType": 12,
				"privilegeValue": 2.00,
				"promoId": 16427,
				"tradeId": 3354394,
				"tradeUuid": "%s%d"%("e7bf82d54146450b98070d027f3f",self.y),
				"updatorId": 88888930971,
				"updatorName": "zhujb",
				"brandIdenty": 4881,
				"clientCreateTime": 826193664692,
				"clientUpdateTime": 826193664692,
				"deviceIdenty": "94:a1:a2:30:65:af",
				"shopIdenty": 810002790,
				"statusFlag": 1,
				"uuid": "%s%d"%("b07aae2817d24ad68579261dfca3",self.y),
				"changed": 'true'
			}, {
				"creatorId": 88888930971,
				"creatorName": "zhujb",
				"privilegeAmount": 0.12,
				"privilegeName": "测试小数位数",
				"privilegeType": 12,
				"privilegeValue": 1.11,
				"promoId": 16431,
				"tradeId": 3354394,
				"tradeUuid": "%s%d"%("e7bf82d54146450b98070d027f3f",self.y),
				"updatorId": 88888930971,
				"updatorName": "zhujb",
				"brandIdenty": 4881,
				"clientCreateTime": self.i,
				"clientUpdateTime": self.i,
				"deviceIdenty": "94:a1:a2:30:65:af",
				"shopIdenty": 810002790,
				"statusFlag": 1,
				"uuid": "%s%d"%("7f9f99be92634138b0c86e0d3e8d",self.y),
				"changed": 'true'
			}, {
				"creatorId": 88888930971,
				"creatorName": "zhujb",
				"privilegeAmount": 0.22,
				"privilegeName": "测试费用1",
				"privilegeType": 12,
				"privilegeValue": 2.00,
				"promoId": 16408,
				"tradeId": 3354394,
				"tradeUuid":"%s%d"%( "e7bf82d54146450b98070d027f3f",self.y),
				"updatorId": 88888930971,
				"updatorName": "zhujb",
				"brandIdenty": 4881,
				"clientCreateTime": self.i,
				"clientUpdateTime": self.i,
				"deviceIdenty": "94:a1:a2:30:65:af",
				"shopIdenty": 810002790,
				"statusFlag": 1,
				"uuid": "%s%d"%("17bebdd06c644780811cd94a2916",self.y),
				"changed": 'true'
			}, {
				"creatorId": 88888930971,
				"creatorName": "zhujb",
				"privilegeAmount": 0.07,
				"privilegeName": "配送费",
				"privilegeType": 12,
				"privilegeValue": 0.07,
				"promoId": 16548,
				"tradeId": 3354394,
				"tradeUuid": "%s%d"%("e7bf82d54146450b98070d027f3f",self.y),
				"updatorId": 88888930971,
				"updatorName": "zhujb",
				"brandIdenty": 4881,
				"clientCreateTime": 826193664692,
				"clientUpdateTime": 826193664692,
				"deviceIdenty": "94:a1:a2:30:65:af",
				"shopIdenty": 810002790,
				"statusFlag": 1,
				"uuid": "%s%d"%("ca9f134473004ae3b8939b8c5f62",self.y),
				"changed": 'true'
			}],
			"tradeTables": [{
				"creatorId": 88888930971,
				"creatorName": "zhujb",
				"memo": "无",
				"selfTableStatus": 0,
				"tableId": 4000162905,
				"tableName": "4",
				"tablePeopleCount": self.y,
				"tradeId": 3354394,
				"tradeUuid": "%s%d"%("e7bf82d54146450b98070d027f3f",self.y),
				"updatorId": 88888930971,
				"updatorName": "zhujb",
				"waiterId": 0,
				"waiterName": "zhujb",
				"brandIdenty": 4881,
				"clientCreateTime": 826193664692,
				"clientUpdateTime": 826193664692,
				"deviceIdenty": "94:a1:a2:30:65:af",
				"id": 1047745,
				"serverCreateTime":self.suttime,
				"serverUpdateTime":self.suttime,
				"shopIdenty": 810002790,
				"statusFlag": 1,
				"uuid": "%s%d"%("511edc9d1f85435ca56ae48e5a3a",self.y),
				"changed": 'true'
			}],
			"actionType": 1,
			"bizDate": 1462464000000,
			"businessType": 2,
			"creatorId": 88888930971,
			"creatorName": "zhujb",
			"deliveryType": 1,
			"domainType": 1,
			"privilegeAmount": 0.00,
			"saleAmount": 27.18,
			"skuKindCount": 1,
			"source": 10,
			"sourceChild": 1,
			"tradeAmount": 27.18,
			"tradeAmountBefore": 27.18,
			"tradeNo": "10116050611282000%d"%self.y,
			"tradePayForm": 1,
			"tradePayStatus": 1,
			"tradePeopleCount": 8,
			"tradeStatus": 3,
			"tradeTime": 1462505300721,
			"tradeType": 1,
			"updatorId": 88888930971,
			"updatorName": "zhujb",
			"brandIdenty": 4881,
			"clientCreateTime": 826193664692,
			"clientUpdateTime": 826193664692,
			"deviceIdenty": "94:a1:a2:30:65:af",
			"id": 3354394,
			"serverCreateTime":self.suttime,
			"serverUpdateTime":self.suttime,
			"shopIdenty": 810002790,
			"statusFlag": 1,
			"uuid": "%s%d"%("e7bf82d54146450b98070d027f3f",self.y),
			"changed": 'true'
		}
	},
	"deviceID": "94:a1:a2:30:65:af",
	"shopID": 810002790,
	"systemType": "android",
	"versionCode": "2110060800",
	"versionName": "6.8.0"
}
		jdata = json.dumps(tradedata)  # 传参json格式化处理
		head = {'Content-Type': 'application/json'}  # json请求头
		url = "http://test.calm.shishike.com/CalmRouter/v1/trade/modify+cash"
		# self.re=requests.post("https://testcalm.shishike.com/CalmRouter/v1/trade/submit",data=jdata,headers=head)
		re2 = requests.post(url, data=jdata, headers=head)
		timestr = time.strftime('%Y-%m-%d/%H：%M：%d', time.localtime(time.time()))
		print "第%d次改单收银的系统时间是:" % (self.m) + timestr
		if '操作成功' in re2.text:
			print '第%d次改单收银通过' % self.m
			self.sut2time = re.search('serverCreateTime":\d{12}', str(re2.text)).group()[18:]  # 正则表达式查询后切片读取数据
			print '桌台清台前服务器最新更新时间是：%s' % self.sut2time
		else:
			print '第%d次改单收银失败,返回的错误信息如下:' % self.m
			print re2.text

		# 传参数据
		tradedata ={
	"appType": "5",
	"brandID": 4881,
	"content": {
		"serverUpdateTime": self.sut2time,
		"tableId": 4000162905,
		"updatorId": 88888930971,
		"updatorName": "zhujb"
	},
	"deviceID": "94:a1:a2:30:65:af",
	"shopID": 810002790,
	"systemType": "android",
	"versionCode": "2110060800",
	"versionName": "6.8.0"
}
		jdata = json.dumps(tradedata)  # 传参json格式化处理
		head = {'Content-Type': 'application/json'}  # json请求头
		url = "http://test.calm.shishike.com/CalmRouter/v1/tradeTable/clear"
		# self.re=requests.post("https://testcalm.shishike.com/CalmRouter/v1/trade/submit",data=jdata,headers=head)
		re3 = requests.post(url, data=jdata, headers=head)
		timestr = time.strftime('%Y-%m-%d/%H：%M：%d', time.localtime(time.time()))
		print "第%d次清台的系统时间是:" % (self.m) + timestr
		if '操作成功' in re3.text:
			print '第%d次清台通过' % self.m
		else:
			print '第%d次清台失败,返回的错误信息如下:' % self.m
			print re3.text
if __name__=='__main__':
	# unittest.main()
	suite=unittest.TestSuite()
	suite.addTest(testFSR_here("test_dinnerSubmit"))
	suite.addTest(testFSR_here("test_modify_cash"))
	suite.addTest(testFSR_here("test_clearTable"))
