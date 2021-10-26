```mysql
（1）建立用户tom,创建数据库ST，使得tom拥有数据库ST
create user tom with password '123456'
create database ST owner tom

postgres=# create user tom with password 'Whr123456'
postgres-# ;
CREATE ROLE
postgres=# create database ST owner tom;
CREATE DATABASE

（2）以tom用户链接数据库ST
\q退出当前登录的用户
[omm@whr ~]$ gsql -d st -p 26000 -U tom -W Whr123456  -r
gsql ((openGauss 1.1.0 build 392c0438) compiled at 2020-12-31 20:08:21 commit 0 last mr  )
Non-SSL connection (SSL connection is recommended when requiring high-security)
Type "help" for help.

st=>
（3）创建SCHEMA
create schema tom authorization tom

st=> create schema tom authorization tom;
CREATE SCHEMA
st=>

（4）建立课程表
create table if not exists C
(
	cno int(2),
    cname varchar(20),
    cpno int(2),
    ccredit int(2),
    primary key(cno),
    foreign key(cpno) references C(cno),
    check (ccredit>0)
);

create table if not exists C(cno int,cname varchar(20),cpno int,ccredit int,primary key(cno),foreign key(cpno) references C(cno),check (ccredit>0));

st=> create table if not exists C(cno int,cname varchar(20),cpno int,ccredit int,primary key(cno),foreign key(cpno) references C(cno),check (ccredit>0));
NOTICE:  CREATE TABLE / PRIMARY KEY will create implicit index "c_pkey" for table "c"
CREATE TABLE


（5）建立学生表
create table if not exists S
(
	sclass int(2),
    sno int(2),
    sname varchar(20) not null,
    ssex varchar(3),
    sage int(3),
    sdept varchar(50) not null,
    primary key(sclass,sno),
    check(ssex='男'or ssex='女'),
    check(sage>0)
);

create table if not exists S(sclass int,sno int,sname varchar(20) not null,ssex varchar(3),sage int,sdept varchar(50) not null,primary key(sclass,sno),check(ssex='男'or ssex='女'),check(sage>0));

st=> create table if not exists S(sclass int,sno int,sname varchar(20) not null,ssex varchar(3),sage int,sdept varchar(50) not null,primary key(sclass,sno),check(ssex='男'or ssex='女'),check(sage>0));
NOTICE:  CREATE TABLE / PRIMARY KEY will create implicit index "s_pkey" for table "s"
CREATE TABLE

（6）建立选课表
create table if not exists SC 
(
	sclass int(2),
    sno int(2),
    cno int(2),
    grade int(3),
    primary key(sclass,sno,cno),
    foreign key(sclass,sno) references S(sclass,sno),
    foreign key(cno) references C(cno),
    check(grade>=0 and grade<=100)
);

create table if not exists SC (sclass int,sno int,cno int,grade int,primary key(sclass,sno,cno),foreign key(sclass,sno) references S(sclass,sno),foreign key(cno) references C(cno),check(grade>=0 and grade<=100));

st=> create table if not exists SC (sclass int,sno int,cno int,grade int,primary key(sclass,sno,cno),foreign key(sclass,sno) references S(sclass,sno),foreign key(cno) references C(cno),check(grade>=0 and grade<=100));
NOTICE:  CREATE TABLE / PRIMARY KEY will create implicit index "sc_pkey" for table "sc"
CREATE TABLE

（7）分别向课程表、学生表、选课表中插入数据
//顺序很重要
insert into C(cno,cname,ccredit)
values
    (2,'数学',2),
    (6,'数据处理',2);

st=> insert into C(cno,cname,ccredit)
st-> values
st->     (2,'数学',2),
st->     (6,'数据处理',2);
INSERT 0 2

insert into C(cno,cname,cpno,ccredit)
values
    (1,'数据库',5,4),
    (3,'信息系统',1,4),
    (4,'操作系统',6,3),
    (5,'数据结构',7,4),
    (7,'PASCAL语言',6,4);

st=> insert into C(cno,cname,cpno,ccredit)
st-> values
st->     (1,'数据库',5,4),
st->     (3,'信息系统',1,4),
st->     (4,'操作系统',6,3),
st->     (5,'数据结构',7,4),
st->     (7,'PASCAL语言',6,4);
INSERT 0 5

insert into S(sclass,sno,sname,ssex,sage,sdept)
values
    (1,1,'李勇','男',20,'IS'),
    (1,2,'刘晨','女',19,'IS'),
    (1,3,'刘朋','男',20,'IS'),
    (2,1,'王敏','女',18,'MA'),
    (2,2,'张锋','男',19,'MA'),
    (2,3,'李敏','男',20,'MA');
st=> insert into S(sclass,sno,sname,ssex,sage,sdept)
st-> values
st->     (1,1,'李勇','男',20,'IS'),
st->     (1,2,'刘晨','女',19,'IS'),
st->     (1,3,'刘朋','男',20,'IS'),
st->     (2,1,'王敏','女',18,'MA'),
st->     (2,2,'张锋','男',19,'MA'),
st->     (2,3,'李敏','男',20,'MA');
INSERT 0 6

insert into SC
values
    (1,1,1,92),
    (1,1,2,85),
    (1,1,3,88),
    (1,2,2,90),
    (1,2,3,80),
    (2,1,1,75),
    (2,1,2,92),
    (2,2,2,87),
    (2,2,3,89),
    (2,3,1,90);
    
st=> insert into SC
st-> values
st->     (1,1,1,92),
st->     (1,1,2,85),
st->     (1,1,3,88),
st->     (1,2,2,90),
st->     (1,2,3,80),
st->     (2,1,1,75),
st->     (2,1,2,92),
st->     (2,2,2,87),
st->     (2,2,3,89),
st->     (2,3,1,90);
INSERT 0 10
（8）查询所有学生的详细信息（包含学生、选课及课程信息）
select s.sclass,s.sno,sname,ssex,sdept,sage,sc.cno,cname,grade
from s,sc,c
where s.sclass=sc.sclass and s.sno=sc.sno and sc.cno=c.cno

st=> select s.sclass,s.sno,sname,ssex,sdept,sage,sc.cno,cname,grade
st-> from s,sc,c
st-> where s.sclass=sc.sclass and s.sno=sc.sno and sc.cno=c.cno;
 sclass | sno | sname | ssex | sdept | sage | cno | cname  | grade
 
--------+-----+-------+------+-------+------+-----+--------+------
-
      1 |   1 | 李勇  | 男   | IS    |   21 |   1 | 数据库 |    92
      1 |   1 | 李勇  | 男   | IS    |   21 |   2 | 数学   |    85
      1 |   2 | 刘晨  | 女   | IS    |   19 |   2 | 数学   |    90
      2 |   1 | 王敏  | 女   | MA    |   18 |   1 | 数据库 |    75
      2 |   1 | 王敏  | 女   | MA    |   18 |   2 | 数学   |    92
      2 |   2 | 张锋  | 男   | MA    |   19 |   2 | 数学   |    87
      2 |   3 | 李敏  | 男   | MA    |   21 |   1 | 数据库 |    90
(7 rows)
（9）查询1班的学生学号及姓名
select sno,sname
from S
where sclass=1

st=> select sno,sname
st-> from S
st-> where sclass=1;
 sno | sname 
-----+-------
   1 | 李勇
   2 | 刘晨
   3 | 刘朋
(3 rows)

（10）查询‘刘晨’的出生年
select 2021-sage as birth_year
from S
where sname='刘晨'

st=> select 2021-sage as birth_year
st-> from S
st-> where sname='刘晨';
 birth_year 
------------
       2002
(1 row)

（11）查询姓‘刘’的学生的详细情况(包括学生表、选课表及课程表的全部信息)
select
S.sclass 班级号,S.sno 学号,S.sname 姓名,S.ssex 性别,S.sage 年龄,S.sdept 院系,SC.cno 课程号,C.cname 课程名,SC.grade 分数,C.cpno 选修课号,C.ccredit 学分数
from S,SC,C
where S.sclass=SC.sclass and S.sno=SC.sno and C.cno=SC.cno and S.sname like '刘_%';

st-> S.sclass 班级号,S.sno 学号,S.sname 姓名,S.ssex 性别,S.sage 年龄,S.sdept 院系,SC.cno 课程号,C.cname 课程名,SC.grade 分数,C.cpno 选修课号,C.ccredit 学分数
st-> from S,SC,C
st-> where S.sclass=SC.sclass and S.sno=SC.sno and C.cno=SC.cno and S.sname like '刘_%';
 班级号 | 学号 | 姓名 | 性别 | 年龄 | 院系 | 课程号 |  课程名  | 分数 | 选修课号 | 学分数 
--------+------+------+------+------+------+--------+----------+------+----------+--------
      1 |    2 | 刘晨 | 女   |   19 | IS   |      2 | 数学     |   90 |          |      2
      1 |    2 | 刘晨 | 女   |   19 | IS   |      3 | 信息系统 |   80 |        1 |      4
(2 rows)

（12）查询选修了1号课的学生姓名、性别、成绩
select sname,ssex,grade
from S,SC
where S.sclass=SC.sclass and S.sno=SC.sno and cno=1

st=> select sname,ssex,grade
st-> from S,SC
st-> where S.sclass=SC.sclass and S.sno=SC.sno and cno=1;
 sname | ssex | grade 
-------+------+-------
 李勇  | 男   |    92
 王敏  | 女   |    75
 李敏  | 男   |    90
(3 rows)

（13）查询没有先行课课程的课程号和课程名
select cno,cname
from C
where cpno is NULL

st=> select cno,cname
st-> from C
st-> where cpno is NULL;
 cno |  cname   
-----+----------
   2 | 数学
   6 | 数据处理
(2 rows)

（14）查询2班的所有女生的情况
select *
from S
where sclass=2 and ssex='女'

st=> select *
st-> from S
st-> where sclass=2 and ssex='女';
 sclass | sno | sname | ssex | sage | sdept 
--------+-----+-------+------+------+-------
      2 |   1 | 王敏  | 女   |   18 | MA
(1 row)

（15）查询学分为2到3之间的课程号及课程名
select cno,cname
from C
where ccredit between 2 and 3

st=> select cno,cname
st-> from C
st-> where ccredit between 2 and 3;
 cno |  cname   
-----+----------
   2 | 数学
   6 | 数据处理
   4 | 操作系统
(3 rows)

（16）查询选修1号课的学生的班号、学号、姓名、课程名及成绩，要求成绩按照递减排序输出
select S.sclass,S.sno,sname,cname,grade
from S,SC,C
where S.sclass=SC.sclass and S.sno=SC.sno and SC.cno=1 and C.cno=SC.cno
order by grade desc

st=> select S.sclass,S.sno,sname,cname,grade
st-> from S,SC,C
st-> where S.sclass=SC.sclass and S.sno=SC.sno and SC.cno=1 and C.cno=SC.cno
st-> order by grade desc
st-> ;
 sclass | sno | sname | cname  | grade 
--------+-----+-------+--------+-------
      1 |   1 | 李勇  | 数据库 |    92
      2 |   3 | 李敏  | 数据库 |    90
      2 |   1 | 王敏  | 数据库 |    75
(3 rows)

（17）查询2班至少选修一门其先行课为1号课的学生的班号、学号、姓名、性别、系、课程号及成绩
select S.sclass,S.sno,sname,ssex,sdept,cno,grade
from S,SC
where S.sclass=SC.sclass and S.sno=SC.sno and S.sclass=2 and SC.cno in (select cno from C where cpno=1)

st=> select S.sclass,S.sno,sname,ssex,sdept,cno,grade
st-> from S,SC
st-> where S.sclass=SC.sclass and S.sno=SC.sno and S.sclass=2 and SC.cno in (select cno from C where cpno=1);
 sclass | sno | sname | ssex | sdept | cno | grade 
--------+-----+-------+------+-------+-----+-------
      2 |   2 | 张锋  | 男   | MA    |   3 |    89
(1 row)

（18）查询2号课成绩最高的学生班号、学号、姓名
select S.sclass,S.sno,S.sname
from S,SC
where S.sclass=SC.sclass and S.sno=SC.sno and cno=2 and grade=(
    select
    max(grade) 
    from SC 
    where cno=2)
    
st=> select S.sclass,S.sno,S.sname
st-> from S,SC
st-> where S.sclass=SC.sclass and S.sno=SC.sno and cno=2 and grade=(
st(>     select
st(>     max(grade) 
st(>     from SC 
st(>     where cno=2);
 sclass | sno | sname 
--------+-----+-------
      2 |   1 | 王敏
(1 row)

（19）查询1班2号课成绩最低的学生班号、学号
select sclass,sno 
   from SC 
   where cno=2 and grade=(
       select min(grade) 
       from SC 
       where cno=2 and sclass=1)
   
st=> select sclass,sno from SC where cno=2 and grade=(select min(grade) from SC where cno=2 and sclass=1)
st-> ;
 sclass | sno 
--------+-----
      1 |   1
(1 row)

（20）查询选修2号课且成绩不是最低的同学班号、学号
select sclass,sno
from SC
where cno=2 and grade>any (
    select grade from SC
    where cno=2
)
   
st=> select sclass,sno
st-> from SC
st-> where cno=2 and grade>any (
st(>     select grade from SC
st(>     where cno=2
st(> );
 sclass | sno 
--------+-----
      1 |   2
      2 |   1
      2 |   2
(3 rows)

（21）查询包含2班1号同学所选全部课程的同学的班号、学号
select S.sclass,S.sno
from S
where not exists(
        select *
        from SC A
        where A.sclass=2 and A.sno=1 and
        not exists(
            select *
            from SC B
            where A.cno=B.cno and B.sclass=S.sclass and B.sno=S.sno
        )
)

st=> select S.sclass,S.sno
st-> from S
st-> where not exists(
st(>         select *
st(>         from SC A
st(>         where A.sclass=2 and A.sno=1 and
st(>         not exists(
st(>             select *
st(>             from SC B
st(>             where A.cno=B.cno and B.sclass=S.sclass and B.sno=S.sno
st(>         )
st(> );
 sclass | sno 
--------+-----
      1 |   1
      2 |   1
(2 rows)

select S.sclass,S.sno
from S
where not exists(
        select *
        from SC A
        where A.sclass=2 and A.sno=1 and
        not exists(
            select *
            from SC B
            where A.cno=B.cno and B.sclass=S.sclass and B.sno=S.sno
        )
) and (sclass<>2 or sno<>1)
   
st=> select S.sclass,S.sno
st-> from S
st-> where not exists(
st(>         select *
st(>         from SC A
st(>         where A.sclass=2 and A.sno=1 and
st(>         not exists(
st(>             select *
st(>             from SC B
st(>             where A.cno=B.cno and B.sclass=S.sclass and B.sno=S.sno
st(>         )
st(> ) and (sclass<>2 or sno<>1);
 sclass | sno 
--------+-----
      1 |   1
(1 row)
（22）查询选修每门课程的课程号及人数
select cno,count(*)
from SC
group by cno;
   
st=> select cno,count(*)
st-> from SC
st-> group by cno;
 cno | count 
-----+-------
   1 |     3
   3 |     3
   2 |     4
(3 rows)


   
（23）查询选修三门课的同学班号、学号、姓名、课程名及成绩
select S.sclass,S.sno,sname,cname,grade 
from S,SC as A,C
where S.sclass=A.sclass and S.sno=A.sno and A.cno=C.cno
and 3=(
    select count(*)
    from SC as B
    where A.sclass=B.sclass and A.sno=B.sno
    group by B.sclass,B.sno
    )
st=> select S.sclass,S.sno,sname,cname,grade 
st-> from S,SC as A,C
st-> where S.sclass=A.sclass and S.sno=A.sno and A.cno=C.cno
st-> and 3=(
st(>     select count(*)
st(>     from SC as B
st(>     where A.sclass=B.sclass and A.sno=B.sno
st(>     group by B.sclass,B.sno
st(>     );
 sclass | sno | sname |  cname   | grade 
--------+-----+-------+----------+-------
      1 |   1 | 李勇  | 数据库   |    92
      1 |   1 | 李勇  | 数学     |    85
      1 |   1 | 李勇  | 信息系统 |    88
(3 rows)
```

Whr824655-root

Whr819987540-test

把系统挂载后，重启，一直显示让我安装。

原来是加载的首选项没有换过来，这时候应该首选硬盘加载，而不是光驱。

开了两个网卡，相当于两个端口，一个用win的xshell进行远程控制，毕竟virtual box的界面太操蛋了。一个公网ip（路由穿透）

```sql
NOTICE:  CREATE TABLE / PRIMARY KEY will create implicit index "s_pkey" for table "s"
```



# 实验问题

## 关于char和varchar

```sql
    cname varchar(10),
st=> insert into C(cno,cname,cpno,ccredit)
st-> values
st->     (1,'数据库',5,4),
st->     (3,'信息系统',1,4),
st->     (4,'操作系统',6,3),
st->     (5,'数据结构',7,4),
st->     (7,'PASCAL语言',6,4);
ERROR:  value too long for type character varying(10)

```

为啥插不进去呢？

gbk编码中文是2字节，utf-8是三个字节，我一开始认为是gbk编码，所以定义的varchar是10字节，现在发现可能太短了。因为配置的是utf-8编码，所以“PASCAL语言”没地方放了。修改一下字段属性就好。

```sql
st=> alter table S modify ssex varchar(3);
ALTER TABLE
st=> alter table S modify sdept varchar(50);
ALTER TABLE
st=> insert into S(sclass,sno,sname,ssex,sage,sdept)
st-> values
st->     (1,1,'李勇','男',20,'IS'),
st->     (1,2,'刘晨','女',19,'IS'),
st->     (1,3,'刘朋','男',20,'IS'),
st->     (2,1,'王敏','女',18,'MA'),
st->     (2,2,'张锋','男',19,'MA'),
st->     (2,3,'李敏','男',20,'MA');
ERROR:  value too long for type character varying(1)
```



```sql
st=> insert into C(cno,cname,cpno,ccredit)
st-> values
st->     (1,'数据库',5,4),
st->     (3,'信息系统',1,4),
st->     (4,'操作系统',6,3),
st->     (5,'数据结构',7,4),
st->     (7,'PASCAL语言',6,4);
ERROR:  insert or update on table "c" violates foreign key constraint "c_cpno_fkey"
DETAIL:  Key (cpno)=(6) is not present in table "c".
```



## 关于外键

```sql
create table if not exists C
(
	cno int(2),
    cname varchar(20),
    cpno int(2),
    ccredit int(2),
    primary key(cno),
    foreign key(cpno) references C(cno),
    check (ccredit>0)
);

alter table C drop foreign key cpno;
```

```sql
但是仔细看看报错
DETAIL:  Key (cpno)=(6) is not present in table "c".
只是说cpno为6的时候没插进去？
也就是说别的插进去了？
一开始为了字段的一致，先插入都非空的记录，然后插入有空值的记录，现在看来可以调换一下顺序。
st=> insert into C(cno,cname,ccredit)
st-> values
st->     (2,'数学',2),
st->     (6,'数据处理',2);
INSERT 0 2
st=> insert into C(cno,cname,cpno,ccredit)
st-> values
st->     (1,'数据库',5,4),
st->     (3,'信息系统',1,4),
st->     (4,'操作系统',6,3),
st->     (5,'数据结构',7,4),
st->     (7,'PASCAL语言',6,4);
INSERT 0 5
st=> 

```



## 一个逻辑问题

如果不用minus，如何实现（21）查询包含2班1号同学所选全部课程的同学的班号、学号去掉2班1号同学本人呢？

首先尝试，用两个and是班号不能是2且学号不能是1，显然不对，这样将2班所有同学和学号是1的所有同学都去掉了。

可以在逻辑上进行一下转换。学号为1且班号为2不行，也就是学号不为1或班号为2可行。

```sql
st=> select S.sclass,S.sno
st-> from S
st-> where not exists(
st(>         select *
st(>         from SC A
st(>         where A.sclass=2 and A.sno=1 and
st(>         not exists(
st(>             select *
st(>             from SC B
st(>             where A.cno=B.cno and B.sclass=S.sclass and B.sno=S.sno
st(>         )
st(> ) and (sclass<>2 and sno<>1);
 sclass | sno 
--------+-----
(0 rows)
   
select S.sclass,S.sno
from S
where not exists(
        select *
        from SC A
        where A.sclass=2 and A.sno=1 and
        not exists(
            select *
            from SC B
            where A.cno=B.cno and B.sclass=S.sclass and B.sno=S.sno
        )
) and (sclass<>2 or sno<>1)
```

