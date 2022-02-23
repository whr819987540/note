

数据库：文件DB
数据库管理系统：操作数据库的软件 DBMS
sql and nosql

mysql不要exe安装，使用压缩包安装
bin目录下net start mysql启动mysql服务

net stop mysql 关闭mysql服务，win平台可以在设备管理器的服务界面进行查看

进入bin

开启mysql服务：net start mysql
退出exit
关闭mysql服务：net stop mysql
sc delete mysql清空mysql服务
基字符集：utf-8
数据库排序规则（utf-general-ci）

关于登录mysql，直接使用mysql -u username -p后提示输入密码，本机为root/123456

在配置文件中可以免密登录，不过需要管理员权限，这是对数据安全的一种保护

basedir是软件的根目录

datadir自己指定，一般是根目录的data目录，用来放数据库文件，不用自己新建

```bash
[mysqld]
basedir=D://software/mysql-5.7.19/mysql-5.7.19-winx64/
datadir=D://software/mysql-5.7.19/mysql-5.7.19-winx64/data/
port=3306
character-set-server=utf8
#skip-grant-tables
```



可视化工具sqlyog的执行操作==sql语句==在历史记录中查看
引擎innoDB

创建数据库--创建数据库中的一张表--表名，表的内容--新增内容

任何时候通过命令行进入数据库时，都需要先通过管理员权限打开mysql服务，然后链接mysql
语句要; 表示结束

命令不需要
show databases;
use school;切换数据库（database changed）
show tables；
describe table_name;    show the rows of table
create database name;
DDL定义define
DML管理操作management
DQL查询query
DCL控制control

create database if not exists name(名称放在exists后面)

mysql> create database if not exists mv;
Query OK, 1 row affected, 1 warning (0.00 sec)

查看warning的命令show warnings;

```bash
mysql> show warnings;
+-------+------+---------------------------------------------+
| Level | Code | Message                                     |
+-------+------+---------------------------------------------+
| Note  | 1007 | Can't create database 'mv'; database exists |
+-------+------+---------------------------------------------+
1 row in set (0.00 sec)
```



drop database if exists name(对于不存在的数据库，drop会报错)

创建时，需要看是否存在，若存在，不能创建

删除时，要看是否存在，若不存在，不能删除

对于数据库、表、字段的名称，最好用``引起来



如果表名或者字段名是特殊字符，需要用``

数据库的数据类型
tinyint, smallint, middleint,int,mediumint,big
float,double
decimal 字符串类型的浮点数（金融领域）参数（总位数，小数点位数），内部以字符形式存储，所以是精确的

char 1字节    0-255
##varchar 可变字符串 0-65536储存字符串
tinytext 2^8-1
##text 2^16-1储存文本

date  日期YYYY-MM-DD
time  时间HH:MM:SS
##datetimeYYYY-MM-DD HH:MM:SS
##timestamp时间戳，1970.1.1到现在的秒数

数据库的字段属性：

unsigned：
无符号，整数，值不能为负数

zerofill：
不够的位数用0填充
int 的长度：
int总是储存为4字节，表示的范围也是固定的，需要和zerofill配合使用
int（5）===123===00123

主键==值唯一的==index

自增：每条记录在上一条的基础上+1，用于序号
和主键配合使用

非空
如果不给值，会报错

默认：（默认值）

id主键，自增
'version'，  乐观锁
is_delete     伪删除
gmt_create  创建时间
gmt_update  修改时间

show create database databasename;

//给出建立databasename的语句

```bash
mysql> show create database test;
+----------+---------------------------------------------------------------+
| Database | Create Database                                               |
+----------+---------------------------------------------------------------+
| test     | CREATE DATABASE `test` /*!40100 DEFAULT CHARACTER SET utf8 */ |
+----------+---------------------------------------------------------------+
```



show create table table_name

给了默认值，是让用户可以不输入，是可选的字段，这时就不需要not null了

不给默认值，又是not null，就是用户必须输入的内容了

```bash
CREATE TABLE `app_user` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT '' COMMENT '用户昵称',
  `email` varchar(50) NOT NULL COMMENT '用户邮箱',
  `phone` varchar(20) DEFAULT '' COMMENT '手机号',
  `gender` tinyint(4) unsigned DEFAULT '0' COMMENT '性别（0：男;1:女）',
  `password` varchar(100) NOT NULL COMMENT '密码',
  `age` tinyint(4) DEFAULT '0' COMMENT '年龄',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `id_name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=1000002 DEFAULT CHARSET=utf8 COMMENT='app用户表' |
```



实例：创建一个数据库，叫做LessonOne。里面有两张表，一张表是学号（int4，非负，自增，零填充，主键）姓名（varchar50，非空），班号（varchar10，非空）；一张是班号（varchar10，非空，主键），班名（varchar50，非空）。

```bash
CREATE TABLE IF NOT EXISTS`student`(
     `id` INT(4) UNSIGNED AUTO_INCREMENT ,
     `name` VARCHAR(50) NOT NULL,
     `class id` VARCHAR(10) NOT NULL,
     PRIMARY KEY(`id`)
     )ENGINE=INNODB AUTO_INCREMENT=1000 DEFAULT CHARSET=utf8;
```



表重命名alter table name rename as newname

```bash
mysql> show tables;
+----------------+
| Tables_in_test |
+----------------+
| app_user       |
| my             |
| mytest         |
| student        |
+----------------+
4 rows in set (0.00 sec)

mysql> alter table mytest rename as mytest_new
    -> ;
Query OK, 0 rows affected (0.01 sec)

mysql> show tables;
+----------------+
| Tables_in_test |
+----------------+
| app_user       |
| my             |
| mytest_new     |
| student        |
+----------------+
4 rows in set (0.00 sec)
```

修改字段

```bash

```



增加字段alter table name add name attr comment

```bash
mysql> describe my
    -> ;
+-------+-------------+------+-----+-----------+-------+
| Field | Type        | Null | Key | Default   | Extra |
+-------+-------------+------+-----+-----------+-------+
| name  | int(5)      | NO   | PRI | 111       |       |
| age   | varchar(20) | YES  |     | Annoymous |       |
| grade | varchar(10) | NO   |     | NULL      |       |
+-------+-------------+------+-----+-----------+-------+
3 rows in set (0.00 sec)

mysql> alter table my add `location` varchar(50) default 'China' comment'出生地';
Query OK, 0 rows affected (0.06 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> describe my;
+----------+-------------+------+-----+-----------+-------+
| Field    | Type        | Null | Key | Default   | Extra |
+----------+-------------+------+-----+-----------+-------+
| name     | int(5)      | NO   | PRI | 111       |       |
| age      | varchar(20) | YES  |     | Annoymous |       |
| grade    | varchar(10) | NO   |     | NULL      |       |
| location | varchar(50) | YES  |     | China     |       |
+----------+-------------+------+-----+-----------+-------+
4 rows in set (0.00 sec)
```



重命名字段alter table name change oldname newname ==属性（至少得有类型）==

```bash
mysql> describe my;
+----------+-------------+------+-----+-----------+-------+
| Field    | Type        | Null | Key | Default   | Extra |
+----------+-------------+------+-----+-----------+-------+
| name     | int(5)      | NO   | PRI | 111       |       |
| age      | varchar(20) | YES  |     | Annoymous |       |
| grade    | varchar(10) | NO   |     | NULL      |       |
| location | varchar(50) | YES  |     | China     |       |
+----------+-------------+------+-----+-----------+-------+
mysql> alter table my change `location` `loc`;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '' at line 1
mysql> alter table my change `location` `loc` varchar(50);
Query OK, 0 rows affected (0.01 sec)
Records: 0  Duplicates: 0  Warnings: 0
mysql> describe my;
+-------+-------------+------+-----+-----------+-------+
| Field | Type        | Null | Key | Default   | Extra |
+-------+-------------+------+-----+-----------+-------+
| name  | int(5)      | NO   | PRI | 111       |       |
| age   | varchar(20) | YES  |     | Annoymous |       |
| grade | varchar(10) | NO   |     | NULL      |       |
| loc   | varchar(50) | YES  |     | NULL      |       |
+-------+-------------+------+-----+-----------+-------+

这里根据error可以看出来，不能只有字段的名称
这个类型也是可以改变的
mysql> alter table my change `loc` `loc_new` varchar(40);
Query OK, 0 rows affected (0.07 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> describe my;
+---------+-------------+------+-----+-----------+-------+
| Field   | Type        | Null | Key | Default   | Extra |
+---------+-------------+------+-----+-----------+-------+
| name    | int(5)      | NO   | PRI | 111       |       |
| age     | varchar(20) | YES  |     | Annoymous |       |
| grade   | varchar(10) | NO   |     | NULL      |       |
| loc_new | varchar(40) | YES  |     | NULL      |       |
+---------+-------------+------+-----+-----------+-------+
```





修改字段的列属性alter table name modify name attr，策略是指定了的如果和之前的冲突，那么就修改，否则不修改

```bash
mysql> alter table my modify `loc_new` varchar(10) not null
    -> ;
Query OK, 0 rows affected (0.09 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> describe my;
+---------+-------------+------+-----+-----------+-------+
| Field   | Type        | Null | Key | Default   | Extra |
+---------+-------------+------+-----+-----------+-------+
| name    | int(5)      | NO   | PRI | 111       |       |
| age     | varchar(20) | YES  |     | Annoymous |       |
| grade   | varchar(10) | NO   |     | NULL      |       |
| loc_new | varchar(10) | NO   |     | NULL      |       |
+---------+-------------+------+-----+-----------+-------+
```



删除表的字段alter table name drop name一个潜在的错误时字段不存在

```bash
mysql> alter table my drop `te`
    -> ;
ERROR 1091 (42000): Can't DROP 'te'; check that column/key exists
mysql> describe my;
+---------+-------------+------+-----+-----------+-------+
| Field   | Type        | Null | Key | Default   | Extra |
+---------+-------------+------+-----+-----------+-------+
| name    | int(5)      | NO   | PRI | 111       |       |
| age     | varchar(20) | YES  |     | Annoymous |       |
| grade   | varchar(10) | NO   |     | NULL      |       |
| loc_new | varchar(10) | NO   |     | NULL      |       |
+---------+-------------+------+-----+-----------+-------+
4 rows in set (0.00 sec)
mysql> alter table my drop loc_new;
Query OK, 0 rows affected (0.10 sec)
Records: 0  Duplicates: 0  Warnings: 0
mysql> describe my;
+-------+-------------+------+-----+-----------+-------+
| Field | Type        | Null | Key | Default   | Extra |
+-------+-------------+------+-----+-----------+-------+
| name  | int(5)      | NO   | PRI | 111       |       |
| age   | varchar(20) | YES  |     | Annoymous |       |
| grade | varchar(10) | NO   |     | NULL      |       |
```



被引用了的表不能直接删除

添加外键
alter table name add 'FK_' foreign key('') references table_name(``)
添加的是数据库级别的外键，物理外键，不好删除

insert into table_name(字段，字段）values（'' ,'' ,）

字段的顺序需要和后面的values的顺序建立对应关系

values的顺序是同一行的顺序，根据字段的顺序来的，所以插入的是同一行的数据
在一行数据中，如果 有默认值，可以不指定；如果没有，必须写上去，否则会报错；对于自增类型的，默认从上面一行开始自增，如果没有上面一行，则从1开始
插入多行数据需要在括号之间用,隔开，括号内的内容同样遵循同一行时的规则
如果一行有多个字段，又只想给一个字段insert，需要保证没有not null，或者有not null 但是有default值
如果不指定字段名，需要一一对应，自增的也不能省略



modify之后必须带上字段类型



# DDL数据库定义语言（搭建一个框架）

## 数据库

1. 创建数据库 create database if not exists database_name
2. 删除数据库 drop database if exists database_name

> 数据库到表还需要一步：use database_name

## 表

1. 创建表create table if not exists table_name(

   ​	\`  字段名 \`  属性,

   primary key('') 

   )engine=innodb charset=utf8

2. 删除表drop table if exists table_name

3. 改表名alter table table_name rename as new_name

## 字段

1. 增加字段alter table table_name add '字段名' 属性
2. 删除字段alter table table_name drop '字段名'
3. 修改字段 alter talbe table_name modify '字段名' 属性（如果属性定义过了，那么就会覆盖；如果没有定义过，那么就是新增属性）###***必须要有字段类型***



# DML数据库管理语言（框架搭好后，写入数据）数据层面的操作

## 插入数据

insert into table_name [('字段1'，'字段2')] values(value1,value2)[,(value1,value2)]

1. 字段名是可选的。如果不指定，字段必须和后面的value对应，即使有的字段有默认值；如果指定，更要对应。
2. 可以一次添加多条数据（excel的多行数据），在保证1的前提下，用','隔开

```bash
mysql> insert into student (`name`,`class id`) values('张华','1904301'),('李宁','1904302');
Query OK, 2 rows affected (0.02 sec)
Records: 2  Duplicates: 0  Warnings: 0

mysql> select * from student
    -> ;
+------+------+----------+
| id   | name | class id |
+------+------+----------+
| 1000 | 张华 | 1904301  |
| 1001 | 李宁 | 1904302  |
+------+------+----------+
```



## 修改数据

update table_name set 字段名（列）=value where condition

1. 字段相当于一列，如果不指定where的条件限制，会修改整列的数据
2.  =&<=&>=&!=&>&<&and&or 

这里强烈建议将字段名和表名用``引用起来

```bash
mysql> select *from student;
+------+------+----------+
| id   | name | class id |
+------+------+----------+
| 1000 | 张华 | 1904301  |
| 1001 | 李宁 | 1904302  |
+------+------+----------+
2 rows in set (0.00 sec)

mysql> update student set class id = '1904302'  where id=1000
    -> ;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'id = '1904302'  where id=1000' at line 1
mysql> update student set `class id` = '1904302'  where `id`=1000;
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select *from student;
+------+------+----------+
| id   | name | class id |
+------+------+----------+
| 1000 | 张华 | 1904302  |
| 1001 | 李宁 | 1904302  |
+------+------+----------+
```



## 删除数据

delete from table_name where condion

1. 删除数据是根据where的条件，选择某一个数据项，也就是根据某个字段删除一行

```bash
mysql> select * from student
    -> ;
+------+------+----------+
| id   | name | class id |
+------+------+----------+
| 1000 | 张华 | 1904301  |
| 1001 | 李宁 | 1904302  |
| 1002 | 张华 | 1904301  |
| 1003 | 李宁 | 1904302  |
+------+------+----------+
4 rows in set (0.01 sec)

mysql> delete from student where id>1001
    -> ;
Query OK, 2 rows affected (0.02 sec)

mysql> select *from student;
+------+------+----------+
| id   | name | class id |
+------+------+----------+
| 1000 | 张华 | 1904301  |
| 1001 | 李宁 | 1904302  |
+------+------+----------+
```



# DQL，数据库查询语言（查询数据）



- select的结果默认没有顺序，或者说select的结果其实是存储的顺序（如果没有order by）。

- 有无分号。在GUI app中，如果是一条语句，不重要；如果是多条语句，那么就需要分号。而在命令行中，是一定要分号的。

  对关键字不区分大小写，insert==INSERT

  对表名和字段呢?

  首先看看表名，大小写是区分的。

  ![image-20210423204631839](https://gitee.com/hit_whr/pic_2.0/raw/master/20210423204631.png)

  ![image-20210423204754304](https://gitee.com/hit_whr/pic_2.0/raw/master/20210423204754.png)



​	对于字段名，大小写是不区分的，类似于关键字。

​		![image-20210423204915456](https://gitee.com/hit_whr/pic_2.0/raw/master/20210423204915.png)



​	无论区不区分，最好按照规范来，数据库名、表名、字段名都用小写。



- 显示与distinct相关联的所有数据，这是不可行的，因为显示哪个呢？

  比如，select a,distinct b from table，这就很迷惑，如果b字段有相同的值，那么a取哪一个呢？

  ![image-20210423205501247](https://gitee.com/hit_whr/pic_2.0/raw/master/20210423205501.png)

- limit规定显示的记录的条数

  第一个参数是开始的下标，第二个参数是找几个。那么必须要求每次select的结果一样。

  都显示出来。

  ![image-20210423205704897](https://gitee.com/hit_whr/pic_2.0/raw/master/20210423205705.png)

  分五条显示

  ![image-20210423205751173](https://gitee.com/hit_whr/pic_2.0/raw/master/20210423205751.png)

  ![image-20210423205815363](https://gitee.com/hit_whr/pic_2.0/raw/master/20210423205815.png)

​		

- select如果没有order by。也不是完全的随机顺序，而是索引的查询顺序，所以只要没有进行修改，就是稳定的使用某个数据库

- 表名不允许相同，但是某两个表的字段名可以相同，如果要同时使用这两个表，需要用完全限定的字段名。同时，可以用完全限定的表名，也就是database_name.table_name

- order by可以一个列，可以多个。多个列时，排序按照字段出现的先后顺序确定优先级，先出现的先作为排序标准

  一个列

  ![image-20210423210257062](https://gitee.com/hit_whr/pic_2.0/raw/master/20210423210257.png)



​		多个列

​			![image-20210423210330797](https://gitee.com/hit_whr/pic_2.0/raw/master/20210423210330.png)

​	现在可以看出来，都是按照升序进行的（默认升序），我们也可以指定为降序（descending）格式为

​	order by 字段1desc，[字段2]

​	![image-20210423211252727](https://gitee.com/hit_whr/pic_2.0/raw/master/20210423211252.png)

​	

![](https://gitee.com/hit_whr/pic_2.0/raw/master/20210423211257.png)

- 尽量少使用*，因为会降低查询的效率，而且将所有数据送给app，是不安全而且没有效率的。

- 现在将from，order by，limit三个子句结合起来。比如，找id大小的前三名。首先是from，得知道是哪张表；然后排序，只有排好序了，limit的结果才有意义。

  ![image-20210423211734138](https://gitee.com/hit_whr/pic_2.0/raw/master/20210423211734.png)

- 

## 简单查询（只涉及一张表）

1. select '字段1'，'字段2'或者全部* from table_name
2. select '字段' as name1 from table_name as name2   在表的结构中字段名以及表名没有发生改变，只是在显示的时候以别名的形式展现
3. 如果as后面的名称和关键字冲突了，加上反引号
4. select '字段1'，'字段2'或者全部* from table_name ***where condition***
5. select ***distinct***  `字段名`from table_name如果查询的结果中字段名对应的数据相同，则只返回一条数据项。显然，是为了看字段名下数据的种类。
6. select concat('string1',字段名) as from table_name 对查询出来的数据进行处理，最终结果为string1+数据项

```bash
mysql> select concat('your ',pid) from category;
+---------------------+
| concat('your ',pid) |
+---------------------+
| your 1              |
| your 1              |
| your 3              |
| your 1              |
| your 3              |
| your 5              |
| your 2              |
+---------------------+
7 rows in set (0.00 sec)
mysql> select concat('your ',pid) as pid from category;
+--------+
| pid    |
+--------+
| your 1 |
| your 1 |
| your 3 |
| your 1 |
| your 3 |
| your 5 |
| your 2 |
+--------+
```



1. 在查询结果中以表达式进行显示：select 'score'/100*5 as newscore from table_name

```bash
mysql> select (pid+1)/2 as pid from category;
+--------+
| pid    |
+--------+
| 1.0000 |
| 1.0000 |
| 2.0000 |
| 1.0000 |
| 2.0000 |
| 3.0000 |
| 1.5000 |
+--------+
```



1. select score from studentinfo where score between 95 and 100 /where score >=95 and score <=100

## 模糊查询

1. is null

   null和''空字符串有区别

   select addreess from studentinfo where address ==is null== or address=‘’

   空字符串不等于NULL

   如果指定了not null，就不要再写default了

2. is not null

3. like 

   select studentname as '名字'，studentid as '学号' from studentinfo where studentname like '刘%'

   %表示任意个字符，_表示一个字符 

   ```bash
   mysql> select * from category where categoryName like "%开发";
   +------------+-----+--------------+
   | categoryid | pid | categoryName |
   +------------+-----+--------------+
   |          3 |   1 | 软件开发     |
   |          6 |   3 | web开发      |
   +------------+-----+--------------+
   2 rows in set (0.00 sec)
   
   mysql> select * from category where categoryName like "_开发";
   Empty set (0.00 sec)
   
   mysql> select * from category where categoryName like "__开发";
   +------------+-----+--------------+
   | categoryid | pid | categoryName |
   +------------+-----+--------------+
   |          3 |   1 | 软件开发     |
   +------------+-----+--------------+
   ```

   

4. in

   select id,grade from sdudentinfo where id in (1,3)

   避免写大量相似的语句，只需要修改括号中的内容

   在使用in的时候是完全匹配，只有完全符合才行；与like不同，而且不能使用通配符

   ```bash
   mysql> select * from category where pid in (1,2,3)
       -> ;
   +------------+-----+--------------+
   | categoryid | pid | categoryName |
   +------------+-----+--------------+
   |          2 |   1 | 信息技术     |
   |          3 |   1 | 软件开发     |
   |          4 |   3 | 数据库       |
   |          5 |   1 | 美术设计     |
   |          6 |   3 | web开发      |
   |          8 |   2 | 办公信息     |
   +------------+-----+--------------+
   ```

   

## 联表查询（涉及多张表）

1. select 字段名 from table_a [as] right/left/inner join table_b [as] on condition where condition
2. 对于字段名，如果table_a table_b中有相同的字段名，需要table_a.字段名来防止ambiguous
3. join的方式取决于需求 
4. on，where都表示条件
5. 思路：
   1. 分析需求，要查询的字段来自哪些表，则后面需要用到哪些表
   2. 确定连接方式
   3. 确定交叉点，即为on的condition
   4. 附加一些判断条件where condition
   5. 要用到多张表时，两张两张的分析

## 排序和分页

1. order by 字段名 asc/desc。ascending升序，descending降序
2. limit 第i条数据，一页显示多少条数据
3. 例如：有0-19的数据，pagesize设为5

| 第一页 | 0，1,2,3,4==0,5           |
| ------ | ------------------------- |
| 第二页 | 5,6,7,8,9==5,5            |
| 第三页 | 10,11,12,13,14==10,5      |
| 第四页 | 15,16,17,18,19==15,5      |
| 第n页  | （n-1)*pagesize，pagesize |

 

## 过滤

顺序是from,where,order by,limit

逻辑运算符包括

` = <= >= <> and or is is not between&and  in not in like is null is not null ()用来显式的指定逻辑运算顺序`

![image-20210423212856110](https://gitee.com/hit_whr/pic_2.0/raw/master/20210423212856.png)



![image-20210423212746931](https://gitee.com/hit_whr/pic_2.0/raw/master/20210423212747.png)





==mysql在执行匹配时不区分大小写，所以与SELECT *FROM customers WHERE cust_country IN ('usa','China')结果相同==

![image-20210423213134919](https://gitee.com/hit_whr/pic_2.0/raw/master/20210423213135.png)



对于between and，可以看出来，是闭区间

![image-20210423213459401](https://gitee.com/hit_whr/pic_2.0/raw/master/20210423213459.png)





is null is not null，查看是否为空值，和0、‘’、空格都不一样，后者是有值的，而null是没有显式的指定值。

![image-20210423213915956](https://gitee.com/hit_whr/pic_2.0/raw/master/20210423213916.png)



选取id在某个集合内的，然后按照id升序，然后名称升序排列

![image-20210423215551728](https://gitee.com/hit_whr/pic_2.0/raw/master/20210423215551.png)



### in的select

in依次检索括号内的所有值，而这个值本身是可以由select返回的，这样条件就变得更加高级了

vendors表中的内容

![image-20210423220146327](https://gitee.com/hit_whr/pic_2.0/raw/master/20210423220146.png)



products表中的内容

![image-20210423220209109](https://gitee.com/hit_whr/pic_2.0/raw/master/20210423220209.png)



根据vendors表获得产地为空的vendor_id，然后根据这些值，获得产品名称（三无产品）

`SELECT prod_name FROM products WHERE vend_id IN (SELECT vend_id FROM vendors WHERE vend_state IS NULL)`

![image-20210423220303323](https://gitee.com/hit_whr/pic_2.0/raw/master/20210423220303.png)



再看看not in（对in否定，取反）

![image-20210423220751844](https://gitee.com/hit_whr/pic_2.0/raw/master/20210423220751.png)



### like

like的特点就是可以和通配符一起使用

- %，匹配任意数量的任意字符，0，1，2---

  ![image-20210423221848681](https://gitee.com/hit_whr/pic_2.0/raw/master/20210423221848.png)

- %不能匹配null

- _匹配且仅匹配一个任意字符

- 少用通配符；少在开头使用通配符，减少mysql的工作量

- ![image-20210423222334368](https://gitee.com/hit_whr/pic_2.0/raw/master/20210423222334.png)



### 有限的正则

首先得明确，mysql支持的正则表达式只是一小部分

需要用到关键字REGEXP

工作原理是在列的每一个值中进行匹配，如果存在，即返回一整行

![image-20210423224259351](https://gitee.com/hit_whr/pic_2.0/raw/master/20210423224259.png)



默认不区分大小写，如果非得区分，加上关键字REGEXP BINARY

![image-20210423224328525](https://gitee.com/hit_whr/pic_2.0/raw/master/20210423224328.png)



![image-20210423224501319](https://gitee.com/hit_whr/pic_2.0/raw/master/20210423224501.png)



![image-20210423224515602](https://gitee.com/hit_whr/pic_2.0/raw/master/20210423224515.png)



通过例子可以看出来，REGEXP实际上就是字符串的匹配

匹配多个串‘string a|string b’

![image-20210423224738425](https://gitee.com/hit_whr/pic_2.0/raw/master/20210423224738.png)





![image-20210423224759687](https://gitee.com/hit_whr/pic_2.0/raw/master/20210423224759.png)



匹配字符范围（类似in的清单）

[abc]或者写成[a-c]

否定范围（类似not in的清单）

[^abc]

清单内是或的关系

![image-20210423225040824](https://gitee.com/hit_whr/pic_2.0/raw/master/20210423225040.png)



![image-20210423225137999](https://gitee.com/hit_whr/pic_2.0/raw/master/20210423225138.png)



[abc]或者写成[a-c]

![image-20210423225324790](https://gitee.com/hit_whr/pic_2.0/raw/master/20210423225324.png)



现在看到mysql里面正则的特殊字符有，[]，-，|，.

那么如果串里面有这些字符呢？可以用 \\\\+字符来实现

尴尬的事情是，如果要匹配\呢？答案是\\\\\\来实现



预定义的字符类（类似c的字符类型判断isdigit(),isalpha())

![image-20210424151612880](https://gitee.com/hit_whr/pic_2.0/raw/master/20210424151620.png)



指定出现的数量

*出现任意次，+出现一次或多次，？出现一次或0次，{n}出现n次，{n，m}出现n次或m次，{n,}出现n次及其以上

![image-20210424151923324](https://gitee.com/hit_whr/pic_2.0/raw/master/20210424151923.png)



![image-20210424152202193](https://gitee.com/hit_whr/pic_2.0/raw/master/20210424152202.png)



定位符（^确定以……开头，$确定以……结尾，

![image-20210424152358430](https://gitee.com/hit_whr/pic_2.0/raw/master/20210424152358.png)





如果数据库中没有很好的测试数据，如何在query前测试正则表达式是否满足我们的需求，是否正确呢？

一个方法是select string regexp string返回的结果是1或0



## 自连接

1. 一张表中的数据项之间相互关联，类似于树
2. 需要多次用到这唯一的一张表
3. 同样需要明确需求，来源是这张唯一的表
4. 用别名来标识

select a.categoryname as '父名', b.categoryname as '子名'

from table as a,table as b

where a.categoryid = b.pid

## 子查询


1. 在查询语句中的WHERE条件子句中,又嵌套了另一个查询语句
2. 嵌套查询可由多个子查询组成,求解的方式是由里及外;
3. 子查询返回的结果一般都是集合,故而建议使用IN关键字;

清空数据

1. delete from table_name -- with no condition

2. truncate table_name

3. 二者都能清空数据，而对表的结构（字段及其属性）没有影响。

4. truncate的速度更快，重置auto_increment计数器（似乎一切都恢复到创建表时的样子了）；不会对事务产生影响

   

创建表之前一般先删一下

drop table if exists table_name

create table table_name

查询数据库的版本号select version()

查询自增的步长select @@auto_increment_increment



# 计算字段

为什么说数据需要计算呢？

因为按照关系数据库的设计，每个字段都是不可再分的，比如工资如果包括基本工资和提成，那么放到数据库里面的一定是两项，而不是一项，这样做对于存储数据有好处，但是如果app就需要工资这一项呢？

可以将两类数据一起给app，让app来处理。但更好的做法是让数据库给出app需要的数据。

![](https://gitee.com/hit_whr/pic_2.0/raw/master/20210424154057.png)



so，计算字段指的是不存在于数据库内，在运行时select创建的字段

==注意计算字段是在select里面定义的==





## 拼接字段

字段串拼接函数concat（）

![image-20210424154532806](https://gitee.com/hit_whr/pic_2.0/raw/master/20210424154532.png)

将vend_name和vend_country拼接起来，构成新的字段，as 对这个字段进行命名，方便后续的order by操作。而且，在显示的时候mysql不会用之前的名字（如果有）而是别名

去除空格的函数，trim（字段）去除左右两侧的空格，rtrim（字段）去除右侧空格，ltrim（字段）去除左侧空格



## 对结果进行测试

和之前select直接测试regexp一样，可以用select计算字段进行实验

![image-20210424155507761](https://gitee.com/hit_whr/pic_2.0/raw/master/20210424155507.png)





# 常用函数

最好的查询网站

https://www.w3schools.com/mysql/func_mysql_dayofweek.asp

## 数学运算

1. abs()
2. ceiling()
3. floor()
4. rand()

## 字符串运算

1. char_length 返回显示出来的字符个数
2. length返回占用的字节数，utf-8下，中文为3字节
3. insert(target,start pos,char_num,new_string)   start_pos是开始计数的位置，从1开始，char_num，是有几个字符被替换，被替换为new_string。     显然，如果改为char_num=0，就是直接插入了
4. left（string，num）从左侧开始截取num个字符
5. right（string，num）从右侧开始截取
6. trim，只能去除左右两端的空格
7. replace（target，‘被替换的字符/字符串’，‘替换者；）
8. substring（target，起始位置-可以为负数，截取的长度）
9. reverse(target)逆序字符串

![image-20210424155747601](https://gitee.com/hit_whr/pic_2.0/raw/master/20210424155747.png)









![image-20210424160018041](https://gitee.com/hit_whr/pic_2.0/raw/master/20210424160018.png)

关于soundex，工作流程是，基于单词的发音来给字段的值进行一次映射，那么当发音大概匹配时，就能够返回结果，完成了基于发音的模糊匹配。

==关键是发音类似==



![image-20210424160146628](https://gitee.com/hit_whr/pic_2.0/raw/master/20210424160146.png)







## 日期时间函数

1. current_date()返回当前的日期

   ![image-20210424160347564](https://gitee.com/hit_whr/pic_2.0/raw/master/20210424160347.png)

2. current_time()返回当前的时间

   ![image-20210424160419536](https://gitee.com/hit_whr/pic_2.0/raw/master/20210424160419.png)

3. adddate（date/current_date(),interval year,month,day)

   ![image-20210424160737612](https://gitee.com/hit_whr/pic_2.0/raw/master/20210424160737.png)

4. addtime(time/current_time(),’hour:minute:second’)

   ![image-20210424161140005](https://gitee.com/hit_whr/pic_2.0/raw/master/20210424161140.png)

   

   

5. current_timestamp()返回相当于date和time的集合版

   更简洁的版本是now

   ![image-20210424161441871](https://gitee.com/hit_whr/pic_2.0/raw/master/20210424161441.png)

   ![](https://gitee.com/hit_whr/pic_2.0/raw/master/20210424161927.png)

6. date返回date和time的date部分

   ![image-20210424161532808](https://gitee.com/hit_whr/pic_2.0/raw/master/20210424161532.png)

7. time返回time部分

   ![image-20210424161626523](https://gitee.com/hit_whr/pic_2.0/raw/master/20210424161626.png)

8. 类似上面的还有year，month，day，hour，minute，second

   ![image-20210424161759068](https://gitee.com/hit_whr/pic_2.0/raw/master/20210424161759.png)

9. 计算两个日期的差datediff（）

10. 最后看看星期几dayofweek（date，timestamp）

    ![image-20210424162230316](https://gitee.com/hit_whr/pic_2.0/raw/master/20210424162230.png)

    为啥是7，今天明明星期6啊？

    官网这样解释的

    > The DAYOFWEEK() function returns the weekday index for a given date (a number from 1 to 7).
    >
    > **Note:** 1=Sunday, 2=Monday, 3=Tuesday, 4=Wednesday, 5=Thursday, 6=Friday, 7=Saturday.
    >
    > 从周日开始计算index值

11. user()当前用户名

最后补充一下，在忘数据库里面插入的时候，最好保证数据的格式是类似yyyy-mm-dd形式的，便于后续处理。

同时，即使我们知道存储的是date类型，为了程序的可移植性，建议将字段转换为date(字段)，防止后来修改为datetime类型

![image-20210424163739279](https://gitee.com/hit_whr/pic_2.0/raw/master/20210424163739.png)



![image-20210424163915849](https://gitee.com/hit_whr/pic_2.0/raw/master/20210424163915.png)



现在查询九月份的所有数据

- 可以用between and

  ![image-20210424164031323](https://gitee.com/hit_whr/pic_2.0/raw/master/20210424164031.png)

- 正则

  ![image-20210424164135729](https://gitee.com/hit_whr/pic_2.0/raw/master/20210424164135.png)

- lke

  ![image-20210424164301953](https://gitee.com/hit_whr/pic_2.0/raw/master/20210424164302.png)

- 年份为2005月份为9

  ![image-20210424164415971](https://gitee.com/hit_whr/pic_2.0/raw/master/20210424164416.png)





## 聚合函数

当app想要的是一组数据经过处理之后的结果时，返回所有的值并交给app处理是不合适的，并且让sql显示出来也很不合适，所以我们只得到结果即可。



1. count
   1. count(字段名)  返回该字段的行数，忽略null
   2. count(*) ，count(1) 返回字段的行数，不忽略null
2. sum（字段），此时执行简单的求和操作。也可以是sum(字段的运算组合)

![image-20210424183731208](https://gitee.com/hit_whr/pic_2.0/raw/master/20210424183731.png)

![image-20210424183747197](https://gitee.com/hit_whr/pic_2.0/raw/master/20210424183747.png)



1. avg（），min（），max（）。这些函数都涉及一整列的数据。忽略null

假设数据结构是这样的

| studentno | subjectno | result |
| --------- | --------- | ------ |
| 1         | 1         | 99     |
| 2         | 1         | 55     |
| 3         | 2         | 66     |
| 4         | 2         | 33     |

如果直接`select avg(result) from result` 返回的是∑result /4

如果``select subjectno,avg(result) from result`` 则会直接报错，因为avg是一行的数据，subjectno是四行的数据，二者不匹配。

应该改为对响应的subjectno求avg，即gruop by分组，限定result的范围

```sql
SELECT sub.subjectname,AVG(studentresult),MIN(studentresult),MAX(studentresult)
FROM result AS r
INNER JOIN `subject` AS sub
ON sub.subjectno = r.subjectno
GROUP BY r.subjectno
```

![image-20210219123026560](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210219123026560.png)

如果要对分组后生成的字段avg再次进行筛选，就不能在group by后面添加where了，因为不符合顺序

也不能在group by前面加，因为那时候还没有分组，没有建立新的字段

要用到一个新的关键字having

```sql
SELECT sub.subjectname,AVG(studentresult),MIN(studentresult),MAX(studentresult)
FROM result AS r
INNER JOIN `subject` AS sub
ON sub.subjectno = r.subjectno
GROUP BY r.subjectno
HAVING AVG(studentresult)>70
```

![image-20210219123215261](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210219123215261.png)



# 分组

group by

![image-20210424184641083](https://gitee.com/hit_whr/pic_2.0/raw/master/20210424184641.png)

现在的数据需求是知道每个生产商各生产了多少种产品，也就是将行按照vend_id分组后，对组内的行进行计数

![image-20210424184908856](https://gitee.com/hit_whr/pic_2.0/raw/master/20210424184908.png)



- group by 允许后面跟多个字段，比如group by(字段1，字段2)也就是对数据先按照字段1进行分组，在此基础上对字段2进行分组。比如先按照院系分组，然后按照班级分组

![image-20210424185251201](https://gitee.com/hit_whr/pic_2.0/raw/master/20210424185251.png)



现在有个问题，select子句的顺序为from，where，group by，order by，limit

那么，如果要对group by之后的分组进行过滤应该如何解决？

==where是对行进行过滤，而having是基于聚合函数对分组进行过滤==

比如，要找出产品种类超过两种的订单，给出订单号和产品种类数

![image-20210424185807637](https://gitee.com/hit_whr/pic_2.0/raw/master/20210424185807.png)



![image-20210424190050776](https://gitee.com/hit_whr/pic_2.0/raw/master/20210424190050.png)



再要求：能够生产两种产品及其以上，并且产品价格都在10以上的生产者

![image-20210424190501803](https://gitee.com/hit_whr/pic_2.0/raw/master/20210424190501.png)



![image-20210424190732591](https://gitee.com/hit_whr/pic_2.0/raw/master/20210424190732.png)

先过滤价格，然后按照生产者进行分组，最后选出分组中count>=2的结果



# 子查询

## 利用子查询进行过滤

需求是where的条件太直接了，where的过滤条件是可以直接给出的，但是如果我只知道间接条件呢？也就是说，直接的过滤条件还需要经过查询才能知道。

可以看出来，上面经过了两次查询，所以叫做子查询。

需求：列出订购TNT2的所有客户的信息

先看看订单表（这些表不是自己建的，如果是自己建的，根据关系模型，很容易确定需要的数据在哪儿和关系）

先找TNT2-》order_num->cust_id->

![image-20210424192251864](https://gitee.com/hit_whr/pic_2.0/raw/master/20210424192251.png)



![image-20210424192330820](https://gitee.com/hit_whr/pic_2.0/raw/master/20210424192330.png)



<img src="https://gitee.com/hit_whr/pic_2.0/raw/master/20210424192407.png" alt="image-20210424192407734" style="zoom:67%;" />



![image-20210424192644798](https://gitee.com/hit_whr/pic_2.0/raw/master/20210424192644.png)

不能用等号，因为子查询的结果可能不为一行，应该是在一个序列里面

用in

![image-20210424192753899](https://gitee.com/hit_whr/pic_2.0/raw/master/20210424192753.png)



加上缩进，看起来更加清晰

```sql
SELECT *FROM customers
WHERE cust_id IN 
	(
		SELECT cust_id FROM orders
		WHERE order_num IN
		(
			SELECT order_num FROM orderitems
			WHERE prod_id='TNT2'
		)
	)
```



需求：显示每个客户订单总数

orders

![image-20210424200230140](https://gitee.com/hit_whr/pic_2.0/raw/master/20210424200230.png)

从customers中得到cust的信息，根据cust_id对orders分组，计数

![image-20210424200518797](https://gitee.com/hit_whr/pic_2.0/raw/master/20210424200518.png)

报错，因为子查询返回的是所有cust_id计数的结果，是多行，我们需要当前cust_id的计数值

![image-20210424200834152](https://gitee.com/hit_whr/pic_2.0/raw/master/20210424200834.png)



这里突然发现，分组是没有意义的，因为当有了where进行过滤后，虽然结果是多行，但是我们进行了count，还是一行。

所以最终是

![image-20210424200947565](https://gitee.com/hit_whr/pic_2.0/raw/master/20210424200947.png)



并且，这里使用的完全限定的名称，为什么呢？因为在过滤的时候，当前的cust_id来自customers表，而要进行比较的来自orders表，为了避免二义性，需要指出分别来自哪个表。







需求：显示每个客户订单中的产品总数

customers表->cust_id->order_num->order_item求和

要知道客户信息，需要知道cust_id

![image-20210424194249529](https://gitee.com/hit_whr/pic_2.0/raw/master/20210424194249.png)

在orders里面，有cust_id到order_num的映射

![image-20210424194451025](https://gitee.com/hit_whr/pic_2.0/raw/master/20210424194451.png)

在orderitems里面，可以根据order_num进行计数

<img src="https://gitee.com/hit_whr/pic_2.0/raw/master/20210424194508.png" alt="image-20210424194508264" style="zoom: 67%;" />





![image-20210424202218181](https://gitee.com/hit_whr/pic_2.0/raw/master/20210424202218.png)

这个查询其实已经比较复杂了，正确的方法应该是采用渐进的方法逐渐调试，把中间结果都弄准确然后再合并起来。当然，对于中间的一些结果，我们最好不要全都写进去，只要部分结果符合我们的预期即可。然后再将具体的中间结果以子查询代替



# 联结（join）

先得了解主键和外键

假设有两张表vendor(生产商)和products（产品）一个产品需要存储名称、产品描述、生产厂家。对于产品而言，名称是主键，厂家是外键，外键可以联系到vendor表。

但是，如果所需的数据来自多张表呢？

那么就需要使用联结，

## 参照完整性

如果products表中某个厂家的id在vendor中找不到再怎么办？

通过制定外键和主键来实现

## 实例

联结的过程是，从vendors，products各找一行，过滤条件是两行的vend_id相等

![image-20210425092053217](https://gitee.com/hit_whr/pic_2.0/raw/master/20210425092053.png)

如果没有过滤条件，设vendors里面有m行，products里面有n行，则最终的结果是mxn的笛卡尔积

![image-20210425092416108](https://gitee.com/hit_whr/pic_2.0/raw/master/20210425092416.png)



## 内部联结

inner join

![image-20210425095302933](https://gitee.com/hit_whr/pic_2.0/raw/master/20210425095303.png)



inner join是个啥意思呢？

就是说，如果用了table inner join table on 条件

那么只在符合这个结果（也就是取得交集的时候）时，才进行显示

![image-20210425094042747](https://gitee.com/hit_whr/pic_2.0/raw/master/20210425094042.png)



left join则是，可以符合这个结果（取得交集）也可以直接在left join左边那个表也就是第一个表中找，当然，这个时候，由于过滤条件不符合，右边的表肯定是返回不了行的，所以与右边行相关的字段都是null

![image-20210425094220843](https://gitee.com/hit_whr/pic_2.0/raw/master/20210425094220.png)

![image-20210425094921453](https://gitee.com/hit_whr/pic_2.0/raw/master/20210425094921.png)



![image-20210425094933908](https://gitee.com/hit_whr/pic_2.0/raw/master/20210425094934.png)



![image-20210425095118364](https://gitee.com/hit_whr/pic_2.0/raw/master/20210425095118.png)

公共部分只有1001,1002,1003,1005

而左边，也就是vendors表在vend_id字段所特有的值，也会被放进去，由于所要select的其他字段没有这样的行，所有都是null

而上面的inner join则不会出现这些情况

类似的right join，full join则是，将二者匹配的部分拿进来，同时不匹配的部分也都拿进来

## 多表查询

获得prod_name,vend_name,prod_price,quantity,sum

products.prod_name,products.prod_price   vend_id

vendors.vend_id,vendors.vend_name

orderitems.prod_id,orderitems.quantity,orderitems.item_price

![image-20210425101734342](https://gitee.com/hit_whr/pic_2.0/raw/master/20210425101734.png)



## 与子查询的比较

联结的好处在于可以显示的列可以来自不同的表，而子查询的本质是表的逐个查询，所以最外层不能显示来自不同表的列。

当然，子查询的思路看起来更加清晰。

![image-20210425102822740](https://gitee.com/hit_whr/pic_2.0/raw/master/20210425102822.png)



![image-20210425102838578](https://gitee.com/hit_whr/pic_2.0/raw/master/20210425102838.png)



## 高级联结

### 表别名

表别名和字段别名、计算字段别名，差不多，但是表的别名不返回给app

表别名在from中声明，可以在from前（select）或from后（where 等）中使用

这样写起来十分简洁，而且不容易出错

![image-20210425103454402](https://gitee.com/hit_whr/pic_2.0/raw/master/20210425103454.png)



### 自联结

自联结要求多次使用同一张表，具体过程是：先对这张表进行一次过滤，得到一张表p1，然后以p1中的行为基准，对p2再进行筛选。

找到生产id为DTNTR的厂家所生产的所有产品

- 使用子查询

![image-20210425104215209](https://gitee.com/hit_whr/pic_2.0/raw/master/20210425104215.png)



- 使用自联结

  ![image-20210425104656998](https://gitee.com/hit_whr/pic_2.0/raw/master/20210425104657.png)

  先对p2的prod_id进行筛选，得到一个新表，然后将这表和原来的表，比照，得到想要的字段

效率比较

子查询

![image-20210425105019534](https://gitee.com/hit_whr/pic_2.0/raw/master/20210425105019.png)

自联结

![image-20210425104946349](https://gitee.com/hit_whr/pic_2.0/raw/master/20210425104946.png)

![image-20210425105029980](https://gitee.com/hit_whr/pic_2.0/raw/master/20210425105030.png)







### 外部联结

现在来看一组对比

用法有left outer join,right outer join



### 带聚集函数的联结

得到每个客户所下的订单数(在orders表中，cust_id出现几次，就下了几次订单)

![image-20210425150710526](https://gitee.com/hit_whr/pic_2.0/raw/master/20210425150710.png)



如果想知道所有用户（包括没下单的），要用left join

![image-20210425150753982](https://gitee.com/hit_whr/pic_2.0/raw/master/20210425150754.png)







# 加密（数据库）

传递密码123456

写入数据库insert into table(`pwd`) values (MD5('123456'))

校验，用户传递的密码user_pwd

select * from table where pwd=MD5(user_pwd) and user_name = name

# 最后：DQL中关键字的顺序

```sql
SELECT [ALL | DISTINCT]
{* | table.* | [table.field1[as alias1][,table.field2[as alias2]][,...]]}
FROM table_name [as table_alias]
  [left | right | inner join table_name2]  -- 联合查询
  [WHERE ...]  -- 指定结果需满足的条件
  [GROUP BY ...]  -- 指定结果按照哪几个字段来分组
  [HAVING]  -- 过滤分组的记录必须满足的次要条件
  [ORDER BY ...]  -- 指定查询记录按一个或多个条件排序
  [LIMIT {[offset,]row_count | row_countOFFSET offset}];
   -- 指定查询的记录从哪条至哪条
```

```sql
select distinct去重 要找的字段名 as 别名
from 字段来自的表
xxxx join 一张表不够，需要将表连接起来
on 等值条件
where 第一次过滤
group by 分组
having 对分组后的结果进行第二次过滤
order by 根据什么字段来排序，排序方式[asc/desc]
limit start_index,pagesize
```







SELECT CONCAT('姓名:',studentname) AS 新姓名 FROM student;

字段名重命名为新姓名（as），每个数据项显示为concat

查询为空的记录：1.data='' OR data is null

sqlyog两个','很难分辨出来啊





# 事务

## 事务的原则：一组sql要么都执行成功，要么都执行失败

## 事务的定义

- 事务就是将一组SQL语句放在同一批次内去执行
- 如果一个SQL语句出错,则该批次内的所有SQL都将被取消执行
- MySQL事务处理只支持InnoDB和BDB数据表类型

## 事务的特性：ACID

1. 原子性。要么都成功，要么都失败
2. 一致性。事务完成前后，数据的完整性保持一致
3. 隔离性。多个用户并发访问数据库时，开启多个事务，事务之间相互隔离。
4. 持久性。事务提交后被持久化到数据库中



## 由隔离性引发的问题

1. 脏读。一个事务读取了另一个事务未提交的数据。也就是一个事务读取到了另一个事务在执行时的中间状态

![7](https://images.cnblogs.com/cnblogs_com/CareySon/201201/201201291407156692.png)

2. 不可重复读。在一个事务内读取表中的某一行数据，不同时候读取的结果不同。

![9](https://images.cnblogs.com/cnblogs_com/CareySon/201201/20120129140717793.png)

3. 幻读。幻读,是指当事务不是独立执行时发生的一种现象，例如第一个事务对一个表中的数据进行了修改，这种修改涉及到表中的全部数据行。同时，第二个事务也修改这个表中的数据，这种修改是向表中插入一行新数据。那么，以后就会发生操作第一个事务的用户发现表中还有没有修改的数据行，就好象发生了幻觉一样.

![13](https://images.cnblogs.com/cnblogs_com/CareySon/201201/201201291407193533.png)

<img src="https://images.cnblogs.com/cnblogs_com/CareySon/201201/20120129140720600.png" alt="12" style="zoom:150%;" />



## mysql默认开启事务

```sql
-- mysql中默认开启自动提交
set autocommit = 1

-- 关闭mysql的自动提交
set autocommit = 0

--开启一个事务
start transaction
--执行一组sql
xxx
--如果全都执行成功，提交数据（持久化）
commit
--没有全都执行成功，进行回滚
rollback

--恢复到自动提交
set autocommit = 1
```

```sql
SET autocommit = 0 --关闭自动提交
START TRANSACTION  --开始一个事务

UPDATE test SET money=money-500 WHERE `name`='a'
UPDATE test SET money=money+500 WHERE `name`='b'
SELECT * FROM test

COMMIT  --如果都执行成功，提交，持久化
ROLLBACK  --如果不都执行成功，回滚

SET autocommit=1  --开启自动提交
```

# 索引

## 索引的定义

## 索引的分类

1. 主键索引。primary key（字段名），主键索引是唯一的，值也是唯一的
2. 唯一索引。unique key 索引名（字段名）。字段名是把哪一列作为索引，一般索引名和字段名设置相同。
3. 常规索引。key 索引名（字段名）
4. 全文索引。fulltext index 索引名（字段名）

## 操作

```sql
--查看表格索引信息
show index from table_name
```

![image-20210219173145624](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210219173145624.png)

cardinality非空--主键索引

```sql
--增加索引/修改表
ALTER TABLE student ADD KEY `studentname`(`studentname`)
ALTER TABLE student ADD FULLTEXT KEY `studentname`(`studentname`)

--分析sql的执行情况
EXPLAIN SELECT * FROM student
```

查询的记录数（rows）进而影响性能

![image-20210219174159980](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210219174159980.png)



## 实测

创建一张表，一开始只有id为主键，主键自动创建索引

```sql
CREATE TABLE `app_user` (
`id` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
`name` VARCHAR(50) DEFAULT'' COMMENT'用户昵称',
`email` VARCHAR(50) NOT NULL COMMENT'用户邮箱',
`phone` VARCHAR(20) DEFAULT'' COMMENT'手机号',
`gender` TINYINT(4) UNSIGNED DEFAULT '0'COMMENT '性别（0：男;1:女）',
`password` VARCHAR(100) NOT NULL COMMENT '密码',
`age` TINYINT(4) DEFAULT'0'  COMMENT '年龄',
`create_time` DATETIME DEFAULT CURRENT_TIMESTAMP,
`update_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (`id`)
) ENGINE=INNODB DEFAULT CHARSET=utf8 COMMENT = 'app用户表'
```

写入数据

```sql
SET GLOBAL log_bin_trust_function_creators=1; -- 开启创建函数功能
/*
  第一个语句 delimiter 将 mysql 解释器命令行的结束符由”;” 改成了”$$”，
  让存储过程内的命令遇到”;” 不执行
*/
DELIMITER $$
CREATE FUNCTION mock__data()
RETURNS INT
BEGIN
	DECLARE num INT DEFAULT 1000000;
	DECLARE i INT DEFAULT 0;
	WHILE i<num DO
		INSERT INTO `app_user`(`name`,`email`,`phone`,`gender`,`password`)VALUES(CONCAT('用户',i),'19224305@qq.com','123456789',FLOOR(RAND()*2),'123456');
		SET i=i+1;
	END WHILE;
	RETURN i;
END;$$

SELECT mock__data()$$ -- 执行此函数 生成一百万条数据
```

### 索引的作用：作为where的条件，利用b+tree提高查询性能

说白了，利用等值查询时，如果为where后面的等值条件（字段）创建了索引，就不用了挨个遍历，前提是为查找的这个字段创建了索引



测试等值条件

```sql
EXPLAIN SELECT * FROM app_user WHERE `name` = '用户10000'   --994560，并没有为name创建索引
EXPLAIN SELECT * FROM app_user WHERE `id` = '10000'  --1  id这个字段是有索引的
SELECT * FROM app_user WHERE `name` = '用户10000'
SELECT * FROM app_user WHERE `id` = '10000'  
```

![image-20210220110857160](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210220110857160.png)

![image-20210220111259069](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210220111259069.png)

![image-20210220110947943](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210220110947943.png)

![image-20210220111320766](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210220111320766.png)

测试不等值条件

```sql
EXPLAIN SELECT * FROM app_user WHERE `id`>=10000 AND `id`<20000
EXPLAIN SELECT *FROM app_user WHERE `id` LIKE ('1____')
SELECT * FROM app_user WHERE `id`>=10000 AND `id`<20000
SELECT *FROM app_user WHERE `id` LIKE ('1____')
```

![image-20210220111540189](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210220111540189.png)

![image-20210220111600811](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210220111600811.png)

![image-20210220111618165](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210220111618165.png)

![image-20210220111631839](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210220111631839.png)

接下来为name创建索引，来看看效果

`alter table table_name add index index_name(一般是id_name)(字段名)`

```sql
ALTER TABLE app_user ADD INDEX id_name(`name`)
```

![image-20210220111835349](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210220111835349.png)

创建索引是一个非常耗时的事情，而且在添加数据时，又要对索引表进行操作，所以慎重创建索引，最好是查询操作大于增加和删除操作。

```sql
EXPLAIN SELECT * FROM app_user WHERE `name`='用户10000'
SELECT * FROM app_user WHERE `name`='用户10000'
```

之前是994560，现在是1；之前是0.583，现在是0.002

![image-20210220112208580](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210220112208580.png)

![image-20210220112154213](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210220112154213.png)

在对where字段创建索引后，效率明显提升，但创建索引也比较耗时。

```SQL
INSERT INTO `app_user`(`name`,`email`,`phone`,`gender`,`password`)VALUES(CONCAT('用户',1000001),'19224305@qq.com','123456789',FLOOR(RAND()*2),'123456');

```

![image-20210220112449812](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210220112449812.png)

插入操作由0.001秒级响应转到0.01秒级响应

## 建立索引的原则

1. 索引不是越多越好，只有在大数据量，查询显著变慢的时候才加索引
2. 不要对经常进行修改的数据加索引
3. 索引一般加在经常where的字段上

运维级别的mysql，偏向底层

业务级别的mysql，偏向操作

localhost ip：127.0.0.1

对用户进行增删或者密码修改后，或者skip grant tables后，都要记得flush privileges

# 权限管理

一个ip或host上对应一个数据库；一个host上的DBMS是多用户软件，分配了权限，共享上面所有的数据库/文件（权限）；只有一个root用户，但可以在当前ip下创建其他的用户，并进行权限管理。

## 操作

***每次操作结束后，记得flush privileges，否则后面总有莫名其妙的报错***

创建用户（没有任何privileges，包括查看权限）

```sql
create user user_name identified by 'pwd'
```

重命名用户

```sql
rename user old_name to new_name
--如果是root，需要加上@ip_addr
```

删除用户

```sql
drop user user_name
```

设置密码

```sql
set password [for user_name]=password('')
```

权限查看

```sql
SHOW GRANTS FOR root@localhost
GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' WITH GRANT OPTION
```

赋予权限

```sql
GRANT 权限列表 ON 表名 TO 用户名 [IDENTIFIED BY [PASSWORD] 'password']
  - all privileges 表示所有权限
  - *.* 表示所有库的所有表
  - 库名.表名 表示某库下面的某表
  - 如果没有这个用户，则进行用户创建
GRANT ALL PRIVILEGES ON myschool.* TO 'astudent'@'localhost' IDENTIFIED BY '1111'
```

权限中最后的with/without grant option 是区分root和非root的一个重要权限

撤销权限

```sql
-- 撤消权限
REVOKE 权限列表 ON 表名 FROM 用户名
REVOKE ALL PRIVILEGES, GRANT OPTION FROM 用户名    -- 撤销所有权限
```



# 数据库备份

## 物理拷贝

直接对data文件进行拷贝

## sqlyog可视化操作

可以选择整个数据库，或者数据库中的某张表；

可以导出数据（insert）/结构（字段及其属性）

## 命令行下操作

mysqldump -h主机名 -u用户名 -p 密码 数据库 表 >path

windows下，导出到c盘可能出错

```sql
1. 导出一张表 -- mysqldump -uroot -p123456 school student >D:/a.sql
　　mysqldump -u用户名 -p密码 库名 表名 > 文件名(D:/a.sql)
2. 导出多张表 -- mysqldump -uroot -p123456 school student result >D:/a.sql
　　mysqldump -u用户名 -p密码 库名 表1 表2 表3 > 文件名(D:/a.sql)
3. 导出所有表 -- mysqldump -uroot -p123456 school >D:/a.sql
　　mysqldump -u用户名 -p密码 库名 > 文件名(D:/a.sql)
4. 导出一个库 -- mysqldump -uroot -p123456 -B school >D:/a.sql
　　mysqldump -u用户名 -p密码 -B 库名 > 文件名(D:/a.sql)
```

导入：

```sql
source path
1. 在登录mysql的情况下：-- source D:/a.sql
　　source 备份文件
2. 在不登录的情况下
　　mysql -u用户名 -p密码 库名 < 备份文件
```



# insert

## 不指定字段

这种情况下，所有字段必须按照顺序进行赋值，即使有默认值也需要

![image-20210422150751855](https://gitee.com/hit_whr/pic_2.0/raw/master/20210422150751.png)

不指定有默认值的，直接报错

![image-20210422151048073](https://gitee.com/hit_whr/pic_2.0/raw/master/20210422151048.png)

如果指定null，进去的是咱们的null，所以这种情况default没起到作用



对于主键，我们知道不允许为空，但是可以自增啊？能不能不赋值？不行，如果不赋值，需要用null告诉mysql，用上一个值自增的值之后的结果。如果赋值，那就是该结果，反正不能空着，否则，当主键不是第一个字段，而是中间的字段时，咋区分呢？

![image-20210422150940382](https://gitee.com/hit_whr/pic_2.0/raw/master/20210422150940.png)

这样是不安全的，当表的结构改变，比如新增了一个字段，之前的插入语句需要改写，移植性比较差



## 指定字段

前提是至少需要包括所有的not null字段（否则不行）

![image-20210422151629662](https://gitee.com/hit_whr/pic_2.0/raw/master/20210422151629.png)

这里cust_name不允许为空，我们看看不指定这个字段会怎样

![image-20210422151921253](https://gitee.com/hit_whr/pic_2.0/raw/master/20210422151921.png)

报错，cust_name不允许为空，又没有给值



对于主键，如果咱们不指定这个字段，是没有问题的，因为主键虽然not null，但是会自增，当我们不指定值时，自动生成。not null的字段必须给值

![image-20210422152411200](https://gitee.com/hit_whr/pic_2.0/raw/master/20210422152411.png)

并且，对于cust_email。由于我们没有指定一个值，mysql会使用默认值，而不是像之前一样被null覆盖



总结一下，什么时候可以省略字段：

- null yes
- null no。default value

一般而言，对于大型数据库，插入操作比较费时，因为在插入时，需要重建索引，可以降低插入操作的优先级，让查询先去执行。

==insert low_priority into==

## 多记录插入

![image-20210422153313872](https://gitee.com/hit_whr/pic_2.0/raw/master/20210422153313.png)

这里在values后面跟上了（）,（）

使得单条语句可以执行多条语句的插入效果，提高了性能

## 插入检索出的数据

就是先select，将select的结果进行insert

形式是

insert into table_name

(字段1,字段2)

select

字段1,

字段2

from table_name2

需要考虑主键

table2的主键可能和table1中的某条记录的主键值冲突了，这样插入不了

一个好的方法是，不select主键，让主键自己决定应有的值

下面新建一个customer_new表，字段是一样的，然后select除主键外的字段，完成customer到customer_new的复制操作

![image-20210422154355336](https://gitee.com/hit_whr/pic_2.0/raw/master/20210422154355.png)

## 关于null

可以在声明字段时，用上default null

这样在insert或update的时候，可以不指定它的值

![image-20210422163716375](https://gitee.com/hit_whr/pic_2.0/raw/master/20210422163716.png)



![image-20210422163939695](https://gitee.com/hit_whr/pic_2.0/raw/master/20210422163939.png)

第一条insert没有指定test的值，是(NULL)，为啥要用括号括起来呢？防止插入的字符是NULL。

然后第二条insert，基本操作相同，但是test插入的是空字符，所以没有显示（NULL），这也说明NULL！=空字符串

![image-20210422164118880](https://gitee.com/hit_whr/pic_2.0/raw/master/20210422164118.png)











# 更新

update table_name 

set

​	字段1=value1,字段2=value2

where(过滤的条件)

更新的时候必须对条件进行很好的限制，否则会更改不用更改的数据，造成数据错误

在更新的时候，只要有错误，整个update操作被取消，也就是之间执行的更新都不会被保存，这样不是我们想要的。可以在update后面加上ignore，使得错误被忽略，正常的更新结果能够被保存

比如更新一下cc的数据

![image-20210422160441924](https://gitee.com/hit_whr/pic_2.0/raw/master/20210422160441.png)



![image-20210422160531400](https://gitee.com/hit_whr/pic_2.0/raw/master/20210422160531.png)

# 删除

这里的删除指的是记录，删除库和表是drop

delete from table_name

where（过滤条件）

比如，现在的数据是

![image-20210422160221231](https://gitee.com/hit_whr/pic_2.0/raw/master/20210422160221.png)

![image-20210422160409767](https://gitee.com/hit_whr/pic_2.0/raw/master/20210422160409.png)



如果是想删除所有的行，那么可以直接使用（truncate table_name)，实际上是drop，然后create一样的表

![image-20210422160740263](https://gitee.com/hit_whr/pic_2.0/raw/master/20210422160740.png)



# 在修改数据时

修改数据时，需要非常的小心。

在update或者delete前，必须先select，看看我们是不是想修改这些数据，确保过滤条件是正确的

![image-20210422160930383](https://gitee.com/hit_whr/pic_2.0/raw/master/20210422160930.png)



![image-20210422160950145](https://gitee.com/hit_whr/pic_2.0/raw/master/20210422160950.png)



# 关于主键

主键可以是一个字段，这时要求这个字段的值唯一

也可以是字段的组合，要求组合唯一

在声明的时候primary key(字段1，【字段2，字段3】)

主键必须是==not null==

# 关于自增

每个表只允许一个auto_increment列，而且这个列必须被索引（比如成为主键）

当表相互关联时，也就意味着，auto_increment部分要作为外键时，如何确定二者的值？一个方法是select，插入的那一行，但是这似乎有点麻烦，因为还得where过滤，并且结果不一定唯一

可以直接从auto_increment的值入手，last insert_id返回这个表最后一个auto_increment的值

![image-20210422165316369](https://gitee.com/hit_whr/pic_2.0/raw/master/20210422165316.png)



# 引擎

## 多重引擎及其特性

![image-20210422165547879](https://gitee.com/hit_whr/pic_2.0/raw/master/20210422165547.png)



## 引擎可以混用

![image-20210422165612214](https://gitee.com/hit_whr/pic_2.0/raw/master/20210422165612.png)



## 外键不能跨引擎

![image-20210422165720898](https://gitee.com/hit_whr/pic_2.0/raw/master/20210422165720.png)



# 外键



# show

![image-20210423203414415](https://gitee.com/hit_whr/pic_2.0/raw/master/20210423203421.png)



![image-20210423203419308](https://gitee.com/hit_whr/pic_2.0/raw/master/20210423203419.png)

![image-20210423203432826](https://gitee.com/hit_whr/pic_2.0/raw/master/20210423203432.png)





show status查看服务器的状态信息

![image-20210423203526798](https://gitee.com/hit_whr/pic_2.0/raw/master/20210423203526.png)

show erros/warnings查看错误或者警告

![image-20210423203641073](https://gitee.com/hit_whr/pic_2.0/raw/master/20210423203641.png)



查看创建数据库或者表的语句

show create database/table name

![image-20210423203810566](https://gitee.com/hit_whr/pic_2.0/raw/master/20210423203810.png)

![](https://gitee.com/hit_whr/pic_2.0/raw/master/20210423203813.png)



查看用户的权限

show grants[for user_name]

如果没有for，默认显示所有用户的权限

![image-20210423203921643](https://gitee.com/hit_whr/pic_2.0/raw/master/20210423203921.png)

命令行下用help show查看show的命令



# 服务器端数据库

服务器端mysql

教程https://blog.csdn.net/qq_39667424/article/details/105879549



启动与查看运行状态，关闭与查看运行状态

systemctl start/status/stop mysqld.service

```bash
[root@iZm5e98zphj5y525q4v5k4Z yum.repos.d]# systemctl start mysqld.service
[root@iZm5e98zphj5y525q4v5k4Z yum.repos.d]# systemctl status mysqld.service
● mysqld.service - MySQL Server
   Loaded: loaded (/usr/lib/systemd/system/mysqld.service; enabled; vendor preset: disabled)
   Active: active (running) since Thu 2021-04-22 11:59:37 CST; 8s ago
     Docs: man:mysqld(8)
           http://dev.mysql.com/doc/refman/en/using-systemd.html
  Process: 27527 ExecStart=/usr/sbin/mysqld --daemonize --pid-file=/var/run/mysqld/mysqld.pid $MYSQLD_OPTS (code=exited, status=0/SUCCESS)
  Process: 27475 ExecStartPre=/usr/bin/mysqld_pre_systemd (code=exited, status=0/SUCCESS)
 Main PID: 27530 (mysqld)
   CGroup: /system.slice/mysqld.service
           └─27530 /usr/sbin/mysqld --daemonize --pid-file=/var/run/mysqld/mysql...

Apr 22 11:59:33 iZm5e98zphj5y525q4v5k4Z systemd[1]: Starting MySQL Server...
Apr 22 11:59:37 iZm5e98zphj5y525q4v5k4Z systemd[1]: Started MySQL Server.
[root@iZm5e98zphj5y525q4v5k4Z yum.repos.d]# systemctl stop mysqld.service
[root@iZm5e98zphj5y525q4v5k4Z yum.repos.d]# systemctl status mysqld.service
● mysqld.service - MySQL Server
   Loaded: loaded (/usr/lib/systemd/system/mysqld.service; enabled; vendor preset: disabled)
   Active: inactive (dead) since Thu 2021-04-22 12:01:01 CST; 3s ago
     Docs: man:mysqld(8)
           http://dev.mysql.com/doc/refman/en/using-systemd.html
  Process: 27527 ExecStart=/usr/sbin/mysqld --daemonize --pid-file=/var/run/mysqld/mysqld.pid $MYSQLD_OPTS (code=exited, status=0/SUCCESS)
  Process: 27475 ExecStartPre=/usr/bin/mysqld_pre_systemd (code=exited, status=0/SUCCESS)
 Main PID: 27530 (code=exited, status=0/SUCCESS)

Apr 22 11:59:33 iZm5e98zphj5y525q4v5k4Z systemd[1]: Starting MySQL Server...
Apr 22 11:59:37 iZm5e98zphj5y525q4v5k4Z systemd[1]: Started MySQL Server.
Apr 22 12:00:59 iZm5e98zphj5y525q4v5k4Z systemd[1]: Stopping MySQL Server...
Apr 22 12:01:01 iZm5e98zphj5y525q4v5k4Z systemd[1]: Stopped MySQL Server.

```



查看默认密码

grep ”password” /var/log/mysqld.log

```bash
[root@iZm5e98zphj5y525q4v5k4Z yum.repos.d]# grep 'password' /var/log/mysqld.log
2021-04-22T03:59:34.809533Z 1 [Note] A temporary password is generated for root@localhost: So/CiWpa(38a
2021-04-22T04:00:59.888883Z 0 [Note] Shutting down plugin 'validate_password'
2021-04-22T04:01:01.701924Z 0 [Note] Shutting down plugin 'sha256_password'
2021-04-22T04:01:01.701930Z 0 [Note] Shutting down plugin 'mysql_nativepassword'

```

现在进行登录(先开启mysql的服务)

先看看数据库

```bash
mysql> show databases
    -> ;
ERROR 1820 (HY000): You must reset your password using ALTER USER statement before executing this statement.
```

需要先改密码

set global validate_password_policy=0;允许设置简单密码（因为我们是练习，密码不需要太复杂）

`alter user 'root'@'localhost' identified by 'new pwd' `

现在是个全新的DBMS，先来看看有哪些内置的数据库（内部库）show databases同样加载内部库（涉及用户，配置，权限）



```bash
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.00 sec)
| user                      |
+---------------------------+
31 rows in set (0.00 sec)

mysql> show columns from user
    -> ;
+------------------------+-----------------------------------+------+-----+-----------------------+-------+
| Field                  | Type                              | Null | Key | Default               | Extra |
+------------------------+-----------------------------------+------+-----+-----------------------+-------+
| Host                   | char(60)                          | NO   | PRI |                       |       |
| User                   | char(32)                          | NO   | PRI |                       |       |
| Select_priv            | enum('N','Y')                     | NO   |     | N                     |       |
| Insert_priv            | enum('N','Y')                     | NO   |     | N                     |       |
| Update_priv            | enum('N','Y')                     | NO   |     | N                     |       |
| Delete_priv            | enum('N','Y')                     | NO   |     | N                     |       |
| Create_priv            | enum('N','Y')                     | NO   |     | N                     |       |

```

用到了`show databases;usr mysql;show talbes;show columns from user`



在服务器上操作不好玩，现在在win的mysql命令行应用中操作，相当于是将服务器和客户机分开了（之前都是在一台计算机上，用端口来区分cs）

首先得知道mysql在服务器上的端口号

```bash
//查看mysql对应的pid
ps -axu |grep mysql
[root@iZm5e98zphj5y525q4v5k4Z ~]# ps -axu |grep mysql
mysql    28781  0.0  9.7 1155844 183372 ?      Sl   12:23   0:01 /usr/sbin/mysqld --daemonize --pid-file=/var/run/mysqld/mysqld.pid
root     29973  0.0  0.2 135612  4056 pts/0    S+   12:46   0:00 mysql -u root -p
root     30292  0.0  0.0 112708   984 pts/1    R+   12:52   0:00 grep --color=auto mysql

netstat -anp |grep 28781
[root@iZm5e98zphj5y525q4v5k4Z ~]# netstat -anp |grep 28781
tcp6       0      0 :::3306                 :::*                    LISTEN      28781/mysqld        
tcp6       0      0 172.17.22.1:3306        222.175.198.19:2851     ESTABLISHED 28781/mysqld        
tcp6       0      0 127.0.0.1:3306          127.0.0.1:56910         ESTABLISHED 28781/mysqld        
unix  2      [ ACC ]     STREAM     LISTENING     287283   28781/mysqld         /var/lib/mysql/mysql.sock

可以看到是本机的3306端口，额，我先用win（222.175.198.19）连接了，所以显示出来了
知道了端口号后，去win操作
mysql -u root -P 3306 -h 47.105.91.11 -p
进行登录
```

和xshell里面的没有区别

然后用mysql的GUI应用程序来连接远程服务器

用的是mysql administrator，感觉界面不如sqlyog

![image-20210422130005269](https://gitee.com/hit_whr/pic_2.0/raw/master/20210422130005.png)

还是用sqlyog把



# 程序远程连接数据库

如果没有在服务器数据库上进行配置，尽管ip，密码，端口都正确，也连不上。要进行修改。

将root这个user对应的host改为%，即任何密码正确的远程主机都能连上该数据库。

**然后记得service mysqld restart**

```bash
mysql> use mysql;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> select user,host from user
    -> ;
+---------------+-----------+
| user          | host      |
+---------------+-----------+
| root          | %         |
| mysql.session | localhost |
| mysql.sys     | localhost |
+---------------+-----------+
3 rows in set (0.00 sec)

```



# 忘记密码

## 修改配置文件

```bash
[root@iZm5e98zphj5y525q4v5k4Z etc]# cat my.cnf
# For advice on how to change settings please see
# http://dev.mysql.com/doc/refman/5.7/en/server-configuration-defaults.html
[mysql]
protocol=tcp

[mysqld]
#
# Remove leading # and set to the amount of RAM for the most important data
# cache in MySQL. Start at 70% of total RAM for dedicated server, else 10%.
# innodb_buffer_pool_size = 128M
#
# Remove leading # to turn on a very important data integrity option: logging
# changes to the binary log between backups.
# log_bin
#
# Remove leading # to set options mainly useful for reporting servers.
# The server defaults are faster for transactions and fast SELECTs.
# Adjust sizes as needed, experiment to find the optimal values.
# join_buffer_size = 128M
# sort_buffer_size = 2M
# read_rnd_buffer_size = 2M
datadir=/var/lib/mysql
socket=/var/lib/mysql/mysql.sock
# skip-grant-tables
# Disabling symbolic-links is recommended to prevent assorted security risks
symbolic-links=0

log-error=/var/log/mysqld.log
pid-file=/var/run/mysqld/mysqld.pi

```

加上skip-grant-tables，

## 重启mysql服务

`service mysqld restart`



## 修改密码

```bash
bash:mysql

mysql> use mysql;(系统表)
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed

mysql> select user,authentication_string from user;
+---------------+-------------------------------------------+
| user          | authentication_string                     |
+---------------+-------------------------------------------+
| mysql.session | *THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE |
| mysql.sys     | *THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE |
| root          | *53F0F088C8AD802553979B4B9523A40A1607D412 |
+---------------+-------------------------------------------+
3 rows in set (0.00 sec)

mysql> update user set authentication_string=password('123456') where user='root';
Query OK, 1 row affected, 1 warning (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 1

mysql> select user,authentication_string from user;
+---------------+-------------------------------------------+
| user          | authentication_string                     |
+---------------+-------------------------------------------+
| mysql.session | *THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE |
| mysql.sys     | *THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE |
| root          | *6BB4837EB74329105EE4568DDA7DC67ED2CA2AD9 |
+---------------+-------------------------------------------+
3 rows in set (0.00 sec)
```



## 修改配置文件

```bash
[root@iZm5e98zphj5y525q4v5k4Z etc]# vim my.cnf
[root@iZm5e98zphj5y525q4v5k4Z etc]# cat my.cnf
# For advice on how to change settings please see
# http://dev.mysql.com/doc/refman/5.7/en/server-configuration-defaults.html
[mysql]
protocol=tcp

[mysqld]
#
# Remove leading # and set to the amount of RAM for the most important data
# cache in MySQL. Start at 70% of total RAM for dedicated server, else 10%.
# innodb_buffer_pool_size = 128M
#
# Remove leading # to turn on a very important data integrity option: logging
# changes to the binary log between backups.
# log_bin
#
# Remove leading # to set options mainly useful for reporting servers.
# The server defaults are faster for transactions and fast SELECTs.
# Adjust sizes as needed, experiment to find the optimal values.
# join_buffer_size = 128M
# sort_buffer_size = 2M
# read_rnd_buffer_size = 2M
datadir=/var/lib/mysql
socket=/var/lib/mysql/mysql.sock
# skip-grant-tables
# Disabling symbolic-links is recommended to prevent assorted security risks
symbolic-links=0

log-error=/var/log/mysqld.log
pid-file=/var/run/mysqld/mysqld.pid
```



## 重启mysql服务

```bash
[root@iZm5e98zphj5y525q4v5k4Z etc]# service mysqld restart
Redirecting to /bin/systemctl restart mysqld.service
```



## 完成

```bash
[root@iZm5e98zphj5y525q4v5k4Z etc]# mysql -uroot -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 2
Server version: 5.7.34 MySQL Community Server (GPL)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> 
```



# 备份与恢复

## 备份

```bash
mysqldump -uroot -p123456 database_name > filename.sql
```



## 恢复

```bash
mysql> create database stu_info_manage;
Query OK, 1 row affected (0.00 sec)
mysql> use stu_info_manage;
Database changed
mysql> source C:\Users\user\Desktop\数据库课设\src\back_up\2021-07-23-08-37-18-stu_info_manage.backup.sql
Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected, 1 warning (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.03 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 3 rows affected (0.00 sec)
Records: 3  Duplicates: 0  Warnings: 0

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.02 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 3 rows affected (0.00 sec)
Records: 3  Duplicates: 0  Warnings: 0

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.02 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.01 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.01 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.02 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 1 row affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.03 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 4 rows affected (0.00 sec)
Records: 4  Duplicates: 0  Warnings: 0

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.03 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 5 rows affected (0.00 sec)
Records: 5  Duplicates: 0  Warnings: 0

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.02 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 5 rows affected (0.00 sec)
Records: 5  Duplicates: 0  Warnings: 0

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.02 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 2 rows affected (0.00 sec)
Records: 2  Duplicates: 0  Warnings: 0

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.02 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 6 rows affected (0.00 sec)
Records: 6  Duplicates: 0  Warnings: 0

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.01 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected, 1 warning (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

mysql>
```

![image-20210723150314841](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210723150314841.png)

服务器上也一样

```bash
mysql> create database stu_info_manage;
Query OK, 1 row affected (0.00 sec)

mysql> use stu_info_manage ;
Database changed
mysql> source /root/2021-07-23-10-01-05-stu_info_manage.backup.sql 
Query OK, 0 rows affected (0.00 sec)
mysql> show tables;
+---------------------------+
| Tables_in_stu_info_manage |
+---------------------------+
| course                    |
| dept                      |
| evaluation                |
| exam_class_total          |
| exkur_class_total         |
| management                |
| select_course             |
| student                   |
| teach_course              |
| teacher                   |
| user_login                |
+---------------------------+
11 rows in set (0.00 sec)
```

