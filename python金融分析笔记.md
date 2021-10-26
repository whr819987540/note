机器学习

用来进行数据分析

# 分类

- 监督学习：将特征变量和目标变量一起作为数据集。

  训练好模型后，输入特征变量就可以得到目标变量。

  包括回归分析（连续值，如股价变化）和分类问题（离散值，如股价涨跌）

- 非监督学习：只有特征变量，目的是将特征变量进行分类或者降维

  包括数据聚类与分群（分类）、数据降维



# 软件准备

本机已经有python解释器了，看到anoconda内置的jupyter notebook用来调试和显示二维数组挺方便的，而且pycharm也支持自己选择解释器，anoconda内置了科学计算的库，所以安装一个anoconda

==记得在pycharm里面换一个解释器==

显示了两个解释器

![image-20210425215058932](https://gitee.com/hit_whr/pic_2.0/raw/master/20210425215059.png)



具体看看内容

一个是创建新项目时的解释器配置，一个是现在环境的解释器配置，make available是对所有之后的项目都默认一个解释器（不推荐）

![image-20210425215206430](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210425215206430.png)



# jupyter notebook

首先在anaconda的组件里面打开jupyter，会弹出一个cmd窗口，不要关闭

![image-20210425215534345](https://gitee.com/hit_whr/pic_2.0/raw/master/20210425215619.png)

然后默认浏览器弹出窗口

![image-20210425215615879](https://gitee.com/hit_whr/pic_2.0/raw/master/20210425215616.png)



默认进入的是c盘的文件夹，而且浏览器中不支持盘符的跳转，所以只能cmd进入某个文件夹，然后开启jupyter的服务

（jupyter的py文件是ipynb后缀）

`jupyter notebook命令`

![image-20210425222052740](https://gitee.com/hit_whr/pic_2.0/raw/master/20210425222052.png)

快捷键：enter+ctrl是运行本代码块；shift+enter是运行本代码块，然后转到下一个代码块

文件类型为ipynb

![image-20210425222132228](https://gitee.com/hit_whr/pic_2.0/raw/master/20210425222132.png)



可以在file->download as里导出为.py文件

# numpy

主要是一维数组（array）

python里面内置列表list

区别在于：

- list用,分隔，array用空格分隔

![image-20210425223704675](https://gitee.com/hit_whr/pic_2.0/raw/master/20210425224042.png)

- list只能放一维数据，array可以放多维数据

![image-20210425224134794](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210425224134794.png)

- 进行乘法运算的结果不同，list是进行复制，array是每个元素进行乘法运算

![image-20210425223942869](https://gitee.com/hit_whr/pic_2.0/raw/master/20210425223942.png)

相同点：

- 都可以用下标进行访问
- 都可以切片（左闭右开）

![image-20210425223857593](https://gitee.com/hit_whr/pic_2.0/raw/master/20210425223857.png)

## 创建array



### 利用list

b=np.array(list)



#### 一维

![image-20210425224238771](https://gitee.com/hit_whr/pic_2.0/raw/master/20210425224238.png)

#### 二维

![image-20210425224134794](https://gitee.com/hit_whr/pic_2.0/raw/master/20210425224255.png)

### 利用范围



#### 一维

b=np.arange(start,end,offset)

![image-20210425224509882](https://gitee.com/hit_whr/pic_2.0/raw/master/20210425224509.png)



#### 二维

b=np.arange(start,end,offset).reshape(rows,columns)

![image-20210425224652471](https://gitee.com/hit_whr/pic_2.0/raw/master/20210425224652.png)



### 利用随机数



#### 一维

b=no.random.randn(num)

创建num个符合正态分布的数，而且是array形式

![image-20210425224901288](https://gitee.com/hit_whr/pic_2.0/raw/master/20210425224901.png)



#### 二维

b=np.random.randint(start,end.(rows,columns))

同样是左闭右开

![image-20210425225027285](https://gitee.com/hit_whr/pic_2.0/raw/master/20210425225027.png)



# pandas

主要用来处理二维的数据

含有series和dataframe（二维）两种数据结构



## series

属于可以自定义索引值的列表



## dataframe

二维表格

### 用列表创建

a=pd.DataFrame(list)

![image-20210425225548304](https://gitee.com/hit_whr/pic_2.0/raw/master/20210425225548.png)



类似于sql，列索引用columns表示，行索引用index表示

下面对索引进行自定义，columns和index的值都可以用列表来指定，前提是满足数量关系

![image-20210425225804808](https://gitee.com/hit_whr/pic_2.0/raw/master/20210425225804.png)



还可以逐列进行创建，缺点是指定不了行索引

df[列名]=list

![image-20210425230055328](https://gitee.com/hit_whr/pic_2.0/raw/master/20210425230055.png)



### 用字典创建

![image-20210426180326103](https://gitee.com/hit_whr/pic_2.0/raw/master/20210426180326.png)



默认是将字典的key作为column，列的value作为列的值

也可以颠倒过来，将字典的key作为index，字典的value作为行的值

pd.dateframe.from_dict(dic,orient=‘index’)

![image-20210426180635836](https://gitee.com/hit_whr/pic_2.0/raw/master/20210426180635.png)



### 用二维数组创建

![image-20210426181155660](https://gitee.com/hit_whr/pic_2.0/raw/master/20210426181155.png)



### 转置

name(type dataframe).T

T是dataframe类型的一种属性，返回原二维表的转置结果



# 读取文件内容

前面都很无聊，不过是熟悉库的数据结构的过程

a=pd.read_excel(path,sheet_name=,encoding=‘utf-8’)中文内容的时候最好加上编码格式，文件称为工作簿，里面可能有多张表，类似database和table

sheet_name可以是字符串，也可是排序时的顺序，从0开始



还有csv文件，本质上是用，和换行符分隔的文本文件，“，”用来区分列，换行符区分行，不能存储格式信息，公式等，占用磁盘资源比较少。

a=pd.read_csv(path,delimiter=‘’)第二个参数是指定分隔符，默认为逗号，实际上文件内容里面很多都是逗号

![image-20210426183035860](https://gitee.com/hit_whr/pic_2.0/raw/master/20210426183035.png)

## 查看文件内容

可以直接打印，不过如果数据太多，也可以用上a.head(line_number)

![image-20210426183157244](https://gitee.com/hit_whr/pic_2.0/raw/master/20210426183157.png)



## 写入文件

dataframe.to_excel(path)

![image-20210426183612959](https://gitee.com/hit_whr/pic_2.0/raw/master/20210426183613.png)



## 读取指定行

data[start:end]

类似于切片操作，行索引从0开始

![image-20210426184438608](https://gitee.com/hit_whr/pic_2.0/raw/master/20210426184438.png)



指定某个索引值

data.iloc[[1,2]]

![image-20210426184804663](https://gitee.com/hit_whr/pic_2.0/raw/master/20210426184804.png)

## 读取指定列

直接data[column_name]，不包含列索引

![image-20210426183952464](https://gitee.com/hit_whr/pic_2.0/raw/master/20210426183952.png)



data[[column_name]]

![image-20210426184141489](https://gitee.com/hit_whr/pic_2.0/raw/master/20210426184141.png)



多列，同时看到这样返回的是DataFrame类型的

![image-20210426184229584](https://gitee.com/hit_whr/pic_2.0/raw/master/20210426184229.png)



## 读取矩形

data.iloc[start:end]\[[column1,column2]]

![image-20210426185138484](https://gitee.com/hit_whr/pic_2.0/raw/master/20210426185138.png)



data.loc【【rows】，【columns】】

![image-20210426194912537](https://gitee.com/hit_whr/pic_2.0/raw/master/20210426194912.png)



对于离散的值，iloc和loc都行

==共同点是，第一个【】内的是行索引，如果是多个值，要再用一个【】连接起来，切片本身的结果是列表，所以不同【】括起来；第二个【】内是列索引，一般用【】括起来里面的，因为是多个值==



![image-20210426195150874](https://gitee.com/hit_whr/pic_2.0/raw/master/20210426195150.png)



## 实战一下

有一个xlsx文件value.xlsx，里面只有一列（value，1,2,3,4），多行数据

有一个xlsx文件res.xlsx，里面有四列，分别为利好，利空，中性，未知

要求根据value的值对res进行填充，1,2,3,4分别对应利好，利空，中性，未知，对应时填充1。如果不是1-4，则不进行填充

先构造code文件，内容为

![image-20210426190103712](https://gitee.com/hit_whr/pic_2.0/raw/master/20210426190103.png)

res.xlsx为空

![image-20210426190146624](https://gitee.com/hit_whr/pic_2.0/raw/master/20210426190146.png)

现在进行读取和写入

```python
import numpy as np
import pandas as pd
value_file="value.xlsx"
res_file="res.xlsx"
values=pd.read_excel(value_file,encoding="utf-8")
    value
# 1       3
# 2       5
# 3       6
# 4       1
# 5       2
# 6       3
# 7       6
# 8       1
# 9       5
# 10      2
# 11      4
# 12      3
res=pd.read_excel(res_file,encoding="utf-8")
print(values)
#print(len(values)) 直接对dataframe进行len操作，返回行数
dic={}
# dic["利好"]=[]
# dic["利空"]=[]
# dic["中性"]=[]
# dic["未知"]=[]
#有点麻烦，先放进去，再做映射
for i in range(1,5):
    dic[i]=[]
print(dic)
{1: [], 2: [], 3: [], 4: []}
for i in range(len(values)):
    #print(values.iloc[i])根据i这个index返回对应的值
    #最好加上对应的列，因为这里只有一行，看不出来
    #print(values.iloc[i]['value'])
    tmp=values.iloc[i]['value']
    if tmp<=4 and tmp>=1:
        dic[tmp].append(1)
    #其他部分填充空值（np.nan）
    for j in range(1,5):
        if j!=tmp:
            dic[j].append(np.nan)
print(dic)

res=pd.DataFrame(dic)
names=["利好","利空","中性","未知"]
new_columns={}
for i in range(1,5):
    new_columns[i]=names[i-1]
print(new_columns)
res.rename(columns=new_columns,inplace=True)
print(res)
res.to_excel("res.xlsx")
```



总结一下：

- 获取dataframe的行数，用len函数
- 在对dataframe的columns进行改名时，用dataframe.rename(columns=,inplace=True)
  - 其中inplace参数必须要有
  - columns的参数是一个字典，key是原来的索引，value是新的索引
- 访问某一行dataframe.iloc[num]这个是从0开始的行索引
- 访问某一个单元格，dataframe.iloc[num] [column]访问num行，column列

重构后的代码

```python
import numpy as np
import pandas as pd
value_file="value.xlsx"
res_file="res.xlsx"
values=pd.read_excel(value_file,encoding="utf-8")
res=pd.read_excel(res_file,encoding="utf-8")
dic={}
for i in range(1,5):
    dic[i]=[]
for i in range(len(values)):
    tmp=values.iloc[i]['value']
    if tmp<=4 and tmp>=1:
        dic[tmp].append(1)
    for j in range(1,5):
        if j!=tmp:
            dic[j].append(np.nan)
res=pd.DataFrame(dic)
names=["利好","利空","中性","未知"]
new_columns={}
for i in range(1,5):
    new_columns[i]=names[i-1]
res.rename(columns=new_columns,inplace=True)
print(res)
res.to_excel("res.xlsx")
```

![image-20210426194442091](https://gitee.com/hit_whr/pic_2.0/raw/master/20210426194442.png)



# 内置函数

- data[column].value_counts()计数，column列出现过哪几个值，出现了几次

  ![image-20210426195814232](https://gitee.com/hit_whr/pic_2.0/raw/master/20210426195814.png)

- 排序函数。

  类似数据库，以什么进行排序，降序还是升序

  data.sort_values(by=column,ascending=)

  ![image-20210426200036596](https://gitee.com/hit_whr/pic_2.0/raw/master/20210426200036.png)

# 列运算

data[new_coumn]=f(data[column1],data[column2])

![image-20210426200241351](https://gitee.com/hit_whr/pic_2.0/raw/master/20210426200241.png)

# 删除

data.drop(index=[],columns=[],inplace=)

如果inplace为true，那么会在data上直接进行改动，否则会有一个返回值，相当于data本身并没有发生改变

index，columns指定删除的行和列的名称

![image-20210426200549665](https://gitee.com/hit_whr/pic_2.0/raw/master/20210426200549.png)



![image-20210426200628653](https://gitee.com/hit_whr/pic_2.0/raw/master/20210426200628.png)

# 连接

这和数据库就很像了

pd.merge(d1,d2,on,how)

on是根据什么来连接，和sql的on一样

how是连接方式，比如，left（left outer join），right（right outer join），inner（默认 inner join），outer（fully join）

假设有两个dataframe

![image-20210426201836836](https://gitee.com/hit_whr/pic_2.0/raw/master/20210426201836.png)

想把他们放在一起

- 要求每个公司都出现，需要分数和股价

  ![](https://gitee.com/hit_whr/pic_2.0/raw/master/20210426201956.png)

- 要求只有公司的分数和股价都不为空

  ![image-20210426202030247](https://gitee.com/hit_whr/pic_2.0/raw/master/20210426202030.png)

- 要求必须显示分数

  ![image-20210426202127319](https://gitee.com/hit_whr/pic_2.0/raw/master/20210426202127.png)

- 必须显示股价

  ![image-20210426202151169](https://gitee.com/hit_whr/pic_2.0/raw/master/20210426202151.png)





# 绘图

```python
import matplotlib.pyplot as plt
```

前面提到过，numpy的数组适合对里面的每一个元素进行算术运算，所以都用数组，而不用列表

![image-20210426203718279](https://gitee.com/hit_whr/pic_2.0/raw/master/20210426203718.png)



![image-20210426203832272](https://gitee.com/hit_whr/pic_2.0/raw/master/20210426203832.png)

直接进行算数运算，很简单

## 折线图plot

![image-20210426204018466](https://gitee.com/hit_whr/pic_2.0/raw/master/20210426204018.png)





## 柱形图bar



![image-20210426204255312](https://gitee.com/hit_whr/pic_2.0/raw/master/20210426204255.png)



## 散点图scatter

![image-20210426204508693](https://gitee.com/hit_whr/pic_2.0/raw/master/20210426204508.png)



## 直方图hist

np.random.rand(num)返回num个0-1之间的随机数

np.random.randn(num)返回num个符合==标准==正态分布的随机数

![image-20210426205008126](https://gitee.com/hit_whr/pic_2.0/raw/master/20210426205008.png)



重点看看bins参数

> If *bins* is an integer, it defines the number of equal-width bins in the range.
>
> If *bins* is a sequence, it defines the bin edges, including the left edge of the first bin and the right edge of the last bin; in this case, bins may be unequally spaced. All but the last (righthand-most) bin is half-open. 

就是说这个参数默认为10，也就是10个区间范围

指定一个整数，就对max，min进行n段的一个划分

指定一个序列，就是逐个划分

### 频数直方图

横轴为区间范围，纵轴为在此范围内出现的次数

![image-20210426205632852](https://gitee.com/hit_whr/pic_2.0/raw/master/20210426205632.png)

看到默认的区间数目效果不好，区间数增加当然划分越精细，但是不能和总的数据量过于接近

![image-20210426205729318](https://gitee.com/hit_whr/pic_2.0/raw/master/20210426205729.png)





## 饼图







## 散点图





## 用pandas

格式为dataframe[列名].plot(kind=‘图名’)

==同样需要plt.show()，因为pandas的绘图函数也是基于plt，否则不会进行显示==

比如

![image-20210426210546288](https://gitee.com/hit_whr/pic_2.0/raw/master/20210426210546.png)

![image-20210426210705338](https://gitee.com/hit_whr/pic_2.0/raw/master/20210426210705.png)



将一组数据用两种图表现，比较好

### 图形参数

| line | 折线图 |
| ---- | ------ |
| bar  | 柱形图 |
| hist | 直方图 |
| box  | 箱体图 |
| area | 面积图 |
| pie  | 饼图   |

![image-20210426211018531](https://gitee.com/hit_whr/pic_2.0/raw/master/20210426211018.png)



## 美化

这个板块需要在实战中不断总结

- color线条颜色，linewidth线条宽度，linestyle是线条的形态



# K线图

## 先看看中国的股票代码

有一个A股列表文件，不过这个xlsx没有行索引，所以需要进行一下转化（不如说是一个csv文件）

就是加上行索引

![image-20210426213707886](https://gitee.com/hit_whr/pic_2.0/raw/master/20210426213707.png)

类似这种东西，我们需要知道A股代码和A股简称的映射关系

```python
import tushare as ts
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
name2code=pd.read_excel("A股列表.xlsx")
columns=list(name2code.columns)
name=name2code['A股简称']
code=name2code['A股代码']
name_code,code_name={},{}
for i in range(len(name)):
    name_code[name[i]]=code[i]
    code_name[str(code[i]).zfill(6)]=name[i]
print(code_name['000002'])
```

建立名称到代码的两个一一映射关系



## 获取股票数据

tushare库，爬取中国股票的实时价格

> A utility for crawling historical and Real-time Quotes data of China stocks

```python
code='000001'
name=code_name[code]
data=ts.get_k_data(code,start='2021-01-01',end='2021-01-30')
print(data)
print(name)
```

第一个参数是股票代码，start，end是‘yyyy-mm-dd’格式的日期，返回这个时间段的价格，dataframe格式

![image-20210426221533061](https://gitee.com/hit_whr/pic_2.0/raw/master/20210426221533.png)

## 重置行索引

dataframe.set_index(column_name,inplace=True)

![image-20210426221706950](https://gitee.com/hit_whr/pic_2.0/raw/master/20210426221707.png)



## 绘图

index自然作为横坐标（这也是上面为什么要将index换成日期，ts返回的index是单纯的计数值，在图表上不具备实际意义）

这里选‘close’作为纵坐标

```python
data['close'].plot(kind='line')
plt.xticks(rotation=60)
plt.show()
```



```python
from datetime import datetime
date['date']=data['date'].apply(lamdba x:datetime.strptime(x,"%Y-%m-%d"))
```





## plt的中文编码

```python
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
```





# 译码实战

源文件是这样的

![image-20210427152614861](https://gitee.com/hit_whr/pic_2.0/raw/master/20210427152621.png)

特点：

- 没有规范的索引列（序号列虽然有123，但是index不能有名称）

  比如，我将序号作为索引，但是根据索引得到的结果是

  应该是和2007那一行的

  ![image-20210427153025765](https://gitee.com/hit_whr/pic_2.0/raw/master/20210427153025.png)

  

- 如果没有索引列，每次read_excel时，自动添加索引index

  ![image-20210427153201496](https://gitee.com/hit_whr/pic_2.0/raw/master/20210427154128.png)

- ==在访问某个单元格时，必须使用data.loc[index,column]的格式，否则不停报错==

  SettingWithCopyWarning: A value is trying to be set on a copy of a slice from a DataFrame

- 最后处理结束后，我们输出这个data，还是有index这一行，比较讨厌，需要去除

  ![image-20210427153419925](https://gitee.com/hit_whr/pic_2.0/raw/master/20210427153419.png)



​		在进行数据处理时，index帮助我们遍历，但是输出时我们不希望有这一列

​		可以在to_excel时，指定index=None

- 编码1234这一列是我们的辅助column，结果中需要去掉，所以用了drop，==drop可以是index，也可以是column，所以需要指明==，inplace是在不在原来的数据上进行操作
- 还有一个需要注意的是，我们虽然是对源文件进行处理，但是在输出的时候最好不要放到源文件里面，因为这样可能让我们的源数据丢失



最终的结果为这个，比较符合我们的预期

![image-20210427153926873](https://gitee.com/hit_whr/pic_2.0/raw/master/20210427153926.png)



```python
import pandas as pd
data=pd.read_excel("2.xlsx")
for i in range(len(data)):
    if data.loc[i,"编码1234"]==1:
        data.loc[i,"利好"]=1
    elif data.loc[i,"编码1234"]==2:
        data.loc[i,"利空"]=1
    elif data.loc[i,"编码1234"]==3:
        data.loc[i,"模糊中性"]=1
    elif data.loc[i,"编码1234"]==4:
        data.loc[i,"存在标题信息不足等问题"]=1
    else:
        print("第"+str(i+1)+"行有问题"+data[i])
data.drop(columns='编码1234',inplace=True)
data.to_excel('二组王浩然.xlsx',index=None)
```





再详细说说上面那个loc的问题

想改变pandas dataframe中某数值的方法，用 dfc[‘A’][0] = 12 明显错误
test.py:28: SettingWithCopyWarning:
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
dfc[‘A’][0] = 12

则下例中，不使用.copy()，则一同改变了，即使是使用了copy()，也要使用data.loc[index,‘列名’]的方法
index,可以使用data.index[-1]这样的方法取得倒数第一位的index等方法。

```python
import pandas as pd
dfc = pd.DataFrame({'A': ['aaa', 'bbb', 'ccc'], 'B': [1, 2, 3]})
dfd=dfc
dfc['A'][0] = 12
dfd.loc[0, 'A'] = 112
print(dfc)
print(dfd)

dfc = pd.DataFrame({'A': ['aaa', 'bbb', 'ccc'], 'B': [1, 2, 3]})
dfd=dfc
dfc.loc[0, 'A'] = 12
dfd.loc[0, 'A'] = 112
print(dfc)
print(dfd)

dfc = pd.DataFrame({'A': ['aaa', 'bbb', 'ccc'], 'B': [1, 2, 3]})
dfd=dfc.copy()
dfc.loc[0, 'A'] = 12
dfd.loc[0, 'A'] = 112
print(dfc)
print(dfd)

```





# 排序和数据分析实战

数据集是英语竞赛c类的初赛成绩

先进行读入，然后查看columns的名称及类型

`data.dtypes` 

`data.columns`只能看到列的名称

![image-20210427223328996](https://gitee.com/hit_whr/pic_2.0/raw/master/20210427223336.png)

类型转换是

`data[column].astype(typename)`

![image-20210427223422527](https://gitee.com/hit_whr/pic_2.0/raw/master/20210427223422.png)



排序函数是

`data.sort_values(by=column,inplace,ascending)`

by指根据哪一列排序

![image-20210427223543526](https://gitee.com/hit_whr/pic_2.0/raw/master/20210427223543.png)

现在有一个比较讨厌的，因为源数据没有index，所以在读入后，自动加了index

排序后，index跟着一起移动，所以index的顺序也乱了

要调整index

`data.reset_index(drop=True,inplace=True)`

![image-20210427223749587](https://gitee.com/hit_whr/pic_2.0/raw/master/20210427223749.png)



drop是说是否保留原来的index，如果保留，会将原来的index单独拿出来作为一行，有时候在我们需要回到源数据的排列顺序时比较有用（不过源数据直接inplace=False也可以呀）

![image-20210427223939157](https://gitee.com/hit_whr/pic_2.0/raw/master/20210427223939.png)

同样的，inplace在说是否修改源数据



数据排序好了之后，我们对数据进行写入，同样不写入index

![image-20210427224125398](https://gitee.com/hit_whr/pic_2.0/raw/master/20210427224125.png)

![image-20210427224114071](https://gitee.com/hit_whr/pic_2.0/raw/master/20210427224114.png)



现在我们完成了排序，再来找找自己的信息，然后对这个信息进行分析（名次、百分比）

找自己的信息是根据学号来的（主键）

输入学号（转成int，根据data.dtypes，都是int），然后遍历，与学号列进行匹配

如果找到了，由于是降序，直接用遍历时的下标+1除以总的人数

这里有点傻，想知道index是多少，如果不知道index就不知道这一行

现在知道了这一行，肯定有index了，不用再求了

找到index后，输出排名和百分成绩

`round(digit,n)` 是对digit小数取n位小数的操作

`data.index`

![image-20210427231022130](https://gitee.com/hit_whr/pic_2.0/raw/master/20210427231022.png)

data.index.tolist

![image-20210427231117675](https://gitee.com/hit_whr/pic_2.0/raw/master/20210427231117.png)

`data.index.tolis()`

![image-20210427231150312](https://gitee.com/hit_whr/pic_2.0/raw/master/20210427231150.png)

`data.loc[i].index.tolist()`

![image-20210427231221115](https://gitee.com/hit_whr/pic_2.0/raw/master/20210427231221.png)

返回的是第index为i的行的columns的名称，相比于直接用`data.columns`返回一堆字符串，这样的list就让调试更加方便了（不用自己手动输入）

由于返回值是list，可以用下标进行访问

![image-20210427231355236](https://gitee.com/hit_whr/pic_2.0/raw/master/20210427231355.png)

```python
import pandas as pd
file_name='grade.xlsx'
data=pd.read_excel(file_name)
data['总分']=data['总分'].astype(float)
data.sort_values(by='总分',ascending=False,inplace=True)
data.reset_index(drop=True,inplace=True)
data.to_excel('sorted_grade.xlsx',index=None)
student_id=190300211#int(input("学号为："))
signal=0
for i in range(len(data)):
    if data.loc[i]['考生学号']==student_id:
        print(data.loc[
        signal=1
        print("排名为"+str(i+1)+'-'+str(round(1.0*(i+1)/len(data)*100,4))+'%')
        break
if signal==0:
    print(str(student_id)+' not found')
```

显示的时候学号为

