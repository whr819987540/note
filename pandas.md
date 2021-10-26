# 读取数据

## 纯文本

- csv，comma separated values。
  - 一行，用逗号分割出各个字段；行之间，用换行符分割。
  - 表头可以有，可以没有。如果有，可以指定，也可以使用文件中的表头；如果没有，默认使用第一行（这样当然不行），需要自己制定

```python
import pandas as pd
csv_path='datas/ml-latest-small/links.csv'
df=pd.read_csv(csv_path)
print(df.head())
```



- tsv，tab separated values
  - 用tab键分割
- txt，自定义的分隔符
  - 在读入的时候需要告诉程序，具体使用了什么分隔符

```python
import pandas as pd
txt_path='datas/crazyant/access_pvuv.txt'
# 文本文件中以tab(看起来及其像空格)进行分割，没有表头
with open(txt_path,'r') as f:
    print(f.read())
2019-09-10  139	92
2019-09-09	185	153
2019-09-08	123	59
2019-09-07	65	40
2019-09-06	157	98
2019-09-05	205	151
2019-09-04	196	167
2019-09-03	216	176
2019-09-02	227	148
2019-09-01	105	61
df=pd.read_csv(txt_path,sep='\t')
print(df)
   2019-09-10  139   92
0  2019-09-09  185  153
1  2019-09-08  123   59
2  2019-09-07   65   40
3  2019-09-06  157   98
4  2019-09-05  205  151
5  2019-09-04  196  167
6  2019-09-03  216  176
7  2019-09-02  227  148
8  2019-09-01  105   61
# 这个结果很奇怪，为什么呢？因为pandas将第一行视为表头，但其实不是这样
df=pd.read_csv(txt_path,sep='\t',header=None,names=['year','a','b'])
print(df)
         year    a    b
0  2019-09-10  139   92
1  2019-09-09  185  153
2  2019-09-08  123   59
3  2019-09-07   65   40
4  2019-09-06  157   98
5  2019-09-05  205  151
6  2019-09-04  196  167
7  2019-09-03  216  176
8  2019-09-02  227  148
9  2019-09-01  105   61
# 这里header=None告诉pandas，没有表头；names告诉pandas用这个列表的值作为表头

```



## excel

- xlsx，xls

和csv差不多，因为分割符不需要指定



## mysql

连接到数据库，执行一个查询语句，将查询结果作为读入的值

```python
import pandas
import pandas as pd,pymysql
connect=pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    db='pramet'
)
df=pandas.read_sql('select *from pm_cmp',con=connect)
print(df.head())
   cmp_id         cmp_name cmp_short_name
0  000001       平安银行股份有限公司           平安银行
1  000002       万科企业股份有限公司            万科A
2  000004   深圳国华网安科技股份有限公司           国华网安
3  000005     深圳世纪星源股份有限公司           ST星源
4  000006  深圳市振业(集团)股份有限公司           深振业A
```





## 查看数据

### DateFrame

#### df.head()

查看前几行（默认是5），返回值仍然是DataFrame类型的二维表

```python
import pandas as pd
csv_path='datas/ml-latest-small/links.csv'
df=pd.read_csv(csv_path)
print(df.head())
   movieId  imdbId   tmdbId
0        1  114709    862.0
1        2  113497   8844.0
2        3  113228  15602.0
3        4  114885  31357.0
4        5  113041  11862.0
print(df.head(3))
   movieId  imdbId   tmdbId
0        1  114709    862.0
1        2  113497   8844.0
2        3  113228  15602.0
print(type(df.head()))
<class 'pandas.core.frame.DataFrame'>
```



#### df.shape

返回一个元组，第一个参数是行数，第二个参数是列数

```python
print(df.shape)
print(f"rows: {df.shape[0]}")
print(f"columns: {df.shape[1]}")
(9742, 3)
rows: 9742
columns: 3
```



#### df.columns

返回一个列表，可以遍历，可以下标访问

```python
print(type(df.columns))
print(df.columns)
print(df.columns[-1])
for i in df.columns:
    print(i)
<class 'pandas.core.indexes.base.Index'>
Index(['movieId', 'imdbId', 'tmdbId'], dtype='object')
tmdbId
movieId
imdbId
tmdbId
```



#### df.index

返回一个range，有start，stop，step。当然index也可能不是数值类型，但都可以用for类进行遍历，都可以通过下标进行访问

```python
print(type(df.index))
print(df.index)
print(df.index[0])
print(df.index[-1])
for i in df.index:
    print(i)
<class 'pandas.core.indexes.range.RangeIndex'>
RangeIndex(start=0, stop=9742, step=1)
0
9741

0
1
2
---
9741
```



#### df.dtypes

返回列对应的数据类型。index是之前的列名，值为列的数据类型，由于只有一列，所以是一维数组，series。可以通过下标进行访问。如果是同一个下标，返回类型，不需要建立映射关系；如果是多个下标，返回类型的serie。

```python
print(type(df.dtypes))
<class 'pandas.core.series.Series'>

print(df.dtypes)
movieId      int64
imdbId       int64
tmdbId     float64
dtype: object
    
print(df.dtypes[df.columns[0]])
int64

print(df.dtypes[[df.columns[0],df.columns[1]]])
movieId    int64
imdbId     int64
dtype: object
```



#### df.loc

##### 获取一行

输入某一行的index，返回Series，如果不存在，会报错

```python
df = pd.DataFrame(data,index=['a','b','c','d','e'])
print(df)
#     state  year  pop
# a    Ohio  2000  1.5
# b    Ohio  2001  1.7
# c    Ohio  2002  3.6
# d  Nevada  2001  2.4
# e  Nevada  2002  2.9
print(type(df.loc['a']))
# <class 'pandas.core.series.Series'>
print(df.loc['a'])
# state    Ohio
# year     2000
# pop       1.5
# Name: a, dtype: object
print(df.loc['a'].values)
# ['Ohio' 2000 1.5]
```



##### 获取多行

输入多个index，返回DateFrame。相当于对原来的DateFrame截取了某些行

```python
print(type(df.loc[['a','b']]))
# <class 'pandas.core.frame.DataFrame'>
print(df.loc[['a','b']])
#   state  year  pop
# a  Ohio  2000  1.5
# b  Ohio  2001  1.7
```



#### df.iloc

##### 获取一行

根据第几行（从0开始）获取数据，输出为Series

```python
print(type(df.iloc[0]))
# <class 'pandas.core.series.Series'>
print(df.iloc[0])
# state    Ohio
# year     2000
# pop       1.5
print(df.iloc[-1])
# state    Nevada
# year       2002
# pop         2.9
```



##### 获取多行

可以指定是第几行，也可以用切片，获得连续的行。返回值为DateFrame

```python
print(df.iloc[[0,-1]])
#     state  year  pop
# a    Ohio  2000  1.5
# e  Nevada  2002  2.9
print(df.iloc[:3])
#   state  year  pop
# a  Ohio  2000  1.5
# b  Ohio  2001  1.7
# c  Ohio  2002  3.6
```





### Series

#### sr.index

返回一维数组的索引，默认是range，start=0，step=1

```python
print(type(data.index))
print(data.index)
<class 'pandas.core.indexes.range.RangeIndex'>
RangeIndex(start=0, stop=4, step=1)
```

#### sr.values

返回所有的值，类型是一个列表，可以遍历，可以用下标进行访问

```python
print(type(data.values))
print(data.values)
for value in data.values:
    print(value)
<class 'numpy.ndarray'>
[1 'a' 5.2 7]
1
a
5.2
7
```



# 数据类型

## Series

series是一维数组，包括index和value，类似于字典格式的key和values。

value的类型不必相同，甚至index的类型也不必相同。

### 创建

#### 基于列表

##### 不指定index

如果不指定index，默认是start=0,step=1

```python
import pandas as pd
data=pd.Series([1,'a',5.2,7])
print(type(data))
print(data)
<class 'pandas.core.series.Series'>
0      1
1      a
2    5.2
3      7
dtype: object
```



##### 指定index

```python
sr=pd.Series(values,index=['a','b','c','d'])
print(sr)
a      1
b      a
c    5.2
d      7
dtype: object
    
sr=pd.Series(values,index=list(range(1,len(values)+1)))
print(sr)
1      1
2      a
3    5.2
4      7
dtype: object
```



#### 基于字典

映射关系为字典的key,value,分别映射为Series的index，value

```python
values={'rge':24,'ewf':11.2,'weg':'gwe'}
sr=pd.Series(values)
print(sr)
print(sr.index)
print(sr.values)

rge      24
ewf    11.2
weg     gwe
dtype: object
Index(['rge', 'ewf', 'weg'], dtype='object')
[24 11.2 'gwe']
```



### 查询

查询都是根据index来查询，如果只有一个index，直接返回值（如果没有这个index，返回）；如果有多个index，返回的仍然是Series

#### 一个index

```python
# index存在
print("sr['rge']:"+str(sr['rge']))
# sr['rge']:24
    
# index不存在,直接用下标访问会引起异常

```



#### 多个index

sr[[index_1,index_2]]

```python
new_sr=sr[[sr.index[0],sr.index[-1]]]
print(type(new_sr))
print(new_sr)
<class 'pandas.core.series.Series'>
rge     24
weg    gwe
dtype: object
```



## DateFrame

相比于Series，DateFrame只是多个列公用一个index，然后给每个列加上一个名字作为标识。

### 创建

可以从文件创建，也可以利用多个字典创建

#### 基于多个字典

```python
import pandas as pd
data={
        'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],
        'year':[2000,2001,2002,2001,2002],
        'pop':[1.5,1.7,3.6,2.4,2.9]
    }
df = pd.DataFrame(data)
print(df)
    state  year  pop
0    Ohio  2000  1.5
1    Ohio  2001  1.7
2    Ohio  2002  3.6
3  Nevada  2001  2.4
4  Nevada  2002  2.9
```



### 查询

#### 列

##### 一列

结果是Series，Series的index和之前DateFrame的index一样，没有发生变化，只是截取了一列。

```python
import pandas as pd
data={
        'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],
        'year':[2000,2001,2002,2001,2002],
        'pop':[1.5,1.7,3.6,2.4,2.9]
    }
df = pd.DataFrame(data,index=list(range(1,len(data['pop'])+1)))
print(df)
    state  year  pop
1    Ohio  2000  1.5
2    Ohio  2001  1.7
3    Ohio  2002  3.6
4  Nevada  2001  2.4
5  Nevada  2002  2.9

print(type(df['year']))
<class 'pandas.core.series.Series'>
print(df['year'])
1    2000
2    2001
3    2002
4    2001
5    2002
Name: year, dtype: int64
```



##### 多列

结果是DataFrame，index同样没有发生变化

```python
print(df)
	state  year  pop
1    Ohio  2000  1.5
2    Ohio  2001  1.7
3    Ohio  2002  3.6
4  Nevada  2001  2.4
5  Nevada  2002  2.9
print(type(df[[df.columns[0],df.columns[1]]]))
print(df[[df.columns[0],df.columns[1]]])
<class 'pandas.core.frame.DataFrame'>
    state  year
1    Ohio  2000
2    Ohio  2001
3    Ohio  2002
4  Nevada  2001
5  Nevada  2002
```



#### 行

##### 一行

loc,iloc

##### 多行

loc,iloc