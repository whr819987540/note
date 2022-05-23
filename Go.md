

# Go

## 1.背景

应用于web服务器，进行分布式并行计算，提高效率

集群：要提高服务器性能，可以增加单个服务器性能，也可以用集群技术，通过多个低性能服务器的组合，来替代单个高性能服务器。

可以实现负载均衡，降低单点故障的影响，降低成本。

go是编译型语言，比解释型语言快。

并发性好

保存时，自动格式化，将格式统一起来

有垃圾回收机制

## 2.安装

用的是goland ide，下载goland 并执行破解过程，发现没有SDK，go version检验版本信息，发现命令无效。原来是没有安装go version-amd64.msi这种东西。

> 就像pycharm一样，也需要编译器

## 3.一般格式

```go 
package main
import "fmt"
func main(){
    /*this is the first
    test for goland*/
    fmt.Print("Hello world!")
}
```

1.第一行代码 *package main* 定义了包名。你必须在源文件中非注释的第一行指明这个文件属于哪个包，如：package main。***package main表示一个可独立执行的程序，每个 Go 应用程序都包含一个名为 main 的包。***这里的包名是说如果别的包引用这个包时，所需要的的标识符。

如果要把这个文件夹作为一个可执行的程序，而不是一个库，必须声明为package main 然后有一个main函数（fmt这种是库，没有入口函数）



> 文件名与包名没有直接关系，不一定要将文件名与包名定成同一个
>
> 文件夹名与包名没有直接关系，并非需要一致
>
> 同一个文件夹下的文件只能有一个包名，否则编译报错

```html
文件组织格式
root(dir)
	dir:test
		file:mycode.go
	dir:math
		file:math1.go
		file2:math2.go
```

```go
//mycode.go
package main
/*当test文件夹下的所有go文件被调用时，他们所属的包名都是main，所以同一文件夹下的go文件中package标识符应该相同*/
import ("fmt"
        "./math")
/*import的实际上是文件夹名，下面所属多个go*/
func main(){
    fmt.Print(mathtool.Add(1,2))
    fmt.Print(mathtool.Devi(7,9))
}
```

```go
//math(dir),code1.go
package mathtool
func Add(x,y int) int{
    return x+y
}
//math(dir),code2.go
package mathtool//只能有一个包名
func Devi(a,b,int)int {
    return a-b
}
```



2.下一行 *import "fmt"* 告诉 Go 编译器这个程序需要使用 ***fmt 包***（的函数，或其他元素），fmt 包实现了格式化 IO（输入/输出）

3.下一行 ***func main() 是程序开始执行的函数（类似C语言）***。main 函数是每一个可执行程序所必须包含的，一般来说都是在启动后第一个执行的函数***（如果有 init() 函数则会先执行该函数）。***

在一个project中有且只有一个func main()，与c语言的project类似

4.单行注释// 多行注释/**/

5.fmt.Print格式化输出，fmt.Println()格式化输出+'\n'

6.**包中标识符的第一个字符为==大写字母==时，可以被外部程序引用，称为导出；以小写字母开头则不行**

7.编译并执行命令go run name.go(位于name.go目录)

## 4.变量类型及其声明

### 1.变量类型

bool，int，float32，float64，string字符串中的字符采用utf-8编码

### 2.变量声明

var identifier1, identifier2 type = value1,value2

这里的变量可以有多个，但是type是唯一的

`var a,b int = 2,2` is valid

`var a,b int,float = 2,3.3` is invalid

`var a,b = 2,3.3` is valid

var1,var2 := value1,value2

交给编译器来确定var1,var2的类型

***如果没有初始化，默认为零值***

如果初始化时没有指定type，编译器会自己决定type

```go
var intVal int //声明语句

intVal :=1 // 这时候会产生编译错误，intVal = -1 为赋值语句

intVal,intVal1 := 1,2 // 此时不会产生编译错误，因为有声明新的变量，因为 := 是一个声明语句

// 这种因式分解关键字的写法一般用于声明全局变量
var (
    vname1 v_type1
    vname2 v_type2
)

//这种不带声明格式的只能在函数体中出现
//g, h := 123, "hello"
//也就是说var1,var2 := value1,value2只能放在代码块中
```

```go
//变量声明与赋值
var a,b,c int = 1,2,3
var a,b,c = 11.2,2,"golang"
var a,b,c int
a,b,c = 1,2,3
a,b,c := 1.2,33,"golang"
```

### 全局变量的声明

```go
package main
import "fmt"
var x,y int
var (
	a int
    b float
)
func main(){
    
}
```

### 常量声明

`const var_name type = values`

声明的时候必须同时进行初始化

valid: `const a,b int = 11,12`

valid: `const a,b = 11,11.2`

valid:

```go
	var a int =1//声明与赋值的一般方法
	var b float32 =1
	var(//多个量一起赋值
		c int =10
		d =12//进行自动类型的判断
	)
	var e=13
	var i int
	i=13//先声明后赋值
	f:=14//简洁，自动类型判断
	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(c)
	fmt.Println(d)
	fmt.Println(e)
	fmt.Println(i)

```



```go
 const (

	a="abc"

	b=12

	c=12.3

)
```

常量自增

```go
const (
	mon float32 = 1.2+iota
    tue
    wed//值分别为1.2,2.2,3.2
    //iota起到了自增的作用
)

const(
	first =1<<iota//移位运算
    second
    third
)
m=6//110,001,010,100
fmt.Println(m&first==first,m&second==second,m&third==third)

```



invalid: 

```go 
const a,b=3

b=4
```

### iota

>iota，特殊常量，可以认为是一个可以被编译器修改的常量。

> iota 在 const关键字出现时将被重置为 0(const 内部的第一行之前)，const 中每新增一行常量声明将使 iota 计数一次(iota 可理解为 const 语句块中的行索引)。

```go
const (
	a=iota//iota=0
    b//=1
    c//=2
    d="string"//=3
    e=iota//=4
    f//=5
    g//=6
    h=12//=7
    i=iota//=8
)
```

go不支持隐式的类型转换，即使是短的转换为长的类型

除非进行强制类型的转换，（type）var

不支持指针运算，如ptr+1



## 5.格式控制符

%d整数

## 6.if语句

```go
var a,b = 12,13
if a>b{
    fmt.Println(">")
} else if a==b {
    fmt.Println("=")
} else {
    fmt.Println("<")
}
//{必须和所属的关键字在一行
//}必须和后面的条件判断一行
```

另外一个特性是：支持在if语句里面进行变量赋值

```go
if var declaration; condition{
	statement
}
```





## 7.switch语句

对switch的变量类型不做限制 ，可以不是整数

可以不设置switch var，此时相当于if if else if else

case后面可以有多个符合条件，之间是或的关系

***不需要break***

```go
switch var{
    case value1,value2:
    	action1
    case value3:
    	action2
    default:
    action3
}
```

当某个条件成立时，执行case内的代码块或者语句

如果要执行其余的代码块，加上fallthrough

## 8.循环

for init;condition;post{

}//eauals to for in C

for condition{

statement 

}//equals to while in C

for ;conditon;{

}//equals to while but in the form of for



## 数组

声明

var array_name[size] type

初始化，逐个赋值

声明并初始化

array_name :=[size]type{}

array_name :=[,,,]type{}

遍历数组

```go
for index,value :=range list{
    fmt.Println(index,value)
}
//这里的range有索引和数组值两个返回值，如果不想要索引，（go要求声明了的变量都必须被使用，否则无法通过编译），可以用一个_表示占位
for _,value :=range list{
    fmt.Println(value)
}
for i:=0;i<len(list);i++{
    fmt.Println(list[i])
}

```

数组截取

a[index1,index2]包括a[index1]，不包括a[index2]

```go
list_copy:=list//数组可以进行赋值
list_copy_again:=list_copy[:2]//先对数组进行截取，然后再赋值
for _,value:=range list_copy_again{
    fmt.Println(value)
}
```



数组可以进行直接赋值,而且数组的地址不相同

```go
g:=[...]int{1,2,3}
f:=g
g[0]=5
fmt.Println(g)
fmt.Println(f)
//[5 2 3]
//[1 2 3]
```









### 杂记

- len()，返回字符串中字符的个数

- go中声明的局部变量必须都被使用，否则编译错误

- 合理丢弃不需要用到的函数返回值（函数的返回值需要用变量来存储，如果某个变量没有用到，编译错误）
- 对于全局变量，可以在当前目录的所有函数内访问，也可以在包外访问（如果import了）



抛弃一个值： 

> _,b = Func1(parameters)



## 切片

声明

var name [] type

var slice [] int

赋值

name = append(name,value)

slice=append(slice,2)//动态数组，里面有首地址，元素个数len，容量cap

声明并初始化

name:=[]type{}

slice:=[]int{1,3,4,5}

```go
var slice []int//声明
slice=append(slice,1)//赋值
fmt.Println(slice)
slice_copy:=[]int{1,2,4}//声明并初始化
fmt.Println(slice_copy)
```



slice的底层实现

当len=cap时，如果再进行加入元素，会重新分配存储空间，那么首地址可能发生变化，（c语言是realloc）。如果没变化，直接加入元素；如果变化了，那么还得复制之前的元素

每次重新分配的空间是之前分配的两倍

```go
var b[]int
for i:=0;i<100;i++{
    b=append(b,i)
    fmt.Println(len(b),cap(b))
}
1 1
2 2
3 4
4 4
5 8
6 8
7 8
8 8
9 16
10 16
11 16
12 16
13 16
14 16
15 16
16 16
17 32
18 32
19 32
20 32
21 32
22 32
23 32
24 32
25 32
26 32
27 32
28 32
29 32
30 32
31 32
32 32
33 64
34 64
35 64
36 64
37 64
38 64
39 64
40 64
41 64
42 64
43 64
44 64
45 64
46 64
47 64
48 64
49 64
50 64
51 64
52 64
53 64
54 64
55 64
56 64
57 64
58 64
59 64
60 64
61 64
62 64
63 64
64 64
65 128
66 128
67 128
68 128
69 128
70 128
71 128
72 128
73 128
74 128
75 128
76 128
77 128
78 128
79 128
80 128
81 128
82 128
83 128
84 128
85 128
86 128
87 128
88 128
89 128
90 128
91 128
92 128
93 128
94 128
95 128
96 128
97 128
98 128
99 128
100 128
```

在添加元素时，用的是slice=append(slice,item)

是因为当capacity不够时，可能需要重新分配存储空间



关于切片的共享存储空间

```go
b_copy:=b[:20]
           fmt.Println(b_copy,len(b_copy),cap(b_copy))
```

结果是[0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19] 20 128

确实进行了复制，而且b_copy的容量和b的容量是一样的。

类似的，如果对b_copy进行了修改，由于是同一段存储空间，必然会对b产生影响，所以叫切片

### 调用切片

第一个返回值是index，后一个才是值	

```go
func not_concrete(m float64,arg ... int){
   for _,i :=range arg{
      fmt.Println(i)
   }
   fmt.Println(m)
}
```



## map

声明及初始化

```go
map[键的类型]值的类型{[key:value]}
name[键的类型]=值的类型
make(map[键的类型]值的类型，cap)
map1:=map[int]int{1:1,2:4,3:9}
map2:=map[int]int{}
map2[2]=4
map3:=make(map[int]int,3)
fmt.Println(map1)//map[1:1,2:4,3:9]
fmt.Println("len of map1:",len(map1))//3
map1[4]=16
fmt.Println(map1)//map[1:1,2:4,3:9,4:16]
fmt.Println("len of map1:",len(map1))//4
fmt.Println(map2)//map[2:4]
fmt.Println("len of map2:",len(map2))//1
fmt.Println(map3)//map[]
fmt.Println("len of map3:",len(map3))//0
```

在用make（map【type】type，cap）定义map时，可以指定容量。

但是不能用cap（map）访问map的容量，只能得到它的len（map）



关于值不存在与值为0

在go里面，如果key不存在，但却是对key对应的value进行了访问，go返回0，以及一个状态（bool）

如果存在，返回true；如果不存在，返回false（go的函数可以有多个返回值）

```go
if _,status:=map1[100];status{
    fmt.Println("status is true")
}else{
    fmt.Println("status is false")//select this
}

if _,status:=map1[0];status{
    fmt.Println("status is true")//select this
}else{
    fmt.Println("status is false")
}
```



遍历map

```go
for key,value:=range map1{
    fmt.Println("map[",key,"] is ",value)
}
map[ 1 ] is  1
map[ 2 ] is  4
map[ 3 ] is  9
map[ 4 ] is  16
map[ 0 ] is  0
```



map的值也可以是函数

```go
map4 := map[int]func(a int) int{}
map4[2] = func(a int) int { return a * a }
map4[3] = func(a int) int { return map4[2](a) * a }
fmt.Println(map4[3](5))
//要求函数的参数列表以及返回值相同
```



用map实现set（集合）

也就是没有相同的键或者值

由于值可以相同，所以用键

要让键不相同，在添加前，先对键的值进行访问。

如果状态时true那么是存在

```go
map5:=map[int]bool{}
map5[1]=true
map5[4]=true
index:=3
if map5[index]{
    fmt.Println(index," exists")
}else{
    fmt.Println(index," not exists")//this
}
index=4
if map5[index]{
    fmt.Println(index," exists")//this
}else{
    fmt.Println(index," not exists")
}

delete(map5,index)
if map5[index]{
    fmt.Println(index," exists")
}else{
    fmt.Println(index," not exists")//this
}

3  not exists
4  exists
4  not exists
```

对map键值对的删除，delete（map，index）





## 字符串

- string是数据类型，不是引用，不是指针
- 只读byte slice，len返回字节数

```go
eng_list:=[...]string{"abcdef","thisis"}
fmt.Println(len(eng_list))//2
fmt.Println(len(eng_list[0]))//6
ch_list:=[...]string{"进行一下","测试","我","你"}
fmt.Println(len(ch_list))//4
fmt.Println(len(ch_list[2]))//3
fmt.Println(len(ch_list[0]))//12
```

utf-8下，中文字符为三个字节

![image-20210323112825447](https://raw.githubusercontent.com/whr819987540/pic/main/image-20210323112825447.png)

string是只读的slic，不能修改内容



strings.Split(string,””)

strings.Join(slice,””)

strconv.Itoa()将整数转化为字符串



字符串和整数的相互转化

字符串（里面的字符确实是整数的字面值）到整数

strconv.Atoi()

两个返回值，一个是转化后的整数，一个是表示转化是否成功的标志

整数到字符串

strconv.Itoa()

而这个函数的返回值只有转化成功后的字符串，没有表示状态的返回值

因为任何字符都可以表示为字符串，不存在转化不成

```go
s2:="123"
fmt.Println(strconv.Atoi(s2))//转化成功，123 <nil>
if value,error:=strconv.Atoi(s2);error==nil{
    fmt.Println(value)//进行判断，nil是转化成功的标志
}
s3:="1as"
if value,error:=strconv.Atoi(s3);error==nil{
    fmt.Println(value)
}else{
    fmt.Println("invalid convert")
}

s4:=123
fmt.Println(strconv.Itoa(s4))//123 strconv.Itoa() only one return value
```













## 函数

go中的函数支持多返回值



所有的参数都是按照值来传递

slice（结构）首先复制结构里面的值（首地址，len，cap），实际上对内存进行操作；相当于指针

函数可以赋值给变量，作为变量的值

函数可以作为参数和返回值

支持变长参数作为函数的参数

```go
func sum(vars ...int)int{
	res:=0
	for _,value :=range vars{
		res+=value
	}
	return res
}
func main(){
	fmt.Println(sum(1,2,3,4,5))
	fmt.Println(sum(1,3,5,7))
}
```



defer关键词：用defer声明的函数，只有当所在代码块执行完毕后，才开始执行

```go
func before(){
	fmt.Println("before defer runs")
}
func toge(){
	before()
	fmt.Println("maybe this first runs")
}

func toge_v2()	{
	defer before()
	fmt.Println("maybe this first runs")
}
func main(){
	toge()
	toge_v2()
}
//before defer runs
//maybe this first runs
//maybe this first runs
//before defer runs
```

panic(string)

首先程序就此停止，然后回显stirng进行提示

在程序停止前，还是会执行defer里面的内容，但是panic后面的内容是不会被执行的。

```go
func before(){
	fmt.Println("before defer runs")
}
func toge(){
	before()//1
	fmt.Println("maybe this first runs")//2
}

func toge_v2()	{
	defer before()//2
	panic("delay for a while")//1
	fmt.Println("maybe this first runs")
}
func main(){
	toge()
	toge_v2()
}
1 before defer runs
2 maybe this first runs
2 before defer runs
1 panic: delay for a while
```



### 1.定义

```go
func function_name (parameters) return_type{

}
//parameters实际上是局部变量的定义，所以是var_name var_type

func output(a int,b float32,c string){
    fmt.Println(a)
    fmt.Println(b)
    fmt.Println(c)
}

func swap(a int, b string) (string, int){
    return b,a
}
```

### 2.参数传递的类型

1.值传递（默认）

2.引用传递

### 可变参数

可变参数使用name ...Type的形式声明在函数的参数列表中，而且需要是参数列表的==最后一个参数==，这点与其他语言类似；

### 将函数作为参数或返回值

函数的类型通过type关键字进行定义或者不进行定义



```go
func add_copy(args [] int)int{
	sum:=0
	for _,value:=range args{
		sum=sum+value
	}
	return sum
}

func del(args [] int)int{
	sum:=args[0]
	for _,value:=range args[1:]{
		sum=sum-value
	}
	return sum
}

type cal_type func(args [] int)int

func cal(calType cal_type,args [] int)int{
	return calType(args)
    //这里不能将args作为参数，因为args是【】int类型的，虽然calType允许传入多个参数，但每个参数实际上还是int，只是go在处理时，将他们都放到切片中，产生一种可变参数的感觉
    //另外一种写法是还是用可变参数，不过在切片后加上...
}
func main(){
    list:=[]int{1,2,3}
	fmt.Println(cal(add_copy,list)
	fmt.Println(cal(del,list))
}
```

```go
//在功能函数里面，用可变参数，函数类型声明里面也是可变参数
//但在调用接口的时候传入的是slice，用slice...将slice转为一个个参数

package main

import "fmt"

func add_copy(args ... int)int{
sum:=0
for _,value:=range args{
sum=sum+value
}
return sum
}

func del(args ... int)int{
sum:=args[0]
for _,value:=range args[1:]{
sum=sum-value
}
return sum
}

type cal_type func(args ... int)int

func cal(calType cal_type,args [] int)int{
return calType(args...)
//这里不能将args作为参数，因为args是【】int类型的，虽然calType允许传入多个参数，但每个参数实际上还是int，只是go在处理时，将他们都放到切片中，产生一种可变参数的感觉
//另外一种写法是还是用可变参数，不过在切片后加上...
}
func main(){
list:=[]int{1,2,3}
fmt.Println(cal(add_copy,list))
fmt.Println(cal(del,list))
}
```



这样写的好处就在于，可以传递函数，然后进行复用，便于维护

```go
type even_odd_type func(int)bool
func determine(a []int,f even_odd_type)[]int{
   var res []int
   for _,value:=range a{
      if(f(value)){
         res= append(res, value)
      }
   }
   return res
}
func isEven(a int)bool{
   if a%2==0{
      return true
   }else{
      return false
   }
}
func isOdd(a int)bool{
   if a%2!=0{
      return true
   }else{
      return false
   }
}

func main(){
   var slice  []int
   for i:=0;i<10;i++{
      slice=append(slice,i)
   }

   fmt.Print("偶数有：")
   fmt.Println(determine(slice,isEven))
   fmt.Print("奇数有：")
   fmt.Println(determine(slice,isOdd))
```

不支持利用main函数传递参数，main函数没有返回值，os.exit（）返回状态码

传入的参数用os.Args【】显示

第一个参数为exe的路径







- os.Exit退出时不点用defer

  os.Exit(n int)需要一个整数作为退出时的状态码

  ![image-20210326095848392](https://raw.githubusercontent.com/whr819987540/pic/main/20210326095855.png)

- os.Exit退出时不调用栈的信息

- 由于panic在终止程序前会有error传入，然后执行defer

先看看程序执行的顺序：panic->defer

![image-20210326100212325](https://raw.githubusercontent.com/whr819987540/pic/main/20210326100212.png)

- 在defer里面的recover，返回当前的错误，对错误进行判断，然后进行补救
  defer func(){
     if error:=recover();error!=nil{
        //错误恢复机制
     }
  }()
  recover如果没有做到真正的恢复手段，对于程序而言只是掩盖了一个错误
  后来还是会有，会继续出现
  有时不如重启然后退出

![image-20210326100442891](https://raw.githubusercontent.com/whr819987540/pic/main/20210326100443.png)



这样就没有执行panic之后的内容，即异常没有被解决掉，反而掩盖了编译器的报错

## 匿名函数

通常用在闭包和回调函数

```go
func ()(){
    
}(实参)
```

### 只用一次

```go
func (a int){
   fmt.Println(a)
}(10)
```

### 将匿名函数作为变量

```go
	f:=func (a int){
		fmt.Println(a)
	}
	f(1)
```



### 作为回调函数

感觉和将函数赋值给一个变量区别不大

```go
func se(list []float64,f func(float64))  {
	for _,value:=range list{
		f(value)
	}
}
func main(){
	list:=[]float64{1,2,3,4,5}
	se (list,func (a float64){
		fmt.Println(math.Pow(a,2))
	})
}
```







## 模块与复用

首先查看本机的GOPATH

> go env GOPATH

因为是要复用，所以首先要指定一个位置，告诉编译器，要复用的代码在那里



# 关于找不到package

如果是在linux下，自动先去gopath下找，然后去goroot下找，

```bash
main.go:4:2: cannot find package "func_test" in any of:
  /usr/lib/golang/src/func_test (from $GOROOT)
  /root/go/src/func_test (from $GOPATH)
我移动了一下目录后，
[root@iZm5e98zphj5y525q4v5k4Z src]# ls
func_test  test1
[root@iZm5e98zphj5y525q4v5k4Z src]# cd test1
[root@iZm5e98zphj5y525q4v5k4Z test1]# go run test1
this
This is a test
```

说明linux支持者两个路径，而windows下默认只支持goroot路径

所以需要进行修改

```bash
C:\Users\user\go\src\main>go run main.go
main.go:3:8: package my_func is not in GOROOT (C:\Program Files\Go\src\my_func)
```

> C:\Users\user\go\src\main>go env -w GO111MODULE=off

然后go run file.go就能找到自己定义的package了

当然，go run的前提是这个文件是用的package main，并且有main函数

如果没有上述两条，那么只能用init来代替

并且只能go build（生成可执行文件在当前文件夹内）

![image-20210326132708687](https://raw.githubusercontent.com/whr819987540/pic/main/20210326132715.png)



对于没有main的文件，执行go build

![image-20210326132809963](https://raw.githubusercontent.com/whr819987540/pic/main/20210326132810.png)

![image-20210326184654580](https://raw.githubusercontent.com/whr819987540/pic/main/20210326184701.png)

没有exe文件，因为它本身就只有函数，没有入口函数，无法执行



import new_name ”package name”

func TestXXX(t *testing.T){

}





# 并发

## 概念

- 并发与并行
  - 宏观上看，并发是说同时处理多个任务；微观上看，还是将任务串行的交给处理器，只不过每个任务很快被执行，感觉是同时处理
  - 并行，是从微观上来说的，将不同任务同时交给多个处理器。
- 程序与进程
  - 程序是辅存上的，不占用系统资源
  - 进程（正在进行的程序），是在运行的程序
  - 一个程序可以对应多个进程（开启两个qq）
- 进程与线程
  - 一个进程包括多个线程
  - 线程又叫轻量级进程
  - 系统对进程分配资源
  - 而线程是独立运行的基本单位
- 协程
  - 比线程更轻量
  - 一个线程有多个协程
  - 协程是编译器级别的，不被操作系统的内核管理，由程序控制，不存在线程（操作系统级别的）切换时的开销

## 创建go中的协程

关键字go创建Goroutine（go中的协程是并行的，所以谁先被执行不好说），但是main()的协程结束后，程序终止，所有的协程被终止。

print对应的协程和main的协程谁先执行完会影响最终的结果

```go
package main

import "fmt"

func print(){
	fmt.Println("in child goroutine")
}
func main()  {
	go print()
	fmt.Println("in main")
}
```



![image-20210326211930271](https://raw.githubusercontent.com/whr819987540/pic/main/20210326211930.png)

![image-20210326211923228](https://raw.githubusercontent.com/whr819987540/pic/main/20210326211940.png)



如果让main的等一会儿，则结果是唯一的

```go
func main()  {
	go print()
	time.Sleep(time.Second*2)
	fmt.Println("in main")
}
```



一个简单的例子，一边打印，一边通过监测可能的输入让main的协程终止

```go
package main

import (
	"fmt"
	"time"
)

func tick(){
	seconds:=0
	for{
		seconds++
		fmt.Println(seconds," s")
		time.Sleep(time.Second*1)
	}
}
func main()  {
	go tick()
	var input string
	fmt.Scanln(&input)
	fmt.Println(input)
}
```



## 多个Goroutine

多个协程被创建后，被系统内核执行的顺序是不可知的



## 调整并发性能

runtime是go中调度Goruntine的管理器

使用runtime.Gosched()，交出控制权

像维护线程池中线程数量与CPU核心数量一样，也需要控制Goroutine的数量。使用time.GOMAXPROCS(逻辑CPU数量)

<1 不修改；=1单核执行；>1 多核并发执行

## channel

### 用处

一般做法，线程之间进行数据交换用的是共享内存，而根据数据库的知识，类似脏读，如何保证数据的同步问题，需要用互锁，这样性能比较低

在Goroutine中，用channel来进行数据传递，用数据传递来实现数据共享

### 创建

make可以用来创建channel，slice

在创建slice时，指定的是len和cap

在创建channel时，chan type指定传送的数据的类型

```go
	list:=make([]int,10)
	fmt.Println(len(list))
	fmt.Println(cap(list))
	ch1:=make(chan int)
```

### 传递数据

如果接收方一直没有接受，发送操作将会处于阻塞状态。

此时所有goroutine处于等待。

可能发生死锁deadlock