#coding=utf-8
import MySQLdb
import random
import re

connect=MySQLdb.connect(
    host='rdst5ai4d32fe3qd6if46public.mysql.rds.aliyuncs.com',
    port=3306,
    user='qgd_stf_wt_qa',
    passwd='NPzMwpzYVobbCYBSlv6M',
    db='calm_test',
)
cur=connect.cursor()
#获取数据库有多少条数据
# a=cur.execute("SELECT * FROM trade WHERE shop_identy = 810002790 AND source = 3 AND trade_status = 3 AND trade_time>'2016-04-28' limit 10 ")
# #删除数据库未处理的2000的订单
# # b=cur.execute('DELETE FROM trade WHERE shop_identy = 810002790 AND trade_status = 1 limit 2000')
# print '本次数据查询出合适的数据为%d条' %a
# print '详情如下'
# #打印列表中的数据
# info=cur.fetchmany(a)
# for i in  info:
#     print i
# y = random.randint(1000, 9999)
sut1 = cur.execute("select 1000*UNIX_TIMESTAMP(server_create_time) from trade where uuid = 'e7bf82d54146450b98070d027f3f2054'"),
sut1times = cur.fetchone()
print str(sut1times)[10:23]
y=2054
sct2 = cur.execute("select 1000*UNIX_TIMESTAMP(server_create_time) from trade where uuid = 'e7bf82d54146450b98070d027f3f%s'"% y),
sct2times =cur.fetchone()
print str(sct2times)[10:23]




#关闭表单
cur.close()
connect.commit()
connect.close


