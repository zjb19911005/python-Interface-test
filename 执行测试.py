import HTMLTestRunner

testunit = unittest.TestSuite()
testunit.addTest(testQSRtrade("test001"))
timestr = time.strftime('%Y%m%d%H%M%d', time.localtime(time.time()))

filename = 'D:\\result' + timestr + '.html'
fp = file(filename, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'快餐下单测试报告',description=u'快餐下单压力测试结果')
runner.run(testunit)
