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

| type   | meaning      |
| ------ | ------------ |
| %d     | 十进制整数   |
| %x     | 十六进制整数 |
| %o     | 八进制整数   |
| %b     | 二进制整数   |
| %f     | 浮点数       |
| %t     | 布尔         |
| %c     | 字符         |
| %s     | 字符串       |
| %**q** | **引语**     |
| %**v** | **内置格式** |
| %**T** | **类型信息** |



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





## http

### http.Get

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



# goroutine

use chan(channel) to communite among goroutines

## demo

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

```go
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

![image-20220121100919045](https://gitee.com/hit_whr/pic_2.0/raw/main/image-20220121100919045.png)



## go get





## 