```bash
uwsgi unrecognized option '--wsgi-file'
yum install uwsgi-plugin-python

在测试uwsgi时，发现现在8000端口仍然被之前的python manage.py runserver占用
而我以为退出了当时的程序就行了，显然仍然有进程在占用8000端口，看一下是谁
yum install lsof
[root@iZm5e98zphj5y525q4v5k4Z ~]# lsof -i:8000
COMMAND  PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
python  4645 root    7u  IPv4 108933      0t0  TCP localhost:irdmi (LISTEN)
kill -9 4645

uwsgi --http-socket :8001 --plugin python --wsgi-file foobar.py 
[root@iZm5e98zphj5y525q4v5k4Z ~]# lsof -i:8001
COMMAND   PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
uwsgi   10198 root    3u  IPv4 112406      0t0  TCP *:vcom-tunnel (LISTEN)
当前开启的端口确实在被uwsgi占用
foobar.py里面是
def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World"]
Internal Server Error[root@iZm5e98zphj5y525q4v5k4Z ~]# curl http://127.0.0.1:8001/
Hello World
[root@iZm5e98zphj5y525q4v5k4Z ~]# 

uwsgi默认是单线程和单进程，下面进行配置
uwsgi --http-socket :8001 --plugin python --wsgi-file foobar.py --master --processes 4 --threads 2
四个进程，每个进程两个线程，一个主进程（将其他进程复活）
--stats 127.0.0.1:9191
重开一个端口，进行数据记录（json）
这里的ip地址需要是私有的，否则别人可以进行访问


现在进行完整测试
uwsgin --http-socket :8000 --plugin python --wsgi-file foobar.py --master --process 4 --threads 2
[root@iZm5e98zphj5y525q4v5k4Z ~]# lsof -i:8000
COMMAND   PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
uwsgi   11442 root    3u  IPv4 113522      0t0  TCP *:irdmi (LISTEN)
uwsgi   11443 root    3u  IPv4 113522      0t0  TCP *:irdmi (LISTEN)
uwsgi   11444 root    3u  IPv4 113522      0t0  TCP *:irdmi (LISTEN)
uwsgi   11445 root    3u  IPv4 113522      0t0  TCP *:irdmi (LISTEN)
uwsgi   11446 root    3u  IPv4 113522      0t0  TCP *:irdmi (LISTEN)

[root@iZm5e98zphj5y525q4v5k4Z ~]# lsof -i:8001
COMMAND   PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
uwsgi   11442 root   15u  IPv4 113560      0t0  TCP localhost:vcom-tunnel (LISTEN)

[root@iZm5e98zphj5y525q4v5k4Z ~]# curl 127.0.0.1:8000/
Hello World
curl 127.0.0.1:8001/
查看统计信息（json格式）
[root@iZm5e98zphj5y525q4v5k4Z ~]# curl 127.0.0.1:8001/
	"version":"2.0.18",
	"listen_queue":0,
	"listen_queue_errors":0,
	"signal_queue":0,
	"load":0,
	"pid":11442,
	"uid":0,
	"gid":0,
	"cwd":"/root",
	"locks":[
		{
			"user 0":0
		},
		{
			"signal":0
		},
		{
			"filemon":0
		},
		{
			"timer":0
		},
		{
			"rbtimer":0
		},
		{
			"cron":0
		},
		{
			"rpc":0
		},
		{
			"snmp":0
		}
	],
	"sockets":[
		{
			"name":":8000",
			"proto":"http",
			"queue":0,
			"max_queue":100,
			"shared":0,
			"can_offload":0
		}
	],
	"workers":[
		{
			"id":1,
			"pid":11443,
			"accepting":1,
			"requests":0,
			"delta_requests":0,
			"exceptions":0,
			"harakiri_count":0,
			"signals":0,
			"signal_queue":0,
			"status":"idle",
			"rss":0,
			"vsz":0,
			"running_time":0,
			"last_spawn":1618732094,
			"respawn_count":1,
			"tx":0,
			"avg_rt":0,
			"apps":[
				{
					"id":0,
					"modifier1":0,
					"mountpoint":"",
					"startup_time":0,
					"requests":0,
					"exceptions":0,
					"chdir":""
				}
			],
			"cores":[
				{
					"id":0,
					"requests":0,
					"static_requests":0,
					"routed_requests":0,
					"offloaded_requests":0,
					"write_errors":0,
					"read_errors":0,
					"in_request":0,
					"vars":[

					],
					"req_info":					{

					}
				},
				{
					"id":1,
					"requests":0,
					"static_requests":0,
					"routed_requests":0,
					"offloaded_requests":0,
					"write_errors":0,
					"read_errors":0,
					"in_request":0,
					"vars":[

					],
					"req_info":					{

					}
				}
			]
		},
		{
			"id":2,
			"pid":11444,
			"accepting":1,
			"requests":0,
			"delta_requests":0,
			"exceptions":0,
			"harakiri_count":0,
			"signals":0,
			"signal_queue":0,
			"status":"idle",
			"rss":0,
			"vsz":0,
			"running_time":0,
			"last_spawn":1618732094,
			"respawn_count":1,
			"tx":0,
			"avg_rt":0,
			"apps":[
				{
					"id":0,
					"modifier1":0,
					"mountpoint":"",
					"startup_time":0,
					"requests":0,
					"exceptions":0,
					"chdir":""
				}
			],
			"cores":[
				{
					"id":0,
					"requests":0,
					"static_requests":0,
					"routed_requests":0,
					"offloaded_requests":0,
					"write_errors":0,
					"read_errors":0,
					"in_request":0,
					"vars":[

					],
					"req_info":					{

					}
				},
				{
					"id":1,
					"requests":0,
					"static_requests":0,
					"routed_requests":0,
					"offloaded_requests":0,
					"write_errors":0,
					"read_errors":0,
					"in_request":0,
					"vars":[

					],
					"req_info":					{

					}
				}
			]
		},
		{
			"id":3,
			"pid":11445,
			"accepting":1,
			"requests":0,
			"delta_requests":0,
			"exceptions":0,
			"harakiri_count":0,
			"signals":0,
			"signal_queue":0,
			"status":"idle",
			"rss":0,
			"vsz":0,
			"running_time":0,
			"last_spawn":1618732094,
			"respawn_count":1,
			"tx":0,
			"avg_rt":0,
			"apps":[
				{
					"id":0,
					"modifier1":0,
					"mountpoint":"",
					"startup_time":0,
					"requests":0,
					"exceptions":0,
					"chdir":""
				}
			],
			"cores":[
				{
					"id":0,
					"requests":0,
					"static_requests":0,
					"routed_requests":0,
					"offloaded_requests":0,
					"write_errors":0,
					"read_errors":0,
					"in_request":0,
					"vars":[

					],
					"req_info":					{

					}
				},
				{
					"id":1,
					"requests":0,
					"static_requests":0,
					"routed_requests":0,
					"offloaded_requests":0,
					"write_errors":0,
					"read_errors":0,
					"in_request":0,
					"vars":[

					],
					"req_info":					{

					}
				}
			]
		},
		{
			"id":4,
			"pid":11446,
			"accepting":1,
			"requests":1,
			"delta_requests":1,
			"exceptions":0,
			"harakiri_count":0,
			"signals":0,
			"signal_queue":0,
			"status":"idle",
			"rss":0,
			"vsz":0,
			"running_time":157,
			"last_spawn":1618732094,
			"respawn_count":1,
			"tx":55,
			"avg_rt":78,
			"apps":[
				{
					"id":0,
					"modifier1":0,
					"mountpoint":"",
					"startup_time":0,
					"requests":1,
					"exceptions":0,
					"chdir":""
				}
			],
			"cores":[
				{
					"id":0,
					"requests":1,
					"static_requests":0,
					"routed_requests":0,
					"offloaded_requests":0,
					"write_errors":0,
					"read_errors":0,
					"in_request":0,
					"vars":[

					],
					"req_info":					{

					}
				},
				{
					"id":1,
					"requests":0,
					"static_requests":0,
					"routed_requests":0,
					"offloaded_requests":0,
					"write_errors":0,
					"read_errors":0,
					"in_request":0,
					"vars":[

					],
					"req_info":					{

					}
				}
			]
		}
	]
curl: (56) Recv failure: Connection reset by peer


初步熟悉了uwsgi后，看看nginx
先看看nginx的进程
[root@iZm5e98zphj5y525q4v5k4Z ~]# ps aux |grep nginx
root     22106  0.0  0.1 105496  1988 ?        Ss   19:22   0:00 nginx: master process nginx
nginx    22107  0.0  0.1 105964  2976 ?        S    19:22   0:00 nginx: worker process
root     22264  0.0  0.0 112708   984 pts/1    R+   19:25   0:00 grep --color=auto nginx
看到了三个进程，后面详细看看master和worker进程
根据进程号查端口，选择master进程
netstat -anp|grep

[root@iZm5e98zphj5y525q4v5k4Z ~]# netstat -anp|grep 22106
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      22106/nginx: master 
tcp6       0      0 :::80                   :::*                    LISTEN      22106/nginx: master 
unix  3      [ ]         STREAM     CONNECTED     120877   22106/nginx: master  
unix  3      [ ]         STREAM     CONNECTED     120876   22106/nginx: master

看到开了80端口

下面来配置nginx，虽然uwsgi可以完成一部分webserver的工作，但是这不是它的主旨工作（考虑到并发数）
把静态文件的请求直接返回静态文件资源，把动态文件的请求转发给后台的处理程序
yum install nginx(之前用的源码安装，不过直接用编译的好像也行)
然后在/usr/bin添加soft link
nginx -v 看看安上没，没有就源码安装（https://www.nginx.cn/install）吧
nginx 直接启动服务
nginx -s quit 安全的关闭
打开后，试试
curl 127.0.0.1:80/
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
  <title>Welcome to CentOS</title>
有页面，不过是centOS的（神之迷惑）

正式开始配置
首先看看目录结构，一切皆文件，熟悉一个工具，先从文件结构入手，弄清楚每个文件是干什么
https://www.cnblogs.com/liang-io/p/9340335.html#_label4
.
├── conf.d //比较贴心，用.d告诉我们是个directory，里面存放我们自己写的配置，所以这些配置需要放到总
│   └── nginx.conf//的配置文件中才能生效，这里写了个自己的配置文件，内容放在后边
├── default.d
├── fastcgi.conf
├── fastcgi.conf.default
├── fastcgi_params
├── fastcgi_params.default
├── koi-utf
├── koi-win
├── mime.types
├── mime.types.default
├── nginx.conf//这个就是咱们总的配置文件
├── nginx.conf.default
├── scgi_params
├── scgi_params.default
├── uwsgi_params
├── uwsgi_params.default
└── win-utf

先看看总的配置文件
user nginx;
worker_processes auto;
error_log /var/log/nginx/error.log;//日志生成路径
pid /run/nginx.pid;

# Load dynamic modules. See /usr/share/doc/nginx/README.dynamic.
include /usr/share/nginx/modules/*.conf;

events {
    worker_connections 1024;
}
//http区才是我们应该重点关注的
http {
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile            on;
    tcp_nopush          on;
    tcp_nodelay         on;
    keepalive_timeout   65;
    types_hash_max_size 2048;

    include             /etc/nginx/mime.types;
    default_type        application/octet-stream;

    # Load modular configuration files from the /etc/nginx/conf.d directory.
    # See http://nginx.org/en/docs/ngx_core_module.html#include
    # for more information.
    include /etc/nginx/conf.d/*.conf;
//加载咱们自己的配置文件
//server可以有多个，有个default的
//从后面的include可以看出来，对应上面的default.d配置文件
//现在看看资源文件在哪儿
//root: /usr/share/nginx/html目录
//先看看后面的404,50xhtml（先看看服务器上的对应资源，然后访问不存在的资源，看看是否加载这两个html）
[root@iZm5e98zphj5y525q4v5k4Z html]# ls
404.html  50x.html  en-US  icons  img  index.html  nginx-logo.png  poweredby.png
[root@iZm5e98zphj5y525q4v5k4Z html]# pwd
/usr/share/nginx/html
确实有相应的资源
curl 127.0.0.1:80/not.html
        <div class="content">

            <h3>The page you are looking for is not found.</h3>

            <div class="alert">
                <h2>Website Administrator</h2>
访问到了，ok
然后再看看存在的资源，比如index.html
curl 127.0.0.1:80/index.html
有意思的事情来了
出现的是
  <title>Welcome to CentOS</title>
好吧，资源文件确实是
  <title>Welcome to CentOS</title>
总结一下
root是静态资源的根目录，location进行一次正则匹配，然后给回响应的静态资源
location [=|~|~*|^~] /uri/ { … }
=是精确匹配，比如location = /logs.html{}
^~ 开头表示uri以某个常规字符串开头，理解为匹配 url路径即可。nginx不对url做编码，因此请求为/static/20%/aa，可以被规则^~ /static/ /aa匹配到（注意是空格）。以xx开头

~ 开头表示区分大小写的正则匹配                     以xx结尾

~* 开头表示不区分大小写的正则匹配                以xx结尾

!~和!~*分别为区分大小写不匹配及不区分大小写不匹配 的正则

/ 通用匹配，任何请求都会匹配到。
匹配是从上往下的，存在优先级

比如我们做一下修改（然后用nginx -s reload重新加载总的配置文件）访问localhost:80/时，出现我们自己的东西
index.html
    server {
        listen       80 default_server;
        listen       [::]:80 default_server;
        server_name  _;#不启用域名
        root         /usr/share/nginx/html;

        # Load configuration files for the default server block.
        include /etc/nginx/default.d/*.conf;

        location / {
        }

        error_page 404 /404.html;
        location = /404.html {
        }

        error_page 500 502 503 504 /50x.html;
        location = /50x.html {
        }
    }

# Settings for a TLS enabled server.
#
#    server {
#        listen       443 ssl http2 default_server;
#        listen       [::]:443 ssl http2 default_server;
#        server_name  _;
#        root         /usr/share/nginx/html;
#
#        ssl_certificate "/etc/pki/nginx/server.crt";
#        ssl_certificate_key "/etc/pki/nginx/private/server.key";
#        ssl_session_cache shared:SSL:1m;
#        ssl_session_timeout  10m;
#        ssl_ciphers HIGH:!aNULL:!MD5;
#        ssl_prefer_server_ciphers on;
#
#        # Load configuration files for the default server block.
#        include /etc/nginx/default.d/*.conf;
#
#        location / {
#        }
#
#        error_page 404 /404.html;
#        location = /404.html {
#        }
#
#        error_page 500 502 503 504 /50x.html;
#        location = /50x.html {
#        }
#    }

先做好备份，然后进行如下修改
index_mine.html(/usr/share/nginx/html/index_mine.html)
<!DOCTYPE HTML><!--这是HTML5的文档声明-->

<html><!--这是html的开始标签-->
    <head><!--这是设置网页标签,html的编码设置,以及标题和链接资源都写在这里-->
        <!--这是设置移动端观看时,网页不缩放-->
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <!--设置网页在ie上观看时,按照浏览器的最高版本的IE观看-->
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <meta charset="utf-8"> <!--这是设置网页编码-->
        <title>我的主页</title><!--这是设置网页标题-->
    </head>
    <body><!--这是网页内容-->
    
修改
        location / {
                index index_mine.html;
        }
		location = /logs{
}
先加载最新的配置文件nginx -s reload
然后查看配置文件的状态nginx -t

location / {
#index index_mine.html;
include uwsgi_params;
uwsgi_pass 127.0.0.1:9001;
} 
这个操作是让nginx把request发到通过9001端口发到127.0.0.1，发送给uwsgi，然后现在打开uwsgi，同样设置为3031端口，运行我们自己的程序，（动态网页）
uwsgi --socket 127.0.0.1:9001 --plugin python --wsgi-file foobar.py --master --processes 4 --threads 2 --stats 127.0.0.1:9002
通过这个socket接收request，然后运行py


命令
-c </path/to/config> 为 Nginx 指定一个配置文件，来代替缺省的。

有一个后续可能的问题，uwsgi对应的python解释器是2.7，后面用django的时候可能出问题
spawned uWSGI master process (pid: 26757)#master进程
spawned uWSGI worker 1 (pid: 26758, cores: 2)#四个worker进程以及每个进程下两个线程
spawned uWSGI worker 2 (pid: 26759, cores: 2)
spawned uWSGI worker 3 (pid: 26760, cores: 2)
spawned uWSGI worker 4 (pid: 26761, cores: 2)
*** Stats server enabled on 127.0.0.1:9002 fd: 15 ***
[pid: 26761|app: 0|req: 1/1] 127.0.0.1 () {32 vars in 335 bytes} [Sun Apr 18 20:54:25 2021] GET / => generated 11 bytes in 0 msecs (HTTP/1.1 200) 1 headers in 44 bytes (1 switches on core 0)
发起请求
curl 127.0.0.1:80/
Hello World

这样其实已经达成了我们的目的，什么时候把静态资源让nginx直接返回，什么时候用python生成，就是在nginx location区进行配置

If your proxy/webserver/router speaks HTTP, you have to tell uWSGI to natively speak the http protocol (this is different from –http that will spawn a proxy by itself):

现在可能发现，命令很长了，每次都输入一遍，有大量重复的内容，所以放到一个配置文件里面，每次要使用的时候就直接加载
name.ini文件(统一放到/etc/uwsgi.d目录下或者放到虚拟环境的项目目录中)

目前加载了一个简单的py文件，现在加载我们的project
要求用uwsgi命令行

先使用python manage.py runserver对站点进行访问测试
先配置虚拟环境，（requirements.txt的依赖，静态资源，python版本）

先在本机上测试
[18/Apr/2021 22:11:40] "GET /logs/ HTTP/1.1" 200 3197
[18/Apr/2021 22:11:48] "GET /logs/topics/ HTTP/1.1" 302 0
[18/Apr/2021 22:44:16] "GET /logs/topics/ HTTP/1.1" 302 0
[18/Apr/2021 22:44:19] "GET /logs/ HTTP/1.1" 200 3197
[18/Apr/2021 22:45:04] "GET /users/ HTTP/1.1" 404 179
[18/Apr/2021 22:45:11] "GET /users/login/ HTTP/1.1" 200 3729
[18/Apr/2021 22:45:41] "GET /users/register/ HTTP/1.1" 200 4130
[18/Apr/2021 22:46:27] "GET /users/login/ HTTP/1.1" 200 3729
请求的资源都可以使用

然后用uwsgi+命令行完成
具体步骤：激活虚拟环境，安装uwsgi
Successfully built uwsgi
Installing collected packages: uwsgi
Successfully installed uwsgi-2.0.19.1
uwsgi --socket 127.0.0.1:9000 --chdir /root/env/learning_log/ --wsgi-file learning_log/wsgi.py --stats 127.0.0.1:9001 --master --processes 4 --threads 2
两个关键点，一是chdir（根目录）
在/root/env目录下
bin  learning_log  lib  lib64  pyvenv.cfg
learning_log是项目的同名目录，里面放了project和apps，必须是项目所在目录
wsgi-file是项目（第二个learning_log）下的wsgi文件
这样就可以理解chdir最后跟了/，从而指向了project和apps的位置
最后，是socket，这是不对的，套接字的max_size是有规定的（详见计网），所以产生下面的报错。
invalid request block size: 21573 (max 4096)...skip
下面做出改正
uwsgi --http-socket 127.0.0.1:9000 --chdir /root/env/learning_log/ --wsgi-file learning_log/wsgi.py --stats 127.0.0.1:9001 --master --processes 4 --threads 2

还有一个可能的错误是没有提示sqlite3版本不够，需要安装，然后必须将sqlite3放入环境变量（export LD_LIBRARY_PATH="/usr/local/lib" 然后 source ~/.bashrc）
，并且！！！cp /usr/local/lib/sqlite3.so.0（库文件）到lib 和lib64，否则虚拟环境中的django去自己的package里面找
网上的教程都说啥升级降级，没用，关键得找到
https://blog.csdn.net/weixin_43364556/article/details/109719370
https://yinleilei.blog.csdn.net/article/details/92218635?dist_request_id=1331989.12585.16188176672487797&depth_1-
这个说到点子了

[pid: 19849|app: 0|req: 1/1] 127.0.0.1 () {24 vars in 295 bytes} [Mon Apr 19 16:05:39 2021] GET /users/register/ => generated 4130 bytes in 116 msecs (HTTP/1.1 200) 7 headers in 349 bytes (1 switches on core 0)

ok，很好，目前完成了命令行来配置uwsgi，现在用文件来加载配置
创建一个ini（uwsgi在虚拟环境中，但是nginx不是，nginx是全局的，配置在虚拟环境外）
内容为

用uwsgi name.ini加载（位置建议放在project中）
一个太容易被忽略的地方了文件里面第一行是
文件叫做logs.ini
[uwsgi]
...
[app1]
...
[app2]
FUCK!
[uwsgi]
http-socket = 127.0.0.1:9000
plugin = python
chdir = /root/env/learning_log/
wsgi-file = learning_log/wsgi.py
master = True
processes = 4
threads = 2

uwsgi logs.ini（我放在/root/env/learning_log/下）
[pid: 20350|app: 0|req: 2/2] 127.0.0.1 () {24 vars in 275 bytes} [Mon Apr 19 16:15:47 2021] GET /logs/ => generated 3197 bytes in 25 msecs (HTTP/1.1 200) 6 headers in 181 bytes (1 switches on core 1)
成功
现在对配置文件进行一下修改，将进程放到后台，便于管理，将日志放到文件里面，将统计信息通过一个端口（private）进行访问
[uwsgi]
#内网测试
http-socket = 127.0.0.1:9000
#plugin = python
#根目录
chdir = /root/env/learning_log/
#project的wsgi文件
wsgi-file = learning_log/wsgi.py
#master 进程可以存在
master = True
#四个worker进程（两个线程）
processes = 4
threads = 2
#移除unix socket和pid，如果停止服务
vacuum = True
#将接受的内容序列化
thunder-lock = True
#统计信息访问,先放在内网上
stats = 127.0.0.1:9001
#将日志输出，使得进程可以在后台运行
daemonize = uwsgi_running_log
#控制日志的大小,500m够了
log-maxsize = 500000
#日志中有如果有大量200文件非常恐怖，我们只关心错误的请求
disable-logging = True
#指定pid文件的位置，记录主进程的pid号

加载 uwsgi logs.ini
(env) [root@iZm5e98zphj5y525q4v5k4Z learning_log]# uwsgi logs.ini
[uWSGI] getting INI configuration from logs.ini
先进行一下访问，ok（太长，就不放了）
然后去看看日志文件
(env) [root@iZm5e98zphj5y525q4v5k4Z learning_log]# ls
collected_static  learning_logs  manage.py         test.py
db.sqlite3        ll_env         not_forget        users
learning_log      logs.ini       requirements.txt  uwsgi_running_log
probably another instance of uWSGI is running on the same address (127.0.0.1:9000).
bind(): Address already in use [core/socket.c line 769]
额，之前的没关
lsof -i:9000然后全杀了
lsof -i:9001关了
其实这里很容易看出来，如果没有pid文件，关闭进程很麻烦，因为我们不知道pid
重新加载一下
uwsgi logs.ini
*** Stats server enabled on 127.0.0.1:9001 fd: 21 ***
正常了
进行正常访问
没有任何增加的信息(文件大小没变)
进行404
  <h1>Not Found</h1><p>
额，还是没有内容，先关闭
pkill -f uwsgi -9
注释掉disable-logging
[pid: 22285|app: 0|req: 1/1] 127.0.0.1 () {24 vars in 281 bytes} [Mon Apr 19 16:53:06 2021] GET /users/l/ => generated 179 bytes in 32 msecs (HTTP/1.1 404) 5 headers in 158 bytes (1 switches on core 0)
现在有了404，可能这里是不记录所有request了
talk is cheap
咱们去官方文档验证下，描述为
enable/disable logging
ok，是整个禁用或启用日志功能
内网访问测试完毕

进行公网访问测试
修改配置文件
[uwsgi]
#内网测试
http-socket = 127.0.0.1:9000
#公网测试
#http-socket = 47.105.91.99:9000
#plugin = python
#根目录
chdir = /root/env/learning_log/
#project的wsgi文件
wsgi-file = learning_log/wsgi.py
#master 进程可以存在
master = True
#四个worker进程（两个线程）
processes = 4
threads = 2
#移除unix socket和pid，如果停止服务
vacuum = True
#将接受的内容序列化
thunder-lock = True
#统计信息访问,先放在内网上
#stats = 127.0.0.1:9001
#放到文件中
stats = %(chdir)uwsgi/uwsgi.stats
#将日志输出，使得进程可以在后台运行
daemonize = %(chdir)uwsgi/uwsgi.log
#控制日志的大小,500m够了
log-maxsize = 500000
#日志中有如果有大量200文件非常恐怖，我们只关心错误的请求
#disable-logging = True
#指定pid文件的位置，记录主进程的pid号
pidfile = %(chdir)uwsgi/uwsgi.pid

现在uwsgi目录下有
-rw-r--r--  1 root root  2542 Apr 19 17:16 uwsgi.log
-rw-r--r--  1 root root 12288 Apr 19 17:18 .uwsgi.log.swp
-rw-rw-rw-  1 root root     6 Apr 19 17:15 uwsgi.pid
srwxrwxrwx  1 root root     0 Apr 19 17:15 uwsgi.stats
-rw-r--r--  1 root root     0 Apr 19 17:15 uwsig.stats
是我们指定的log，stats，pid
当前pid里面是23567，而
uwsgi   23567 root    6u  IPv4 172956      0t0  TCP localhost:cslistener (LISTEN)
所以记录的是master 的pid
现在想关闭重启就很简单了
启动
(env) [root@iZm5e98zphj5y525q4v5k4Z uwsgi]# uwsgi --ini ../logs.ini 
[uWSGI] getting INI configuration from ../logs.ini
(env) [root@iZm5e98zphj5y525q4v5k4Z uwsgi]# lsof -i:9000
COMMAND   PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
uwsgi   24119 root    6u  IPv4 173832      0t0  TCP localhost:cslistener (LISTEN)
uwsgi   24121 root    6u  IPv4 173832      0t0  TCP localhost:cslistener (LISTEN)
uwsgi   24122 root    6u  IPv4 173832      0t0  TCP localhost:cslistener (LISTEN)
uwsgi   24123 root    6u  IPv4 173832      0t0  TCP localhost:cslistener (LISTEN)
uwsgi   24124 root    6u  IPv4 173832      0t0  TCP localhost:cslistener (LISTEN)
：
(env) [root@iZm5e98zphj5y525q4v5k4Z uwsgi]# uwsgi --stop uwsgi.pid
(env) [root@iZm5e98zphj5y525q4v5k4Z uwsgi]# lsof -i:9000
修改配置文件后重启
(env) [root@iZm5e98zphj5y525q4v5k4Z uwsgi]# uwsgi --reload ../logs.ini 
(env) [root@iZm5e98zphj5y525q4v5k4Z uwsgi]# lsof -i:9000
COMMAND   PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
uwsgi   24119 root    6u  IPv4 173832      0t0  TCP localhost:cslistener (LISTEN)
uwsgi   24121 root    6u  IPv4 173832      0t0  TCP localhost:cslistener (LISTEN)
uwsgi   24122 root    6u  IPv4 173832      0t0  TCP localhost:cslistener (LISTEN)
uwsgi   24123 root    6u  IPv4 173832      0t0  TCP localhost:cslistener (LISTEN)
uwsgi   24124 root    6u  IPv4 173832      0t0  TCP localhost:cslistener (LISTEN)

注意，pid文件不需要你指定，内容是在ini时候加载进去的，目的是方便reload和stop

开始公网测试
先在阿里云放行端口80
将logs.ini修改为公网ip和80端口
检测80端口
(env) [root@iZm5e98zphj5y525q4v5k4Z learning_log]# lsof -i:80
COMMAND     PID  USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
AliYunDun   934  root   21u  IPv4  14732      0t0  TCP iZm5e98zphj5y525q4v5k4Z:41444->100.100.30.26:http (ESTABLISHED)
nginx     22106  root    6u  IPv4 120872      0t0  TCP *:http (LISTEN)
nginx     22106  root    7u  IPv6 120873      0t0  TCP *:http (LISTEN)
nginx     28093 nginx    6u  IPv4 120872      0t0  TCP *:http (LISTEN)
nginx     28093 nginx    7u  IPv6 120873      0t0  TCP *:http (LISTEN)
(env) [root@iZm5e98zphj5y525q4v5k4Z learning_log]# pkill -f nginx -9
(env) [root@iZm5e98zphj5y525q4v5k4Z learning_log]# lsof -i:80
COMMAND   PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
AliYunDun 934 root   21u  IPv4  14732      0t0  TCP iZm5e98zphj5y525q4v5k4Z:41444->100.100.30.26:http (ESTABLISHED)
加载文件
uwsgi --ini logs.ini
[root@iZm5e98zphj5y525q4v5k4Z learning_log]# curl 47.105.91.99:80/logs/
curl: (7) Failed connect to 47.105.91.99:80; Connection refused
拒绝了
换个端口9000
(env) [root@iZm5e98zphj5y525q4v5k4Z learning_log]# lsof -i:9000
COMMAND   PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
uwsgi   24119 root    6u  IPv4 173832      0t0  TCP localhost:cslistener (LISTEN)
uwsgi   24121 root    6u  IPv4 173832      0t0  TCP localhost:cslistener (LISTEN)
uwsgi   24122 root    6u  IPv4 173832      0t0  TCP localhost:cslistener (LISTEN)
uwsgi   24123 root    6u  IPv4 173832      0t0  TCP localhost:cslistener (LISTEN)
uwsgi   24124 root    6u  IPv4 173832      0t0  TCP localhost:cslistener (LISTEN)
(env) [root@iZm5e98zphj5y525q4v5k4Z learning_log]# pkill -f uwsgi -9
(env) [root@iZm5e98zphj5y525q4v5k4Z learning_log]# uwsgi --ini logs.ini 
[uWSGI] getting INI configuration from logs.ini
[root@iZm5e98zphj5y525q4v5k4Z learning_log]# curl 47.105.91.99:9000/logs/
curl: (7) Failed connect to 47.105.91.99:9000; Connection refused

迷惑
看看日志
*** Starting uWSGI 2.0.19.1 (64bit) on [Mon Apr 19 17:33:56 2021] ***
compiled with version: 4.8.5 20150623 (Red Hat 4.8.5-44) on 18 April 2021 14:52:16
os: Linux-3.10.0-957.21.3.el7.x86_64 #1 SMP Tue Jun 18 16:35:19 UTC 2019
nodename: iZm5e98zphj5y525q4v5k4Z
machine: x86_64
clock source: unix
pcre jit disabled
detected number of CPU cores: 1
current working directory: /root/env/learning_log
writing pidfile to /root/env/learning_log/uwsgi/uwsgi.pid
detected binary path: /root/env/bin/uwsgi
uWSGI running as root, you can use --uid/--gid/--chroot options
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
chdir() to /root/env/learning_log/
your processes number limit is 7270
your memory page size is 4096 bytes
detected max file descriptor number: 65535
lock engine: pthread robust mutexes
thunder lock: enabled
bind(): Cannot assign requested address [core/socket.c line 769]

https://blog.csdn.net/JT31520/article/details/89644410
根据这篇博客，就直接配置nginx把




#然后用uwsgi+nginx，跳过
```





```python
STATIC_URL = '/static/'#静态的url（%static指向每个app的static/app_name/目录
STATIC_ROOT = os.path.join(BASE_DIR,'static')
#静态资源导向的目录 python manage.py collectstatic
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static')
]
```



一个很傻的问题，-- unavailable modifier requested: 0 --

无法访问界面

操作：uwsgi logs.ini

（用的内网）

为什么？没进入虚拟环境，uwsgi找不到依赖





![image-20210419181636768](https://raw.githubusercontent.com/whr819987540/pic/main/20210419181643.png)

![image-20210419181717174](https://raw.githubusercontent.com/whr819987540/pic/main/20210419181717.png)





现在通了，待会儿贴上uwsgi和nginx的ip配置和端口配置

但是现在nginx的9999端口没通，uwsgi的9000端口通了

uwsgi的log里面有访问记录，nginx的里面没有记录

说明流量还是没经过nginx

而uwsgi的9000端口没有给出图片这个静态资源

所以是nginx的原因

应该是静态资源路径的问题

plus（静态资源如果返回304状态码，表明是cache给的，应该清空缓存，重新测试）

> uwsgi服务器默认不托管静态资源，一般需要配合Nginx使用(静态资源交给Nginx处理)。





setting.py

![image-20210420193300938](https://raw.githubusercontent.com/whr819987540/pic/main/20210420193301.png)

uwsgi日志

[pid: 4443|app: 0|req: 3/12] 222.175.198.19 () {32 vars in 700 bytes} [Tue Apr 20 19:27:34 2021] GET /static/learning_logs/images/most2.png => generated 179 bytes in 1 msecs (HTTP/1.1 404) 5 headers in 158 bytes (1 switches on core 0)

目录结构![image-20210420193506665](https://raw.githubusercontent.com/whr819987540/pic/main/20210420193506.png)