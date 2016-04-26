#coding=utf-8
_author__ = 'Junior'

#用python来做接口测试
import requests
import MySQLdb
connect=MySQLdb.connect(
    host='rdst5ai4d32fe3qd6if46public.mysql.rds.aliyuncs.com',
    port=3306,
    user='qgd_stf_wt_qa',
    passwd='NPzMwpzYVobbCYBSlv6M',
    db='calm_test',
)
cur=connect.cursor()
a=cur.execute("select * from trade where shop_identy='810002790' ")

print a

# login={}
# re=requests.post("https",data=login)


# if __name__=='__main__':
#     url='http://gitlab.shishike.com/sync/api/wikis/sync/commercial_order_setting'
#     shishike(url)
#     testunit = unittest.TestSuite()
#     testunit.addTest(shishike)
#     timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
#
# filename = 'D:\\result' + timestr + '.html'
# fp = file(filename, 'wb')
# runner = HTMLTestRunner.HTMLTestRunner(
#      stream=fp,
#      title=u'自动化测试报告',
#      description=u'自动化测试结果'
#      )
# runner.run(testunit)
