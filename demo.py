#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb
import datetime

# 对用户命令做出判读：＃ 为存储文本，> 为命令
def textHandle(inputText):
    if "＃" in inpuText or "#" in inpuText:
        print ("存储")
        inpuTextlist = inpuText.split()
        print (inpuTextlist)
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

        # sql命令语句
        sql_dropTable = "DROP TABLE " + tag
        sql_creatTable = "CREATE TABLE IF NOT EXISTS " + tag + " ( create_time TEXT NOT NULL, content TEXT NOT NULL)"
        sql_insert = "INSERT INTO " + tag + " VALUES ('%s','%s')" % (query_datetime,content)
        sql_select = "SELECT * from %s" % tag
        
        # print 检查sql语句的正确性
        print (sql_creatTable)
        print (sql_insert)
        print (sql_select)
        
        # 执行sql命令
        #cursor.execute(sql_dropTable)
        cursor.execute(sql_creatTable)
        cursor.execute(sql_insert)
        cursor.execute(sql_insert)
        cursor.execute(sql_insert)
        cursor.execute(sql_select)

        # 使用 fetchone() 方法获取一条数据库。
        data = cursor.fetchall()
        print (data)
        print (query_datetime)
        # 关闭数据库连接
        db.close()


if __name__ == '__main__':

    # 用户输入
    # 存储笔记：＃ 标签 文本
    # 删除笔记：> d
    while 1:
        Op = MySQLdb_operation()
        inpuText = input("请输入您的笔记 形式如＃ 标签 文本（请勿忽略＃后的空格）:")
        tag,content = textHandle(inpuText)
        print(tag,content)

        Op.Creat_table(tag,content)













