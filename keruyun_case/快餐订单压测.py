#coding=utf-8


import requests as requests

_author__ = 'Junior'

#用python来做接口测试
import json
import requests
import random
import MySQLdb
# connect=MySQLdb.connect(
#     host='rdst5ai4d32fe3qd6if46public.mysql.rds.aliyuncs.com',
#     port=3306,
#     user='qgd_stf_wt_qa',
#     passwd='NPzMwpzYVobbCYBSlv6M',
#     db='calm_test',
# )
# cur=connect.cursor()
# a=cur.execute("select * from trade where shop_identy='810002790' ")


x=random.randint(10,99)
m=1
for m in range(x):
	i = random.randint(1461726490000, 1561726497979)
	y = random.randint(100, 999)
	print i, y
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
					"paymentUuid": "%s%d"%('b663b8067b9349919252dcda9f987',y),
					"refundWay": 1,
					"usefulAmount": 6.1,
					"brandIdenty": 4881,
					"clientCreateTime": i,
					"clientUpdateTime": i,
					"deviceIdenty": "94:a1:a2:30:8f:7f",
					"shopIdenty": 810002790,
					"statusFlag": 1,
					"uuid":"%s%d"%("d2e6d05624dc4b7fac1bd2c280074",y),
					"changed": "true"
				}],
				"actualAmount": 6.1,
				"creatorId": 88888904893,
				"creatorName": "admin",
				"exemptAmount": 0.0,
				"isPaid": 1,
				"paymentType": 1,
				"receivableAmount": 6.10,
				"relateUuid": "%s%d"%("3d154e6981cf4d629e1e646aae7c1",y),
				"updatorId": 88888904893,
				"updatorName": "admin",
				"brandIdenty": 4881,
				"clientCreateTime": i,
				"clientUpdateTime": i,
				"deviceIdenty": "94:a1:a2:30:8f:7f",
				"shopIdenty": 810002790,
				"statusFlag": 1,
				"uuid":"%s%d"%("b663b8067b9349919252dcda9f987",y),
				"changed": "true"
			}],
			"relateUuid":"%s%d"% ("3d154e6981cf4d629e1e646aae7c1",y),
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
				"tradeUuid":"%s%d"%("3d154e6981cf4d629e1e646aae7c1",y),
				"updatorId": 88888904893,
				"updatorName": "admin",
				"brandIdenty": 4881,
				"clientCreateTime": i,
				"clientUpdateTime": i,
				"deviceIdenty": "94:a1:a2:30:8f:7f",
				"shopIdenty": 810002790,
				"statusFlag": 1,
				"uuid":"%s%d"%("3951e49c6e7e4c9899709e89a173c",y),
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
				"skuUuid":"%s%d"%("43b9067e34f848fbbae1dbd523c77",y),
				"sort": 0,
				"tradeUuid":"%s%d"%("3d154e6981cf4d629e1e646aae7c1",y),
				"type": 0,
				"unitName": "份",
				"updatorId": 88888904893,
				"updatorName": "admin",
				"brandIdenty": 4881,
				"clientCreateTime": i,
				"clientUpdateTime": i,
				"deviceIdenty": "94:a1:a2:30:8f:7f",
				"shopIdenty": 810002790,
				"statusFlag": 1,
				"uuid":"%s%d"%("b52cc023e332411194f05cb285812",y),
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
				"tradeUuid":"%s%d"%("3d154e6981cf4d629e1e646aae7c1",y),
				"updatorId": 88888904893,
				"updatorName": "admin",
				"brandIdenty": 4881,
				"clientCreateTime": i,
				"clientUpdateTime": i,
				"deviceIdenty": "94:a1:a2:30:8f:7f",
				"shopIdenty": 810002790,
				"statusFlag": 1,
				"uuid":"%s%d"%("d7a1223d1e224d89a4a63397bb5a3",y),
				"changed": "true"
			}, {
				"creatorId": 88888904893,
				"creatorName": "admin",
				"privilegeAmount": 0.07,
				"privilegeName": "配送费",
				"privilegeType": 12,
				"privilegeValue": 0.07,
				"promoId": 16548,
				"tradeUuid":"%s%d"%("3d154e6981cf4d629e1e646aae7c1",y),
				"updatorId": 88888904893,
				"updatorName": "admin",
				"brandIdenty": 4881,
				"clientCreateTime": i,
				"clientUpdateTime": i,
				"deviceIdenty": "94:a1:a2:30:8f:7f",
				"shopIdenty": 810002790,
				"statusFlag": 1,
				"uuid":"%s%d"%("2a091f451602425d9fa8e363d087c",y),
				"changed": "true"
			}, {
				"creatorId": 88888904893,
				"creatorName": "admin",
				"privilegeAmount": 2.00,
				"privilegeName": "WWWW",
				"privilegeType": 12,
				"privilegeValue": 2.00,
				"promoId": 16427,
				"tradeUuid":"%s%d"%("3d154e6981cf4d629e1e646aae7c1d",y),
				"updatorId": 88888904893,
				"updatorName": "admin",
				"brandIdenty": 4881,
				"clientCreateTime": i,
				"clientUpdateTime": i,
				"deviceIdenty": "94:a1:a2:30:8f:7f",
				"shopIdenty": 810002790,
				"statusFlag": 1,
				"uuid":"%s%d"%("2b58d27e66614c509789b4f58e680",y),
				"changed": "true"
			}, {
				"creatorId": 88888904893,
				"creatorName": "admin",
				"privilegeAmount": 0.02,
				"privilegeName": "测试费用1",
				"privilegeType": 12,
				"privilegeValue": 2.00,
				"promoId": 16408,
				"tradeUuid":"%s%d"%("3d154e6981cf4d629e1e646aae7c1",y),
				"updatorId": 88888904893,
				"updatorName": "admin",
				"brandIdenty": 4881,
				"clientCreateTime": i,
				"clientUpdateTime": i,
				"deviceIdenty": "94:a1:a2:30:8f:7f",
				"shopIdenty": 810002790,
				"statusFlag": 1,
				"uuid":"%s%d"%("da58277cc2e0466b8abbf4609a04a",y),
				"changed": "true"
			}, {
				"creatorId": 88888904893,
				"creatorName": "admin",
				"privilegeAmount": 3.00,
				"privilegeName": "餐盒费",
				"privilegeType": 12,
				"privilegeValue": 3.00,
				"promoId": 6404,
				"tradeUuid":"%s%d"%("3d154e6981cf4d629e1e646aae7c1",y),
				"updatorId": 88888904893,
				"updatorName": "admin",
				"brandIdenty": 4881,
				"clientCreateTime": i,
				"clientUpdateTime": 1461742758002,
				"deviceIdenty": "94:a1:a2:30:8f:7f",
				"shopIdenty": 810002790,
				"statusFlag": 1,
				"uuid":"%s%d"%("f9aabbaa1d21451d8e2c56077c843",y),
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
			"tradeNo": "1011604271535401231%"%y,
			"tradePayForm": 1,
			"tradePayStatus": 1,
			"tradePeopleCount": 1,
			"tradeStatus": 3,
			"tradeTime": 1461742540547,
			"tradeType": 1,
			"updatorId": 88888904893,
			"updatorName": "admin",
			"brandIdenty": 4881,
			"clientCreateTime": i,
			"clientUpdateTime": i,
			"deviceIdenty": "94:a1:a2:30:8f:7f",
			"shopIdenty": 810002790,
			"statusFlag": 1,
			"uuid":"%s%d"%("3d154e6981cf4d629e1e646aae7c1",y),
			"changed": "true"
		}
	},
	"deviceID": "94:a1:a2:30:8f:7f",
	"shopID": 810005454,
	"systemType": "android",
	"versionCode": "2110060701",
	"versionName": "6.7.1"
	}
	jdata=json.dumps(tradedata)
	head={'Content-Type':'application/json'}

	re=requests.post("http://121.40.154.42:9820/CalmRouter/v1/trade/create+cash",data=jdata,headers=head)
	m=m+1,
	if m==1 and re.status_code==200:
		print re.text
	elif re.status_code==200:
		print '第%d次测试通过'%m
	else:
		print 'error,please try again!'

# if __name__=='__main__':
#     url='http://gitlab.shishike.com/sync/api/wikis/sync/commercial_order_setting'
#     shishike(url)
#     testunit = unittest.TestSuite()
#     testunit.addTest(shishike)
#     timestr = time.strftime('%Y%m%d%H%M%d', time.localtime(time.time()))
#
# filename = 'D:\\result' + timestr + '.html'
# fp = file(filename, 'wb')
# runner = HTMLTestRunner.HTMLTestRunner(
#      stream=fp,
#      title=u'自动化测试报告',
#      description=u'自动化测试结果'
#      )
# runner.run(testunit)
