HTTP/1不支持服务器主动向客户端发送数据。用websocket解决。

```bash
# telnet连接
telnet www.taohui.pub 80
# http请求
GET / HTTP/1.1
Host: www.baidu.com
# 输入Host后输入一个回车，再输入一个回车
```

# HTTP协议的格式

## 自然语言描述

![image-20210908222626050](https://raw.githubusercontent.com/whr819987540/pic/main/image-20210908222626050.png)



## 形式化（ABNF范式）

![image-20210908222718248](https://raw.githubusercontent.com/whr819987540/pic/main/image-20210908222718248.png)



![image-20210908222742765](https://raw.githubusercontent.com/whr819987540/pic/main/image-20210908222742765.png)



![image-20210908222943185](https://raw.githubusercontent.com/whr819987540/pic/main/image-20210908222943185.png)



## request

```bash
method SP resource_path SP HTTP/版本号/r/n
header-name:[SP]header-value\r\n
\r\n
```





## response

```bash
HTTP-版本号 SP status_code SP desp_str
header-name:[SP]header-value/r/n
/r/n
[response_body] 
```





# OSI

![image-20210908223336003](https://raw.githubusercontent.com/whr819987540/pic/main/image-20210908223336003.png)



![image-20210908223512401](https://raw.githubusercontent.com/whr819987540/pic/main/image-20210908223512401.png)



解决封装层数过多带来的性能下降问题：interl DPDK



# HTTP

## 功能决定形式

![image-20210908225202558](https://raw.githubusercontent.com/whr819987540/pic/main/image-20210908225202558.png)



## http的功能

人机交互。

中介：浏览器



JavaScript的执行放在本地：提高用户交互体验



## 问题

![image-20210908225713831](https://raw.githubusercontent.com/whr819987540/pic/main/image-20210908225713831.png)



- 大粒度是指数据量比较大
- 规模无法控制
- 客户端、服务器端都是无状态的，因为负载是未知的，如果有状态，难以维持高负载下的运转
- 兼容性（向前兼容）



