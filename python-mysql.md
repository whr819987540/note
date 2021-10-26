

环境：

win10、mysql、sqlyog、python3

# 安装pymysql库

`pip install pymysql`



# 连接本地数据库

## 建立本地数据库

首先打开数据库服务`net start mysql`

登录`mysql -u root -p`

建表

```mysql
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
```

![image-20210530200904072](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210530200904072.png)



![image-20210530200906957](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210530200906957.png)



![image-20210530200920663](https://gitee.com/hit_whr/pic_3.0/raw/master/img/image-20210530200920663.png)



## 代码

### 连接数据库

```python
host 本机为localhost，服务器就是IP地址
port 端口号，默认为3306，所以可以不指定
user 要登录的用户名
passwd 密码
database 要连接DBMS的数据库
charset 字符集 utf8
read_default_file 读取配置文件
cursorclass 游标的类型
autocommit 自动提交，默认为false，主要是更新的时候用
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 如果发生错误则回滚
   db.rollback()
```



下面是官方文档的一个示例。

with的作用就是在代码块结束后，自动释放在此分配的所有资源。比如打开文件的时候with open就是关闭文件，释放文件的句柄。

这里就是close连接，或者close游标。

`connect=pymysql.connect()`

`cursor=connect.cursor(cursor=type)`

type下述的四种类型

sql语句写成字符串的类型，可以是单引号，双引号，三引号。参数可以用格式控制符代替，在执行的时候一起作为参数传进去，成为动态的查询语句。

定义游标后，执行查询，返回Number of affected rows。

`cursor.execute(sql,(parameter))`

然后就可以通过游标获得查询的结果

`result=cursor.fetchall()` 列表，返回的所有结果

`res=cursor.fetchone()` 返回一条记录，如果有

`res=cursor.fetchmany(size=num)` 最多返回num条记录

```python
import pymysql
connect=pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='code',
    #建议还是不要在连接里面指定cursor的类型，要生成cursor对象的时候再指定比较好，因为可能不是要一种cursor
    #cursorclass=pymysql.cursors.DictCursor,
    charset='utf8',
)
with connect:
    with connect.cursor() as cursor:
        sql='select `sname` from `s` where `sdept`=%s'
        sdept='IS'
        print(cursor.execute(sql,(sdept)))
        print(type(cursor))
        for i in cursor:
            print(i)
            print("-------")
    #cursor.close()
#connect.close()
3
<class 'pymysql.cursors.DictCursor'>
{'sname': '李勇'}
-------
{'sname': '刘晨'}
-------
{'sname': '刘朋'}
-------
```

如果是SSDictCursor，因为每次只拿一个数据，所以提前是不知道execute返回的值，也就是查询结果的行数。

```python
with connect:
    with connect.cursor(cursor=pymysql.cursors.SSDictCursor) as cursor:
        sql='select `sname` from `s` where `sdept`=%s'
        sdept='IS'
        print(cursor.execute(sql,(sdept)))
        print(type(cursor))
        for i in cursor:
            print(i)
            print("-------")
        sql='show tables'
        cursor.execute(sql)
        #print(cursor.fetchall())
        for i in cursor:
            print(i)
18446744073709551615
<class 'pymysql.cursors.SSDictCursor'>
{'sname': '李勇'}
-------
{'sname': '刘晨'}
-------
{'sname': '刘朋'}
-------
{'Tables_in_code': 'c'}
{'Tables_in_code': 's'}
{'Tables_in_code': 'sc'}
```





### 游标

#### Cursor



#### DictCursor



#### SSCursor



Unbuffered Cursor, mainly useful for queries that return a lot of data, or for connections to remote servers over a slow network.

非缓存的游标，主要用于查询的结果非常多或者是网速非常慢。

先看看buffer是啥意思，buffer就是说，一次性从server那里得到所有的data，并加载到内存中，用的时候就是对list进行遍历，好处是本地可以拿到所有的数据，坏处有两个：一是对内存的压力，二是如果网速比较慢且数据量比较大，那么程序会在这里停留很长的时间。

所以这里的非缓存就可以边拿数据边处理，而不用等待所有数据都拿回来。

Instead of copying every row of data into a buffer, this will fetch rows as needed. The upside of this is the client uses much less memory, and rows are returned much faster when traveling over a slow network or if the result set is very big.

There are limitations, though. The MySQL protocol doesn’t support returning the total number of rows, so the only way to tell how many rows there are is to iterate over every row returned. Also, it currently isn’t possible to scroll backwards, as only the current row is held in memory.

也有弊端：一是不知道查询结果一共有多少行，除非把所有的行都拿回来并计数。并且，不能回滚，因为没往内存里面加载，只能用当前拿回来的，之前的不见了。

另外，SSCursor 是没有缓存的游标,结果集只要没取完，这个 conn 是不能再处理别的 sql，包括另外生成一个 cursor 也不行的。如果需要干别的，请另外再生成一个连接对象。

每次读取后处理数据要快，不能超过 60 s，否则 mysql 将会断开这次连接，也可以修改 SET NET_WRITE_TIMEOUT = xx 来增加超时间隔。



基于上述特点，游标本身就是一个iterator，可以直接迭代，没有必要逐个fetchone了。数据量比较大的时候更没必要fetchall了。



#### DictSSCursor



### 使用查询结果



### 查询状态信息

```python
import pymysql
connect=pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='code',
    charset='utf8',
)
with connect:
    with connect.cursor(cursor=pymysql.cursors.SSDictCursor) as cursor:
        sql='select `sname` from `s` where `sdept`=%s'
        sdept='IS'
        #cursor.execute()的返回值是收到影响的记录数目。前提是cursor是缓存的
        print(cursor.execute(sql,(sdept)))
        print(type(cursor))
        #如果cursor是ss的，直接迭代
        for i in cursor:
            print(i)
            print("-------")
        #查询状态信息
        sql='show tables'
        cursor.execute(sql)
        for i in cursor:
            print(i)
        #也可以fetch，这里的fetchmany还可以指定返回的记录的条数
        #由于这里是ss，不可回滚
        sql='describe `c`'
        cursor.execute(sql)
        print(cursor.fetchone())
        print(cursor.fetchmany(size=3))
    #cursor.close()
#connect.close()
3
<class 'pymysql.cursors.DictCursor'>
{'sname': '李勇'}
-------
{'sname': '刘晨'}
-------
{'sname': '刘朋'}
-------
{'Tables_in_code': 'c'}
{'Tables_in_code': 's'}
{'Tables_in_code': 'sc'}
{'Field': 'cno', 'Type': 'int(2)', 'Null': 'NO', 'Key': 'PRI', 'Default': None, 'Extra': ''}
[{'Field': 'cname', 'Type': 'varchar(20)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}, {'Field': 'cpno', 'Type': 'int(2)', 'Null': 'YES', 'Key': 'MUL', 'Default': None, 'Extra': ''}, {'Field': 'ccredit', 'Type': 'int(2)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}]
```



### update

注意要`connect.commit()`



### insert

也要`connect.commit()`否则修改不会提交到数据库里面

插入记录

```python
with connect:
    with connect.cursor(cursor=pymysql.cursors.SSDictCursor) as cursor:
        #插入
        sql='select *from s'
        cursor.execute(sql)
        for i in cursor:
            print(i)
        sql="""
            insert into `s`(sclass,sno,sname,ssex,sage,sdept)
            values
            (1,4,'陈刚','男',19,'IS'),
            (2,4,'刘成','男',21,'IE')
        """
        print(cursor.execute(sql))
{'sclass': 1, 'sno': 1, 'sname': '李勇', 'ssex': '男', 'sage': 20, 'sdept': 'IS'}
{'sclass': 1, 'sno': 2, 'sname': '刘晨', 'ssex': '女', 'sage': 19, 'sdept': 'IS'}
{'sclass': 1, 'sno': 3, 'sname': '刘朋', 'ssex': '男', 'sage': 20, 'sdept': 'IS'}
{'sclass': 2, 'sno': 1, 'sname': '王敏', 'ssex': '女', 'sage': 18, 'sdept': 'MA'}
{'sclass': 2, 'sno': 2, 'sname': '张锋', 'ssex': '男', 'sage': 19, 'sdept': 'MA'}
{'sclass': 2, 'sno': 3, 'sname': '李敏', 'ssex': '男', 'sage': 20, 'sdept': 'MA'}
2
```

返回的结果数为2，是插入成功了。

但是再次查询时，没有看到insert的记录。

```python
{'sclass': 1, 'sno': 1, 'sname': '李勇', 'ssex': '男', 'sage': 20, 'sdept': 'IS'}
{'sclass': 1, 'sno': 2, 'sname': '刘晨', 'ssex': '女', 'sage': 19, 'sdept': 'IS'}
{'sclass': 1, 'sno': 3, 'sname': '刘朋', 'ssex': '男', 'sage': 20, 'sdept': 'IS'}
{'sclass': 2, 'sno': 1, 'sname': '王敏', 'ssex': '女', 'sage': 18, 'sdept': 'MA'}
{'sclass': 2, 'sno': 2, 'sname': '张锋', 'ssex': '男', 'sage': 19, 'sdept': 'MA'}
{'sclass': 2, 'sno': 3, 'sname': '李敏', 'ssex': '男', 'sage': 20, 'sdept': 'MA'}
```

因为没有commit

```python
with connect:
    with connect.cursor(cursor=pymysql.cursors.SSDictCursor) as cursor:
        #插入
        sql='select *from s'
        cursor.execute(sql)
        for i in cursor:
            print(i)
        sql="""
            insert into `s`(sclass,sno,sname,ssex,sage,sdept)
            values
            (1,4,'陈刚','男',19,'IS'),
            (2,4,'刘成','男',21,'IE')
        """
        print(cursor.execute(sql))
        connect.commit()
{'sclass': 1, 'sno': 1, 'sname': '李勇', 'ssex': '男', 'sage': 20, 'sdept': 'IS'}
{'sclass': 1, 'sno': 2, 'sname': '刘晨', 'ssex': '女', 'sage': 19, 'sdept': 'IS'}
{'sclass': 1, 'sno': 3, 'sname': '刘朋', 'ssex': '男', 'sage': 20, 'sdept': 'IS'}
{'sclass': 2, 'sno': 1, 'sname': '王敏', 'ssex': '女', 'sage': 18, 'sdept': 'MA'}
{'sclass': 2, 'sno': 2, 'sname': '张锋', 'ssex': '男', 'sage': 19, 'sdept': 'MA'}
{'sclass': 2, 'sno': 3, 'sname': '李敏', 'ssex': '男', 'sage': 20, 'sdept': 'MA'}
2
```

再次查询结果

```python
with connect:
    with connect.cursor(cursor=pymysql.cursors.SSDictCursor) as cursor:
        #插入
        sql='select *from s'
        cursor.execute(sql)
        for i in cursor:
            print(i)
 {'sclass': 1, 'sno': 1, 'sname': '李勇', 'ssex': '男', 'sage': 20, 'sdept': 'IS'}
{'sclass': 1, 'sno': 2, 'sname': '刘晨', 'ssex': '女', 'sage': 19, 'sdept': 'IS'}
{'sclass': 1, 'sno': 3, 'sname': '刘朋', 'ssex': '男', 'sage': 20, 'sdept': 'IS'}
{'sclass': 1, 'sno': 4, 'sname': '陈刚', 'ssex': '男', 'sage': 19, 'sdept': 'IS'}
{'sclass': 2, 'sno': 1, 'sname': '王敏', 'ssex': '女', 'sage': 18, 'sdept': 'MA'}
{'sclass': 2, 'sno': 2, 'sname': '张锋', 'ssex': '男', 'sage': 19, 'sdept': 'MA'}
{'sclass': 2, 'sno': 3, 'sname': '李敏', 'ssex': '男', 'sage': 20, 'sdept': 'MA'}
{'sclass': 2, 'sno': 4, 'sname': '刘成', 'ssex': '男', 'sage': 21, 'sdept': 'IE'}
```

发现记录已经进去了。

有时候动态sql可能出问题，这样解决

```python
with connect:
    with connect.cursor(cursor=pymysql.cursors.Cursor)as cursor:
        target='s'
        sql='select * from %s'
        cursor.execute(sql %(target))
        res=cursor.fetchall()
        print(res)
```



这个里面还有字符串，所以显示的结果是select * from s where saddr=威海

而saddr的类型是varchar，威海这个组汉字必须用引号包起来

![image-20210614112730316](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210614112730316.png)



![image-20210614112853809](https://gitee.com/hit_whr/pic_3.0/raw/master/img/image-20210614112853809.png)



在模糊匹配中，要用到这种形式的sql

`select * from s where name like '%mysql%'`

用两个%%表示%

![image-20210614113841436](https://gitee.com/hit_whr/pic_3.0/raw/master/img/image-20210614113841436.png)



![image-20210614113932605](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210614113932605.png)





还有个问题就是，怎么知道插入是否成功？

需要用到try，except，因为如果插入不成功，比如类型不匹配，values的字段不匹配，主键冲突，外键没找到等等，反正没有插入成功，就会有报错。

主键冲突

`pymysql.err.IntegrityError: (1062, "Duplicate entry '1-4' for key 'PRIMARY'")`

类型不匹配

`pymysql.err.DataError: (1366, "Incorrect integer value: 'r' for column 'sno' at row 1")`

try except帮忙确定错误

```python
with connect:
    with connect.cursor(cursor=pymysql.cursors.SSDictCursor) as cursor:
        #插入
        sql='select *from s'
        cursor.execute(sql)
        for i in cursor:
            print(i)
        sql="""
            insert into `s`(sclass,sno,sname,ssex,sage,sdept)
            values
            (1,4,'陈刚','男',19,'IS'),
            (2,4,'刘成','男',21,'IE')
        """
        try:
            print(cursor.execute(sql))
        except:
            print('error')
        connect.commit()
{'sclass': 1, 'sno': 1, 'sname': '李勇', 'ssex': '男', 'sage': 20, 'sdept': 'IS'}
{'sclass': 1, 'sno': 2, 'sname': '刘晨', 'ssex': '女', 'sage': 19, 'sdept': 'IS'}
{'sclass': 1, 'sno': 3, 'sname': '刘朋', 'ssex': '男', 'sage': 20, 'sdept': 'IS'}
{'sclass': 1, 'sno': 4, 'sname': '陈刚', 'ssex': '男', 'sage': 19, 'sdept': 'IS'}
{'sclass': 2, 'sno': 1, 'sname': '王敏', 'ssex': '女', 'sage': 18, 'sdept': 'MA'}
{'sclass': 2, 'sno': 2, 'sname': '张锋', 'ssex': '男', 'sage': 19, 'sdept': 'MA'}
{'sclass': 2, 'sno': 3, 'sname': '李敏', 'ssex': '男', 'sage': 20, 'sdept': 'MA'}
{'sclass': 2, 'sno': 4, 'sname': '刘成', 'ssex': '男', 'sage': 21, 'sdept': 'IE'}
error
```



更精细一点，还可以根据报错类型，进行更精确的相应操作。



### delete



### 关闭游标

`cursor.close()`

### 断开连接

`connect.close()`

# 连接服务器的数据库



# GUI

设计思路是先写cmd的后台，测试正确后，编写UI。

编写UI的时候，可以直接用qt designer进行拖拽，搭建一个大体的框架，好处是所见即所得。

然后用

`pyioc5 -o ui.py name.ui`

直接生成ui界面

关于生成的这个ui.py，以类封装了整个界面的代码，我们只需要关心逻辑即可。

逻辑就是信号和槽。这个可以在designer中用槽编辑器编写，也可以自己编写。用编辑器编写的好处是选定发送方接收方后，能够用的信号就出来了。

有了这些后，就可以编写处理数据的槽函数了。

![image-20210614160957379](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210614160957379.png)



![image-20210614161008405](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210614161008405.png)

入口函数

```python
    app=QApplication(sys.argv)
    MainWindow=QMainWindow()
    ui=Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
```

```python
def vague_process(self):
    sql=self.vague_sql
    #获取要查询的地址
    addr=self.result.text()
    self.listWidget.clear()
    #打开游标并查询
    #判断查询到的结果是否为空
    if(self.cursor.execute(sql %(addr))):
        res=self.cursor.fetchall()
        for i in res:
            string=""
            for a in i:
                string+=" - "+str(a)
                self.listWidget.addItem(string)
                self.label_2.setText("找到了")
                else:
                    self.label_2.setText("没找到")
```



# 动态sql

判断是哪个表，然后写对应的sql

现在的关键是确定表的类型后，如何根据值有没有确定sql

因为很多值都不是必须的，如果挨个判断，很麻烦



# 事务

mysql里面要想使用事务，engine必须选inno-db。

在选定数据库后，用`show engine`命令查看所用的数据库。

基本流程

```mysql
begin [transaction]
xxx
条件判断
	rollback
	commit
```

基本操作

begin【开启事务】

![image-20210620104202810](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210620104202810.png)

进行插入操作

![image-20210620104223540](https://i.loli.net/2021/06/20/ZFd7a1xmfMN6jcT.png)

现在已经对数据库进行了修改

![image-20210620104313874](https://i.loli.net/2021/06/20/mAJ1VxBOjptUZC5.png)



如果回滚

![image-20210620104331508](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210620104331508.png)

再次查询时，不会看到之前的插入记录

![image-20210620104344442](https://i.loli.net/2021/06/20/If2lDHTz1NjZW4w.png)



