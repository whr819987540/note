# 代码框

````mysql
```mysql 

```
````







# 卸载mysql



## 安装路径

```mysql
which mysql
```

## 配置文件路径

```mysql
/usr/bin/mysql --verbose --help | grep -A 1 'Default options'
```



## 

```bash
dpkg --list|grep mysql
sudo apt remove mysql-common
sudo apt autoremove --purge mysql-server
dpkg -l|grep ^rc|awk '{print$2}'|sudo xargs dpkg -P
dpkg --list|grep mysql
sudo apt autoremove --purge mysql-apt-config

apt-get autoremove --purge mysql-server-{version}
apt-get remove mysql-common
dpkg -l |grep ^rc|awk ‘{print $2}’ |sudo xargs dpkg -P
```



# 安装

```mysql
apt-get update
apt-get install mysql-server-8.0

# no password needed
mysql -uroot
use mysql;
alter user 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '12';
```





# docker 运行mysql





- 首先拉取相应的镜像，并运行容器

```bash
docker run --name learn_mysql -p 3310:3306 -e MYSQL\_ROOT\_PASSWORD=123456 -d mysql:5.7.37-debian
docker exec -it 01cca6c6df4ca20584f06d905a522cacf4f5fba40fdea7bcc6e244fd26f713f2 /bin/bash

# 这里的端口映射可以随意使用
# 这样只会启动容器，但是容器外还是无法连接到数据库，除非进入到容器中操作，但这样太麻烦
# 可以在容器外下载一个mysql-client
# 这样在容器外就可以访问到了
```

- 容器外下载mysql-client并安装

[Ubuntu20.04中安装MySQL 5.7.x - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/348317883)

- 测试连接
  - 先在容器中创建一个数据库
  - 然后再容器外用mysql连接并查看

```mysql
```



# 系统变量

## autocommit自动提交

查看是否开启了自动提交，如果要测试事务，需要关闭自动提交

```mysql 
show variables like "autocommit";
```



## datadir查看mysql的存储路径

```mysql 
show variables like "datadir";
```

- .frm文件中定义了表的结构

![image-20220218182758823](https://raw.githubusercontent.com/whr819987540/pic/main/image-20220218182758823.png)



![image-20220218182805569](https://raw.githubusercontent.com/whr819987540/pic/main/image-20220218182805569.png)



## 



# 表信息

## 表的信息

```mysql 
mysql> show table status like "employees" \G; # \G让显示更加美观
*************************** 1. row ***************************
           Name: employees
         Engine: InnoDB
        Version: 10
     Row_format: Dynamic # 有三种
     # dynamic，行的长度是变化的，适用于有可变字段，如varchar
     # fixed，没有可变字段
     # compressed，压缩字段，只能读不能写
           Rows: 299246.
 Avg_row_length: 50 # 字节为单位
    Data_length: 15220736 # 字节为单位
Max_data_length: 0
   Index_length: 0
      Data_free: 4194304
 Auto_increment: NULL
    Create_time: 2022-02-18 18:17:31 # 表的创建时间
    Update_time: 2022-02-18 18:17:33 # 表的更新时间
     Check_time: NULL
      Collation: utf8_general_ci
       Checksum: NULL
 Create_options:
        Comment:
1 row in set (0.00 sec)

ERROR:
No query specified
```



# 复制表

## 复制表的结构

### 首先查看原表的结构

```mysql
mysql> desc employees;
+------------+---------------+------+-----+---------+-------+
| Field      | Type          | Null | Key | Default | Extra |
+------------+---------------+------+-----+---------+-------+
| emp_no     | int(11)       | NO   | PRI | NULL    |       |
| birth_date | date          | NO   |     | NULL    |       |
| first_name | varchar(14)   | NO   |     | NULL    |       |
| last_name  | varchar(16)   | NO   |     | NULL    |       |
| gender     | enum('M','F') | NO   |     | NULL    |       |
| hire_date  | date          | NO   |     | NULL    |       |
+------------+---------------+------+-----+---------+-------+
```

也可以这样，优点是可以看到建表语句，方便修改，缺点是可能不那么清晰。

```mysql
mysql> show create table employees;
| employees | CREATE TABLE `employees` (
  `emp_no` int(11) NOT NULL,
  `birth_date` date NOT NULL,
  `first_name` varchar(14) NOT NULL,
  `last_name` varchar(16) NOT NULL,
  `gender` enum('M','F') NOT NULL,
  `hire_date` date NOT NULL,
  PRIMARY KEY (`emp_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 |
1 row in set (0.00 sec)
```



## 复制表的结构

```mysql
mysql> create table employees_copy like employees;
Query OK, 0 rows affected (0.04 sec)

mysql> select * from employees_copy;
Empty set (0.00 sec)
```

可以看到只是复制了表的结构，而没有复制表的数据部分。



## 复制表的数据

```mysql
mysql> insert into employees_copy select * from employees;
Query OK, 300024 rows affected (1.45 sec)
Records: 300024  Duplicates: 0  Warnings: 0

mysql> show table status like "employees_copy" \G;
*************************** 1. row ***************************
           Name: employees_copy
         Engine: InnoDB
        Version: 10
     Row_format: Dynamic
           Rows: 299512
 Avg_row_length: 50
    Data_length: 15220736
Max_data_length: 0
   Index_length: 0
      Data_free: 4194304
 Auto_increment: NULL
    Create_time: 2022-02-18 18:44:06
    Update_time: 2022-02-18 18:45:46
     Check_time: NULL
      Collation: utf8_general_ci
       Checksum: NULL
 Create_options:
        Comment:
1 row in set (0.00 sec)
```



# 导出表(很慢)

```mysql
```



# 修改引擎

## alter

```mysql
alter table engine=;
```

- 两个缺点
  - 复制表，io时间很长
  - 对表加锁，如果频繁修改，印象业务



## 导出导入

用mysqldump导出为.sql文件，然后修改.sql文件

- 数据库名（防止覆盖）
- engine的类型



## create+alter+insert

```mysql
create table new_tb like old_tb;
alter table new_tb engine=;
insert into old_tb select *from new_tb;
```



# 基准测试

## Apache ab

[Apache ab - 简书 (jianshu.com)](https://www.jianshu.com/p/f0976dc7ffd2)



## http_load



## mysqlslap

- 待测数据库
  - 如果没有指定待测数据库，会自动生成一个数据库
    - 测试数据
      - --auto-generate-sql，自动生成测试sql
  - `--create-schema=`，指定待测数据库
- 测试sql
  - `--query="sql语句"`指定测试语句
  - `--query=".sql file"`指定多个sql语句
- 并发
  - `--concurrency=`并发数
- 测试次数
  - `--number-of-queries=`总的测试次数
  - `--iterations`迭代次数（重复次数）
- 





## super smack





## sysbench



# 生成测试数据mysqlslap

```mysql
# 首先建立表
use test;
drop table if exists test_insert_into;
create table test_insert_into(
	id int auto_increment,
	name varchar(255) not null,
	age int,
	primary key (id)
)engine=innodb default charset=utf8;

# 利用mysqlslap插入一千万条数据
mysqlslap -uroot -p123456 --concurrency=10 --number-of-queries=10000000 --create-schema=test --query="insert into test_insert_into(name,age) values(uuid(),rand()*100);
```

