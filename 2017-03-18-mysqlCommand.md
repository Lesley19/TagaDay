# 有效命令小结

有效命令：

bash>
mysql.server start
mysql.server stop

mysql>
CREATE USER username IDENTIFIED BY 'password';

[Mysql 创建、删除用户 - fly1988happy - 博客园](http://www.cnblogs.com/fly1988happy/archive/2011/12/15/2288554.html)

Mysql 创建、删除用户
MySql 中添加用户, 新建数据库, 用户授权, 删除用户, 修改密码 (注意每行后边都跟个; 表示一个命令语句结束):

1. 新建用户

登录 MYSQL：
　　@>mysql -u root -p

　　@> 密码

创建用户：
　　mysql> insert into mysql.user(Host,User,Password) values("localhost","test",password("1234"));

　　这样就创建了一个名为：test 密码为：1234 的用户。

　　注意：此处的 "localhost"，是指该用户只能在本地登录，不能在另外一台机器上远程登录。如果想远程登录的话，将 "localhost" 改为 "%"，表示在任何一台电脑上都可以登录。也可以指定某台机器可以远程登录。

然后登录一下：
　　mysql>exit;

　　@>mysql -u test -p

　　@> 输入密码

　　mysql > 登录成功

2. 为用户授权

　　授权格式：grant 权限 on 数据库.* to 用户名 @登录主机 identified by "密码";　

登录 MYSQL（有 ROOT 权限），这里以 ROOT 身份登录：
　　@>mysql -u root -p

　　@> 密码

首先为用户创建一个数据库 (testDB)：
　　mysql>create database testDB;

授权 test 用户拥有 testDB 数据库的所有权限（某个数据库的所有权限）：
　　 mysql>grant all privileges on testDB.* to test@localhost identified by '1234';

 　　mysql>flush privileges;// 刷新系统权限表

　　格式：grant 权限 on 数据库.* to 用户名 @登录主机 identified by "密码";　

如果想指定部分权限给一用户，可以这样来写:
　　mysql>grant select,update on testDB.* to test@localhost identified by '1234';

　　mysql>flush privileges; // 刷新系统权限表

授权 test 用户拥有所有数据库的某些权限： 　 
　　mysql>grant select,delete,update,create,drop on *.* to test@"%" identified by "1234";

     //test 用户对所有数据库都有 select,delete,update,create,drop 权限。

　 //@"%" 表示对所有非本地主机授权，不包括 localhost。（localhost 地址设为 127.0.0.1，如果设为真实的本地地址，不知道是否可以，没有验证。）

// 对 localhost 授权：加上一句 grant all privileges on testDB.* to test@localhost identified by '1234'; 即可。

3. 删除用户

 @>mysql -u root -p

 @> 密码

 mysql>Delete FROM user Where User='test' and Host='localhost';

 mysql>flush privileges;

 mysql>drop database testDB; // 删除用户的数据库

删除账户及权限：>drop user 用户名 @'%';

　　　　　　　　>drop user 用户名 @ localhost; 

4. 修改指定用户密码

  @>mysql -u root -p

  @> 密码

  mysql>update mysql.user set password=password('新密码') where User="test" and Host="localhost";

  mysql>flush privileges;

5. 列出所有数据库

mysql>show database;

6. 切换数据库

mysql>use '数据库名';

7. 列出所有表

mysql>show tables;

8. 显示数据表结构

mysql>describe 表名;

9. 删除数据库和数据表

mysql>drop database 数据库名;

mysql>drop table 数据表名;

