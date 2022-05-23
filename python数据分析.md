python数据分析

两个包matplotlib(数学会图库），pagal（生成图表）

> import matplotlib.pyplot as plt 

我们创建了一个列表，在其中存储了前述平方数，再将这个列表传递给函数plot()，这个函

数尝试根据这些数字绘制出有意义的图形。plt.show()打开matplotlib查看器，并显示绘制的图形，



![image-20210403214607366](https://raw.githubusercontent.com/whr819987540/pic/main/20210403214614.png)



美化

linewidth，

title，fontsize

xlable，fontsize

ylabel，fontsize

tick_params（刻度标记），axis（显示哪条坐标轴），labelsize（这个是刻度/tick数值的字体大小）

```python
import matplotlib.pyplot as plt
list=[]
for i in range(5):
    list.append(i*i)
plt.plot(list,linewidth=10)
plt.xlabel("xlabel",fontsize=20)
plt.ylabel("ylabel",fontsize=10)
#plt.xticks()
plt.tick_params(axis="both"，labelsize=15)
plt.show()
```

plot（input,result)



scatter绘制散点图

edgecolor默认黑色轮廓，none进行清除

c=（r,g,b)设置颜色，不过这里的颜色设置是在0-1之间，而不是255。值越接近0，指定的颜色越深，值越接近1，指定的颜色越浅

一次绘制一个点或者传递两个列表，得到一组散点

参数：(x,y,点的大小s=)

plt.axis([0,100,400,1000])

分别设置xy轴的坐标范围

cmap颜色映射（colormap）是一系列颜色，它们从起始颜色渐变到结束颜色。在可视化中，颜色映射用于突出数据的规律，例如，你可能用较浅的颜色来显示较小的值，并使用较深的颜色来显示较大的值。

使用cmap意味着要更改颜色，使用c参数，指定将什么作为渐变色的量度（比如y的值，x的值），然后选择一个渐变方案，cmap=plt.cm.xxx

自动保存图表

> plt.savefig('squares_plot.png', bbox_inches='tight') 

保存的路径，是否去掉图表周围多余的空白区域

这个顺序很有讲究，scatter或者plot之前，python已经绘图了，只不过没有show（显示出来），下面的title，label都是对这个图的修饰，修饰好了，就可以savefig了，如果show了，就加载出来了，不能save了

```python
import matplotlib.pyplot as plt,random
x=list(range(1000))
y=[random.random() for m in x]
plt.scatter(x,y,edgecolors="none",c=y,cmap=plt.cm.Blues)
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("test.jpg",bbox_inches="tight")
plt.show()
```



在命名的时候不要用list，容易冲突

![image-20210404192803353](https://raw.githubusercontent.com/whr819987540/pic/main/20210404192803.png)



绘制随机移动的图案

很有意思的是，如果把方向和距离放在一个变量中，得到的结果和直接给常量是不一样的，一个是条带状，一个是簇状，结合y的坐标变化，放在常量里面的随机性更强一点

```python
from random import choice
import matplotlib.pyplot as plt
class Random_Walk:
    def __init__(self,randomnum=5000):
        self.num=randomnum
        self.x,self.y=[0],[0]
    def walk(self):
        x_dir_list=[1,-1]
        x_distance_list=list(range(5))
        y_dir_list=[1,-1]
        y_distance_list=list(range(5))
        cnt=0
        while cnt<self.num:
            # x_dir=choice(x_dir_list)
            # y_dir=choice(x_distance_list)
            #
            # x_dis=choice(x_distance_list)
            # y_dis=choice(y_distance_list)
            x_dir=choice([1,-1])
            y_dir=choice([1,-1])

            x_dis=choice([0,1,2,3,4])
            y_dis=choice([0,1,2,3,4])
            if x_dis==0 and y_dis==0:
                continue
            self.x.append(self.x[-1]+x_dir*x_dis)
            self.y.append(self.y[-1]+y_dir*y_dis)
            cnt+=1
        self.show()
    def show(self):
        #这个解决方法很好，先把所有的点都画出来，起点终点要加粗换颜色，在先前的位置进行覆盖即可
        #没必要将全部点-起点终点与起点终点分开处理，终究会覆盖
        plt.scatter(self.x, self.y,
                    c=list(range(len(self.x))),cmap=plt.cm.Blues,edgecolor="none")
        plt.scatter(self.x[0],self.y[0],c="red",edgecolor="none",s=100)
        plt.scatter(self.x[-1],self.y[-1],c="yellow",edgecolor="none",s=100)
        plt.axes().get_xaxis().set_visible(False)
        plt.axes().get_yaxis().set_visible(False)
        plt.show()

rw=Random_Walk(9999)
rw.walk()
from random import choice
import matplotlib.pyplot as plt
class Random_Walk:
    def __init__(self,randomnum=5000):
        self.num=randomnum
        self.x,self.y=[0],[0]
    def walk(self):
        x_dir_list=[1,-1]
        x_distance_list=list(range(5))
        y_dir_list=[1,-1]
        y_distance_list=list(range(5))
        cnt=0
        while cnt<self.num:
            # x_dir=choice(x_dir_list)
            # y_dir=choice(x_distance_list)
            #
            # x_dis=choice(x_distance_list)
            # y_dis=choice(y_distance_list)
            x_dir=choice([1,-1])
            y_dir=choice([1,-1])

            x_dis=choice([0,1,2,3,4])
            y_dis=choice([0,1,2,3,4])
            if x_dis==0 and y_dis==0:
                continue
            self.x.append(self.x[-1]+x_dir*x_dis)
            self.y.append(self.y[-1]+y_dir*y_dis)
            cnt+=1
        self.show()
    def show(self):
        #这个解决方法很好，先把所有的点都画出来，起点终点要加粗换颜色，在先前的位置进行覆盖即可
        #没必要将全部点-起点终点与起点终点分开处理，终究会覆盖
        plt.scatter(self.x, self.y,
                    c=list(range(len(self.x))),cmap=plt.cm.Blues,edgecolor="none")
        plt.scatter(self.x[0],self.y[0],c="red",edgecolor="none",s=100)
        plt.scatter(self.x[-1],self.y[-1],c="yellow",edgecolor="none",s=100)
        plt.axes().get_xaxis().set_visible(False)
        plt.axes().get_yaxis().set_visible(False)
        plt.show()

rw=Random_Walk(9999)
rw.walk()
```

在绘图前先指定一个图层，对图层的参数进行设置

figsize（），宽度和高度，单位是英寸





使用Python可视化包Pygal来生成可缩放的矢量图形文件

生成可视化的漂亮图表

python中检查某个键是否存在：直接

> if key in dic:

绘制一个简单的直方图

首先创建一个instance，用title设置标题

x_title，y_title分别为横纵轴名称

直方图的映射关系是在x_labels中单独设置标签，然后add对应添加数据，add(数据项的名称【相当于图例】，数据)

render_to_file(”name.svg”)

svg是scalable vector graphics，是基于浏览器的一种矢量图形标准

所以生成后，只能导出到文件，然后用浏览器进行观看

优点是分辨率高，支持自由缩放，不受到显示器自身尺寸及分辨率的限制

```python
bar =Bar(x_label_rotation=45)#将横轴标签旋转一个角度
```

封装起来的一个函数

```python
die_func.py
import pygal
from die import Die
import die_func as df

die_num=df.get_an_int("请输入骰子的个数")
die_sides=[]
df.get_die_sides(die_sides,die_num)#输入骰子的面数
dies=df.create_dies(die_sides)#储存所有的骰子（对象）
roll_times=df.get_an_int("输入骰子摇动的次数")
frequencies=df.roll_dies(die_sides,roll_times,dies)

bar = pygal.Bar()
bar.title=str(die_num)+" Dies frequencies"
bar.x_title="total sides"
bar.y_title="frequencies"
bar.x_labels=frequencies.keys()
bar.add("tow dies",frequencies.values())
bar.render_to_file(df.now_time()+".svg")

pygal_test.py
import time
from die import Die
def now_time():
    return time.strftime("%Y_%m_%d_%H_%M")
def get_side(cnt):
    while True:
        tmp=input("请输入第"+str(cnt+1)+"个骰子的面数：")
        if tmp.isdigit() and int(tmp)>0:
            return int(tmp)
        else:
            print("非法输入，重试")

def get_an_int(str):
    while 1:
        res=input(str)
        if res.isdigit() and int(res)>0:
            return int(res)
        else:
            print("非法输入请重试")

def get_die_sides(die_sides,cnt):
    for i in range(cnt):
        die_sides.append(get_side(i))

def create_dies(die_sides):
    dies=[]
    for side in die_sides:
        tmp=Die(side)
        dies.append(tmp)
    return dies
def roll_dies(die_sides,roll_times,dies):
    total_dies=get_total_dies(die_sides)
    res={}
    for i in range(len(die_sides),total_dies+1):
        res[i]=0
    for time in range(roll_times):
        total_sides=0
        for die in dies:
            total_sides+=die.roll_die()
        res[total_sides]+=1
    return res

def get_total_dies(die_sides):
    tmp=0
    for side in die_sides:
        tmp+=side
    return tmp
    
if __name__=="__main__":
    die_sides=[]
    get_die_sides(die_sides,6)
    print(create_dies(die_sides))
    print(get_total_dies(die_sides))
```



将py打包成exe，使程序能够运行在没有python第三方库甚至没有python解释器的终端上：

使用pyinstaller，能用from import就用，尽量不使用import

exe不能直接运行在centos（任何linux上），linux提供了wine进行辅助

不管这个 Python 应用是单文件的应用，还是多文件的应用，只要在使用 pyinstaller 命令时编译作为程序入口的 Python 程序即可。

-F onefile 结果就是一个可执行文件

-D onedir 结果是一个包含exe以及依赖项的目录

-w 生成GUI界面，前提是能生成

--name=文件名（如果是目录，目录名和可执行文件都是这个名字）





将一个正整数sum，写成n个正整数相加的形式，给出相加的式子及可能的情况数





python返回当前时间

```
def get_roll_times():
    input("输入骰子摇动的次数")
```

```
def get_roll_times():
    input("输入骰子摇动的次数")
```

```bash
>>> time.time()
1617546514.3504856  #时间戳
>>> time.localtime()  #当地时间，但是不整洁
time.struct_time(tm_year=2021, tm_mon=4, tm_mday=4, tm_hour=22, tm_min=28, tm_sec=43, tm_wday=6, tm_yday=94, tm_isdst=0)
>>> time.strftime("%Y %m %d %H %M %S")
'2021 04 04 22 29 19'  #值得注意的是month和minute冲突
#%D表示date，即%Y %m %d
```





用python处理csv格式和json

csv，comma-separated values，用逗号（也可以是其他字符）来分割值的一种文件格式

里面都是字符序列，不必是二进制数字

每条记录之间以换行符间隔，每条记录中有相同类型的字段

类似excel，并且可以用excel打开，也可以用记事本（文本文件）打开

![image-20210405101328781](https://raw.githubusercontent.com/whr819987540/pic/main/20210405101335.png)

上面的记录之间用的换行符，记录内用的逗号来进行分割

CSV文件对人来说阅读起来比较麻烦，但程序可轻松地提取并处理其中的值，这有助于加快数据分析过程。

导入csv模块；打开文件，reader创建与文件对象相关联的阅读器对象，为什么非得创建阅读器对象，而不继续使用文件对象？为了使用csv模块内置的函数

next返回一行，然后指向下一行

```python
import csv
filename="sitka_weather_07-2014.csv"
try:
    with open(filename) as f:
        reader=csv.reader(f)
        line=next(reader)
        print(line)
except:
    print("open error")
['AKDT', 'Max TemperatureF', 'Mean TemperatureF', 'Min TemperatureF', 'Max Dew PointF', 'MeanDew PointF', 'Min DewpointF', 'Max Humidity', ' Mean Humidity', ' Min Humidity', ' Max Sea Level PressureIn', ' Mean Sea Level PressureIn', ' Min Sea Level PressureIn', ' Max VisibilityMiles', ' Mean VisibilityMiles', ' Min VisibilityMiles', ' Max Wind SpeedMPH', ' Mean Wind SpeedMPH', ' Max Gust SpeedMPH', 'PrecipitationIn', ' CloudCover', ' Events', ' WindDirDegrees']
```



```python
import csv
filename="sitka_weather_07-2014.csv"
try:
    with open(filename) as f:
        reader=csv.reader(f)
        line=next(reader)
        print(line)
        line=next(reader)
        print(line)
except:
    print("open error")
    
['AKDT', 'Max TemperatureF', 'Mean TemperatureF', 'Min TemperatureF', 'Max Dew PointF', 'MeanDew PointF', 'Min DewpointF', 'Max Humidity', ' Mean Humidity', ' Min Humidity', ' Max Sea Level PressureIn', ' Mean Sea Level PressureIn', ' Min Sea Level PressureIn', ' Max VisibilityMiles', ' Mean VisibilityMiles', ' Min VisibilityMiles', ' Max Wind SpeedMPH', ' Mean Wind SpeedMPH', ' Max Gust SpeedMPH', 'PrecipitationIn', ' CloudCover', ' Events', ' WindDirDegrees']
['2014-7-1', '64', '56', '50', '53', '51', '48', '96', '83', '58', '30.19', '30.00', '29.79', '10', '10', '10', '7', '4', '', '0.00', '7', '', '337']
```



对于表格头（首行），建议单独放在一个变量中

类似字典的for key,value in dic.items()，列表获取索引值及其value用enumerate

```python
>>> a=[1,2,3]
>>> for index,value in enumerate(a):
...     print(index,value)
...
0 1
1 2
2 3
```

路线，根据表头获得需要数据的索引值，然后在之后的每一行截取对应索引值的数据

![image-20210405103333881](https://raw.githubusercontent.com/whr819987540/pic/main/20210405103333.png)

对于每一行的记录，可以直接用index来访问第index个字段，reader本身iterable

读取出来的记录不管是什么，都是以文本的形式记录，python理解为字符串，这样精度其实是很高的，类似mysql直接用字符存数字

处理日期（统一成xxxx-xx-xx的形式）

strptime(date,”%-%-%”)

![image-20210405122145261](https://raw.githubusercontent.com/whr819987540/pic/main/20210405122145.png)

```python
figure=plt.figure(figsize=(10,6))
plt.plot(dates,max,c="blue")
plt.plot(dates,min,c="red")
plt.legend(["max","min"])
plt.title("Daily high temperatures, July 2014",fontsize=20)
plt.xlabel("Dates",fontsize=12)
plt.ylabel("Temperatures(F)",fontsize=12)
figure.autofmt_xdate()
plt.savefig("2.png",bbox_inches="tight")
plt.show()
自动调整figure中的x日期标签
```



![image-20210405110041072](https://raw.githubusercontent.com/whr819987540/pic/main/20210405110041.png)



进行两条折线之间的颜色填充

```python
plt.plot(dates,max,c="blue",alpha=0.5)
plt.plot(dates,min,c="red",alpha=0.5)
plt.fill_between(dates,max,min,facecolor="green",alpha=0.3)
```

alpha设置透明度，0为完全透明不可见，1为完全不透明

现在的问题是，如果某一条记录不完整，使得提取不到数据就会报错，程序终止，可以使用tryexcept，发现value error，就忽略这条记录。为了不让这条记录的其他字段被加入，只有当所有字段都被成功提取时，才append

> Traceback (most recent call last):
>   File "D:/pythoncode/pygame/test_csv/test.py", line 14, in <module\>
>     max.append(int(line[1]))
> ValueError: invalid literal for int() with base 10: ''

```python
for line in reader:
    try:
        # date=re.sub(r"20(.*?)-","",line[0])
        date=datetime.strptime(line[0],"%Y-%m-%d")
        max=int(line[1])
        mean=int(line[2])
        min=int(line[3])
        except ValueError:
            print(line)
            print("errpr")
            else:
                dates.append(date)
                maxes.append(max)
                means.append(mean)
                mins.append(min)
```

去掉了字段不完整的记录，对于图像来说几乎没有区别，程序更加健壮了



![image-20210405125230726](https://raw.githubusercontent.com/whr819987540/pic/main/20210405125230.png)



重构上述代码并进行举例

这样写不是很舒服

```python
list=[]
get_list(list)
```

主逻辑里面产生了两行，不如把这样的放到函数里面，让函数返回list，除非返回值太多，做不到，否则还是建议直接返回，主逻辑里面缩减为一行

```python
list=get_list()
```



matplotlib更适合绘制一些偏向数学的图案，而pagal适合绘制一些比较绚丽的图案



json

```
#这个json文件的组织形式实际上是列表，元素为字典，键值对为population的数据
#导入json模块
#打开文件，将文件对象传给json.load(file_object)
#python将文件内容转化为python可以处理的，此处为列表和字典
```

人口原始数据不干净，首先得检验是否为数字格式，然后得检验为整数（小数是插值得到的）



pygal的世界地图-数据映射工具要求用国别码表示国家，所以需要用国家-国别码作一次映射

pygal的国别码是两个字母的

在pygal中的pygal.maps.world模块内置了二位国别码到国名的映射

为了便于查找，创建一个国名到二位国别码的映射

```python
import pygal.maps.world
worldmap_chart = pygal.maps.world.World()
worldmap_chart.title = 'Some countries'
worldmap_chart.add('F countries', ['fr', 'fi'])
worldmap_chart.add('M countries', ['ma', 'mc', 'md', 'me', 'mg','mk', 'ml', 'mm', 'mn', 'mo','mr', 'mt', 'mu', 'mv', 'mw','mx', 'my', 'mz'])
worldmap_chart.add('U countries', ['ua', 'ug', 'us', 'uy', 'uz'])
worldmap_chart.render_to_file("1.svg")
```



worldmap_chart.add(图例名，[字典/列表])

如果是列表，对这些国别码对应的地区进行渲染

如果是字典，键值对=国别码-数字，根据数字大小进行颜色渲染

```python
wd=pygal.maps.world.World()
wd.title="World Population"
wd.add("pop",code_value)
wd.render_to_file("pop.svg")
```

![image-20210406123314231](https://raw.githubusercontent.com/whr819987540/pic/main/20210406123321.png)



进一步，根据人口的数量对国家进行分组，显示不同的颜色

首先得确立一个划分范围，然后将同范围的code_value放到一起，进行一次ad

![image-20210406124734541](https://raw.githubusercontent.com/whr819987540/pic/main/20210406124734.png)

更改颜色

pygal的样式存储在style中

创建这个类的实例时，需要提供一个实参——十六进制的RGB颜色；Pygal将根据指定的颜色为每组选择颜色。十六进制格式的RGB颜色是一个以井号（#）打头的字符串，后面跟着6个字符，其中前两个字符表示红色分量，接下来的两个表示绿色分量，最后两个表示蓝色分量。

创建了实例还需要将实例作为style参数传给World

> ```python
> wd_style=RotateStyle("#336699")
> wd=pygal.maps.world.World(style=wd_style)
> 
> wd_style=RotateStyle("#336699")
> wd=pygal.maps.world.World(style=wd_style,base_style=LightColorizedStyle)
> ```

![image-20210406144514589](https://raw.githubusercontent.com/whr819987540/pic/main/20210406144531.png)

![image-20210406144516304](https://raw.githubusercontent.com/whr819987540/pic/main/20210406144534.png)

![image-20210406144517602](https://raw.githubusercontent.com/whr819987540/pic/main/20210406144538.png)





API调用

我们将编写一个程序，它自动下载GitHub上星级最高的Python项目的信息，并对这些信息进行可视化。

**https://api.github.com/search/repositories?q=language:python&sort=stars**

这个调用返回GitHub当前托管了多少个Python项目，还有有关最受欢迎的Python仓库的信息。

第一部分（https://api.github.com/）将请求发送到GitHub网站中响

应API调用的部分；接下来的一部分（search/repositories）让API搜索GitHub上的所有仓库。

repositories后面的问号指出我们要传递一个实参。q表示查询，而等号让我们能够开始指定查询（q=）。通过使用language:python，我们指出只想获取主要语言为Python的仓库的信息。最后一部分（&sort=stars）指定将项目按其获得的星级进行排序。





```python
import requests
url="https://api.github.com/search/repositories?q=language:python&sort=stars"
try:
    r=requests.get(url)
    r.raise_for_status()
except:
    print("requests forbidden")
else:
    print(r.text)
```

这个API返回JSON格式的信息，因此我们使用方法json()将这些信息转换为一个Python字典，我们将转换得到的字典存储在response_dict中。

返回值包括三个部分，可以转换为json，形成python可以处理的字典，items是列表，里面的元素为字典

> total_count":6813764,"incomplete_results":true,"items":

==大多数API都存在速率限制，即你在特定时间内可执行的请求数存在限制。==

很多API都要求你注册获得API密钥后才能执行API调用。编写本书时，GitHub没有这样的要求，但获得API密钥后，配额将高得多。

![image-20210406151704261](https://raw.githubusercontent.com/whr819987540/pic/main/20210406151704.png)



删除`bar.y_labels=stars`前

![image-20210406153011088](https://raw.githubusercontent.com/whr819987540/pic/main/20210406153011.png)



后

![image-20210406153022424](https://raw.githubusercontent.com/whr819987540/pic/main/20210406153022.png)

横线消失了



想删除图例`stars`

但是只是`bar.add("",stars)` 似乎不管用，只是把图例变成了空字符串

![image-20210406153237981](https://raw.githubusercontent.com/whr819987540/pic/main/20210406153238.png)

`show_legend=False`

我们使用LightenStyle类（别名LS）定义了一种样式，并将其基色设置为深蓝色。我们还传递了实参base_style，以使LightColorizedStyle类（别名LCS）。然后，我们使用Bar()创建一个简单的条形图，并向它传递了my_style。我们还传递了另外两个样式实参：

让标签绕*x*轴旋转45度（x_label_rotation=45），并隐藏了图例（show_legend=False），因为我们只在图表中绘制一个数据系列。接下来，我们给图表指定了标题，并将属性x_labels设置为列表names。



重构：

将配置写到一个对象中，就像style一样

注意，写的是配置，而不是title，xlabel，add这里面的参数



在工具提示中添加内容

现在工具提示中有了name，star，还需要description

之前add的是stars，是一个列表

现在还是add列表，但是里面的元素不只是一个数值，而是字典，字典的value对应直方图的值，label对应直方图工具提示的内容

完整代码

```python
import requests,sys,pygal
from pygal.style import LightenStyle as LS,LightColorizedStyle as LCS
url="https://api.github.com/search/repositories?q=language:python&sort=stars"
try:
    r=requests.get(url)
    r.raise_for_status()
except:
    print("requests forbidden")
    sys.exit()
else:
    content=r.json()
    print(content.keys())
    program_list=content["items"]
    for key in program_list[0]:
        print(key)
    print("得到了"+str(len(program_list))+"个仓库信息")
    names,stars,urls,descriptions=[],[],[],[]
    star_des=[]
    for program in program_list[:20]:
        tmp_dic={}
        names.append(program["name"])
        stars.append(program["stargazers_count"])
        urls.append(program["html_url"])
        descriptions.append(program["description"])
        tmp_dic["value"]=program["stargazers_count"]
        tmp_dic["label"]=program["description"]
        star_des.append(tmp_dic)
        print(tmp_dic)
print(stars)
style=LS("#333366",base_style=LCS)
config=pygal.Config()
config.x_label_rotation=45
config.show_legend=False
config.title_font_size=24
config.label_font_size=12#所有的x轴标签，大部分的y轴标签
config.truncate_label=15#设置标签字符数限制，超过的在工具提示中显示
config.major_label_font_size=16#主标签
#config.show_y_guides=False 去掉到y轴的水平线
bar=pygal.Bar(style=style,config=config)
bar.title="GitHub上最受欢迎的python项目"
bar.x_labels=names
bar.add("",star_des)
bar.render_in_browser()
```



重构代码

```python
test.py
import test_func as tf
url="https://api.github.com/search/repositories?q=language:python&sort=stars"
r=tf.get_html(url)
names, stars, urls, descriptions, star_des = [], [], [], [], []
tf.get_data(r,names, stars, urls, descriptions, star_des)
tf.render(names,star_des)

test_func.py
import requests,sys,pygal
from pygal.style import LightenStyle as LS,LightColorizedStyle as LCS

def get_html(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
    except:
        print("requests forbidden")
        sys.exit()
    else:
        return r

def get_data(r,names, stars, urls, descriptions, star_des):
    """从response里解析出数据"""
    content = r.json()
    print(content.keys())  # 返回的格式是字典
    program_list = content["items"]  # 数据在item-value里
    for key in program_list[0]:
        print(key)
    print("得到了" + str(len(program_list)) + "个仓库信息")
    tmp_dic = {}
    for program in program_list[:20]:
        names.append(program["name"])
        stars.append(program["stargazers_count"])
        urls.append(program["html_url"])
        descriptions.append(program["description"])
        tmp_dic["value"] = program["stargazers_count"]
        tmp_dic["label"] = program["description"]
        star_des.append(tmp_dic)
        print(tmp_dic)
def render(names,star_des):
    style = LS("#333366", base_style=LCS)
    config = pygal.Config()
    config.x_label_rotation = 45
    config.show_legend = False
    config.title_font_size = 24
    config.label_font_size = 12  # 所有的x轴标签，大部分的y轴标签
    config.truncate_label = 15  # 设置标签字符数限制，超过的在工具提示中显示
    config.major_label_font_size = 16  # 主标签
    # config.show_y_guides=False 去掉到y轴的水平线
    bar = pygal.Bar(style=style, config=config, font_family="Yahei Consolas Hybrid")
    bar.title = "GitHub上最受欢迎的python项目"
    bar.x_labels = names
    bar.add("", star_des)
    bar.render_in_browser()
    bar.render_to_file("python_code_rank.svg")
```

![python_code_rank](https://raw.githubusercontent.com/whr819987540/pic/main/20210406183413.svg)

time.strptime(string,format)p是解析，将string（时间字符串）按照指定的格式format，解析为时间元祖

time.strftime(format)将当前时间按照指定的format

```bash
>>> import time
>>> t="2021 9 6"
>>> time.strptime(t,"%Y %m %d")
time.struct_time(tm_year=2021, tm_mon=9, tm_mday=6, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=0, tm_yday=249, tm_isdst=-1)
>>> time.strftime("%Y-%m-%d")
'2021-04-06'
```

将时间戳转化为日期+时间的格式

```bash
>>> import time
>>> now=time.time()
>>> now
1617707730.463211
>>> timeStruct=time.localtime(now)
>>> timeStruct
time.struct_time(tm_year=2021, tm_mon=4, tm_mday=6, tm_hour=19, tm_min=15, tm_sec=30, tm_wday=1, tm_yday=96, tm_isdst=0)
>>> time.strftime("%Y-%m-%d %H:%M:%S",timeStruct)
'2021-04-06 19:15:30'
>>>
```



再添加一个功能：点击任意一个直方，都可以转到对应的url

需要在value，label后再加上xlink





如果文章还没有评论，响应字典中将没有键'descendants'。不确定某个键是否包含在字典中时，可使用方法dict.get()，它在指定的键存在时返回与之相关联的值，并在指定的键不存在时返回你指定的值（这里是0）。

response_dict.get('descendants', 0) 





![image-20210406195052101](https://raw.githubusercontent.com/whr819987540/pic/main/20210406195052.png)





Django是一个**Web****框架**——一套用于帮助开发交互式网站的工具。Django能够响应网页请求，还能让你更轻松地读写数据库、管理用户等。

# Django

Django项目由一系列应用程序组成，它们协同工作，让项目成为一个整体。

## 项目规范

## 创建虚拟环境

虚拟环境是系统的一个位置，你可以在其中安装包，并将其与其他Python包隔离。将项目的库与其他项目分离是有益的。

先为项目新建一个目录，将其命名为learning_log，再在终端中切换到这个目录，并创建一个虚拟环境。

### 代码

```bash
mkdir
cd
python -m venv ll_env（创建名为ll_env）的虚拟环境
没有报错后，激活虚拟环境
ll_env\Scripts\activate
运行activate
直到出现（虚拟环境名）
(ll_env) d:\pythoncode\learning_log\ll_env\Scripts>
停止激活虚拟环境
deactivate
```

## 安装Django

虚拟环境的包和系统的包是不联系的，Django需要自己再安装一遍

> pip install django

Django仅在虚拟环境处于活动状态时才可用。

## 创建项目

首先进入脚本目录，activate

然后执行

> django-admin startproject learning_log .

==特别注意后面还跟着一个逗点==

千万别忘了这个句点，否则部署应用程序时将遭遇一些配置问题。如果忘记了这个句点，就将创建的文件和文件夹删除（ll_env除外），再重新运行这个命令。

目录learning_log包含4个文件，其中最重要的是settings.py、urls.py和wsgi.py。文件

settings.py指定Django如何与你的系统交互以及如何管理项目。在开发项目的过程中，我们将修

改其中一些设置，并添加一些设置。文件urls.py告诉Django应创建哪些网页来响应浏览器请求。

文件wsgi.py帮助Django提供它创建的文件，这个文件名是web server gateway interface（Web服务

器网关接口）的首字母缩写。

![image-20210406205109073](https://raw.githubusercontent.com/whr819987540/pic/main/20210406205109.png)

## 创建数据库（sqllite)

> python manage.py migrate

将修改数据库称为迁移数据库，如果没有，将创建一个数据库

可以看出来mange.py确实是一个类似命令行的工具，相当于提供了一个命令行的入口

## 启动服务器

> python manage.py runserver

Django启动一个服务器，让你能够查看系统中的项目，了解它们的工作情况。当你在浏览器中输入URL以请求网页时，该Django服务器将进行响应：生成合适的网页，并将其发送给浏览器。

> Starting development server at http://127.0.0.1:8000/

URL http://127.0.0.1:8000/表明项目将在你的计算机（即localhost）的端口8000上侦听请求。localhost是一种只处理当前系统发出的请求，而不允许其他任何人查看你正在开发的网页的服务器。

![image-20210406210029600](https://raw.githubusercontent.com/whr819987540/pic/main/20210406210029.png)



当使用ctrl+c关闭服务器时，服务再对该url进行访问

### 更换端口

如果8000端口不可用（默认），换一个端口即可

> python manage.py runserver 8001

## 创建应用程序

先激活，然后进入项目目录

> python manage.py startapp learning_logs

在该目录下生成

![image-20210406213039110](https://raw.githubusercontent.com/whr819987540/pic/main/20210406213039.png)



### 创建模型

进入learning_logs，有models.py文件，专门存放模型

模型告诉Django如何处理应用程序中存储的数据。在代码层面，模型就是一个类，就像前面讨论的每个类一样，包含属性和方法。

```python
from django.db import models

# Create your models here.
class Topic(models.Model):
    """用户学习的主题"""
    text=models.CharField(200)
    added_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
```



### 激活应用程序

进入project的目录，learning_log的settings文件

在installed_apps（元组）里面添加自己的app名称

### 建立数据库

接下来，需要让Django修改数据库，使其能够存储与模型Topic相关的信息。

> python manage.py makemigrations learning_logs

命令makemigrations让Django确定该如何修改数据库，使其能够存储与我们定义的新模型相关联的数据

输出表明Django创建了一个名为0001_initial.py的迁移文件，==这个文件将在数据库中为模型Topic创建一个表。==

![image-20210406214024837](https://raw.githubusercontent.com/whr819987540/pic/main/20210406214024.png)

最后一行表明learning_logs app在迁移时正常

## 创建超级用户

> python manage.py createsuperuser



## 注册模型

![image-20210406214547652](https://raw.githubusercontent.com/whr819987540/pic/main/20210406214547.png)

在应用程序目录下，有admin文件

导入模型，注册模型

```python
from learning_logs.models import Topic
admin.site.register(Topic)
```

## 添加新模型后

- 修改models.py
- python manage.py makemigrations app_name

- python manage.pu migrate
- 在admin中注册模型

然后检查数据库迁移的输出是否正确

```bash
(ll_env) D:\pythoncode\learning_log>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, learning_logs, sessions
Running migrations:
  Applying learning_logs.0002_entry... OK

```



第二步报错

```bash
TypeError: __init__() missing 1 required positional argument: 'on_delete'
在Django2中，如果用了外键，必须声明如果外键删除，对这个表进行什么操作
	on_delete=None,               # 删除关联表中的数据时,当前表与其关联的field的行为
	=models.CASCADE,     # 删除关联数据,与之关联也删除
	on_delete=models.DO_NOTHING,  # 删除关联数据,什么也不做
	on_delete=models.PROTECT,     # 删除关联数据,引发错误ProtectedError
	# models.ForeignKey('关联表', on_delete=models.SET_NULL, blank=True, null=True)
	on_delete=models.SET_NULL,    # 删除关联数据,与之关联的值设置为null（前提FK字段需要设置为可空,一对一同理）
	# models.ForeignKey('关联表', on_delete=models.SET_DEFAULT, default='默认值')
	on_delete=models.SET_DEFAULT, # 删除关联数据,与之关联的值设置为默认值（前提FK字段需要设置默认值,一对一同理）
	on_delete=models.SET,         # 删除关联数据,
	 a. 与之关联的值设置为指定值,设置：models.SET(值)
	 b. 与之关联的值设置为可执行对象的返回值,设置：models.SET(可执行对象)

```

通过一个测试，在entry下创建了两个属于test（Topic）的记录，删除记录，对test（Topic）没有影响；选择`on_delete=models.CASCADE` ，删除test（关联数据），下面的记录都没了



## 学习之处

嵌套定义的meta类

对于返回的字符串，只显示前五十个

## 内置的shell

```bash
>>> from learning_logs.models import Topic
>>> t=Topic.objects.all()#获取模型中的所有对象
>>> t
<QuerySet [<Topic: Goland>, <Topic: Python>, <Topic: Chess>, <Topic: Rock Climbing>]>
>>> for topic in t:#遍历对象（列表）
...     print(topic.id,topic)
...
1 Goland
2 Python
3 Chess
4 Rock Climbing
>>> first=Topic.objects.get(id=1)#根据id获得对象
>>> first
<Topic: Goland>
>>> first.text
'Goland'
>>> first.added_time
datetime.datetime(2021, 4, 6, 13, 51, 39, 751377, tzinfo=<UTC>)
>>> chess=Topic.objects.get(id=3)
>>> chess.added_time
datetime.datetime(2021, 4, 6, 13, 52, 18, 872763, tzinfo=<UTC>)
>>> chess.entry_set.all()
<QuerySet [<Entry: django 升级到2.0之后,表与表之间关联的时候,必须要写on_delete参数,否则会报异常:...>, <Entry: In the opening
 phase of the game, it’s important t...>]>

```

类名（小写）_set表示通过外键关系获取数据

## 创建网页

使用Django创建网页的过程通常分三个阶段：定义URL、编写视图和编写模板

### 定义url模式

URL模式描述了URL是如何设计的，让Django知道如何将浏览器请求与网站URL匹配，以确定返回哪个网页。

模块admin.site.urls定义了可在管理网站中请求的所有URL。

> ```python
> path(r'',include(("learning_logs.urls","learning_logs"),namespace='learning_logs'))
> 如果在urlpatterns里面指定了namespace，需要给include一个二元组，一个是urls，一个是app_name
> ```

### 编写模板

模板定义了网页的结构，指出网页是什么样的，当网页被请求时，填入相关数据即可

模板能够访问视图提供的数据

数据库专家可专注于==模型==，程序员可专注于==视图代码==，而Web设计人员可专注于==模板==

## 创建其他网页

### 模板（html）继承

由于站点的所有网页都可能有一些相同的元素，所有把他们写到一个通用的父模板中，然后其他网页进行继承，而不必重复定义，同时便于修改

在大型项目中，通常有一个用于整个网站的父模板——base.html，且网站的每个主要部

分都有一个父模板。每个部分的父模板都继承base.html，而网站的每个网页都继承相应

部分的父模板。这让你能够轻松地修改整个网站的外观、网站任何一部分的外观以及任

何一个网页的外观。这种配置提供了一种效率极高的工作方式，让你乐意不断地去改进

网站。

#### 模板标签

一般的超链接这样写

`<a href="link_url"> link_text</a>`

为了保持动态的更新

`<a href="{% url'learning_logs:index'%">Learning Log</a>`

模板标签，它是用大括号和百分号（{% %}）表示的。模板标签是一小段代码，生成要在网页中显示的信息。在这个实例中，模板标签{% url 'learning_logs:index' %}生成一URL，该URL与learning_logs/urls.py中定义的名为index的URL模式匹配

learning_logs是一个命名空间，而index是该命名空间中一个名称独特的URL模式

这样写，在后面的所有网页中都包含了到index（主页）的链接，即使主页的url发生了变动

![image-20210407102644239](https://raw.githubusercontent.com/whr819987540/pic/main/20210407102644.png)

块标签，子模板中不是需要使用全部的块标签，按需定义并使用

> ```python
> <a href="{% url 'learning_logs:index' %}">Learning Log</a>
> ```

特别注意{%中间没有空格，和url之间有空格，url和字符串有空格，字符串结束和%}有空格

#### 重写index.html

首先声明继承哪个父模板

> {% extends ”learning_logs/base.html” %}

然后就是可选部分的block content和固定的回到主页的超链接

#### 生成topic页面

##### url模式

规定localhost:port/topics/返回所有主题页面

##### 视图

在views.py文件中

先返回所有的topic，存储到一个字典中，然后渲染

```python
def topics(request):
    topics=Topic.objects.order_by("added_time")
    context={"topics":topics}
    return render(request,"learning_logs/topics.html",context)
```

##### 模板

继承base.html

```html
<ul>
    {% for topic in topics %}
        <li>{{ topic }}</li>
    {% empty %}
    <li>No topics</li>
    {% endfor %}
</ul>
```

ul是unorder list无序标签

所以需要在view里面对数据进行处理

实际上，model写模型，viem处理数据，html写模板，加载数据

for也是一个标签，处理topics数据

<li> 是无序列表的每一项

for不用缩进代表结束，而是endfor

如果为空，用empty标签表示





#### 生成topic下的entry页面

点击topic转到对应的entries

##### url

一个topic对应一组entry，对应的url用topic的id表示，即localhost:8000/logs/topics/topic_id

显示topic的所有entry

## 添加topic

添加topic的关键是让用户输入数据，让用户输入并提交信息的页面是表单，需要导入包含表单的模块forms.py

对于输入的信息还需要进行验证，然后存储

生成表单

```python
import learning_logs.models as m
from django import forms

class TopicForm(forms.ModelForm):
    class Meta():
        model=m.Topic#根据哪个模型创建表单
        field=['text']#根据模型的哪个字段创建表单
        #labels = {'text': ''}
```

viem函数

首先显示出表单，然后得到数据，提交到数据库，将页面重定向到之前的topics

如果提交了表单，且表单的数据有效，进行重定向

```python
elif request.method=="POST":
    #获取数据
    form=TopicForm(request.POST)
    if form.is_valid():
        form.save()
        #重定向
        return HttpResponseRedirect(            return HttpResponseRedirect(reverse("learning_logs:topics"))
```

reverse根据url模型确定url，HttpResponseRedirect根据url进行重定向，返回url对应的界面，相当于再次发起GET请求

用户输入的数据放在request.POST里面

创建空的表单，或根据post的数据创建

Django使用模板标签{% csrf_token %}来防止攻击者利用表单来获得对服务器未经授权的访问（这种攻击被称为跨站请求伪造）。

显示表单

```python
{{ form.as_p }}
<button name="submit">add topic</button>
as_p表示把form表单在前端页面渲染成p标签的形式展示，此外还有as_ul,as_table等。
```



## 添加entry

相比于添加topic，entry多了一点：确定当前的topic，这需要作为参数（因为外键的存在）

在添加界面，先显示当前的topic





## 修改topic

## 修改entry

在topic界面每一个entry下面都有一个`edit this entry` 点击后，进入edit_url，然后提交表单，对entry进行更新

![image-20210407200038379](https://raw.githubusercontent.com/whr819987540/pic/main/20210407200038.png)

from中是action，不是actions

button中是submit，不是commit

method=是单引号，不是双引号

## 删除entry

在topic下面加一个，delete链接，然后直接删除id对应的entry



## 关于模板

在定义模板的时候，实际上给出了可以自由发挥的地方，没有定义的地方根本不会显示，比如这个

![](https://raw.githubusercontent.com/whr819987540/pic/main/20210407192339.png)

结果是：

![image-20210407192403929](https://raw.githubusercontent.com/whr819987540/pic/main/20210407192403.png)



## 统计topic的entry数目(undone)

==其实就是统计entry_set里面的个数，涉及数据处理，即使是这种计数，也要将处理过程完全放到viem视图函数中，模板无法处理的==

只需要在topic model里面加上entry_num字段

==记住！==

对模型更改后，必须更新数据库

数据无法保持，一直为0



## 第二个应用程序

这个应用程序的功能是进行用户管理

先创建app（users）

==还要将app添加到项目的settings中，机器不会自动添加==

具体是installed apps

==还要将这个app的url加到项目的urls里面==

## 真正的主界面

应该是登录界面，如果登录完成，记录cookie，就可以跳转到自己的logs界面了

![image-20210407213024556](https://raw.githubusercontent.com/whr819987540/pic/main/20210407213024.png)



input 是指表单在输入时的配置

value是输入成功重定向的位置

利用内置的login视图函数

```python
url(r'login/$',LoginView.as_view(template_name='users/login.html'),name="login"),
```

奇妙的是，django自动去数据库里找用户

之前创建了admin用户，可以进行登录

现在随意输入的都无法登录成功

![image-20210407215327112](https://raw.githubusercontent.com/whr819987540/pic/main/20210407215327.png)



## 在CMD中创建用户

超级用户 `python manage.py createsuperuser` 

创建普通用户是对数据库进行操作

models顾名思义，是在auth（认证）的时候用到的模型（User）

```python
from django.contrib.auth.models import User
user=User.objects.create_user()
u=User.objects(username='name')
u.set_password('123456')
u.save()
```

查看用户

```bash
>>> from django.contrib.auth.models import User
>>> users=User.objects.all()
>>> users
<QuerySet [<User: admin>, <User: foreigh>]>
>>> f=users[1]
>>> f
<User: foreigh>
>>> f.set_password("123456")
>>> f.save()
```

![image-20210407221114420](https://raw.githubusercontent.com/whr819987540/pic/main/20210407221114.png)

![image-20210407221130264](https://raw.githubusercontent.com/whr819987540/pic/main/20210407221130.png)



此时还没有保存，所以提醒错误

如果保存了

![image-20210407221204433](https://raw.githubusercontent.com/whr819987540/pic/main/20210407221204.png)



## 对base进行修改

如果登录了，不显示登录链接，而是显示用户名

在users app中，url用到了内置的view，view的返回值中，有user



在Django身份验证系统中，每个模板都可使用变量user，这个变量有一个is_authenticated

属性：如果用户已登录，该属性将为True，否则为False。这让你能够向已通过身份验证的用户

显示一条消息，而向未通过身份验证的用户显示另一条消息。

## 退出登录界面

如果登录成功，在问候语后面加上logout

首先写url，url视图就是调用内置logout，然后重定向。

## 注册

现在的用户注册只能在后台执行，现在以表单的形式给出

UserCreationForm

这个表单里面有username，password1，password2,（检验两次密码是否相同）

方法save()返回新创建的用户对象，我们将其存储在new_user中。



## 权限问题

其实到这里，用户管理只是实现了login和logout，最重要的权限管理还没有，所以下面进行权限管理

权限包括：

用户只能看到并修改自己的topics，entries

相当于在topic-entry模型上加了user-topic-entry，将user作为topic的外键

![image-20210408105520973](https://raw.githubusercontent.com/whr819987540/pic/main/20210408105521.png)

### 装饰器

用了装饰器@login_required

装饰器是放在函数定义前面的指令

在运行函数前，根据装饰器修改函数代码的行为

### 第一步，只允许login时访问topics

在topics的视图函数（加载数据）前，加上内置的login_required装饰器

![image-20210408111618061](https://raw.githubusercontent.com/whr819987540/pic/main/20210408111618.png)

让Python在运行topics()的代码前先运行

login_required()的代码。

login_required()的代码检查用户是否已登录，仅当用户已登录时，Django才运行topics()

的代码。==如果用户未登录，就重定向到登录页面。==

要告诉django具体重定向到哪儿，也就是哪儿是登录页面

在settings里面加上`LOGIN_URL='/users/login/'`

关于`LOGIN_URL='/users/login/'`

==第一个/确实玄学==

哪些界面与权限无关：主页，login，register

可能想，只给topics加装饰器就行了，因为后面的加主题加entry首先都得看到topics界面

这是从html的角度进行的思考，然而html只是进行数据显示，真正给数据的是view，应该从view角度思考

如果别人知道了站点的结构，那么可以直接访问页面，而不去按照站长定义的规则一步步跳转，这样是危险的，必须给每一个函数都加上装饰器

![image-20210408122432083](https://raw.githubusercontent.com/whr819987540/pic/main/20210408122432.png)

现在直接访问页面，首先得给出数据，而给出数据之前，首先得执行装饰器，验证是否登录

![image-20210408122838189](https://raw.githubusercontent.com/whr819987540/pic/main/20210408122838.png)



### 将数据和user对应起来

user-》topic-》entry

首先在topic model里面加上外键

`owner=models.Foreign(User,	on_delete=models.CASCADE)`







#### 问题

现在的问题是之前创建的topic是没有owner的，那么如何迁移数据库呢？

一个方法是都迁移给admin

```python
python manage.py makemigrations
选择user的id
python manage.py migrate
```

然后重新打开服务器，重新进入shell

![image-20210408125253346](https://raw.githubusercontent.com/whr819987540/pic/main/20210408125253.png)

测试一下，用非admin账户添加topic

不行，因为原始的代码没有给topic.owner赋初值，而这个作为外键不能为空

所以在view函数里面，当form valid时，指定

`form.instance.owner=request.user`

```bash
Goland admin
Python admin
Chess admin
Rock Climbing admin
C++ admin
test for this admin
topic for test admin
tt test
```



## 选择性显示topic

不只是要对login的用户，而且要对特定的login用户显示数据

登录后，有了request.user，在加载topic的时候加上过滤器

`filter(owner=request.user)`

但这也只是在属于html级别的限制，只是限制了用户看到的，用户也可以对页面直接进行访问

当前登录admin，tt属于test用户

![image-20210408143053605](https://raw.githubusercontent.com/whr819987540/pic/main/20210408143053.png)

但是通过url直接访问了，所以在加载topic的时候也需要验证

![image-20210408143111992](https://raw.githubusercontent.com/whr819987540/pic/main/20210408143112.png)

在显示topic之前，验证topic的owner和request的user

又一个bug，虽然不能直接通过url访问topic，但是可以进入entry的修改界面，相当于也能看到entry



## 设置样式Bootstrap

使用应用程序django-bootstrap3，这也让你能够练习使用其他Django开发人员开发的应用程序。

开发路线：关注功能-》关注样式

功能实现是首先要完成的，只有功能有了才能谈美化

### 安装

`pip install django-bootstrap3`

我们需要让django-bootstrap3包含jQuery，这是一个JavaScript库，让你能够使用Bootstrap模板提供的一些交互式元素。

### 放到settings中

```python
INSTALLED_APPS=[
    'bootstrap3',
]
BOOTSTRAP3={
    'include_jquery':True,
           }
```



### 关于BOOTSTRAP

Bootstrap基本上就是一个大型的样式设置工具集，它还提供了大量的模板，你可将它们应用于项目以创建独特的总体风格。



### 使用

复制模板，修改，换成自己的内容



#### 修改base.html



## 对于topics的排序

加一个字段，修改时间，这个字段根据内部entry的修改时间来确定，防止长期不更新的topic一直占据位置

这个字段在edit_topic new_entry edit_entry时都会更新

 null=True表示该字段可以为空

order_by(‘字段’)从上往下，升序排列（时间而言，是先显示比较早的，不合理）

order_by（‘-字段’）降序排列（先显示时间戳大的，是后添加或修改的，是最新的，合理）

auto_time_add是个大bug，只是在创建元素的时候加入时间，而不进行自动更新，这样在动态变化的时间字段中会出问题



## 删除topic功能

一个bug对于

![image-20210408185940590](https://raw.githubusercontent.com/whr819987540/pic/main/20210408185940.png)



![image-20210408185958700](https://raw.githubusercontent.com/whr819987540/pic/main/20210408185958.png)



报错在说，需要两个参数，但实际上只给了一个，原因是默认接收位置参数（有默认值），但我们想传入的是关键字参数id



## 删除entry功能

和删除topic差不多

## 修改topic

和修改entry差不多



## 怎么写自己的装饰器



## 常用模块总结

```python
from django.contrib.auth.decorators import login_required
```



## django的时间

在setting里面有两个参数

USE_TZ，TIMEZ-ZONE

use_tz的优先级最高，true设置为默认时区，false时，设置为time_zone

## 

## 特别注意migrate

==如果migrate总是不通过，而比较确定自己的代码没有问题，直接把app里面的migrations文件里面的除了init都删了，然后把数据库删了。然后，重新makemigrations，migrate就ok了==



## 加载图片

首先需要配置，然后建立文件夹

```python
STATIC_URL='/static/'
STATICFILES_DIRS=[
   os.path.join(BASE_DIR,'static')
]#不要忘记import os，然后重启服务器
```

在app的目录下，建立static/images目录

![image-20210408220929081](https://raw.githubusercontent.com/whr819987540/pic/main/20210408220929.png)

 

```
<body style="background-image: url({% static 'images/most.png' %});
        background-size:100% 200%;background-repeat:no-repeat;">
```

# undone

在index界面给出到各个app的超链接

以防走失（相当于入口函数）



admin 824655

foreign 123456

test 824655whr

## python传参数的类型

```python
def add(first=0,*args):
    print(type(args))
    #元组，args接受任意参数，所以要先放置必须给出的位置参数，然后给args
    for v in args:
        first+=v
    return first
def out(first=0,**kwargs):
    #给关键字参数传值不能用字典，虽然传入后，kwargs成为了字典，相当于把
    #传入的键值对整合到字典里面
    print(type(kwargs))
    for key,value in kwargs.items():
        print(key)
        print(value)
def out_again(*args,**kwargs):
    for v in args:
        print(v)
    for key,value in kwargs.items():
        print(key)
        print(value)
print(add(0,1,2,3,4,5,6,7,8,9,10))
# out(12,{"value1":1,"value2":"string"})#keargs要以key=value的形式传参
out(12,value1="string1",value2=12)
dic={"value1":1,"value2":"string"}
out_again(1,2,3,4,5,dic)#这个dic被视为args的一部分
out_again(1,2,3,4,5,value1="string1",value2=12)

```

































![image-20210408144338575](https://raw.githubusercontent.com/whr819987540/pic/main/20210408144338.png)

![](https://raw.githubusercontent.com/whr819987540/pic/main/20210408144341.png)