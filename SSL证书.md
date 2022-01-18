# 源码安装nginx

```bash
cd /usr/local/src/
wget http://nginx.org/download/nginx-1.20.1.tar.gz
tar -xzf nginx-1.20.1.tar.gz -C ../
cd ../nginx-1.20.1/
mkdir module
cd module/
git clone https://github.com/cuber/ngx_http_google_filter_module
apt install git
git clone https://github.com/cuber/ngx_http_google_filter_module
git clone https://github.com/yaoweibin/ngx_http_substitutions_filter_module
cd ../

apt-get install -y openssl libssl-dev libpcre3 libpcre3-dev zlib1g-dev

./configure --prefix=/usr/local/nginx --with-http_ssl_module --with-http_sub_module --with-http_gzip_static_module --with-http_stub_status_module --add-module=`pwd`/module/ngx_http_google_filter_module --add-module=`pwd`/module/ngx_http_substitutions_filter_module

make && make install
ln -s /usr/local/nginx/sbin/nginx /usr/sbin/nginx
```



## 去**nginx.org**官网寻找稳定版的源码

![image-20210915202022430](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210915202022430.png)



![image-20210915202147192](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210915202147192.png)



## 解压

![image-20210915202213721](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210915202213721.png)



## 目录结构：

![image-20210915202243171](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210915202243171.png)

- auto，辅助configure脚本进行系统判断

- changes，相比于上一版的变化

- html里面放了index.html和50x错误的html

- conf，里面的nginx.conf存放默认的配置文件

- man存放帮助文档

- contrib是辅助nginx配置文件代码的高亮显示，需要将vim放到/usr/bin目录下

  - ```bash
    [root@whr contrib]# mkdir ~/.vim
    [root@whr contrib]# cp -r vim/* ~/.vim
    ```

  - ![image-20210915203641148](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210915203641148.png)

## 编译前的配置

编译前的配置主要是指定编译时包括哪些模块。

先看看帮助文档。

```bash
[root@whr nginx-1.20.1]# ./configure --help

  --help                             print this message

  --prefix=PATH                      set installation prefix
  --sbin-path=PATH                   set nginx binary pathname
  --modules-path=PATH                set modules path
  --conf-path=PATH                   set nginx.conf pathname
  --error-log-path=PATH              set error log pathname
  --pid-path=PATH                    set nginx.pid pathname
  --lock-path=PATH                   set nginx.lock pathname

  --user=USER                        set non-privileged user for
                                     worker processes
  --group=GROUP                      set non-privileged group for
                                     worker processes

  --build=NAME                       set build name
  --builddir=DIR                     set build directory

  --with-select_module               enable select module
  --without-select_module            disable select module
```



需要注意的是--prefix选项，指定nginx的安装位置。



## 配置安装路径

这里安装在/usr/local/目录下

```bash
./configure --prefix=/usr/local/nginx
```



## 编译

`make`



## 安装

make install 



## 软链接

```bash
ln -s /usr/local/nginx/sbin/nginx /usr/sbin/nginx
```



# HTTPS

## 购买一个域名



## 域名解析

在阿里云的控制台配置域名解析

![image-20210915215507723](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210915215507723.png)



![image-20210915215512140](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210915215512140.png)



![image-20210915215539977](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210915215539977.png)



记录值就是DNS服务器向client返回的值，这里就是服务器的IP地址。

然后修改conf/nginx.conf，server name由ip地址修改为域名即可。

![image-20210915215654591](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210915215654591.png)



## ICP备案

申请域名后，需要进行备案





## 配置SSL证书

SSL整数有DV,OV,EV证书。这里申请的是免费的DV证书。

### 工具安装

```bash
pip install certbot
certbot certonly --webroot -w /usr/local/nginx/docs -d ydnd.icu
```

这里显示找不到域名对应的ip，这确实没办法，icu这个顶级域是国内的，而颁发整数的CA似乎不知道这个DNS服务器。



### 阿里云SSL证书

立即购买

![image-20210916161317461](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210916161317461.png)



![image-20210916161342938](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210916161342938.png)



选购SSL证书

![image-20210916161430666](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210916161430666.png)





![image-20210916161501988](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210916161501988.png)



创建证书之后，申请证书。

![image-20210916161533650](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210916161533650.png)



在申请证书、CA机构签发证书后，可以下载pem和key文件。

![image-20210916161712345](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210916161712345.png)



根据服务器类型选择合适的文件。

下载好.pem和.key文件后，复制到安装目录/conf/cert/目录下，然后修改nginx.conf文件。

```bash
#以下属性中，以ssl开头的属性表示与证书配置有关。
server {
    listen 443 ssl;
    #配置HTTPS的默认访问端口为443。
    #如果未在此处配置HTTPS的默认访问端口，可能会造成Nginx无法启动。
    #如果您使用Nginx 1.15.0及以上版本，请使用listen 443 ssl代替listen 443和ssl on。
    server_name yourdomain.com; #需要将yourdomain.com替换成证书绑定的域名。
    root html;
    index index.html index.htm;
    ssl_certificate cert/cert-file-name.pem;  #需要将cert-file-name.pem替换成已上传的证书文件的名称。
    ssl_certificate_key cert/cert-file-name.key; #需要将cert-file-name.key替换成已上传的证书密钥文件的名称。
    ssl_session_timeout 5m;
    ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE:ECDH:AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4;
    #表示使用的加密套件的类型。
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2; #表示使用的TLS协议的类型。
    ssl_prefer_server_ciphers on;
    location / {
        root html;  #站点目录。
        index index.html index.htm;
    }
}
```



然后将http（80）的流量都跳转到https（443）页面。

```bash
#以下属性中，以ssl开头的属性表示与证书配置有关。
server {
    listen 443 ssl;
    #配置HTTPS的默认访问端口为443。
    #如果未在此处配置HTTPS的默认访问端口，可能会造成Nginx无法启动。
    #如果您使用Nginx 1.15.0及以上版本，请使用listen 443 ssl代替listen 443和ssl on。
    server_name yourdomain.com; #需要将yourdomain.com替换成证书绑定的域名。
    root html;
    index index.html index.htm;
    ssl_certificate cert/cert-file-name.pem;  #需要将cert-file-name.pem替换成已上传的证书文件的名称。
    ssl_certificate_key cert/cert-file-name.key; #需要将cert-file-name.key替换成已上传的证书密钥文件的名称。
    ssl_session_timeout 5m;
    ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE:ECDH:AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4;
    #表示使用的加密套件的类型。
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2; #表示使用的TLS协议的类型。
    ssl_prefer_server_ciphers on;
    location / {
        root html;  #站点目录。
        index index.html index.htm;
    }
}
```



最后重启nginx

```bash
nginx -s reload -c /usr/local/nginx/conf/nginx.conf
```





# 杂记

## 重启nginx nginx: [error] open() "/usr/local/nginx/logs/nginx.pid" failed

```bash
[root@whr objs]# nginx -V
nginx version: nginx/1.20.1
built by gcc 4.8.5 20150623 (Red Hat 4.8.5-44) (GCC) 
built with OpenSSL 1.0.2k-fips  26 Jan 2017
TLS SNI support enabled
configure arguments: --prefix=/usr/local/nginx --with-http_ssl_module --with-http_sub_module --with-http_gzip_static_module --with-http_stub_status_module
[root@whr objs]# nginx -s reload -c /usr/local/nginx/conf/nginx.conf
nginx: [error] open() "/usr/local/nginx/logs/nginx.pid" failed (2: No such file or directory)
[root@whr objs]# ps -aux|grep nginx
root     28627  0.0  0.0 112812   976 pts/1    S+   15:31   0:00 grep --color=auto nginx
```

需要重新指定配置文件，而且是手动指定，神之迷惑。

```bash
[root@whr objs]# nginx -c conf/nginx.conf
[root@whr objs]# nginx -s reload
[root@whr objs]# ps -aux|grep nginx
root     28686  0.0  0.1  46156  2708 ?        Ss   15:32   0:00 nginx: master process nginx -c conf/nginx.conf
nobody   28693  0.0  0.1  46548  2088 ?        S    15:32   0:00 nginx: worker process
nobody   28694  0.0  0.1  46548  2336 ?        S    15:32   0:00 nginx: worker process
root     28945  0.0  0.0 112812   976 pts/1    R+   15:37   0:00 grep --color=auto nginx
[root@whr objs]# nginx -t
nginx: the configuration file /usr/local/nginx/conf/nginx.conf syntax is ok
nginx: configuration file /usr/local/nginx/conf/nginx.conf test is successful
```



## 添加官方模块或第三方模块

有时候突然发现编译时没有安装某个模块，所以需要重新编译。

```bash
# 进入到安装包目录
[root@whr module]# cd /root
[root@whr ~]# ls
ad_project  code_plat.backup  nginx-1.20.1  nginx-1.20.1.tar.gz  not_forget  novel  project  requirements.txt  test
[root@whr ~]# cd nginx-1.20.1
[root@whr nginx-1.20.1]# ls
auto  CHANGES  CHANGES.ru  conf  configure  contrib  html  LICENSE  Makefile  man  module  objs  README  src

# 先下载第三方模块
mkdir module
[root@whr nginx-1.20.1]# cd module/
[root@whr module]# git clone https://github.com/cuber/ngx_http_google_filter_module
Cloning into 'ngx_http_google_filter_module'...
remote: Enumerating objects: 314, done.
remote: Total 314 (delta 0), reused 0 (delta 0), pack-reused 314
Receiving objects: 100% (314/314), 84.53 KiB | 0 bytes/s, done.
Resolving deltas: 100% (207/207), done.
[root@whr module]# git clone https://github.com/yaoweibin/ngx_http_substitutions_filter_module
Cloning into 'ngx_http_substitutions_filter_module'...
remote: Enumerating objects: 496, done.
remote: Total 496 (delta 0), reused 0 (delta 0), pack-reused 496
Receiving objects: 100% (496/496), 275.92 KiB | 232.00 KiB/s, done.
Resolving deltas: 100% (260/260), done.
[root@whr module]# ls
ngx_http_google_filter_module  ngx_http_substitutions_filter_module

# 查看之前安装的模块
# nginx在安装时，不会进行增量添加，而是全量添加，所以之前添加的模块还得在命令中再添加一遍
nginx version: nginx/1.20.1
built by gcc 4.8.5 20150623 (Red Hat 4.8.5-44) (GCC) 
built with OpenSSL 1.0.2k-fips  26 Jan 2017
TLS SNI support enabled
configure arguments: --prefix=/usr/local/nginx --with-http_ssl_module --with-http_sub_module --with-http_gzip_static_module --with-http_stub_status_module

# 重新设置模块（这里加上了官方模块和第三方模块）
./configure --prefix=/usr/local/nginx --with-http_ssl_module --with-http_sub_module --with-http_gzip_static_module --with-http_stub_status_module --add-module=/root/nginx-1.20.1/module/ngx_http_google_filter_module --add-module=/root/nginx-1.20.1/module/ngx_http_substitutions_filter_module

make
# 然后替换可执行文件即可
[root@whr nginx-1.20.1]# ls
auto  CHANGES  CHANGES.ru  conf  configure  contrib  html  LICENSE  Makefile  man  module  objs  README  src
[root@whr nginx-1.20.1]# cd objs/
[root@whr objs]# ls
addon  autoconf.err  Makefile  nginx  nginx.8  ngx_auto_config.h  ngx_auto_headers.h  ngx_modules.c  ngx_modules.o  src
[root@whr objs]# ll /usr/sbin/nginx
lrwxrwxrwx 1 root root 27 Sep 15 20:49 /usr/sbin/nginx -> /usr/local/nginx/sbin/nginx
[root@whr objs]# cp /usr/local/nginx/sbin/nginx /usr/local/nginx/sbin/nginx.backup
cp: overwrite ‘/usr/local/nginx/sbin/nginx.backup’? y
[root@whr objs]# cp nginx /usr/local/nginx/sbin/nginx
cp: overwrite ‘/usr/local/nginx/sbin/nginx’? y
cp: cannot create regular file ‘/usr/local/nginx/sbin/nginx’: Text file busy

# nginx在执行，所以该文件被占用了
[root@whr objs]# nginx -s stop
[root@whr objs]# cp nginx /usr/local/nginx/sbin/nginx
cp: overwrite ‘/usr/local/nginx/sbin/nginx’? y

[root@whr objs]# nginx -s reload
nginx: [error] open() "/usr/local/nginx/logs/nginx.pid" failed (2: No such file or directory)
[root@whr objs]# nginx -c conf/nginx.conf
[root@whr objs]# nginx -s reload
[root@whr objs]# curl https://www.ydnd.icu
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN" "http://www.w3.org/TR/REC-html40/loose.dtd">
<html xmlns:g



```



```bash


```



# 更换系统

## 做好代码备份



## 下载软件



### gcc

```bash
```



# nginx路由

```bash
location /test/ {
            root   docs;
            index  index.html index.htm;
        }
这一个代码块是说，如果用户提交的url是https://domain/test/，则在nginx安装目录下找到docs文件夹作为root目录，由于访问的是test/，所以在docs文件夹下找test文件夹

现在的目录结构是
root@iZm5e98zphj5y525q4v5k4Z:/usr/local/nginx# tree -L 2 -d
.
├── client_body_temp
├── conf
│   └── cert
├── fastcgi_temp
├── html
├── logs
├── proxy_temp
├── sbin
├── scgi_temp
├── test
│   └── docs
└── uwsgi_temp
显然访问的应该是 test/为根，下面的docs文件夹
2021/09/24 22:40:56 [error] 94794#0: *16 "/usr/local/nginx/docs/test/index.html" is not found (2: No such file or directory), client: 221.2.164.13, server: www.ydnd.icu, request: "GET /test/ HTTP/1.1", host: "www.ydnd.icu"
root@iZm5e98zphj5y525q4v5k4Z:/usr/local/nginx/logs# vim ../conf/my_nginx.conf 

修改一下配置文件
location /docs/ {
            root   static;
            index  index.html index.htm;
        }
修改一下目录结构
root@iZm5e98zphj5y525q4v5k4Z:/usr/local/nginx# tree -L 2 -d
.
├── client_body_temp
├── conf
│   └── cert
├── fastcgi_temp
├── html
├── logs
├── proxy_temp
├── sbin
├── scgi_temp
├── static
│   └── docs
└── uwsgi_temp
访问

```

![image-20210924224853976](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210924224853976.png)



# wordpress建站





# 自动发邮件

## sendEmail命令安装(失败)

```bash
cd /usr/local/src
wget http://caspian.dotconf.net/menu/Software/SendEmail/sendEmail-v1.56.tar.gz
tar -xzf sendEmail-v1.56.tar.gz
mv sendEmail-v1.56 ../
cd ../sendEmail-v1.56
ln -s `pwd`/sendEmail /usr/bin/
```



```bash
sendEmail -f 15266981370@sina.cn -s smtp.sina.cn \
-xp 958307031162088b -xu 15266981370@sina.cn \
-t 819987540@qq.com \
-u "main_control模块挂掉了" -m "出错机器的ip地址是" \
-o message-content-type=html -o message-charset=utf-8

/usr/bin/sendEmail -f 15266981370@sina.cn -t 819987540@qq.com -s smtp.sina.cn -u "test" -o message-content-type=html -o message-charset=utf-8 -xu 15266981370@sina.cn -xp 958307031162088b -m 'test'


新浪邮箱958307031162088b


163邮箱PJOTYCRDJDGVLBLQ
sendEmail -f whr15266981370@163.com -s smtp.163.com -xp PJOTYCRDJDGVLBLQ -xu whr15266981370@163.com -t 819987540@qq.com -u "main_control模块挂掉了" -m "出错机器的ip地址是" -o message-content-type=html -o message-charset=utf-8
```



## 程序自动发送

### 前提

为了使用第三方工具自动发送，需要让邮件服务器支持SMPT(发送邮件)、IMPT（接收邮件）。

在开启SMPT时，都会发送一个授权码，此时不用密码了，而是授权码。



### 发送方：

- 服务器的25/465端口都放行

- 邮箱：whr15266981370@163.com
- 授权码：PJOTYCRDJDGVLBLQ
- SMTP服务器地址：smtp.163.com
- SMTP服务器端口：465

### 接收方：

-  819987540@qq.com

- 需要在接收方的客户端将发送方的邮箱地址设置为白名单，防止接收方的IMTP服务器拒绝接收邮件

  ```bash
  554 DT:SPM 发送的邮件内容包含了未被许可的信息，或被系统识别为垃圾邮件。请检查是否有用户发送病毒或者垃圾邮件；
  ```

  

```bash
# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
import os
def get_ip():
    r = os.popen(r"ip address |sed -rn '/state UP/{n;n;s#^ *inet (.*)/.*$#\1#gp}'").read().split('\n')
    return r[0]
def get_error_type(ip:str):
    if ip.split('.')=='55':
        return 'main_control'
    else:
        return 'child'
sender = 'whr15266981370@163.com'
receive = '819987540@qq.com'
passwd = 'PJOTYCRDJDGVLBLQ' # 授权码python3
mailserver = 'smtp.163.com'
port = '465'
local_ip = get_ip()
error_type = get_error_type(local_ip)
subject = f'广告项目出错，ip：{local_ip}，类型{error_type}'

msg = MIMEMultipart('related')
msg['From'] = formataddr(["ME", sender])
msg['To'] = formataddr(["YOU,ME", receive])
msg['Subject'] = subject

txt = MIMEText('赶紧来修复吧！', 'plain', 'utf-8')
msg.attach(txt)


server = smtplib.SMTP_SSL(mailserver, port)
server.login(sender, passwd)
server.sendmail(sender, receive, msg.as_string())
server.quit()
```







## telnet发送

```bash
telnet smtp.163.com 25
HELO localhost 
AUTH LOGIN  
# whr15266981370@163.com base64编码后
d2hyMTUyNjY5ODEzNzBAMTYzLmNvbQ==
# PJOTYCRDJDGVLBLQ编码后
UEpPVFlDUkRKREdWTEJMUQ==

mail from: <whr15266981370@163.com>
rcpt to: <819987540@qq.com>
DATA
from: aliyun
to: sina
subject: this is a demo show

this is email content

.
```



## iptable

```bash
# 输入
# 允许通过{port}输入
iptables -A INPUT -p tcp --dport {port} -j ACCEPT
# 禁止通过{port}输入
iptables -A INPUT -p tcp --dport {port} -j DROP
# 输出
# 允许通过{port}输出
iptables -A OUTPUT -p tcp --sport {port} -j ACCEPT
# 禁止通过{port}输出
iptables -A OUTPUT -p tcp --sport {port} -j DROP
```

