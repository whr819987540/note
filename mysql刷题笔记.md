# 题目

## limit



![image-20220213155515055](https://raw.githubusercontent.com/whr819987540/pic/main/image-20220213155515055.png)



前两个用户，应该有order by来进行控制

![image-20220213155707279](https://raw.githubusercontent.com/whr819987540/pic/main/image-20220213155707279.png)



## 通配符

![image-20220213162059260](https://raw.githubusercontent.com/whr819987540/pic/main/image-20220213162059260.png)

## exists实现max

![image-20220213162916378](https://raw.githubusercontent.com/whr819987540/pic/main/image-20220213162916378.png)



## count效率测试

- explain可以看到一些非量化的参数

- 量化的参数

  - 首先用`show variables`检查profilng是否打开

    - 如果没有，用` set profiling = 1`打开该选项

    - 然后用`show profiles`查看具体结果

    - ```bash
      EXPLAIN SELECT COUNT(*) AS male_num,AVG(gpa) AS avg_gpa
      FROM user_profile
      WHERE gender='male';
      
      EXPLAIN SELECT COUNT(id) AS male_num,AVG(gpa) AS avg_gpa
      FROM user_profile
      WHERE gender='male';
      
      EXPLAIN SELECT COUNT(gender) AS male_num,AVG(gpa) AS avg_gpa
      FROM user_profile
      WHERE gender='male';
      
      SHOW PROFILES;
      
      0.00046100
      0.00022050
      0.00036325
      ```

    - `count(*)`最慢

    - 在id上建了索引，id最快
    
    - gender相比于*也要快一点



## join（hard）

[统计每个学校的答过题的用户的平均答题数_牛客题霸_牛客网 (nowcoder.com)](https://www.nowcoder.com/practice/88aa923a9a674253b861a8fa56bac8e5?tpId=199&tags=&title=&difficulty=0&judgeStatus=0&rp=0)

```mysql
SELECT a.university,ROUND(COUNT(b.question_id) / COUNT(DISTINCT a.device_id),4)
FROM user_profile AS a
RIGHT JOIN question_practice_detail AS b
ON a.device_id=b.device_id
GROUP BY a.university
```

- 如果用where来连接两个表，也可以起到相同的效果
- 如果用left join来连接，需要对b.question_id进行null检查，因为有的device_id可能没有对应的question_id
- 用right join
  - 在生成第二个字段时
  - 首先要是答过题的用户，这个用right join处理好了
  - 然后是平均答题数=（答题总数，直接count）/ 用户数
    - question_id可能，不需要去重
    - ![image-20220214110347648](https://raw.githubusercontent.com/whr819987540/pic/main/image-20220214110347648.png)
    - device_id可能，因为还是一个人，所以需要去重
    - ![image-20220214110413954](https://raw.githubusercontent.com/whr819987540/pic/main/image-20220214110413954.png)



## 题意（hard）

[统计每个学校各难度的用户平均刷题数_牛客题霸_牛客网 (nowcoder.com)](https://www.nowcoder.com/practice/5400df085a034f88b2e17941ab338ee8?tpId=199&tags=&title=&difficulty=0&judgeStatus=0&rp=0)

- 题意

  - 首先对学校和难度进行分组
  - 然后将这三个表连起来
  - 第二个表是记录刷题记录
  - 第三个表是提供难度这个字段

- ```mysql
  SELECT a.university,c.`difficult_level`,ROUND(COUNT(b.`question_id`) / COUNT(DISTINCT b.`device_id`),4)
  FROM user_profile AS a,question_practice_detail AS b,question_detail AS c
  WHERE a.device_id=b.device_id AND b.question_id=c.question_id
  GROUP BY a.university,c.difficult_level
  ORDER BY a.`university`
  ```



## 集合运算

- 并
  - 去重，union
    - ![image-20220214155926399](https://raw.githubusercontent.com/whr819987540/pic/main/image-20220214155926399.png)
  - 不去重，union all
    - ![image-20220214155534140](https://raw.githubusercontent.com/whr819987540/pic/main/image-20220214155534140.png)
- 交
  - intersect
- 差
  - except





## case

可以用集合，但是情况多了就比较麻烦

![image-20220214160816348](https://raw.githubusercontent.com/whr819987540/pic/main/image-20220214160816348.png)





![image-20220214160852884](https://raw.githubusercontent.com/whr819987540/pic/main/image-20220214160852884.png)



## 连表查询（hard）

[计算用户的平均次日留存率_牛客题霸_牛客网 (nowcoder.com)](https://www.nowcoder.com/practice/126083961ae0415fbde061d7ebbde453?tpId=199&tags=&title=&difficulty=0&judgeStatus=0&rp=0)

![image-20220214171251529](https://raw.githubusercontent.com/whr819987540/pic/main/image-20220214171251529.png)

- 关键点

  - 一个用户在某一天可能多次刷题，有多个记录
  - 所以任何时候都需要对device_id去重

- 解析

  - 最内层

    - 查询出id和date，注意此处的id经过了去重

    - ```mysql
      SELECT DISTINCT device_id,DATE
      			FROM question_practice_detail
      ```

    - 然后是对查询结果重命名

  - 左连接

    - 这里的思路是让左表和右表的id相同，然后满足时间关系

    - 此处仍然需要去重

    - ```mysql
      SELECT DISTINCT qpd.device_id,qpd.`date` AS date1,uni_id_date.date AS date2
      		FROM question_practice_detail AS qpd
      		LEFT JOIN
      			(SELECT DISTINCT device_id,DATE
      			FROM question_practice_detail) AS uni_id_date
      		ON qpd.`device_id`=uni_id_date.device_id AND DATE_ADD(qpd.`date`,INTERVAL 1 DAY)=uni_id_date.date
      ```

    - 因为左右两个表都有date字段，所以还需要重命名

  - 外层

    - 这里的思路是，因为里面用的是左连接，如果满足时间关系，date2字段不为空，也就是在第二天也刷了题
    -         ```mysql
        SELECT COUNT(res.date2)/COUNT(res.date1)
        FROM 
            (
                SELECT DISTINCT qpd.device_id,qpd.`date` AS date1,uni_id_date.date AS date2
                FROM question_practice_detail AS qpd
                LEFT JOIN
                    (SELECT DISTINCT device_id,DATE
                    FROM question_practice_detail) AS uni_id_date
                ON qpd.`device_id`=uni_id_date.device_id AND DATE_ADD(qpd.`date`,INTERVAL 1 DAY)=uni_id_date.date
            ) AS res
        ```



## 子查询

![image-20220214173829097](https://raw.githubusercontent.com/whr819987540/pic/main/image-20220214173829097.png)



## 多解

![image-20220214201805178](https://raw.githubusercontent.com/whr819987540/pic/main/image-20220214201805178.png)

```mysql
select device_id,university,gpa
from user_profile as a
where not exists(
    select b.gpa 
    from user_profile as b
    where a.university=b.university and b.gpa<a.gpa 
)
order by university

select device_id,university,gpa
from user_profile
where (university,gpa) in (
    select university,min(gpa)
    from user_profile
    group by university
)
order by university

select device_id,a.university,a.gpa
from user_profile as a
join (
    select university,min(gpa) as g
    from user_profile
    group by university
) as b
on a.university=b.university and a.gpa=b.g
order by a.university
```



```mysql
select up.device_id, '复旦大学',
    count(question_id) as question_cnt,
    sum(if(qpd.result='right', 1, 0)) as right_question_cnt
from user_profile as up

left join question_practice_detail as qpd
  on qpd.device_id = up.device_id and month(qpd.date) = 8

where up.university = '复旦大学'
group by up.device_id

```



## 从表插入

- 将一个表的查询结果插入到另一个表中
- 插入的格式
  - 普通插入（全字段）：INSERT INTO table_name VALUES (value1, value2, ...)
  - 普通插入（限定字段）：INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...)
  - 多条一次性插入：INSERT INTO table_name (column1, column2, ...) VALUES (value1_1, value1_2, ...), (value2_1, value2_2, ...), ...
  - 从另一个表导入：INSERT INTO table_name SELECT * FROM table_name2 [WHERE key=value]
- 注意
  - 在从另一个表导入时，主键不能直接导入，否则主键的值会异常
  - 带更新的插入：REPLACE INTO table_name VALUES (value1, value2, ...) （注意这种原理是检测到主键或唯一性索引键重复就删除原记录后重新插入）

[插入记录（二）_牛客题霸_牛客网 (nowcoder.com)](https://www.nowcoder.com/practice/9681abf28745468c8adacb3b029a18ce?tpId=240&tqId=2221797&ru=%2Fta%2Fsql-advanced&qru=%2Fta%2Fsql-advanced%2Fquestion-ranking)



![image-20220215091331189](https://raw.githubusercontent.com/whr819987540/pic/main/image-20220215091331189.png)



## 强制插入

- 插入数据在主键或者唯一索引上产生冲突时，如果还要继续插入
  - 可以先删除，然后再插入
  - 也可以通过`replace into table() values()`来完成
    - 这条语句首先检查要插入的数据和已经存在的数据在主键和唯一索引上是否有冲突，如果有冲突，则删除，然后插入

插入前：

![image-20220215092804764](https://raw.githubusercontent.com/whr819987540/pic/main/image-20220215092804764.png)

replace into插入后：

显示影响了两行，即先删除，然后插入

![image-20220215092831988](https://raw.githubusercontent.com/whr819987540/pic/main/image-20220215092831988.png)

并且主键的值也发生了变化

![image-20220215092909147](https://raw.githubusercontent.com/whr819987540/pic/main/image-20220215092909147.png)



## 更新

- 设置为新值：UPDATE table_name SET column_name=new_value [, column_name2=new_value2] [WHERE column_name3=value3]
- 根据已有值替换：UPDATE table_name SET key1=replace(key1, '查找内容', '替换成内容') [WHERE column_name3=value3]
  - 不仅可以完成替换，还可以进行子串的替换

- tag为PYTHON的tag字段全部修改为Python

  - ```mysql
    UPDATE examination_info
    SET tag = "Python"
    WHERE tag = "PYTHON";
    
    update examination_info
    set tag = replace(tag,'PYTHON','Python')
    where tag = 'PYTHON'
    ```

- 将tag中含有PYTHON的部分，修改为Python

  - ```mysql
    update examination_info
    set tag=replace(tag,'PYTHON','Python')
    where tag like '%PYTHON%'
    ```
    
    
    

## 删除

- 根据条件删除：DELETE FROM tb_name [WHERE options] [ [ ORDER BY fields ] LIMIT n ]
- 全部删除（表清空，包含自增计数器重置）：TRUNCATE tb_name

```mysql
请删除exam_record表中未完成作答或作答时间小于5分钟整的记录中，开始作答时间最早的3条记录。

delete from exam_record
where score is null or (score is not null and timestampdiff(minute,start_time,submit_time)<5)
order by start_time asc
limit 3
```



## 创建表

- 创建表结构

```mysql
CREATE TABLE
[IF NOT EXISTS] tb_name -- 不存在才创建，存在就跳过
(column_name1 data_type1 -- 列名和类型必选
  [ PRIMARY KEY -- 可选的约束，主键
   | FOREIGN KEY -- 外键，引用其他表的键值
   | AUTO_INCREMENT -- 自增ID
   | COMMENT comment -- 列注释（评论）
   | DEFAULT default_value -- 默认值
   | UNIQUE -- 唯一性约束，不允许两条记录该列值相同
   | NOT NULL -- 该列非空
  ], ...
) [CHARACTER SET charset] -- 字符集编码
[COLLATE collate_value] -- 列排序和比较时的规则（是否区分大小写等）

```



- 复制表结构

```mysql
CREATE TABLE tb_name LIKE tb_name_old
```



- 从查询结果复制表结构和表数据

```mysql
CREATE TABLE tb_name AS SELECT * FROM tb_name_old WHERE options
```



## 修改表

```mysql
alter table tb_name
		| ADD COLUMN <列名> <类型>  -- 增加列
		# alter table user_info_vip_copy1 add COLUMN test int(4) default 11 not null
		| CHANGE COLUMN <旧列名> <新列名> <新列类型> -- 修改列名或类型
		# alter table user_info_vip_copy1 change test new_test int(4)
		| ALTER COLUMN <列名> { SET DEFAULT <默认值> | DROP DEFAULT } -- 修改/删除 列的默认值
		# alter table user_info alter column achievement set default 0
		| MODIFY COLUMN <列名> <类型> -- 修改列类型
		| DROP COLUMN <列名> -- 删除列
		# alter table user_info_vip_copy1 drop column job
		| RENAME TO <新表名> -- 修改表名
		# alter table user_info_vip_copy rename to user_info_vip_copy1
		| CHARACTER SET <字符集名> -- 修改字符集
		| COLLATE <校对规则名> } -- 修改校对规则（比较和排序时用到）
```



![image-20220215143905319](https://raw.githubusercontent.com/whr819987540/pic/main/image-20220215143905319.png)



<img src="https://raw.githubusercontent.com/whr819987540/pic/main/image-20220215144109088.png" alt="image-20220215144109088" style="zoom:50%;" />

- 增加一列
  - 注意特别强调了在字段level后面
  - `alter table user_info add column school varchar(15) after level`
- 改名，修改类型
  - `alter table user_info change column job profession varchar(10)`
- achievement这一列，注释也没了
  - `alter table user_info alter column achievement set default 0 `不能清除注释
  - `alter table user_info change column achievement achievement int(11) default 0`



## 索引

- DROP INDEX index_name ON ta_name
  - ![image-20220215145404084](https://raw.githubusercontent.com/whr819987540/pic/main/image-20220215145404084.png)
  - ![image-20220215145548240](https://raw.githubusercontent.com/whr819987540/pic/main/image-20220215145548240.png)
- ALTER TABLE tbl_name ADD PRIMARY KEY (column_list): 该语句添加一个主键，这意味着索引值必须是唯一的，且不能为NULL。
  - 
- ALTER TABLE tbl_name ADD UNIQUE index_name (column_list): 这条语句创建索引的值必须是唯一的（除了NULL外，NULL可能会出现多次）。
  - ![image-20220215150040883](https://raw.githubusercontent.com/whr819987540/pic/main/image-20220215150040883.png)
- ALTER TABLE tbl_name ADD INDEX index_name (column_list): 添加普通索引，索引值可出现多次。
  - ![image-20220215145956333](https://raw.githubusercontent.com/whr819987540/pic/main/image-20220215145956333.png)
- ALTER TABLE tbl_name ADD FULLTEXT index_name (column_list):该语句指定了索引为 FULLTEXT ，用于全文索引。
  - 

![image-20220215150315073](https://raw.githubusercontent.com/whr819987540/pic/main/image-20220215150315073.png)



## if

`if(condition,a,b)`如果条件满足，返回a，否则返回b。

![image-20220215152921924](https://raw.githubusercontent.com/whr819987540/pic/main/image-20220215152921924.png)



![image-20220215152928414](https://raw.githubusercontent.com/whr819987540/pic/main/image-20220215152928414.png)





![image-20220215152854596](https://raw.githubusercontent.com/whr819987540/pic/main/image-20220215152854596.png)

- 已完成的试卷数
  - 即又成绩的试卷，且不能重复
  - `select count(id),count(score),count(distinct if(score is not null,exam_id,null))
    from exam_record`







## 题意hard

![image-20220215161437840](https://raw.githubusercontent.com/whr819987540/pic/main/image-20220215161437840.png)

```mysql
select ym,round(count(id)/count(distinct uid),2),count(distinct uid)
from (
    select id,uid,date_format(submit_time,'%Y%m') as ym
    from exam_record
    where submit_time is not null) tmp
group by ym
```

这个是错的，因为某个月的活跃天数不只是这个月有submit_time的记录数，还得满足对同一天的uid去重。

![image-20220215160931772](https://raw.githubusercontent.com/whr819987540/pic/main/image-20220215160931772.png)

![image-20220215160912556](https://raw.githubusercontent.com/whr819987540/pic/main/image-20220215160912556.png)

- 活跃天
  - 某个用户在某天有submit_time
  - 如果有多条记录，应该去重，不能重复计算
  - uid和submit_time都应该不同
- 月活跃用户
  - 对这个月有submit_time的uid去重
- 平均月活跃天数
  - 某个月总的活跃天数/这个月活跃过的用户数

```mysql
# 2021年月活跃用户
select count(distinct uid)
from exam_record
where year(submit_time)=2021
group by month(submit_time)

# 2021年月活跃天数
select count(distinct uid,day(submit_time))
from exam_record
where year(submit_time)=2021
group by month(submit_time)

# 2021年平均月活跃天数和月活跃用户
# select target list中的值，如果是和group by相关的字段
# 要么对该字段应用聚合函数（sum、avg、max等）
# 要么是来自于group by list中的表达式的值
# 这里对submit_time进行了非聚合函数的处理，所以无法成功
select date_format(submit_time,'%Y%m'),
round(count(distinct uid,day(submit_time)) / count(distinct uid),2),count(distinct uid)
from exam_record
where year(submit_time)=2021
group by month(submit_time)

# 这里，没有对group by的字段进行非聚合函数的处理，而是原来的值，所以可行
# 至于其他字段，没有限制，比如uid这些
select date_format(submit_time,'%Y%m'),
round(count(distinct uid,day(submit_time)) / count(distinct uid),2),count(distinct uid)
from exam_record
where year(submit_time)=2021
group by date_format(submit_time,'%Y%m')
```





## undone

[月总刷题数和日均刷题数_牛客题霸_牛客网 (nowcoder.com)](https://www.nowcoder.com/practice/f6b4770f453d4163acc419e3d19e6746?tpId=240&tags=&title=&difficulty=0&judgeStatus=0&rp=0)



## sql_mode问题

this is incompatible with sql_mode=only_full_group_by

mysql版本过高，如果用了group by，select的结果要么是group by的分组字段，要么是聚合函数。如果有别的字段，就会报这个错误。

比较好的解决方法是在其他字段外面套上ANY_VALUE()函数。

该函数会选择被分到同一组的数据里第一条数据的指定列值作为返回数据。

[(51条消息) MySQL错误-this is incompatible with sql_mode=only_full_group_by完美解决方案_Java修炼记-CSDN博客](https://blog.csdn.net/u012660464/article/details/113977173)



## in

1. create user 'root'@'%' identified by '你自己的mysql密码'



## self function

# 函数

## date_add/date_sub

date_add(date,interval)

```mysql
mysql> SELECT DATE_ADD('2018-05-01',INTERVAL 1 DAY);
        -> '2018-05-02'
mysql> SELECT DATE_SUB('2018-05-01',INTERVAL 1 YEAR);
        -> '2017-05-01'
mysql> SELECT DATE_ADD('2020-12-31 23:59:59',
    ->                 INTERVAL 1 SECOND);
        -> '2021-01-01 00:00:00'
mysql> SELECT DATE_ADD('2018-12-31 23:59:59',
    ->                 INTERVAL 1 DAY);
        -> '2019-01-01 23:59:59'
mysql> SELECT DATE_ADD('2100-12-31 23:59:59',
    ->                 INTERVAL '1:1' MINUTE_SECOND);
        -> '2101-01-01 00:01:00'
mysql> SELECT DATE_SUB('2025-01-01 00:00:00',
    ->                 INTERVAL '1 1:1:1' DAY_SECOND);
        -> '2024-12-30 22:58:59'
mysql> SELECT DATE_ADD('1900-01-01 00:00:00',
    ->                 INTERVAL '-1 10' DAY_HOUR);
        -> '1899-12-30 14:00:00'
mysql> SELECT DATE_SUB('1998-01-02', INTERVAL 31 DAY);
        -> '1997-12-02'
mysql> SELECT DATE_ADD('1992-12-31 23:59:59.000002',
    ->            INTERVAL '1.999999' SECOND_MICROSECOND);
        -> '1993-01-01 00:00:01.000001'
```



## substring_index

substring_index(string,delimiter,index)

- 注意不是像python那样，分割，然后取第n个

![image-20220214173513188](https://raw.githubusercontent.com/whr819987540/pic/main/image-20220214173513188.png)



![image-20220214195734260](https://raw.githubusercontent.com/whr819987540/pic/main/image-20220214195734260.png)



![image-20220214195802018](https://raw.githubusercontent.com/whr819987540/pic/main/image-20220214195802018.png)



使用两次，获得年龄字段

![image-20220214195830733](https://raw.githubusercontent.com/whr819987540/pic/main/image-20220214195830733.png)



## 子句的顺序

```bash
(8) 	SELECT (9) DISTINCT<select_list>
(1) 	FROM <left_table>
(3) 	<join_type> JOIN <right_table>
(2) 	ON <join_condition>
(4) 	WHERE <where_condition>
(5) 	GROUP BY <group_by_list>
(6) 	WITH {CUBE|ROLLUP}
(7) 	HAVING <having_condition>
(10)	ORDER BY <order_by_list>
(11)	LIMIT <offset,limit_number>
```



## sum(if)

`sum(if(condition,a,b))`

如果满足条件，则+a，否则+b

- ![image-20220214211057262](https://raw.githubusercontent.com/whr819987540/pic/main/image-20220214211057262.png)


- ![image-20220214211114205](https://raw.githubusercontent.com/whr819987540/pic/main/image-20220214211114205.png)


- ![image-20220214211141049](https://raw.githubusercontent.com/whr819987540/pic/main/image-20220214211141049.png)



## count(if)

count(if(condition,true,null))

如果条件成立，则计数。

[浙大不同难度题目的正确率_牛客题霸_牛客网 (nowcoder.com)](https://www.nowcoder.com/practice/d8a4f7b1ded04948b5435a45f03ead8c?tpId=199&tags=&title=&difficulty=0&judgeStatus=0&rp=0)

![image-20220214213922742](https://raw.githubusercontent.com/whr819987540/pic/main/image-20220214213922742.png)



## date_format

将date格式的数据转为合适的格式

| format | meaning                                                      |
| ------ | ------------------------------------------------------------ |
| `%Y`   | Year, numeric, four digits                                   |
|        |                                                              |
| `%m`   | Month, numeric (`00`..`12`)                                  |
|        |                                                              |
| `%D`   | Day of the month with English suffix (`0th`, `1st`, `2nd`, `3rd`, …) |
| `%d`   | Day of the month, numeric (`00`..`31`)                       |
| `%e`   | Day of the month, numeric (`0`..`31`)                        |
|        |                                                              |
| `%H`   | Hour (`00`..`23`)                                            |
|        |                                                              |
| `%i`   | Minutes, numeric (`00`..`59`)                                |
|        |                                                              |
| `%s`   | Seconds (`00`..`59`)                                         |

![image-20220214214152491](https://raw.githubusercontent.com/whr819987540/pic/main/image-20220214214152491.png)



```mysql
# 匹配2021-08这个日期的写法

select count(distinct device_id) as did_cnt,count(id) as question_cnt
from question_practice_detail
where DATE_FORMAT(date,'%Y-%m')='2021-08'
# where date like '2021-08%'
# where year(date)=2021 and month(date)=8
```



## datetime相减,interval n unit 、timestampdiff(inverval_unit,start,end)

- datetime相减并不会直接得到秒
  - ![image-20220215094822897](https://raw.githubusercontent.com/whr819987540/pic/main/image-20220215094822897.png)
  - ![image-20220215094842596](https://raw.githubusercontent.com/whr819987540/pic/main/image-20220215094842596.png)

- 用interval来量化
  - ![image-20220215100008939](https://raw.githubusercontent.com/whr819987540/pic/main/image-20220215100008939.png)
  - 注意不要写成`submit_time-start_time<interval 6 minute`
- 用`timestampdiff(inverval_unit,start,end)`
  - 注意是start在前，end在后
  - ![image-20220215100458213](https://raw.githubusercontent.com/whr819987540/pic/main/image-20220215100458213.png)



## lastday

获取某个timestamp所在月的最后一天

```mysql
mysql> select now();
+---------------------+
| now()               |
+---------------------+
| 2022-02-15 16:38:12 |
+---------------------+

mysql> select last_day(now());
+-----------------+
| last_day(now()) |
+-----------------+
| 2022-02-28      |
+-----------------+

mysql> select day(last_day(now()));
+----------------------+
| day(last_day(now())) |
+----------------------+
|                   28 |
+----------------------+
```

