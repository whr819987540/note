jieba(中文分词)

# 安装

```bash
pip install jieba
pip install paddlepaddle-tiny==1.6.1
```



# 使用



## jieba.cut

jieba.cut(string,cut_all,HMM,use_paddle)

返回值是迭代器

string是中文字符串

cut_all是否采用全模式，如果为true则采用全模式（将所有可以分词的情况都列出来）；如果为false则采用精确模式（只显示一种结果）。默认采用精确模式

```python
import jieba
string="中国上海是一座美丽的国际性大都市"
seg_string=jieba.cut(string)
print(seg_string)
print("分词结果："+"/".join(seg_string))

Building prefix dict from the default dictionary ...
Loading model from cache C:\Users\user\AppData\Local\Temp\jieba.cache
<generator object Tokenizer.cut at 0x000001E16050EE60>
分词结果：中国/上海/是/一座/美丽/的/国际性/大都市
Loading model cost 0.638 seconds.
Prefix dict has been built successfully.
```



## 添加自定义词典

jieba.load_dict(file_name)

如果句子里面有很多专业词汇，默认的dict（prefix dict）无法识别这些词汇，需要添加自定义的语料库。

语料库是文本文件，txt/csv都可以

格式是：词语+空格+词频（可选）+词性（可选）

每个词语占一行



不添加自定义词汇

```python
import jieba
string="奥利给，管虎执导的八佰是一部让人热血沸腾的好电影。"
seg_string=jieba.cut(string)
print("res:"+'/'.join(seg_string))

Building prefix dict from the default dictionary ...
Loading model from cache C:\Users\user\AppData\Local\Temp\jieba.cache
res:奥利/给/，/管虎/执导/的/八佰是/一部/让/人/热血沸腾/的/好/电影/。
Loading model cost 0.649 seconds.
Prefix dict has been built successfully.
```



添加自定义词汇

![image-20210714204252866](https://raw.githubusercontent.com/whr819987540/pic/main/image-20210714204252866.png)

```python
import jieba
jieba.load_userdict("dict.txt")
string="奥利给，管虎执导的八佰是一部让人热血沸腾的好电影。"
seg_string=jieba.cut(string)
print("res:"+'/'.join(seg_string))

Building prefix dict from the default dictionary ...
Loading model from cache C:\Users\user\AppData\Local\Temp\jieba.cache
Loading model cost 0.648 seconds.
Prefix dict has been built successfully.
res:奥利给/，/管虎/执导/的/八佰/是/一部/让/人/热血沸腾/的/好/电影/。
```



# 实例

对一章小说进行分词、统计词频、词云图

## 对字符的处理

思路是加载文件，分词，统计词频，对词频结果的字符进行处理

为什么不加载文件后就处理字符？

因为标点符号也是分词的依据之一，这里还不能去掉标点符号。

为什么不分词后就处理字符？

因为分词后处理字符，需要扫描一遍所有字符，统计词频的时候还是需要扫描一遍。如果先统计词频，扫描一遍所有字符，直接对词频结果进行筛选，就极大的减少了搜索范围，关键是只扫描了一所有字符。

而如果先分词，扫描，统计词频，相当于有了两次扫描、



## 读取文件

```python
import jieba,pandas as pd
with open(" 第1章 地狱灵芝.txt",'r',encoding="utf-8") as f:
    string=f.read()
print(string)
```

![image-20210715090214501](https://raw.githubusercontent.com/whr819987540/pic/main/image-20210715090214501.png)





## 分词

```python
import jieba,pandas as pd
with open(" 第1章 地狱灵芝.txt",'r',encoding="utf-8") as f:
    string=f.read()
seg_string=jieba.cut(string)
print("/".join(seg_string))
```

![image-20210715090446160](https://raw.githubusercontent.com/whr819987540/pic/main/image-20210715090446160.png)



## 统计词频

这里统计词频用到pands库的series数据类型，简要了解一下这个数据类型

### pandas.Series

```python
import pandas as pd
# 创建

a=pd.Series(data=[1,2,3],index=[4,5,6])
print(a)
# data和index的元素个数必须是相同的
# 4    1
# 5    2
# 6    3
# dtype: int64

a=pd.Series(range(0,4),index=range(1,5))
print(a)
# 1    0
# 2    1
# 3    2
# 4    3
# dtype: int64

a=pd.Series(data={"a":1,"b":2,"c":3})
print(a)
# a    1
# b    2
# c    3
# dtype: int64

# 参数
print(a.index)
# Index(['a', 'b', 'c'], dtype='object')
print(a.values)
# [1 2 3]
print(a.size)
# 3

# 访问
# 存在的
print(a.get("a"))
# 1
print(a.get("d"))
# None
print(a.at["a"])
# 1
# print(a.at["d"])
# 报错
try:
    print(a.at['d'])
except:
    print("error")
# error
for i in a.items():
    print(i)
# ('a', 1)
# ('b', 2)
# ('c', 3)
```







### 去掉空白字符

分词后，大量空白字符会被保留（空格，换行符，制表符），而词频统计当然不会关心空白字符，如果空白字符的数量比较大了，可能会达到前十，影响词频统计。

```python
import jieba,pandas as pd
with open(" 第1章 地狱灵芝.txt",'r',encoding="utf-8") as f:
    # 读取文本文件
    string=f.read()
print(string)
seg_string=jieba.cut(string)
print("/".join(seg_string))
/ / / / /“/地狱/灵芝/！/”/沈翔/兴奋/的/喊/了/一声/，/目光/激动/地/凝视/下方/，/在/他/脚下/十来丈/的/地方/有着/一块/如同/白色/大饼/的/东西/紧贴着/崖壁/，/他/非常/肯定/这/就是/传说/在/地狱/灵芝/。/
/ / / / /
/ / / / /这里/常年/都/被/黑色/死气/覆盖/着/，/而/地狱/灵芝/的/颜色/和/崖壁/非常/相似/，/很难/发现/。/
```



所以分词前，首先去掉文本中的空白符。

两个步骤：

以空白字符作为分割

`string.split(” ”)`

连接起来

`””.join(string)`

### 词频统计

用pandas库的`Series.value_counts()`来实现

```python
import jieba,pandas as pd
with open(" 第1章 地狱灵芝.txt",'r',encoding="utf-8") as f:
    string=f.read()
seg_string=jieba.cut(string)
data=pd.Series(seg_string)
analysis=data.value_counts()
print(analysis.head(10))

      475
，     196
的     119
\n    118
他      64
。      55
沈翔     48
了      24
这      23
是      23
```



### 对统计结果去掉字符

字符序列：

```python
invalid_char='[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+，。！？“”《》：、． \n'
```



这个没有对原统计结果进行处理，只是显示

```python
import jieba,pandas as pd
with open(" 第1章 地狱灵芝.txt",'r',encoding="utf-8") as f:
    string=f.read()
seg_string=jieba.cut(string)
data=pd.Series(seg_string)
analysis=data.value_counts()
print(analysis.head(10))
invalid_char='[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+，。！？“”《》：、． \n'
cnt=0
for i in analysis.iteritems():
    if(i[0] not in invalid_char):
        print(i)
        cnt+=1
    if(cnt==10):
        break
        
('的', 119)
('他', 64)
('沈翔', 48)
('了', 24)
('是', 23)
('这', 23)
('让', 20)
('在', 20)
('着', 17)
('地狱', 17)
```



可以用Series.iteritems()和Series.drop(labels,replace)对统计结果进行处理

```python
import jieba,pandas as pd
with open(" 第1章 地狱灵芝.txt",'r',encoding="utf-8") as f:
    string=f.read()
seg_string=jieba.cut(string)
data=pd.Series(seg_string)
analysis=data.value_counts()
invalid_char='[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+，。！？“”《》：、． \n'
for i in analysis.items():
    if(i[0] in invalid_char):
        analysis.drop(i[0],inplace=True)
print(analysis.head(10))
的     119
他      64
沈翔     48
了      24
这      23
是      23
在      20
让      20
着      17
地狱     17
```



## 生成词云图

### wordcloud库

font_path：字体的路径

max_words：显示的词的最大个数

stopwords：屏蔽的词语

background_color：背景颜色，用英文单词

prefer_horizontal：词语在水平方向出现的概率，建议设置为1

mask：对词汇范围的限制

```python
from worlcloud import WordCloud as wc
with open(filename,'r') as f:
    # 读取文件内容
    string=f.read()
    # 设置词云的参数
    my_cloud=wc.(font_path="",).generate(string)
    # 生成图片
    image=my_cloud.to_image()
    # 显示图片
    image.show()
    # 保存图片
    my_cloud.to_file(filename)
    # 保存为矢量图片
    my_cloud.to_svg()
```



#### 限定词汇的显示范围

就是加上一层图片

```python
import PIL.Image as image
mask=numpy.array(image.open(file_name))
my_cloud=wc(font_path="",mask=)
```



### 读取多个文件



#### 队列

为啥需要队列？因为需要一个目录下的多个文件，这些文件中有txt文件，也有目录，为了方便递归查询，用上队列。

```python
# 导入先进先出队列
from queue import Queue
# queue的数据量
def print_size(queue):
    print("size:"+str(queue.qsize()))

# 判断队列是否满
def is_full(queue):
    if (queue.full()):
        print("full queue")

# 判断队列是否为空
def is_empty(queue):
    if (queue.empty()):
        print("empty queue")

# 设置队列的最大容量
queue=Queue(maxsize=5)
print_size(queue)
# size: 0
for i in range(10):
    is_empty(queue)
    is_full(queue)
    # 入队列
    queue.put(i)
    # 队列的最大长度为5，如果插入的数据量超过了5直接卡死在这儿了（因为没设置timeout）
    print(i)
# empty
# queue
# 0
# 1
# 2
# 3
# 4
# full

```



为了防止卡死，设置一个timeout

```python
xxxx
    queue.put(i,timeout=1)
xxxx

full queue
Traceback (most recent call last):
  File "D:/pythoncode/中文分词/test_queue.py", line 24, in <module>
    queue.put(i,timeout=1)
  File "C:\Users\user\AppData\Local\Programs\Python\Python36\lib\queue.py", line 141, in put
    raise Full
queue.Full
```



对于出队列queue.get(timeout)也有同样的问题，最好设置一些timeout，或者直接判断是否为空



#### 递归读取文件

```bash
# 1.根目录入队列
# 2.出队列->base_dir
# 3.访问根目录的所有文件
#     1.是文件，进list
#     2.是文件夹，当前base_dir+文件名->队列
# 4.重复2、3，直到队列为空
```



```python
import os
from queue import Queue
base_path="D:/pythoncode/中文分词"
# 返回绝对路径path下所有文件的文件名
# 不会去递归查询文件夹，所以要得到所有文件名（包括子文件夹下的文件）
# 需要判断是否为dir，然后递归
queue=Queue(maxsize=1000)
queue.put(base_path)
file_list=[]
while not(queue.empty()):
    # 当前目录名
    path=queue.get()
    files=os.listdir(path)
    for file in files:
        # 判断是不是dir，可以使用相对路径
        file_path=path+"/"+file
        if os.path.isdir(file_path):
            #以.开头的文件夹是配置文件，不可能有我们想要的txt文件，当然也可能是其
            if(file[0]!='.'):
                print("----------")
                print(file_path+" is dir")
                print("----------")
                queue.put(file_path)
        else:
            print("*******")
            print(file_path)
            print("*******")
            file_list.append(file_path)
for i in file_list:
    print(i)
# 1.根目录入队列
# 2.出队列->base_dir
# 3.访问根目录的所有文件
#     1.是文件，进list
#     2.是文件夹，当前base_dir+文件名->队列
# 4.重复2、3，直到队列为空
```

### 去除无效词语（停用词去除）

运行结果是这样的

![image-20210715161711218](https://raw.githubusercontent.com/whr819987540/pic/main/image-20210715161711218.png)

但是这个图里面，很多词语都没有实际含义，需要去掉（类似于前面去掉标点符号）

```python
# 加载停用词
with open("stop_words.txt",'r',encoding="utf-8") as f:
    for line in f.readlines():
        stop_words.append(line.strip())
# 词频结果筛选（标点符号+停用词）
for i in analysis.items():
    if(i[0] in invalid_char):
        analysis.drop(i[0],inplace=True)
    elif(i[0] in stop_words):
        analysis.drop(i[0],inplace=True)
analysis.to_excel("1.xlsx")
```

![image-20210715165247330](https://raw.githubusercontent.com/whr819987540/pic/main/image-20210715165247330.png)





### 总的代码

```python
import jieba,numpy,pandas as pd
from wordcloud import WordCloud as wc
from traverse_dir import traverse_dir
import PIL.Image as image
# 读取数据
base_path="D:/pythoncode/中文分词/一等家丁/第一战神"
need_file_type=["txt"]
file_list=traverse_dir(base_path,need_file_type)
string=""
max_words=30
background_pic="下载.png"

for file in file_list[:10]:
    with open(file,'r',encoding="utf-8") as f:
        string+=f.read()

# 分词
seg_string=jieba.cut(string)
data=pd.Series(seg_string)
analysis=data.value_counts()
invalid_char='[’!"#$%&\'()*+,-./:;…<=>?@[\\]^_`{|}~]+，。！？“”《》：、． \n'

# 词频结果筛选
for i in analysis.items():
    if(i[0] in invalid_char):
        analysis.drop(i[0],inplace=True)
analysis.to_excel("1.xlsx")

# 生成遮罩层
mask=numpy.array(image.open(background_pic))

# 生成词云图
# frequencies参数必须为字典
# 可以将series强制转换为dict（此时进行排名选择）
my_cloud=wc(font_path="方正书宋简体.ttf",background_color="black",mask=mask,prefer_horizontal=1.0)
my_cloud.generate_from_frequencies(frequencies=dict(analysis[:max_words]))
image=my_cloud.to_image()
image.show()
my_cloud.to_file("res.png")
```

