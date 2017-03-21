#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb
import datetime

# 对用户命令做出判读：＃ 为存储文本，> 为命令
def textHandle(inputText):
    Op = MySQLdb_operation()
    inpuTextlist = inpuText.split()

    ##存储笔记：＃ 标签 文本
    if "＃" == inpuTextlist[0] or "#" == inpuTextlist[0]:
        print ("#存储单条笔记")
        inpuTextlist = inpuText.split()
        print (inpuTextlist)
        tag = inpuTextlist[1]
        content = inpuTextlist[2]
        Op.saveText(tag,content)

    ## 关键词搜索笔记内容：> tag keyword;
    elif ">" == inpuTextlist[0]:
        print(">查询单条笔记")
        tag = inpuTextlist[1]
        keyword = inpuTextlist[2]
        Op.search_keyWord_date(tag,keyword)

    ## 显示某标签下所有内容：? tag 
    elif "?" == inpuTextlist[0] or "？" == inpuTextlist[0]:
        tag = inpuTextlist[1]
        Op.showTagTable(tag)

    ## 删除某条命令：- tag number;
    elif "-" == inpuTextlist[0] or "－" == inpuTextlist[0]:
        tag = inpuTextlist[1]
        num = inpuTextlist[2]
        Op.delete_num(tag,num)

    ## 删除某个标签下所有内容：= tag
    elif "=" == inpuTextlist[0] or "－" == inpuTextlist[0]:
        tag = inpuTextlist[1]
        Op.drop_tagTable(tag)
    else:
        print("错误，请重新输入")
    pass



class MySQLdb_operation(object):

    def __init__(self):

        pass 

    def saveText(self,tag,content):

        query_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # 建立数据库连接
        db = MySQLdb.connect(host="localhost",user="nbr",passwd="1234",db="testDB")
        # 使用cursor()方法获取操作游标 
        cursor = db.cursor()
        print (tag)

        # sql命令语句
        ## 删除/标签表格 删除／插入一行信息  读取特定标签内所有信息/读取今日存入信息

        #sql_dropTable = "DROP TABLE " + tag
        sql_creatTable = "CREATE TABLE IF NOT EXISTS " + tag + " ( col INT NOT NULL AUTO_INCREMENT PRIMARY KEY,create_time TEXT NOT NULL, content TEXT NOT NULL)"
        sql_insert = "INSERT INTO " + tag + " VALUES (NULL,'%s','%s')" % (query_datetime,content)
        # 删除一行信息考虑到微信公众号的消息撤回功能，是否可以代替之？
        #sql_selectTag = "SELECT * from %s" % tag
        #sql_selectDay = " SELECT create_time, content FROM " + tag + " WHERE (create_time like '%" + keyword + "%' )" 
        
        # print 检查sql语句的正确性
        print (sql_creatTable)
        print (sql_insert)
        #print (sql_selectTag)
        #print (sql_selectDay)
        
        # 执行sql命令
        #cursor.execute(sql_dropTable)
        cursor.execute(sql_creatTable)
        cursor.execute(sql_insert)
        #cursor.execute(sql_selectTag)
        #cursor.execute(sql_selectDay)

        # 使用 fetchone() 方法获取一条数据库。
        data = cursor.fetchall() 
        print (data)
        print ("save successfully")
        print (query_datetime)
        # 提交修改
        db.commit()
        # 关闭数据库连接
        db.close()

    def search_keyWord_date(self,tag,keyword):
        db = MySQLdb.connect(host="localhost",user="nbr",passwd="1234",db="testDB")
        cursor = db.cursor()

        sql_selectKeyWord = " SELECT * FROM " + tag + " WHERE (content like '%" + keyword + "%' )" 
        sql_selectDay = " SELECT * FROM " + tag + " WHERE (create_time like '%" + keyword + "%' )" 
        print (sql_selectKeyWord)
        print (sql_selectDay)
        cursor.execute (sql_selectKeyWord)
        cursor.execute (sql_selectDay)
        data = cursor.fetchall() 
        print (data)
        print ("search_keyword successfully")
        
        db.commit()
        db.close()

    def showTagTable(self,tag):
        db = MySQLdb.connect(host="localhost",user="nbr",passwd="1234",db="testDB")
        cursor = db.cursor()

        sql_selectTag = "SELECT * from %s" % tag
        cursor.execute(sql_selectTag)

        data = cursor.fetchall() 
        print (data)
        print('show TagTable successfully')
        db.commit()
        db.close()
        pass


    def delete_num(self,tag,num):
        db = MySQLdb.connect(host="localhost",user="nbr",passwd="1234",db="testDB")
        cursor = db.cursor()

        sql_deleteNum =" DELETE  FROM " + tag + " WHERE (col = " + num +" )" 
        print (sql_deleteNum)
        cursor.execute (sql_deleteNum)

        print ("deleteNum successfully")
        
        db.commit()
        db.close()

    def drop_tagTable (self,tag):
        db = MySQLdb.connect(host="localhost",user="nbr",passwd="1234",db="testDB")
        cursor = db.cursor()

        sql_dropTable ="DROP TABLE " + tag 
        print (sql_dropTable)
        cursor.execute (sql_dropTable)

        print ("dropTable successfully")
        
        db.commit()
        db.close()


if __name__ == '__main__':

    print('''
    ## 存储笔记：＃ 标签 文本;
    ## 关键词／时间搜索笔记内容：> [tag] ［keyword］/[date(like 01-01)]
    ## 显示某标签下所有内容：? [tag]
    ## 删除某条命令：- [tag] [number]
    ## 删除某个标签下所有内容：= [tag]''')

    while 1:
        
        inpuText = input("用户输入:")
        textHandle(inpuText)


        













