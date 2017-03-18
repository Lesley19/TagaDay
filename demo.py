#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

class MySQLdb_operation(object):

    def __init__(self):
        pass

    def Creat_table(self):
        # 建立数据库连接
        db = MySQLdb.connect(host="localhost",user="nbr",passwd="1234",db="testDB")
        # 使用cursor()方法获取操作游标 
        cursor = db.cursor()
        # 使用execute方法执行SQL语句
        cursor.execute("SELECT VERSION()")
        # 使用 fetchone() 方法获取一条数据库。
        data = cursor.fetchone()
        print "Database version : %s " % data
        # 关闭数据库连接
        db.close()


if __name__ == '__main__':

    Op = MySQLdb_operation()
    Op.Creat_table()