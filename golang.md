![image-20211025223337981](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20211025223337981.png)



![image-20211025223353526](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20211025223353526.png)



# 应用

计算能力：排序，推荐，搜索

支持高并发

CDN：content distribution network内容并发网络

分布式文件系统

# 学习策略

学习新技术

- 建立一个整体的框架
- 了解原理，工作过程
- 熟悉语法
- 通过一个简单的案例入门
- 深入研究细节
- 在做中学

# golang特点

- 计算能力，并发能力，利用多核cpu，语法规范（一个问题一种解决形式）
- C：静态编译语言的性能；弱化的指针
- python：动态语言的开发效率
- 在golang里面每个文件都应该属于一个包package，每个package对应于一个文件夹
- 垃圾回收机制



# 程序分析

## 编译方式

go是编译型的语言，在win平台上可以用`go build xx.go` 生成同名的exe文件

也可以用`go build -o yy.exe xx.go`命名exe文件

然后运行这个exe文件

也可以用`go run xx.go`编译并运行这个文件，但是exe文件是temp的，不会被保留下来

- go build

![image-20211025223408925](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20211025223408925.png)

- 运行exe文件

![image-20210610203501992](https://gitee.com/hit_whr/pic_3.0/raw/master/img/image-20210610203501992.png)

- 用del删除.exe文件，然后go run

![image-20211025223427206](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20211025223427206.png)

- 在linux平台上，编译后，用`./`命令执行该可执行文件



## 包

- 每个.go文件都必须属于一个package，如果不声明属于哪个包，无法编译通过



- 然后可以导包，调用包里面的相应函数。

- **在一个包里面只能有一个main函数（入口函数）**

- 在一个包里面，函数可以直接调用（函数见下面），不需要指明当前包的名字

## 导包

import

![image-20211025223442503](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20211025223442503.png)

## 查看内置的包

 ![image-20210610205554164](https://gitee.com/hit_whr/pic_3.0/raw/master/img/image-20210610205554164.png)





## 函数

函数的特点是支持多返回值

格式为`func name(var_name type,var_name type) (return value type , return value type)`

- 调用相同package下的函数，失败

因为没有将func.go文件编译
![image-20210610204705688](https://gitee.com/hit_whr/pic_3.0/raw/master/img/image-20210610204705688.png)

![image-20211025223502377](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20211025223502377.png)



- 解决方法

用`go build .`将目录下的所有文件都编译了，生成一个名为dir_name.go 的exe文件，然后执行

![image-20211025223512810](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20211025223512810.png)

但这样比较麻烦，想在ide中操作

将run的configurations改成以package或者directory为单位，这样就默认编译整个文件夹里面的.go文件了

![image-20210610210608575](https://gitee.com/hit_whr/pic_3.0/raw/master/img/image-20210610210608575.png)



### 函数名

要让a包的函数对b包的函数可见，必须对a包中的函数必须是大写字母开头的，常量变量也是这样，只有以大写字母开头才可见。



## 目录结构

首先是src目录，表明放的是源代码，然后进入go_code目录，在下面建立项目目录，然后再建立某个项目所用的包，可以用多个包，但是要有main包和main函数，作为入口函数。

![image-20211025223523897](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20211025223523897.png)



## undone调用自己的包

![image-20210610211328972](https://gitee.com/hit_whr/pic_3.0/raw/master/img/image-20210610211328972.png)

找不到这个包，因为路径没加进去

[Go 使用自定义包（package） - Ficow - 博客园 (cnblogs.com)](https://www.cnblogs.com/ficow/p/6537363.html)



# 转义字符

\t 制表符

\n 换行符

\r 回车，是退回到当前行的最前边

\\\ 对\进行转义

![image-20211025223536826](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20211025223536826.png)



# 注释

- 推荐用\\\来表示注释内容

![image-20211025223552843](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20211025223552843.png)



# gofmt（规范化）

- c中，缩进不影响程序编译；python用缩进来代表程序块；go中，缩进也不影响程序编译，但是建议规范化

![image-20210610213003632](https://gitee.com/hit_whr/pic_3.0/raw/master/img/image-20210610213003632.png)

- 可以用`gofmt xx.go`查看规范化之后的代码（不会修改原文件的内容）

![image-20210610213134555](https://gitee.com/hit_whr/pic_3.0/raw/master/img/image-20210610213134555.png)



![image-20210610213203139](https://gitee.com/hit_whr/pic_3.0/raw/master/img/image-20210610213203139.png)

- 然后用`gofmt -w xx.go`将规范化后的文本写入原文件

![image-20210610213249230](https://gitee.com/hit_whr/pic_3.0/raw/master/img/image-20210610213249230.png)

![image-20210610213323059](https://gitee.com/hit_whr/pic_2.0/raw/master/image-2021061021332305.png)



# 官网



# 一个project

将网页的go文件发到服务器执行，然后返回执行结果，似乎就是在远程执行程序了。



# dos

cmd将指令发给dos（文件操作系统）进行解析指令，然后对磁盘进行操作

- dir，查看当前目录的内容

![image-20210610215054706](https://gitee.com/hit_whr/pic_3.0/raw/master/img/image-20210610215054706.png)

- cd（change directory）

  - 特别的是，在盘符之间跳转时，需要加上/d

    ![image-20210610214851445](https://gitee.com/hit_whr/pic_2.0/raw/master/image-2021061021485144.png)

- md(make directory) 新建一个目录名，默认在当前目录下建立

  ![image-20210610215116053](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210610215116053.png)

  

- rd(删除目录及其下面的所有内容)/s/q，删除并且不询问

![image-20210610215138629](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210610215138629.png)

![image-20210610215212073](https://gitee.com/hit_whr/pic_2.0/raw/master/image-2021061021521207.png)

![image-20210610215254315](https://gitee.com/hit_whr/pic_3.0/raw/master/img/image-20210610215254315.png)



- copy，复制文件，源文件地址 目的文件地址。源文件默认当前目录，目的文件地址默认不修改文件名

![image-20210610215514173](https://gitee.com/hit_whr/pic_3.0/raw/master/img/image-20210610215514173.png)



- move，移动文件，源文件地址，目的文件地址
- del，删除文件
- 清屏指令，cls



# 安装

![image-20210610220256355](https://gitee.com/hit_whr/pic_2.0/raw/master/image-2021061022025635.png)

![image-20210610220258680](https://gitee.com/hit_whr/pic_3.0/raw/master/img/image-20210610220258680.png)



# 变量

声明变量，变量赋值，变量使用

变量初始化（声明的同时进行赋值）

## 声明变量的方式

### var

#### 指出类型

```go
func main()  {
	var name int
	fmt.Println(name)
}
```

此时也可以给值

```go
func main()  {
	var name int = 1
	fmt.Println(name)
}
```



#### 类型推导（根据值）

```go
func main()  {
	var age = 12
	fmt.Println(age)
}
```



### 没有var

没有var的时候，类似于类型推导，必须指定变量的值

```go
func main()  {
	a:=14
	fmt.Println(a)
}
```



### 多个变量

```go
func main()  {
	var a,b int
	a,b = 1,2
	fmt.Println(a,b)
}
```



```go
func main()  {
	a,b:=1,2
	fmt.Println(a,b)
}
```



### 全局变量

```go
package main

import "fmt"
var (
	x=1
	y=34
)
func main()  {
	a,b:=1,2
	fmt.Println(a,b)
	fmt.Println(x,y)
}
```

![image-20210610221346590](https://gitee.com/hit_whr/pic_2.0/raw/master/image-2021061022134659.png)

### 全局的常量

![image-20210610221428198](https://gitee.com/hit_whr/pic_3.0/raw/master/img/image-20210610221428198.png)

### 总结

没有特殊需求的时候用类型推导比较常见，只有在需要限定变量类型的时候才会用到var name type

## 数据类型

go在溢出的时候会自动报错

### 整数

int，int8，int16，int32，int64

int在32位机器上是32位，在64位机器上是64位

uint，uint8，uint16，uint32，uint64

byte一个字节（无符号）

![image-20210610222214979](https://gitee.com/hit_whr/pic_2.0/raw/master/image-2021061022221497.png)



![image-20210610222303094](https://gitee.com/hit_whr/pic_2.0/raw/master/image-2021061022230309.png)



#### 查看变量的类型和字节

![image-20210610223027549](https://gitee.com/hit_whr/pic_3.0/raw/master/img/image-20210610223027549.png)

### 浮点数

float32，float64



### 字符

- 储存字符：字符->编码->码值->二进制代码
- 显示字符：二进制代码->码值->解码->字符
- go中默认用utf-8编码，英文字符一个字节就可以放下，中文字符需要三个字节
  - byte放不下

![image-20210610224427034](https://gitee.com/hit_whr/pic_2.0/raw/master/image-2021061022442703.png)



![image-20210610224443353](https://gitee.com/hit_whr/pic_2.0/raw/master/image-2021061022444335.png)



![image-20210610224506101](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210610224506101.png)



![image-20210610224528711](https://gitee.com/hit_whr/pic_3.0/raw/master/img/image-20210610224528711.png)



![image-20210610224601881](https://gitee.com/hit_whr/pic_3.0/raw/master/img/image-20210610224601881.png)

- byte本质是无符号的整数，可以存放所有的ASCII字符

```go
func main()  {
	var i byte = 'a'
	fmt.Println(i)
}
```

![image-20210610224328266](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210610224328266.png)

- string是字节的组合
- 在输出的时候byte要用格式控制符进行解释

![image-20210610224351728](https://gitee.com/hit_whr/pic_3.0/raw/master/img/image-20210610224351728.png)

- 在go中，字符被解释为整数，如果直接输出，是字符在utf-8编码下的码值

用byte来存放字符类型



### bool

false，true

### string

- 在go中string是字符序列，按照字节来进行组织
- 用utf-8进行解码
- string一旦经过赋值，这一组字节的值就不可以改变了，相当于常量

![image-20210610225345472](https://gitee.com/hit_whr/pic_3.0/raw/master/img/image-20210610225345472.png)

- 两种方式给出字符串
  - 双引号（识别转义字符，不能处理特殊字符）
  - 反引号（原生字符串，禁用转义字符，识别特殊字符），适合输出源码，比较安全（防止输入转义字符）

```go
package main

import "fmt"

func main()  {
	var s string = "ss\naa"
	a:= `package main

import "fmt"

func main()  {
	var s string = "ss\naa"
}`
	fmt.Println(s)
	fmt.Println("-----------")
	fmt.Println(a)
}


ss
aa
-----------
package main

import "fmt"

func main()  {
	var s string = "ss\naa"
}
```



### 指针





### 数组

### 结构体struct

### 管道

### 函数

### 切片

### 接口

### map