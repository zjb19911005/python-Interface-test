#coding=utf-8

import MySQLdb
connect=MySQLdb.connect(
    host='rdst5ai4d32fe3qd6if46public.mysql.rds.aliyuncs.com',
    port=3306,
    user='qgd_stf_wt_qa',
    passwd='NPzMwpzYVobbCYBSlv6M',
    db='calm_test',
)
cur=connect.cursor()
#获取数据库有多少条数据
a=cur.execute("SELECT * FROM trade WHERE shop_identy = 810002790 AND source = 3 AND trade_status = 3 AND trade_time>'2016-04-28' limit 10 ")
print '本次数据查询出合适的数据为%d条' %a
print '详情如下'
#打印列表中的数据
info=cur.fetchmany(a)
for i in  info:
    print i
#关闭表单
cur.close()
connect.commit()
connect.close


