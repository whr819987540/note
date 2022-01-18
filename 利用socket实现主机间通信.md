# 利用socket实现主机间通信

## 原理

在windows、linux、BSD unix平台上都实现了socket这个网络协议软件接口，可以利用os提供的api，让App和操作系统内核的协议栈进行交互，然后实现网络通信。



## 过程

首先server、client进行dll的初始化。

server创建listen_sock，bind到本机ip和外部访问的固定端口上，然后listen，让listent_sock处于监听状态。

同时client创建sock，connect到server ip和server的固定端口上，此时connect()可能阻塞，让client进入阻塞状态，一旦三次握手后tcp连接建立，则connect()返回，client进入就绪状态，然后client开始向server发送数据。

server的accept发现有tcp连接到来，建立连接后创建connect_sock()，开始recv()，阻塞，知道接收数据到App的应用缓冲区，然后回显这部分数据。让用户输入，调用send，发给client。

client多次调用recv，如果出错，退出；否则，知道recv的返回值为0，即server断开了连接。然后client对收到的数据进行回显。

![image-20211108215340597](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20211108215340597.png)

## 感悟

- 加深了对c/s模型和socket编程的理解
- 通过调用这些api阻塞的函数和设计一个简单的应用层协议，加深了对进程三基本状态的理解