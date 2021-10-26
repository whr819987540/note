# 《Web信息处理实验报告》 



| *实验内容：* | 配置环境并进行RDD编程 |
| ------------ | --------------------- |
| *班   级：*  | 1904301               |
| *学   号：*  | 2190300211            |
| *姓   名：*  | 王浩然                |
| *时   间：*  | 2021年7月24日         |

 

​																																			***哈尔滨工业大学（威海）***

​																																			**计算机科学与技术学院**

 

# 代码设计



## 案例一：求top值

```python
from pyspark import SparkContext
sc = SparkContext(master="local[4]")
print("-----------")
print("求top值")
lines = sc.textFile("data/examples")
lines.filter(lambda line: (len(line.strip()) > 0) and (len(line.split(",")) == 4))\
# 去掉空行+过滤掉数据量不等于4的line
['1,1768,50,155 ', '2,1218,600,211 ', '3,2239,788,242 ', '4,3101,28,599 ', '5,4899,290,129 ', '6,3110,54,1201', '7,4436,259,877 ', '8,2369,7890,27', '100,4287,226,233 ', '101,6562,489,124 ', '102,1124,33,17 ', '103,3267,159,179 ', '104,4569,57,125', '105,1438,37,116']
.map(lambda line:line.split(",")[2])\
# 以，分割然后映射出每行的第三个数据
['50', '600', '788', '28', '290', '54', '259', '7890', '226', '489', '33', '159', '57', '37']
.map(lambda x: (int(x),""))\
# 映射成一个二元组，第二个元素为空
[(50, ''), (600, ''), (788, ''), (28, ''), (290, ''), (54, ''), (259, ''), (7890, ''), (226, ''), (489, ''), (33, ''), (159, ''), (57, ''), (37, '')]
.sortByKey(False)\
# 根据key默认第一个值进行排序
[(7890, ''), (788, ''), (600, ''), (489, ''), (290, ''), (259, ''), (226, ''), (159, ''), (57, ''), (54, ''), (50, ''), (37, ''), (33, ''), (28, '')]
.map(lambda x:x[0]).take(5)
# 映射出每个元组的第一个值，然后取出前五个值
print(res)
[7890, 788, 600, 489, 290] 
```



## 案例二：求最大值最小值

```python
from pyspark import SparkContext
sc = SparkContext(master="local[4]")
print("-----------")
print("求最大最小值")
lines = sc.textFile("data/minmax")
lines.filter(lambda line:len(line.strip()) > 0)\
# 过滤掉空行
['5', '329', '14', '4567', '2186', '457', '35', '267', '129', '54', '167', '324', '111', '54', '26', '697', '4856', '3418']
.map(lambda line: ("key",int(line.strip())))\
# 生成一个二元组
[('key', 5), ('key', 329), ('key', 14), ('key', 4567), ('key', 2186), ('key', 457), ('key', 35), ('key', 267), ('key', 129), ('key', 54), ('key', 167), ('key', 324), ('key', 111), ('key', 54), ('key', 26), ('key', 697), ('key', 4856), ('key', 3418)]
.groupByKey()\
# 根据第一个值进行分组，由于值key都是一样的，所以会进入到同一个分组里
[('key', <pyspark.resultiterable.ResultIterable object at 0x7f5c416be5c0>)]     
.map(lambda x:(max(x[1]),min(x[1])))\
# 对于每一个二元组，生成一个二元组，第一个值是最大值，第二个是最小值
print(lines.collect())
[(4856, 5)]   
print("-----------")
```



## 案例3：文件排序

```python
from pyspark import SparkContext
sc = SparkContext(master="local[4]")
print("-----------")
print("文件排序")
lines = sc.textFile("data/filesort")
index = 0
def getIndexKey(x):
    global index
    index += 1
    return(index, x[0])
result = lines.filter(lambda n:len(n.strip())>0)\
.map(lambda n: (int(n.strip()),""))\
.partitionBy(1)\
# 映射为一个二元组
[(4, ''), (16, ''), (39, ''), (5, ''), (33, ''), (37, ''), (12, ''), (40, ''), (1, ''), (45, ''), (25, '')]
.sortByKey()\
# 升序排序
[(1, ''), (4, ''), (5, ''), (12, ''), (16, ''), (25, ''), (33, ''), (37, ''), (39, ''), (40, ''), (45, '')]
.map(getIndexKey)
# 二元组，第一个是索引，第二个是升序排序的元素
print(result.collect())
[(1, ''), (4, ''), (5, ''), (12, ''), (16, ''), (25, ''), (33, ''), (37, ''), (39, ''), (40, ''), (45, '')]
print("-----------")
```



## 案例4：

```python
from pyspark import SparkContext
from secondsort import SecondSortKey
sc = SparkContext(master="local[4]")
print("二次排序")
sc.addPyFile('secondsort.py')
sortData = sc.parallelize([("3 2"), ("2 4"), ("3 0"), ("4 1"), ("3 0")])
pairRDD = sortData.map(lambda line: (SecondSortKey(int(line.split(" ")[0]), int(line.split(" ")[1])), line))
# 三元组
[(<secondsort.SecondSortKey object at 0x7fc472dec8d0>, '3 2'), (<secondsort.SecondSortKey object at 0x7fc472dec358>, '2 4'), (<secondsort.SecondSortKey object at 0x7fc472dec390>, '3 0'), (<secondsort.SecondSortKey object at 0x7fc472dec2e8>, '4 1'), (<secondsort.SecondSortKey object at 0x7fc472dec320>, '3 0')]
# sortbykey会自动调 secondsort里面的 __cmp__
sorted_pairRDD = pairRDD.sortByKey(False)
# 根据第一个值降序排序
sorted_lines = sorted_pairRDD.map(lambda x: x[1])
# 映射出三元组的第二个值
print(sorted_lines.collect())
['4 1', '3 2', '2 4', '3 0', '3 0'] 
print("-----------")
```



## 案例5：

```python
from pyspark import SparkContext
sc = SparkContext(master="local[4]")
print("-----------")
print("链接操作")
ratingFile = sc.textFile("data/ml-1m/ratings.dat")
ratings = ratingFile.map( lambda line: (int(line.split("::")[1]), float(line.split("::")[2])))
print(ratings.take(5))
# 取出ratings.dat文件每行的第二个数据和第三个数据
[(1193, 5.0), (661, 3.0), (914, 3.0), (3408, 4.0), (2355, 5.0)] 
movieScores = ratings.groupByKey()\
# 根据第一个值归纳起来
.map(lambda x: (x[0],sum(x[1])/len(x[1])))
movieScores.take(5)
# 对二元组的第二个值的集合取平均值
[(914, 4.154088050314465), (3408, 3.863878326996198), (2804, 4.238905325443787), (594, 3.8453473132372213), (938, 3.620320855614973)]

movieFile = sc.textFile("data/ml-1m/movies.dat")
movieskey = movieFile.map( lambda line: (int(line.split("::")[0]), line.split("::")[1]))\
# 二元组，第一个元素是索引，第二个是电影名
[(1, 'Toy Story (1995)'), (2, 'Jumanji (1995)'), (3, 'Grumpier Old Men (1995)'), (4, 'Waiting to Exhale (1995)'), (5, 'Father of the Bride Part II (1995)')]
.keyBy(lambda tup: tup[0])
# 根据二元组的第一个元素生成一个新的二元组
[(1, (1, 'Toy Story (1995)')), (2, (2, 'Jumanji (1995)')), (3, (3, 'Grumpier Old Men (1995)')), (4, (4, 'Waiting to Exhale (1995)')), (5, (5, 'Father of the Bride Part II (1995)'))]

result = movieScores\
.keyBy( lambda tup: tup[0])\
# 根据二元组的第一个元素生成一个新的二元组
[(914, (914, 4.154088050314465)), (3408, (3408, 3.863878326996198)), (2804, (2804, 4.238905325443787)), (594, (594, 3.8453473132372213)), (938, (938, 3.620320855614973))]
.join(movieskey)\
[(3408, ((3408, 3.863878326996198), (3408, 'Erin Brockovich (2000)')))]  
.filter(lambda f: f[1][0][1] > 4.0)\
# 删选出评分>4的记录
.map(lambda f:(f[0],f[1][0][1],f[1][1][1]))
print(result.take(5))
[(2804, 4.238905325443787, 'Christmas Story, A (1983)'), (720, 4.426940639269406, 'Wallace & Gromit: The Best of Aardman Animation (1996)'), (2692, 4.224813432835821, 'Run Lola Run (Lola rennt) (1998)'), (260, 4.453694416583082, 'Star Wars: Episode IV - A New Hope (1977)'), (2028, 4.337353938937053, 'Saving Private Ryan (1998)')]
print("-----------")
```



# 运行截图及说明

## 案例1

 ![image-20210725100515152](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210725100515152.png)

 

## 案例2

 ![image-20210725101442887](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210725101442887.png)

 

## 案例3

![image-20210725102444703](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210725102444703.png)



## 案例4

![image-20210725103041681](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210725103041681.png)



## 案例5

![image-20210725104943062](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210725104943062.png)

# 总结分析

前四个案例在熟悉spark内置的函数操作，最后一个案例根据爬虫获取的电影数据，筛选出评分>4的电影的信息。关键在于数据量非常大，所以用到了spark处理大数据。

 

 

