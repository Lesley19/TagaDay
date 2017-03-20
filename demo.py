#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb
import datetime

def textHandle(inputText):
    if "＃" in inpuText or "#" in inpuText:
        print ("存储")
        inpuTextlist = inpuText.split()
        tag = inpuTextlist[1]
        content = inpuTextlist[2]
        print(content,tag)

        return tag,content

    elif ">" in inpuText:
        print("命令")
    else:
        print("错误，请重新输入")
    pass



class MySQLdb_operation(object):

    def __init__(self):

        pass

    def Creat_table(self,tag,content):
        query_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # 建立数据库连接
        db = MySQLdb.connect(host="localhost",user="nbr",passwd="1234",db="testDB")
        # 使用cursor()方法获取操作游标 
        cursor = db.cursor()
        print (tag)

        #sql语句
        sql_creatTable = "CREATE TABLE IF NOT EXISTS " + tag + " ( create_time DATETIME NOT NULL, content TEXT NOT NULL)"
        sql_insert = "INSERT INTO " + tag + " VALUES ('%s','%s')" % (query_datetime,content)
        

        # 使用execute方法执行SQL语句
        print (sql_creatTable)
        print (sql_insert)

        cursor.execute(sql_creatTable)
        cursor.execute(sql_insert)


        cursor.execute("SELECT VERSION()")
        cursor.execute("SELECT * from %s" % tag)
        # 使用 fetchone() 方法获取一条数据库。
        data = cursor.fetchall()
        print ("Database version : %s " % data)
        print (query_datetime)
        # 关闭数据库连接
        db.close()


if __name__ == '__main__':
    Op = MySQLdb_operation()
    inpuText = input("请输入您的笔记 形式如＃标签 文本:")
    tag,content = textHandle(inpuText)
    print(tag,content)

    Op.Creat_table(tag,content)













