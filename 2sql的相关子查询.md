sql的相关子查询

```sql
进入脚本目录
[root@whr ~]# cd /opt/software/openGauss/script/
切换用户
[root@whr script]# su - omm
Last login: Tue May 25 01:02:07 CST 2021 on pts/0


Welcome to 4.19.90-2003.4.0.0036.oe1.x86_64

System information as of time: 	2021年 05月 25日 星期二 01:16:54 CST

System load: 	0.12
Processes: 	117
Memory used: 	31.1%
Swap used: 	1.1%
Usage On: 	67%
IP address: 	192.168.56.102
Users online: 	2


开启数据库服务
[omm@whr ~]$ gs_om -t start
Starting cluster.
=========================================
[SUCCESS] whr:
[2021-05-25 01:17:08.377][33173][][gs_ctl]: gs_ctl started,datadir is /gaussdb/data/whr 
[2021-05-25 01:17:08.384][33173][][gs_ctl]:  another server might be running; Please use the restart command
=========================================
Successfully started.
登录到tom用户
[omm@whr ~]$ gsql -d st -p 26000 -U tom -W Whr123456  -r
gsql ((openGauss 1.1.0 build 392c0438) compiled at 2020-12-31 20:08:21 commit 0 last mr  )
Non-SSL connection (SSL connection is recommended when requiring high-security)
Type "help" for help.

st=> 

```



```sql

1．查询选了1号课且选了2号课的学生的班号、学号
select A.sclass,A.sno
from SC as A
where cno=1 and exists
(
    select *
    from SC as B
    where A.sclass=B.sclass and A.sno=B.sno and B.cno=2
)

st=> select A.sclass,A.sno
st-> from SC as A
st-> where cno=1 and exists
st-> (
st(>     select *
st(>     from SC as B
st(>     where A.sclass=B.sclass and A.sno=B.sno and B.cno=2
st(> );
 sclass | sno 
--------+-----
      1 |   1
      2 |   1
(2 rows)


2．查询选了1号课但不选2号课的学生的班号、学号
select A.sclass,A.sno
from SC as A
where cno=1 and not exists
(
    select *
    from SC as B
    where A.sclass=B.sclass and A.sno=B.sno and B.cno=2
)

st=> select A.sclass,A.sno
st-> from SC as A
st-> where cno=1 and not exists
st-> (
st(>     select *
st(>     from SC as B
st(>     where A.sclass=B.sclass and A.sno=B.sno and B.cno=2
st(> );
 sclass | sno 
--------+-----
      2 |   3
(1 row)


3．查询1班平均分在85分以上的同学班号、学号、姓名、性别、系、各科课程号及成绩
select S.sclass,S.sno,sname,ssex,sdept,cno,grade
from S,SC as A
where S.sclass=1 and S.sclass=A.sclass and S.sno=A.sno 
   and 85<
   (
       select avg(grade)
       from SC as B 
       where B.sclass=A.sclass and B.sno=A.sno
   )
st=> select S.sclass,S.sno,sname,ssex,sdept,cno,grade
st-> from S,SC as A
st-> where S.sclass=1 and S.sclass=A.sclass and S.sno=A.sno 
st->    and 85<
st->    (
st(>        select avg(grade)
st(>        from SC as B 
st(>        where B.sclass=A.sclass and B.sno=A.sno
st(>    );
 sclass | sno | sname | ssex | sdept | cno | grade 
--------+-----+-------+------+-------+-----+-------
      1 |   1 | 李勇  | 男   | IS    |   1 |    92
      1 |   1 | 李勇  | 男   | IS    |   2 |    85
      1 |   1 | 李勇  | 男   | IS    |   3 |    88
(3 rows)


4．查询至少选了1班2号同学所选课的所有班号、学号及同学姓名
select A.sclass,A.sno,A.sname
from S as A
where not exists(
    select *
    from SC as C
    where C.sclass=1 and C.sno=2 and not exists(
    select *
    from SC as B
    where A.sclass=B.sclass and A.sno=B.sno and B.cno=C.cno
    )
)
st=> select A.sclass,A.sno,A.sname
st-> from S as A
st-> where not exists(
st(>     select *
st(>     from SC as C
st(>     where C.sclass=1 and C.sno=2 and not exists(
st(>     select *
st(>     from SC as B
st(>     where A.sclass=B.sclass and A.sno=B.sno and B.cno=C.cno
st(>     )
st(> );
 sclass | sno | sname 
--------+-----+-------
      1 |   1 | 李勇
      1 |   2 | 刘晨
      2 |   2 | 张锋
(3 rows)


5．查询不选1号课的学生班号及学号
select sclass,sno
from S
where not exists
   (
       select *
       from SC
       where S.sclass=SC.sclass and S.sno=SC.sno and cno=1
   )

st=> select sclass,sno
st-> from S
st-> where not exists
st->    (
st(>        select *
st(>        from SC
st(>        where S.sclass=SC.sclass and S.sno=SC.sno and cno=1
st(>    );
 sclass | sno 
--------+-----
      1 |   2
      1 |   3
      2 |   2
(3 rows)


6．查询选2号课的学生名字及相应2号课成绩，按成绩从高到低排序
select sname,grade
from S,SC
where S.sclass=SC.sclass and S.sno=SC.sno and cno=2
order by grade desc

st=> select sname,grade
st-> from S,SC
st-> where S.sclass=SC.sclass and S.sno=SC.sno and cno=2
st-> order by grade desc;
 sname | grade 
-------+-------
 王敏  |    92
 刘晨  |    90
 张锋  |    87
 李勇  |    85
(4 rows)

7．统计学生选修课程的班号、学号及总学分
select S.sclass,S.sno,sum(SCREDIT.ccredit)
from S left join (
    select sclass,sno,ccredit
    from SC,C
    where SC.cno=C.cno
    ) as SCREDIT
   on S.sclass=SCREDIT.sclass and S.sno=SCREDIT.sno
   group by S.sclass,S.sno
   
st=> select S.sclass,S.sno,sum(SCREDIT.ccredit)
st-> from S left join (
st(>     select sclass,sno,ccredit
st(>     from SC,C
st(>     where SC.cno=C.cno
st(>     ) as SCREDIT
st->    on S.sclass=SCREDIT.sclass and S.sno=SCREDIT.sno
st->    group by S.sclass,S.sno;
 sclass | sno | sum 
--------+-----+-----
      2 |   3 |   4
      1 |   3 |    
      1 |   1 |  10
      1 |   2 |   6
      2 |   1 |   6
      2 |   2 |   6
(6 rows)


8．统计1班选修3号课的学号及平均分
select a.sno,avg(grade)
from sc as a
where a.sclass=1 and exists(
select * from sc as b
where b.sclass=a.sclass and b.sno=a.sno and b.cno= 3
)
group by a.sno;

st=> select a.sno,avg(grade)
st-> from sc as a
st-> where a.sclass=1 and exists(
st(> select * from sc as b
st(> where b.sclass=a.sclass and b.sno=a.sno and b.cno= 3
st(> )
st-> group by a.sno;
 sno |         avg         
-----+---------------------
   1 | 88.3333333333333333
   2 | 85.0000000000000000
(2 rows)
9．把个人信息及选课信息插入到Student和SC 表及新增加一门“无机化学”课程信息
insert into s(sclass,sno,sname,ssex,sage,sdept)
values (1,4,'MA','男',20,'MA');

insert into sc(sclass,sno,cno,grade)
values (1,4,3,88);

insert into c(cno,cname,ccredit)
values (10,'无机化学',6);

st=> insert into s(sclass,sno,sname,ssex,sage,sdept)
st-> values (1,4,'MA','男',20,'MA');
INSERT 0 1
st=> insert into sc(sclass,sno,cno,grade)
st-> values (1,4,3,88);
INSERT 0 1
st=> insert into c(cno,cname,ccredit)
st-> values (10,'无机化学',6);
INSERT 0 1
10. 删除选修3号课的所有选课信息并显示删除后的结果
select *
from SC
where cno=3;

delete from SC
where cno=3;

select *
from SC
where cno=3;

select *from SC;

st=> select *
st-> from SC
st-> where cno=3;
 sclass | sno | cno | grade 
--------+-----+-----+-------
      1 |   1 |   3 |    88
      1 |   2 |   3 |    80
      2 |   2 |   3 |    89
      1 |   4 |   3 |    88
(4 rows)

st=> delete from SC
st-> where cno=3;
DELETE 4
st=> select *
st-> from SC
st-> where cno=3;
 sclass | sno | cno | grade 
--------+-----+-----+-------
(0 rows)

st=> select *from SC;
 sclass | sno | cno | grade 
--------+-----+-----+-------
      1 |   1 |   1 |    92
      1 |   1 |   2 |    85
      1 |   2 |   2 |    90
      2 |   1 |   1 |    75
      2 |   1 |   2 |    92
      2 |   2 |   2 |    87
      2 |   3 |   1 |    90
(7 rows)
11. 把选修1号课的所有男同学年龄增加1岁并显示最终学生Student信息
select *
from S
where ssex='男' and exists(
    select *
    from SC
    where S.sclass=SC.sclass and S.sno=SC.sno and cno=1
)
   
st=> select *
st-> from S
st-> where ssex='男' and exists(
st(>     select *
st(>     from SC
st(>     where S.sclass=SC.sclass and S.sno=SC.sno and cno=1
st(> );
 sclass | sno | sname | ssex | sage | sdept 
--------+-----+-------+------+------+-------
      1 |   1 | 李勇  | 男   |   20 | IS
      2 |   3 | 李敏  | 男   |   20 | MA
(2 rows)
   
update S
set sage=sage+1
where ssex='男' and exists(
    select *
    from SC
    where S.sclass=SC.sclass and S.sno=SC.sno and cno=1
)
st=> update S
st-> set sage=sage+1
st-> where ssex='男' and exists(
st(>     select *
st(>     from SC
st(>     where S.sclass=SC.sclass and S.sno=SC.sno and cno=1
st(> );
UPDATE 2

select *
from S
where ssex='男' and exists(
    select *
    from SC
    where S.sclass=SC.sclass and S.sno=SC.sno and cno=1
)
st=> select *
st-> from S
st-> where ssex='男' and exists(
st(>     select *
st(>     from SC
st(>     where S.sclass=SC.sclass and S.sno=SC.sno and cno=1
st(> );
 sclass | sno | sname | ssex | sage | sdept 
--------+-----+-------+------+------+-------
      1 |   1 | 李勇  | 男   |   21 | IS
      2 |   3 | 李敏  | 男   |   21 | MA
(2 rows)
12. 把每个选课人的学号、班号及平均成绩插入到一个新表中。
create table S_AVG
(
    sclass int,
    sno int,
    avg_grade float,
    primary key(sclass,sno),
    foreign key(sclass,sno) references S(sclass,sno)
)
st=> create table S_AVG
st-> (
st(>     sclass int,
st(>     sno int,
st(>     avg_grade float,
st(>     primary key(sclass,sno),
st(>     foreign key(sclass,sno) references S(sclass,sno)
st(> );
NOTICE:  CREATE TABLE / PRIMARY KEY will create implicit index "s_avg_pkey" for table "s_avg"
   
select sno,sclass,avg(grade)
from SC
group by sclass,sno

st=> select sno,sclass,avg(grade)
st-> from SC
st-> group by sclass,sno;
 sno | sclass |         avg         
-----+--------+---------------------
   3 |      2 | 90.0000000000000000
   1 |      1 | 88.3333333333333333
   2 |      1 | 85.0000000000000000
   1 |      2 | 83.5000000000000000
   2 |      2 | 88.0000000000000000
(5 rows)

insert into s_avg (sno,sclass,avg_grade)
(
select sno,sclass,avg(grade)
from SC
group by sclass,sno
)
   
st=> insert into s_avg (sno,sclass,avg_grade)
st-> (
st(> select sno,sclass,avg(grade)
st(> from SC
st(> group by sclass,sno
st(> );
INSERT 0 5

select *from s_avg
st=> select *from s_avg;
 sclass | sno |    avg_grade     
--------+-----+------------------
      2 |   3 |               90
      1 |   1 | 88.3333333333333
      1 |   2 |               85
      2 |   1 |             83.5
      2 |   2 |               88
(5 rows)
  
```





视图

```sql
（二）视图SQL语言功能
1 使用企业管理器创建视图：在ST库中以“student”表为基础，建立信息系学生的视图V_IS_Student
create view V_IS_Student (sclass,sno,sname,ssex,sage)
as 
select sclass,sno,sname,ssex,sage
from s
where sdept='IS';

st=> create view V_IS_Student (sclass,sno,sname,ssex,sage)
st-> as 
st-> select sclass,sno,sname,ssex,sage
st-> from s
st-> where sdept='IS';
CREATE VIEW
2 使用SQL语句创建视图：
①建立一个每个学生的学号、班号、姓名、选修的课名及成绩的视图     S_C_GRADE；
create view S_C_GRADE (sclass,sno,sname,cname,grade)
as 
select s.sclass,s.sno,sname,cname,grade
from s,sc,c
where s.sclass=sc.sclass and s.sno=sc.sno and sc.cno=c.cno

st=> create view S_C_GRADE (sclass,sno,sname,cname,grade)
st-> as 
st-> select s.sclass,s.sno,sname,cname,grade
st-> from s,sc,c
st-> where s.sclass=sc.sclass and s.sno=sc.sno and sc.cno=c.cno;
CREATE VIEW
②建立信息系建立信息系选修了1号课程且成绩在90分以上的学生的视 图V_IS_Score
create view V_IS_Score (sclass,sno,cno,grade)
as 
select s.sclass,s.sno,cno,grade
from s,sc
where s.sclass=sc.sclass and s.sno=sc.sno and sdept='IS' and grade>90

st=> create view V_IS_Score (sclass,sno,cno,grade)
st-> as 
st-> select s.sclass,s.sno,cno,grade
st-> from s,sc
st-> where s.sclass=sc.sclass and s.sno=sc.sno and sdept='IS' and grade>90;
CREATE VIEW

③ 将各系学生人数，平均年龄定义为视图V_NUM_AVG。
create view V_NUM_AVG (sdept,s_num,s_avg_age)
as 
select sdept,count(*),avg(sage)
from s
group by sdept

st=> create view V_NUM_AVG (sdept,s_num,s_avg_age)
st-> as 
st-> select sdept,count(*),avg(sage)
st-> from s
st-> group by sdept;
CREATE VIEW
3  查询以上所建的视图结果
select *from view

4  查询选修了1号课程的信息系学生
select *
from s,sc
where cno=1 and sdept='IS' and s.sclass=sc.sclass and s.sno=sc.sno

st=> select *
st-> from s,sc
st-> where cno=1 and sdept='IS' and s.sclass=sc.sclass and s.sno=sc.sno;
 sclass | sno | sname | ssex | sage | sdept | sclass | sno | cno |
 grade 
--------+-----+-------+------+------+-------+--------+-----+-----+
-------
      1 |   1 | 李勇  | 男   |   21 | IS    |      1 |   1 |   1 |
    92
(1 row)


5  在信息系学生的视图中找出年龄小于20岁的学生
select *from V_IS_Student where sage<20

st=> select *from V_IS_Student where sage<20;
 sclass | sno | sname | ssex | sage 
--------+-----+-------+------+------
      1 |   2 | 刘晨  | 女   |   19
(1 row)

6  将信息系学生视图V_IS_Student中学号一班2号的学生姓名改为“刘辰”
update V_IS_Student set sname='刘辰'
where sclass=1 and sno=2

 7  用SQL语句删除视图S_C_GRADE
 drop view S_C_GRADE
 
 st=> drop view s_c_grade;
DROP VIEW
```

