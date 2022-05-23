# python的异常处理：

分为try，except和else

try里面放可能引发异常（当python发现有异常时，会返回一个异常对象，然后停止程序，如果不进行处理）的代码；except+异常名，返回异常名对应的异常对象时，执行什么；如果except不加，表示无论有什么异常，都执行下面的代码（这可能不知道发生了什么错误，但是从结果来看，如果只想知道是否正确执行而不关心发生了什么错误，是可行的）。对于错误，我们可能不知道可能有多少（在调试的时候），可以先写已知的错误+异常名，然后再写没有异常名的except，来提示我们发生了新的错误或者是unknown error；else是当try中的代码执行完毕，且没有抛出任何异常时执行的内容

```python
#不关心具体发生了什么错误
try:
    print(12/0)
except:
    print("error")
else:
    print("success")
    
#知道具体的错误
try:
    print(12/0)
except ZeroDivisionError:
    print("ZeroDivisionError")
else:
    print("success")
    
#知道一个错误，还有潜在的错误
while 1:
    print("division calculator,any time 'q' to quit")
    left=input("除数=")
    if left=='q':
        break
    right=input("被除数=")
    if right=='q':
        break
    try:
        print(left/right)
    except ZeroDivisionError:
        print("0不能作为除数")
    except:
        print("unknown error")
    else:
        print("continuing")
division calculator,any time 'q' to quit
除数=13
被除数=12
存在别的问题
division calculator,any time 'q' to quit
除数=q

检查后，发现是type error（把except去掉即可）
进行类型转换即可


while 1:
    print("division calculator,any time 'q' to quit")
    left=input("除数=")
    if left=='q':
        break
    right=input("被除数=")
    if right=='q':
        break
    try:
        print(int(left)/int(right))
    except ZeroDivisionError:
        print("0不能作为除数")
    except:
        print("存在别的问题")
    else:
        print("continuing")

除数=12
被除数=3
4.0
continuing
division calculator,any time 'q' to quit
除数=16
被除数=4
4.0
continuing
division calculator,any time 'q' to quit
除数=a
被除数=12
存在别的问题
division calculator,any time 'q' to quit
除数=

加上except:后，发现又有新的问题了，再去掉except
发现是ValueError（不匹配/这个运算符）

除数=12
被除数=3
4.0
continuing
division calculator,any time 'q' to quit
除数=a
被除数=13
只能输入整数，请重试
division calculator,any time 'q' to quit
除数=13a
被除数=13
只能输入整数，请重试
division calculator,any time 'q' to quit
除数=13
被除数=5
2.6

现在程序就很健壮了，不会因为I/O的导致程序崩溃了
最后，可以在else后面加上finally，就是不管有没有异常，不管进入了except还是else，都会执行finally
除数=12
被除数=3
4.0
continuing
in finally
```



# 打开文件

```python
with open(filename) as name:
    xxx
首先执行open，打开对应的文件，如果打不开，抛出异常，然后为我们关闭
相比于open的好处在于，如果程序打开了文件，而在打开过程中，发生了错误，程序中断了，即使我们写了name.close()，但是程序也不会执行，这样就会导致文件的数据丢失，而with实际上是
try:
    name=open(filename)
    xxxx
except:
    print("somr error")
finally:
    name.close()
    

try:
    name=open("1.txt")
    print(10/0)
except:
    print("somr error")
finally:
    try:
        name.close()
    except NameError:
        print("文件未打开")
    print("in finally")
    
somr error
文件未打开
in finally

try:
    name=open("1.txt")
except FileNotFoundError:
    print("文件没打开")
else:
    try:
        print(10/0)
    except:
        print("打开了，发生错误")
    finally:
        name.close()
        print("in 2 finally")
这种写法更清晰
先看打开了没有，如果没有，直接退出
如果打开了，再进行，不管有没有异常，finally关闭文件

```



相关函数

```python
#逐行读取，迭代器
for line in f:
    line就是每一行内容（包括结尾的换行符）
    
with open("data.txt") as f:
    for line in f:
        print(line)

3.1415926535

 8979323846

 2643383279



#逐行读取，自己控制
line = f.readline()
相当于
while 1:
    line=f.readline()
    if line=="":
        break
        
        
with open("data.txt") as f:
    content = f.readline()
    print(content)
3.1415926535

with open("data.txt") as f:
    while 1:
        content = f.readline()
        if content=="":
            break
        else:
            print(content)
            

3.1415926535

 8979323846

 2643383279

#读取所有行，返回每行构成的一个列表，忽略EOF
contents = f.readlines()
with open("data.txt") as f:
    contents = f.readlines()
print(contents)
print(type(contents))

['3.1415926535\n', ' 8979323846\n', ' 2643383279']
<class 'list'>

#读取所有内容，返回一个字符串，忽略了EOF
with open("data.txt") as f:
    contents = f.read()

print(contents)
print(type(contents))
3.1415926535
 8979323846
 2643383279
<class 'str'>

相当于
with open("data.txt") as f:
    contents = f.readlines()
    content = "".join(contents)

print(content)
print(type(content))
3.1415926535
 8979323846
 2643383279
<class 'str'>
对于join，str.join(iterable)
实际上
res=""
for i in itetable_object:
    res=res+i+str
```



with open不会对文件不存在的错误进行处理，所以还得加上一层try

```python
try:
    with open("ds.txt") as f:
        contents=""
        for line in f:
            contents+=line.strip()
except FileNotFoundError:
    print("ds.txt not exist")
else:
    print(contents)
```



# 对数组元素的访问

```python
list=[]
for i in range(20):
    list.append(i)
print(list)
print(list[:5])#前五个元素
print(list[-5:])#后五个元素
```



string.split(str)首先是返回值，string并不被分割（保证原始数据的完整性），返回一个列表，str作为分割符，不会出现在返回的数组中

```python
str="123456789"
str=str.split("5")
print(str)
['1234', '6789']
```



在一次with open里面，如果需要多次对文件进行全部读写，就是想移动在GUI界面下，光标的位置，有file.seek(int1,int2)函数

int2指示了相对位置，0为文件头，1为当前位置，2位文件尾

int1是偏移量，相对于int2的偏移位置

如果完全读取后，不修改文件指针的位置，后面啥都读不到

```python
name="data.txt"
try:
    with open(name,mode='r',encoding="utf-8") as f:
        #读取整个文件
        content1 = f.read()
        print(content1)
        #遍历
        f.seek(0,0)
        for line in f:
            print(line,end="")
        print("")
        #将行放到一个列表中
        f.seek(0,0)
        content2=f.readlines()
        #打印三次
except FileNotFoundError:
    print(name+" not exist")
print(content2)
```



# 文件写操作：

还是用with open，mode=‘w’

对于r及其变体，文件不存在会出现FileNotFound的异常；对于w及其变体，如果文件存在，都会覆盖，如果文件不存在，会新建；对于a及其变体，如果文件存在，文件指针都在文件尾，如果不存在，会新建文件。

```bash
r:    以只读方式打开文件。文件的指针将会放在文件的开头。这是**默认模式**。
rb: 以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
r+: 打开一个文件用于读写。文件指针将会放在文件的开头。
rb+:以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
w:    打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
wb:    以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
w+:    打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
wb+:以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
a:    打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
ab:    以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
a+:    打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
ab+:以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
```



```python
file_name = "w.txt"
with open(file_name,"a+",encoding="utf-8") as f:
    #在a追加模式下，文件指针默认放在文件尾，如果后续要读入，需要seek
    f.write("this is a test for write")
    f.seek(0,0)
    content = f.read()
print(content)
print("over")

this is a test for writethis is a test for write
over
this is a test for writethis is a test for writethis is a test for write
over
```



关于字符计数，如果要计算一本英文文本中有多少单词，由于结尾‘\n’的存在，再用spilt的时候，如果是空行，也会参与计数

```python
filename = "novel.txt"
try:
    with open(filename,encoding="utf-8") as f:
        count=0
        for i in range(3):
            line=f.readline()
            print(line.split(" "))
            count+=len(line.split(" "))
        print("words: "+str(count))
except FileNotFoundError:
    print(filename+" not exist")


['\n']
['The', 'Project', 'Gutenberg', 'EBook', 'of', 'Alice’s', 'Adventures', 'in', 'Wonderland,', 'by', 'Lewis', 'Carroll\n']
['\n']
words: 14
    

for i in range(3):
    line=f.readline()
    if not line=='\n':
        print(line.split(" "))
        count+=len(line.split(" "))	
['The', 'Project', 'Gutenberg', 'EBook', 'of', 'Alice’s', 'Adventures', 'in', 'Wonderland,', 'by', 'Lewis', 'Carroll\n']
words: 12
    

```



编写得很好且经过详尽测试的代码不容易出现内部错误，如语法或逻辑错误，但只要程序依赖于外部因素，如用户输入、存在指定的文件、有网络链接，就有可能出现异常。凭借经验可判断该在程序的什么地方包含异常处理块，以及出现错误时该向用户提供多少相关的信息。

# json模块

不管专注的是什么，程序都把用户提供的信息存储在列表和字典等数据结构中。用户关闭程序时，你

几乎总是要保存他们提供的信息；一种简单的方式是使用模块json来存储数据。

模块json让你能够将简单的Python数据结构转储到文件中，并在程序再次运行时加载该文件

中的数据。你还可以使用json在Python程序之间分享数据。==更重要的是，JSON数据格式并非Python==

==专用的，这让你能够将以JSON格式存储的数据与使用其他编程语言的人分享==。



两个内置函数

json.dump()  数据流：内存->文件，需要指定写入的数据和文件对象

因此，首先应该打开一个文件（a/w)

json.load()数据流：文件->内存，指定一个文件对象（至少是r），返回内容

==这个load也比较有意思，只支持用‘r’方式打开文件，如果是‘a'就不行==



str.isdigit()可以用来判断字符串里面的字符是不是都是[0-9]



# 重构



对于比较简单的程序，似乎真的没有重构的必要，每一层的逻辑都不是很复杂

```python
# 编写一个程序，提示用户输入他喜欢的数字，并使用
# json.dump()将这个数字存储到文件中。再编写一个程序，从文件中读取这个值，并打
# 印消息“I know your favorite number! It’s _____.”。
# 10-12 记住喜欢的数字：将练习 10-11 中的两个程序合而为一。如果存储了用户喜
# 欢的数字，就向用户显示它，否则提示用户输入他喜欢的数字并将其存储到文件中。运
# 行这个程序两次，看看它是否像预期的那样工作。
import json
def get_num(filename):
    try:
        with open(filename) as f:
            return json.load(f)
    except FileNotFoundError:
        return None
def create_num(filename):
    with open(filename,'w') as f:
        while 1:
            num=input("input your fav num:")
            if num.isdigit():
                json.dump(num,f)
                return num
                break
def out(filename):
    num=get_num(filename)
    if num:
        print("your fav num is ",num)
    else:
        num=create_num(filename)
        print("ok I know ",num," is your fav num")

filename="num.json"
out(filename)
```



# 类



首先是init方法，类似于构造函数，在创建实例时，执行。

__ init __(self,para list)

self不可缺少，且只能位于第一个参数的位置

当调用init创建实例时，self是指向实例本身的引用，进而让类中的方法能够访问到这些数据对象。

> 我们将方法__init__()定义成了包含三个形参：self、name和age。在这个方法的定义中，形
>
> 参self必不可少，还必须位于其他形参的前面。为何必须在方法定义中包含形参self呢？因为
>
> Python调用这个__init__()方法来创建Dog实例时，将自动传入实参self。每个与类相关联的方法
>
> 调用都自动传递实参self，它是一个指向实例本身的引用，让实例能够访问类中的属性和方法。
>
> 我们创建Dog实例时，Python将调用Dog类的方法__init__()。我们将通过实参向Dog()传递名字和
>
> 年龄；self会自动传递，因此我们不需要传递它。每当我们根据Dog类创建实例时，都只需给最
>
> 后两个形参（name和age）提供值。

Dog类还定义了另外两个方法：sit()和roll_over()）。由于这些方法不需要额外的信息，如名字或年龄，因此它们只有一个形参self，只需要能够访问实例即可，具体来说是实例的属性

 my_dog = Dog('willie', 6) 

init函数中并没有显式的return，但的确返回了这样一个实例，并用变量存起来



你需要执行的一个重要任务是修改实例的属性。你可以直接修改实例的属性，也可以编写方法以特定的方式进行修改。

如果init中某个属性有默认值，就无须包含形参

## 修改属性的值

- 直接访问属性并修改
- 通过方法提供参数，进行修改
- 通过方法递增

## 继承

创建子类时，父类必须包含在当前文件中，且位于子类前面。

```python
class ElectricCar(Car): 
    """电动汽车的独特之处""" 

    def __init__(self, make, model, year): 
        """初始化父类的属性""" 
        super().__init__(make, model, year)
```

super()是一个特殊函数，类似于返回父类，然后执行父类的init，这样子类就有了父类的所有属性。

然后子类有父类没有的属性和方法

同样是参数化的

```python
class ECar(Car):
    def __init__(self, make, model, year,size,odometer_reading=0):
        super().__init__(make, model, year,odometer_reading)
        self.battery_size=size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
```

如果子类中的方法与父类的重名，优先使用子类中对该方法的定义，也就是进行覆盖

## 嵌套定义

当类中的方法和属性比较多时，可以将一部分拿出来，放到单独的一个类中，然后将这个类的实例作为大类的一个属性

```python
class ECar(Car):
    def __init__(self, make, model, year,size,odometer_reading=0):
        super().__init__(make, model, year,odometer_reading)
        self.battery=Battery(size)

class Battery():
    def __init__(self,size):
        self.size=size
    def describe(self):
        print("This car has a " + str(self.size) + "-kWh battery.")

c=Car('tesla', 'model s', 2016)
print(c.get_descriptive_name())

e=ECar('tesla', 'model s', 2016,70)
e.battery.describe()
```



## 编写自己的模块

应为自己创建的每个模块都编写文档字符串。

```python
""""""
```

from 文件名（不需要带.py）import 类名

```python
from user import Admin
admin=Admin("Jack Brown",24,["go home at any time","delete"])
admin.privileges.show_privileges()

can add post, can delete post, can ban user, 
go home at any time, delete, 
```

这样多出了一点显示，因为user.py文件里面有使用类的代码

在user.py的非定义部分，这样写：

```python
if __name__=="__main__":
    admin = Admin("Jack Brown",22,["can add post","can delete post","can ban user"])
    admin.privileges.show_privileges()
```

__ name __  ，只有在当前文件被执行时，值才是__ main __，也就是只有在当前文件被执行时，里面的代码才会被使用

此时再执行using_module_user.py就不会执行user.py里面的那部分代码了

![image-20210328204133857](https://raw.githubusercontent.com/whr819987540/pic/main/20210328204133.png)



### 写法：

```python
#导入模块的一个类
from car import ECar
#导入模块的多个方法
from car import ECar,Car
#导入整个模块
import car [as] 
```

如果你喜欢模块和文件的交互方式，可在项目开始时就尝

试将类存储到模块中。先找出让你能够编写出可行代码的方式，再尝试让代码更为组织有序。



### 有序字典

模块collections，OrderedDict类

```python
from _collections import OrderedDict
import re
def read(filename):
    try:
        with open(filename)as f:
            dic=OrderedDict()
            for line in f:
                line=line.replace("   "," ")
                line=line.strip()
                contents=line.split(" ")
                if len(contents)>1:
                    dic[contents[0]]=contents[1]
            return dic
    except FileNotFoundError:
        print(filename+" not exists")
def search(dic):
    while 1:
        target = input("input the words you wanna search:(q to quit) ")
        if target == 'q':
            break
        for key, value in dic.items():
            if key == target:
                print(key + "  " + value)
                break
        if key != target:
            print(target + " not found")
            
file_name="E:/qt/008/dic.txt"
dic=read(file_name)
search(dic)
```



###  randint

random的randint方法，返回[a,b] 之间的一个随机整数

## 书写类的风格

- 命名：对于类名，采用驼峰命名法，每个单词首字母大写，不用下划线，如MyRestaurant；对于实例和模块，都小写，用下划线，如my_tesla
- 对于类，在class name():下面跟一个文档字符串“”“”。
- 类中，一个空行分割方法
- 模块中两个空行分割类
- import时，先导入标准库；加一个空行，导入自己的模块



# 代码测试（很重要）



unittest (单元测试)

## 对单个函数的测试

- 命名规范：类名是xxxTestCase，继承unittest.TestCase
- 对函数的每一个测试方法都必须是test_func_name，因为会自动执行类中以test开头的方法
- 用到__ name __ == ”__ main __”

```python
import unittest

from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    def test_formatted_name(self):
        self.assertEqual(get_formatted_name("jack","brown"),"Jack Brown")


if __name__ == '__main__':
    unittest.main()
```



## 对类的测试

断言方法

- assertEqual （a，b）
- assertNotEqual（a，b）
- assertTrue（x）
- assertFalse（x）
- assertIn（item，list）
- assertNotLn（item，list）



setUp（self）方法类似init，允许创建self的属性，然后在类的方法中共享这些属性，避免多次创建一样的实例

