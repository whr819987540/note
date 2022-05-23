# command params

通过os.Args[]（slice）获得

os.Args[0]是命令的名字（如/root/src/helloworld和./helloworld）

```go
package main

import (
	"fmt"
	"os"
)

func main() {
	fmt.Println("Hello, world")
	fmt.Println(os.Args[0])
}

```



```bash
D:\gocode\learning\ch1\1_helloworld>go run helloword.go
Hello, world
C:\Users\user\AppData\Local\Temp\go-build2273647872\b001\exe\helloword.exe

D:\gocode\learning\ch1\1_helloworld>go build helloword.go

D:\gocode\learning\ch1\1_helloworld>helloword.exe
Hello, world
helloword.exe

```



# for

## structure

```go
package main

import "fmt"

func main() {
	// for initialization; condition; post{
	// statement
	// }
	for i := 1; i < 10; i++ {
		fmt.Println(i)
	}

	// without initialization part
	// for ; condition; post{
	// statement
	// }
	i := 15
	for ; i < 20; i++ {
		fmt.Println(i)
	}

	// without post part
	// for initialization ; condition ; {
	// statement
	// }
	for j := 30; j < 34; {
		fmt.Println(j + 1)
		j++
	}

	// without initialization and post part
	// for condition {
	// statement
	// }
	j := 20
	for j < 25 {
		fmt.Println(j + 1)
		j++
	}
}

```



## range

```go
// for range

package main

import (
	"fmt"
	"os"
)

func main() {
	for index, param := range os.Args[:] {
		fmt.Println(index, param)
	}
}

```



# map

## create

map\[key_type\]value_type

make(map\[key_type\]value_type) to create

```go
package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	// create a map, with string key and int value
	// map provide o(n) to access and modify
	line_num_map := make(map[string]int)

	// bufio.Scan can read from certain source
	// create a scanner
	input := bufio.NewScanner(os.Stdin)

	// read from os.Stdin
	// remove the /n from os.Stdin
	// return True if not empty
	for input.Scan() {
		// Scan.text() get the input
		if input.Text() == "q" {
			break
		}
		// if the key not exists, the value is initialized to zero
		line_num_map[input.Text()] += 1
	}

	// output if value greater than 1
	// iterate, return the key and value
	for line, num := range line_num_map {
		// format print
		if num > 1 {
			fmt.Printf("line:%s, num:%d\n", line, num)
		}
	}
}

```



## iterate

for key,value := range map



## check existence

map[key] return **value and true** if the key exists, return **certain type 'nil' and false** if not.

```go
// the key may not exist
if cycles_key, ok := request.Form["cycles"]; ok {
    // convert the string to int
    if cycles, err := strconv.Atoi(cycles_key[0]); err != nil {
        fmt.Fprintf(response, "wrong params,%s", err)
    } else {
        lissajous(response, cycles)
    }
} else {
    fmt.Fprintf(response, "please enter the 'cycles' param")
}
```





# function

```go
package main

import (
	"bufio"
	"fmt"
	"os"
)

// read and count
func CountLines(handler *os.File, line_num_map map[string]int) {
	input := bufio.NewScanner(handler)
	for input.Scan() {
		line_num_map[input.Text()]++
	}
}

func main() {
	// file names passed by the command params
	if len(os.Args) == 1 { // no file names
		fmt.Println("expected file names")
		return
	}

	// open file, read and count
	line_num_map := make(map[string]int)
	for _, file_name := range os.Args[1:] {
		// open the file
		handler, err := os.Open(file_name)
		if err != nil { // open error
			fmt.Printf("%s open error\n", file_name)
		} else {
			CountLines(handler, line_num_map)
		}
	}

	// output if num greater than 1
	for line, num := range line_num_map {
		if num > 1 {
			fmt.Printf("'%s' %d\n", line, num)
		}
	}
}

```



# type define

type new_type_name init_type_name

```go
package main

import "fmt"

// type define
type Celsius float64
type Fahrenheit float64

const(
	AbsolutZeroC = -273.15
	BoilingPointC = 100
	FreezingPointC = 0
)

func main(){
	// do some conversion
	fmt.Printf("%gC=%gF\n",AbsolutZeroC,CtoF(AbsolutZeroC))
	fmt.Printf("%gF=%gC\n",CtoF(FreezingPointC),FtoC(CtoF(FreezingPointC)))

	// do some arithmetic operations
	var a Celsius
	var b Fahrenheit
	fmt.Printf("%t\n",a == BoilingPointC)
		fmt.Printf("%t\n",a == 0)
	fmt.Printf("%t\n",b == BoilingPointC) // type error
}

func CtoF(c Celsius)Fahrenheit{
	// return c*9/5+32 is error
	// even though the Celsius and Fahrenheit point to the same
	// base type, they are not the same type
	// need type case
	return Fahrenheit(c*9/5+32)
}

func FtoC(f Fahrenheit)Celsius{
	return Celsius((f-32.0)*5/9)
}

```



# string

## byte slice

- 字符串是字节序列
- 统一采用utf-8编码
- len()返回字节数，而不是实际的字符数
- string[]访问的是字节，而不是字符

```go
package main

import "fmt"

func main() {
	s := "hello, world!"
	test_func(s)
	s = "你好啊!"
	test_func(s)
}

func test_func(s string) {
	fmt.Println(s)
	fmt.Printf("len(s)=%d\n", len(s))
	for index, value := range s {
		fmt.Printf("index:%d, value:%c,%d\n", index, value, value)
	}
}
D:\gocode\src\learning\ch5\test_string>main.exe
hello, world!
len(s)=13
index:0, value:h,104
index:1, value:e,101
index:2, value:l,108
index:3, value:l,108
index:4, value:o,111
index:5, value:,,44
index:6, value: ,32
index:7, value:w,119
index:8, value:o,111
index:9, value:r,114
index:10, value:l,108
index:11, value:d,100
index:12, value:!,33
你好啊!
len(s)=10
index:0, value:你,20320
index:3, value:好,22909
index:6, value:啊,21834
index:9, value:!,33

```



## shared memory

- 字符串本身不可变
  - string[index] = value错误
  - 字符串可以进行连接操作，不是对原字符串进行操作，而是生成新的字符串
    - 保证多个变量公用一个字符串时，不能通过任何一个变量对该字符串进行修改
    - 保证进行子串操作时，节省内存

```go
package main

import "fmt"

func main() {
	a := "hello"
	fmt.Printf("a=%q\n", a)
	t := a
	fmt.Printf("a=%q,t=%q\n", a, t)
	a += " world"
	fmt.Printf("a=%q,t=%q\n", a, t)
}

D:\gocode\src\learning\ch5\test_string>main.exe
a="hello"
a="hello",t="hello"
a="hello world",t="hello"
```



## \

- 转义字符（反斜杠）

| \a   | 警告、响铃                   |
| ---- | ---------------------------- |
| \b   | 退格                         |
| \f   | 换页                         |
| \n   | 换行（回到下一行的同一位置） |
| \r   | 回车（回到行首）             |
| \t   | 制表                         |
| \v   | 垂直制表                     |



## raw string literal

- 用\`\`引起来，不解释转义字符、十六进制(\xhh)、八进制(\ooo, less than \377)

```go
package main

import "fmt"

func main() {
	code :=`package main
import "fmt"
func main(){
	fmt.Println("Hello, world!\a\n"
}`
	fmt.Println(code)
}
```





# std package

## bufio

### bufio.NewScanner()

```go
for _, file_name := range os.Args[1:] {
    // open the file
    // handler is *os.File
    // err can be captured by os.Stderr
    handler, err := os.Open(file_name)
    if err != nil { // open error
        fmt.Printf("%s open error, %T\n", file_name, err)
    } else {
        CountLines(handler, line_num_map)
        err := handler.Close()
        if err != nil {
            fmt.Printf("%s close error, %T\n", file_name, err)
        }
    }
}

// read and count
func CountLines(handler *os.File, line_num_map map[string]int) {
	input := bufio.NewScanner(handler)
	for input.Scan() {
		line_num_map[input.Text()]++
	}
}
```





## io

### io.Copy(dst,src)

copy directly without medium buffer

```go
// 1 : response buffer -> buffer -> stdout
// this : response buffer -> stdout

package main

import (
	"fmt"
	"io"
	"net/http"
	"os"
)

func main() {
	for _, url := range os.Args[1:] {
		response, err := http.Get(url)
		if err != nil {
			fmt.Fprintf(os.Stderr, "%v\n", err)
			continue
		}
		_, err = io.Copy(os.Stdout, response.Body)
		if err != nil {
			fmt.Fprintf(os.Stderr, "%v\n", err)
			response.Body.Close()
			continue
		}
	}
}

```



## ioutil

### ioutil.ReadFile(file_name)

return the bytes in the file_name specified.

```go
// open, get the whole content of a file and split into lines
for _, file_name := range os.Args[1:] {
    data, err := ioutil.ReadFile(file_name) // return byte slice
    if err != nil {
        fmt.Printf("%s open error, %v", file_name, err)
        continue
    }
    // split the whole content into lines
    for _, line := range strings.Split(string(data), "\n") {
        line_num_map[line]++
    }
}
```



## fmt

### type control

| type   | meaning                                                      |
| ------ | ------------------------------------------------------------ |
| %d     | 十进制整数                                                   |
| %x     | 十六进制整数                                                 |
| %o     | 八进制整数                                                   |
| %b     | 二进制整数                                                   |
| %f     | 浮点数                                                       |
| %t     | 布尔                                                         |
| %c     | 字符                                                         |
| %s     | 字符串                                                       |
| %**q** | **引语**                                                     |
| %**v** | **内置格式**                                                 |
| %**T** | **类型信息**                                                 |
| **%g** | **根据情况选择 `%e` 或 `%f` 以产生更紧凑的（无末尾的0）输出** |
|        |                                                              |



### fmt.Fprintf()

select where to print

```go
// check the protocol

package main

import (
	"fmt"
	"io"
	"net/http"
	"os"
	"strings"
)

const (
	prefix = "https://"
)

func main() {
	for _, url := range os.Args[1:] {
		if !strings.HasPrefix(url, prefix) {
			url = prefix + url
		}
		response, err := http.Get(url)
		if err != nil {
			fmt.Fprintf(os.Stderr, "%v\n", err)
			continue
		}
		_, err = io.Copy(os.Stdout, response.Body)
		if err != nil {
			fmt.Fprintf(os.Stderr, "%v\n", err)
			response.Body.Close()
			continue
		}
	}
}

```



### fmt.Sprintf()

specify the print format

```go
// http get, pass the time to main goroutine
func function(url string, ch chan string) {
	start := time.Now()
	response, err := http.Get(url)
	if err != nil {
		// pass error msg to main goroutine
		// avoid confusing output when both goroutine try to output to stdout
		// uniform output port
		ch <- fmt.Sprintf("%v", err)
		return
	}
	// get the byte length
	byte_num, err := io.Copy(ioutil.Discard, response.Body)
	if err != nil {
		ch <- fmt.Sprintf("%s reading error, %v", url, err)
		return
	}
	// release resource
	response.Body.Close()
	// time and byte length
	ch <- fmt.Sprintf("%.2fs \t%dbytes", time.Since(start).Seconds(), byte_num)
}
```





## string

### join

```go
package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	fmt.Println(strings.Join(os.Args[:], "\n"))
}

```



### HasPrefix/HasSuffix

check the prefix/suffix

```go
const (
	prefix = "https://"
)

func main() {
	for _, url := range os.Args[1:] {
		if !strings.HasPrefix(url, prefix) {
			url = prefix + url
		}
    }
```







## flag

to parse the command-line flags and params

### define flag

flag.Type(name,value,usage)

- 第一个参数是flag名
- 第二个参数是flag的默认值
- 第三个参数是flag的用法（注释）

```go
// flags declaration
// name is the choice name
// if -n specified, it will take true, so the default value should be false
// separator is the separator between words, like '-s &'
var next_line_flag=flag.Bool("n",false,"append /n when echo is over")
var separator =flag.String("s"," ","choose the separator between words")
```



### parse flag

flag.Parse()

if unknown flag in command-line, exit like:

```bash
D:\gocode\learning\ch2\echo>main.exe -n -s @ -w gg 11 22 33
flag provided but not defined: -w
Usage of main.exe:
  -n    append /n when echo is over
  -s string
        choose the separator between words (default " ")
```

- 只有在所有flag都定义好之后，才能调用
- 用来更新flag的值



### access flag and params

- 返回的都是指针，所以通过*p访问选项的值
- params通过flag.Args返回 string slice（不包括os.Args[0]）

```go
func main(){
	// update the flag from its default value
	flag.Parse()
	// flag.Args return the real params
	// excluding the os.Args[0] and the flag(choice)
	fmt.Printf("%s\n",strings.Join(flag.Args(),*separator))
	// bool is %t
	fmt.Printf("next_line_flag:%t",*next_line_flag)
	if *next_line_flag{
		fmt.Printf("\n")
	}
}
```



```bash
D:\gocode\learning\ch2\echo>main.exe -n -s # 11 22 33
11#22#33
next_line_flag:true

D:\gocode\learning\ch2\echo>main.exe -s # 11 22 33
11#22#33
next_line_flag:false
D:\gocode\learning\ch2\echo>main.exe -s # -t 11 22 33
flag provided but not defined: -t
Usage of main.exe:
  -n    append /n when echo is over
  -s string
        choose the separator between words (default " ")

D:\gocode\learning\ch2\echo>

```



## net

### net

- server
  - net.Listen(protocal，address)
    - 协议，地址
    - 返回一个Listener，监听对应的端口
  - Accept
    - 返回一个对应的连接，阻塞

```go
// use tcp to echo time
package main

import (
	"fmt"
	"net"
	"os"
	"time"
)

func main() {
	// listen tcp localhost:8000
	listener, err := net.Listen("tcp", "localhost:8000")
	if err != nil {
		fmt.Fprintf(os.Stderr, "listen error, %s", err)
		return
	}
	for {
		// accept a tcp connection
		connection, err := listener.Accept()
		if err != nil {
			fmt.Fprintf(os.Stderr, "listen error, %s\n", err)
			continue
		}
		fmt.Fprintf(os.Stdout, "%s start connection\n", connection.RemoteAddr())
		go handle(connection)
	}
}

// handle the tcp connection
// return the time in one second gap
func handle(connection net.Conn) {
	defer connection.Close()
	for {
		// return written bytes, err
		if _, err := fmt.Fprintf(connection, time.Now().Format("15:04:05")); err != nil {
			// write error, probably the client close the connection
			fmt.Fprintf(os.Stderr, "%s close connection\n", connection.RemoteAddr())
			break
		}
		// wait one second
		time.Sleep(1 * time.Second)
	}
}


```



- client
  - net.Dial(protocal, address)
    - 与某个地址建立连接
  - 



```go
package main

import (
	"fmt"
	"net"
	"os"
)

const (
	proto = "tcp"
	addr  = "localhost:8000"
)

func main() {
	// client connect to tcp localhost:8000
	connection, err := net.Dial(proto, addr)
	if err != nil {
		fmt.Fprintf(os.Stderr, "connect to %s error, %s", addr, err)
	} else {
		defer connection.Close()
		buf := make([]byte, 8)
		// read from server, and display it
		for {
			if _, err := connection.Read(buf); err != nil {
				fmt.Fprintf(os.Stderr, "read from %s error, %s\n", addr, err)
				break
			} else {
				fmt.Printf("data:%s\n", buf)
			}
		}
	}
}

```





### net/http

#### http.Get

```go
package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
)

func main() {
	for _, url := range os.Args[1:] {
		response, err := http.Get(url)
		if err != nil {
			fmt.Fprintf(os.Stderr, "%v", err)
		} else {
			html, err := ioutil.ReadAll(response.Body)
			if err != nil {
				fmt.Fprintf(os.Stderr, "%v", err)
			} else {
				fmt.Printf("%s", html)
				// release resource
				response.Body.Close()
			}
		}
	}
}

```



# self package reference

- the order that golang searches for package
  - $GOROOT\src\package_path
  - $GOPATH\src\package_path

```bash
import (
	"fmt"
	"learning/ch2/package_test/functool"
	)
D:\gocode\src\learning\ch2\package_test\reference>go build main.go
main.go:18:2: cannot find package "learning/ch2/packet_test/functool" in any of:
        C:\Program Files\Go\src\learning\ch2\packet_test\functool (from $GOROOT)
        C:\Users\user\go\src\src\learning\ch2\packet_test\functool (from $GOPATH)
        D:\gocode\src\learning\ch2\packet_test\functool
        C:\Users\user\go\src\learning\ch2\packet_test\functool

set GOPATH=D:\gocode
set GOROOT=C:\Program Files\Go
```

- package
  - directory name should be the same with the package name
  - any of the go-file in package should have main-func

```go
package main

// GOPATH=C:\Users\user\go\src;D:\gocode
//D:\gocode\src\learning\ch2>tree
//卷 新加卷 的文件夹 PATH 列表
//卷序列号为 F097-B144
//D:.
//├─boiling_1
//├─boiling_2
//├─echo
//├─map_existence
//├─package_test
//│  ├─functool
//     ├─functool.go
//│  └─reference
//     ├─main.go
//└─tempconv_0
import (
	"fmt"
	"learning/ch2/package_test/functool"
	)

func main(){
	fmt.Println(functool.Add(1,2))
}

```







# goroutine

## web server demo

use chan(channel) to communite among goroutines

- 首先编写执行的函数
  - 并发执行
- chan是通道类型，make(chan type)来创建传递type类型数据的通道
  - 接收，<-ch
  - 发送，ch<-data
- go关键字创建goroutine
- **在执行函数中不进行输出，而是通过通道发送到main routine来输出，防止多个goroutine交替输出**

```go
// parallel using goroutine

package main

import (
	"fmt"
	"io"
	"io/ioutil"
	"net/http"
	"os"
	"strings"
	"time"
)

func main() {
	prefix := "https://"
	start := time.Now()
	// make a channel to pass string
	ch := make(chan string)
	for _, url := range os.Args[1:] {
		if !strings.HasPrefix(url, prefix) {
			url = prefix + url
		}
		// start a goroutine to get the url
		go function(url, ch)
	}
	// use neither of the return value
	// cause one goroutine will only send one string
	for range os.Args[1:] {
		// blocking receive from channel
		ret := <-ch
		fmt.Println(ret)
	}
	fmt.Printf("%.2fs", time.Since(start).Seconds())
}

// http get, pass the time to main goroutine
func function(url string, ch chan string) {
	start := time.Now()
	response, err := http.Get(url)
	if err != nil {
		// pass error msg to main goroutine
		// avoid confusing output when both goroutine try to output to stdout
		// uniform output port
		ch <- fmt.Sprintf("%v", err)
		return
	}
	// get the byte length
	byte_num, err := io.Copy(ioutil.Discard, response.Body)
	if err != nil {
		ch <- fmt.Sprintf("%s reading error, %v", url, err)
		return
	}
	// release resource
	response.Body.Close()
	// time and byte length
	ch <- fmt.Sprintf("%.2fs \t%dbytes", time.Since(start).Seconds(), byte_num)
}

```



## Fibonacci demo

- main函数运行在main goroutine中
  - main函数返回或程序退出后，其他所有的goroutine都返回
  - 其他goroutine并不能直接关闭另外的goroutine，但是可以采用goroutine之间的通信方式，让其自己关闭自己

```go
package main

import (
	"fmt"
	"time"
)

func main(){
	// create a routine to display dynamic running flag
	go display(100 * time.Millisecond)
	fmt.Printf("\b%d",fibonacci(45))
}

func display(delay time.Duration) {
	for {
		for _, s := range `-\|/` {
			fmt.Printf("\r%c", s)
			time.Sleep(delay)
		}
	}
}

func fibonacci(n int) int {
	if n < 2 {
		return n
	} else {
		return fibonacci(n-1) + fibonacci(n-2)
	}
}

```



## echo demo

### sequencial server

```go
// use tcp to echo time
package main

import (
	"fmt"
	"net"
	"os"
	"time"
)

func main() {
	// listen tcp localhost:8000
	listener, err := net.Listen("tcp", "localhost:8000")
	if err != nil {
		fmt.Fprintf(os.Stderr, "listen error, %s", err)
		return
	}
	for {
		// accept
		connection, err := listener.Accept()
		if err != nil {
			fmt.Fprintf(os.Stderr, "listen error, %s\n", err)
		} else {
			fmt.Fprintf(os.Stdout, "%s start connection\n", connection.RemoteAddr())
			handle(connection)
		}
	}
}

// handle the tcp connection
// return the time in one second gap
func handle(connection net.Conn) {
	defer connection.Close()
	for {
		// return written bytes, err
		if _, err := fmt.Fprintf(connection, time.Now().Format("15:04:05")); err != nil {
			// write error, probably the client close the connection
			fmt.Fprintf(os.Stderr, "%s close connection\n", connection.RemoteAddr())
			break
		}
		// wait one second
		time.Sleep(1 * time.Second)
	}
}

```



### parallel server

加上一个go，来一个tcp连接就创建一个goroutine。

```go
// use tcp to echo time
package main

import (
	"fmt"
	"net"
	"os"
	"time"
)

func main() {
	// listen tcp localhost:8000
	listener, err := net.Listen("tcp", "localhost:8000")
	if err != nil {
		fmt.Fprintf(os.Stderr, "listen error, %s", err)
		return
	}
	for {
		// accept a tcp connection
		connection, err := listener.Accept()
		if err != nil {
			fmt.Fprintf(os.Stderr, "listen error, %s\n", err)
			continue
		}
		fmt.Fprintf(os.Stdout, "%s start connection\n", connection.RemoteAddr())
		go handle(connection)
	}
}

// handle the tcp connection
// return the time in one second gap
func handle(connection net.Conn) {
	defer connection.Close()
	for {
		// return written bytes, err
		if _, err := fmt.Fprintf(connection, time.Now().Format("15:04:05")); err != nil {
			// write error, probably the client close the connection
			fmt.Fprintf(os.Stderr, "%s close connection\n", connection.RemoteAddr())
			break
		}
		// wait one second
		time.Sleep(1 * time.Second)
	}
}

```



### client

```go
package main

import (
	"fmt"
	"net"
	"os"
)

const (
	proto = "tcp"
	addr  = "localhost:8000"
)

func main() {
	// client connect to tcp localhost:8000
	connection, err := net.Dial(proto, addr)
	if err != nil {
		fmt.Fprintf(os.Stderr, "connect to %s error, %s", addr, err)
	} else {
		defer connection.Close()
		buf := make([]byte, 8)
		// read from server, and display it
		for {
			if _, err := connection.Read(buf); err != nil {
				fmt.Fprintf(os.Stderr, "read from %s error, %s\n", addr, err)
				break
			} else {
				fmt.Printf("data:%s\n", buf)
			}
		}
	}
}

```



# web server

## echo server

返回http 请求的url path

- http.HandleFunc(path,func)
  - 决定某个url用什么函数来处理
  - func的参数为(http.ResponseWriter, *http.Request)
    - 第一个参数填充响应，第二个参数是客户端的请求
- http.ListenAndServe("localhost:8000", nil)
  - 启动web server

```go
package main

import (
	"fmt"
	"net/http"
)

func main() {
	http.HandleFunc("/", handle_request)
	http.ListenAndServe("localhost:8000", nil)
}

func handle_request(response http.ResponseWriter, request *http.Request) {
	// write sth to response
	fmt.Fprintf(response, "URL.PATH=%q\n", request.URL.Path)
}

```



## echo and count

返回请求次数或者请求的url path

- 注意路由匹配的规则：最长匹配
  - 如果计数函数的规则是`'/count' 和 `/``，浏览器的url是`'/count/'` ，会匹配两个规则
  - 正确的规则应该是`'/count/' 和 `/`
- sync.mutex是互斥锁，保证互斥的访问共享变量count
  - 为什么需要互斥？
    - web server自动对来的请求开启goroutine

```go
// '/' get the path
//'/count/' get the http request times, self excluded

package main

import (
	"fmt"
	"net/http"
	"os"
	"sync"
)

var count_mutex sync.Mutex // count mutex
var count int              // count the request times
func main() {
	http.HandleFunc("/", root_handler)
	http.HandleFunc("/count/", count_request_times)
	http.ListenAndServe("localhost:8000", nil)
}

// return the request path and count plus 1
func root_handler(response http.ResponseWriter, request *http.Request) {
	fmt.Printf("in root_handler\n")
	count_mutex.Lock()
	count++
	count_mutex.Unlock()
	fmt.Fprintf(response, "%s URL.PATH:%q\n", os.Args[0], request.URL.Path)
}

// return the request times
func count_request_times(response http.ResponseWriter, request *http.Request) {
	fmt.Printf("in count_handler\n")
	count_mutex.Lock()
	fmt.Fprintf(response, "total times:%d", count)
	count_mutex.Unlock()
}

```



### method, header, param

- if 如果只有一个表达式，那么这个表达式用来判定条件
- 如果有两个，那么第一个用来初始化（作用域仅在if中）。第二个用来判定条件

```go
// display the concrete http request info

package main

import (
	"fmt"
	"net/http"
	"os"
)

func main() {
	http.HandleFunc("/", display_info_handler)
	http.ListenAndServe("localhost:8000", nil)
}

func display_info_handler(response http.ResponseWriter, request *http.Request) {
	// first line of http request: method, url, protocol
	fmt.Fprintf(response, "%s %s %s\n", request.Method, request.URL, request.Proto)

	// header
	// http.Header is a type Header map[string][]string
	// so iterate
	for key, value := range request.Header {
		fmt.Fprintf(response, "%q %q\n", key, value)
	}

	// url params
	// a simplified form, when initializing err in 'if' expression
	if err := request.ParseForm(); err != nil {
		fmt.Fprintf(os.Stderr, "request parse error, %q\n", err)
		return
	}
	for q, a := range request.Form {
		fmt.Fprintf(response, "q: %q a: %q\n", q, a)
	}
}

```

 





## gif pic in browser

- anonymous function

```bash
func main() {
	// show the http request info
	http.HandleFunc("/show", display_info_handler)
	// show a gif pic
	// anonymous func to simplify code
	http.HandleFunc("/gif", func(resp http.ResponseWriter, requ *http.Request) {
		fmt.Printf("in display_gif_handler\n")
		lissajous(resp)
	})

	http.ListenAndServe("localhost:8000", nil)
}

```



## git pic in browser with param passing

- 可能解析失败
- 可能没有这个参数
- 可能参数的类型不正确

```go
func handle_gif(response http.ResponseWriter, request *http.Request) {
	fmt.Printf("handle /gif\n")
	// parse param
	if err := request.ParseForm(); err != nil {
		fmt.Fprintf(response, "error when parsing the %q form ,%s", request.URL, err)
	}
	// the key may not exist
	if cycles_key, ok := request.Form["cycles"]; ok {
		// convert the string to int
		if cycles, err := strconv.Atoi(cycles_key[0]); err != nil {
			fmt.Fprintf(response, "wrong params,%s", err)
		} else {
			lissajous(response, cycles)
		}
	} else {
		fmt.Fprintf(response, "please enter the 'cycles' param")
	}
}
```



# go command

## go fmt

### command

```bash
(base) PS D:\gocode\learning\ch1\1_helloworld> gofmt -h
usage: gofmt [flags] [path ...]
  -cpuprofile string
        write cpu profile to this file
  -d    display diffs instead of rewriting files
  -e    report all errors (not just the first 10 on different lines)
  -l    list files whose formatting differs from gofmt's
  -r string
        rewrite rule (e.g., 'a[b:len(a)] -> a[b:]')
  -s    simplify code
  -w    write result to (source) file instead of stdout
```

`go fmt -l -s -w`

显示与标准不同的文件+修改文件为标准格式



### ide

![image-20220121100919045](https://raw.githubusercontent.com/whr819987540/pic/main/image-20220121100919045.png)



## go get





## 