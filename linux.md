外网面板地址: http://47.105.91.99:8888/ea0b1f23
内网面板地址: http://172.17.22.1:8888/ea0b1f23
username: kjtlqu4g
password: 91acca0b
If you cannot access the panel,
release the following panel port [8888] in the security group
若无法访问面板，请检查防火墙/安全组是否有放行面板[8888]端口

![image-20210311124910259](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210311124910259.png)

Linux服务器端操作系统
稳定性，不需要界面，需要便利的操作
服务端运维，开发
命令行操作，区别于图形界面

自制：家用多媒体共享服务，资料备份，文件共享

系统操作，服务管理，shell脚本，文本操作，常用服务搭建
搭建常用服务（dns，http，共享，ftp）

Linux，开源操作系统的内核
体验Linux：虚拟机，云主机，多系统（进阶）
内核版本：主版本号，次（奇数为开发版，欧式为稳定版），末
发行版本：厂商定制的fedora，centos，ubantu（玩游戏）



内核，kernel
外核，shell，也称为操作命令接口，（两种形式，图形界面，命令行界面）
api，应用编程接口
GUI，图形用户接口；CLI，命令行接口
bash shell
【当前登录的用户名@登录的主机 ~】波浪线是bash中的一个变量，表示当前用户的家目录
$是普通用户，#是根用户

whoami返回当前登录用户的用户名
命令，选项，参数

echo （回显）用户输出字符串，选项，
echo -e/-n ‘string’
echo 的help要用  /bin/echo --help来完成
-n 不再尾部加上换行符
-e使用转义字符
\b为退格（光标往后移一位）

nano的ctrl键无效
shell：历史命令，用上下键来显示之前的命令
命令自动补全功能：部分命令+一个tab键
部分命令+tabtab，显示出所有匹配的命令用来选择

man（manual）手册，是一个命令
后面加命令
在man的界面中，存在上下键，pgup pgdw键
/+chars可以在当前界面内进行检索
man的帮助文档分为九个部分
不同部分间可能存在同名文档，所以可能需要指定帮助文档所在的部分
默认从数字小的部分开始

对于服务器而言，如何关机或重启很重要

查看在线用户和在线用户
通知关机安排
下达关闭命令
shutdown关机，根用户的权限
shutdown -h time关机很慢
su切换用户 - username
shutdown -c取消之前的关闭命令
shutdown -h time +解释
解释会发送给所有的登录用户（传递关机原因），广播包
shutdown -r表示重启time
用户exit

reboot = shutdown -r now 马上重启
halt = shutdown -h now 马上关机
poweroff = shutdown -h now +断电
不安全，不是平稳的关闭，而是直接删除进程

linux 的配置文件大多都是ASCII码写的

进入vim，默认进入一般模式（移动光标。删除。复制）
hjkl移动光标，x删除光标指向的字符，dd删除光标所在的一行
shift+j 删除当前行的换行符
u撤销最后的一次编辑
ctrl+r撤销撤销
插入模式，输入字符（i进入）
命令行模式，输入命令，打开，保存，查找，替换
在一般模式以外，按esc退出当前的模式

：进入命令行模式
w保存文件
q编辑器退出程序
！不保存文件

根目录下至少有12个目录
bin可执行的命令文件
boot系统核心文件，开机所需的文件
dev，系统设备文件
etc，系统配置文件
home，普通用户的家目录（每个目录都在该目录下创建自己的目录）
lib，库函数文件
root，root用户的家目录
sbin，根用户能够执行的命令文件
srv，服务启动之后需要访问的文件（服务器给用户的文件）
tmp程序临时存放的文件
opt第三方软件的安装目录
media，移动设备相关文件

cd change directory更换工作目录
.表示当前目录
。。表示当前目录的上层目录
cd -表示返回到之前到过的工作目录，也就是windows的返回，后退
cd ~表示当前登录用户的家目录


mkdir make directory选项-p创建嵌套目录
参数，文件路径及其名称

rmdir remove directory默认只能删除空目录
如果是非空目录，可以用-r（recursive，递归）来删除目录下的目录或者文件
-f不询问直接删除

ls 文件名/目录名 或者不加，默认为当前所在目录
列出当前所在目录的内部文件名
-a列出所有文件，包括隐藏文件
-l以长格式列出文件

文件：-rwxr-xr--
拥有者rwx读写执行
从属用户组，读执行
其他用户，r读

用chmod命令修改文件的访问权限（当前登录的用户为文件的拥有者）
change mode
格式为chmod 700 file

d表示是directory，目录
-表示普通文件，类型通过后缀查看
c表示字符设备文件
b块设备文件
l符号链接文件

cp，复制
cp 目标的文件名或者目录名 拷贝到那儿或者是具体的文件名，创建文件并命名
拷贝整个目录时，需要加上-r选项

在拷贝时，文件的拥有者和从属用户组都可能发生改变
-p选项可以拷贝这个信息

mv命令移动，参数与cp相同
-f强制覆盖同名文件，无需询问

linux无重命名命令，可以通过移动，路径不变，文件名改变实现

touch 文件名
如果当前路径下无同名文件，创建空文件
如果有同名文件，会更改文件的时间戳

*任意长度的字符
？任意单个字符
【c1-c2】c1-c2的任意单个字符
【c1,c2】进行列表匹配
{string1，string2}进行字符串匹配
rm -rf {jiaoben,script}*.sh
！不匹配什么

tar tape archive 磁盘归档，用于将文件合并在一起
不对文件进行压缩
一是被打包的文件名，而是打包后放在哪个路径下
选项-c创建
-f 指定文件名

参数顺序：打包后的文件名（name.tar），被打包文件的路径(可以是列表）
查看tar包里面的文件tar -tf name.tar
tar -f name.tat --delete file.name删除包中的一个文件
合并tar -f name1.tar -A -name2.tar
将name2合并到name1中
-r添加新的打包文件
-xf为解包
tar -xf name.tar -C 解压路径

gzip
对文件进行压缩，后面直接跟上待压缩的文件
自动压缩到到当前目录，并创建name.gz的文件
解压：gzip -d name.gz
压缩比，数值越大，速度越慢，占用内存越小

开启安全组列表+端口

以网络为核心

发行版=内核+开发工具

红帽认证工程师（java）

lamp=linux+Apache+mysql+php

lnmp=linux+ngixnx+mysql+php

lnmp=

windows远程登录到linux需要putty

全名mylinux

用户名root

pwd824655

一般用户mylinux-824655

whr+no_pwd



服务，守护进程

ssh登录



sync将内存中的数据加载到硬盘中

如果成功没有回显

linux中没有返回的字符串即为命令成功执行



reboot重启==shutdown -r now

shutdown -h time/now 关机

shutdown -r time/now 重启

shutdown -c cancel the shutdown

/etc目录下存放系统的配置文件和子目录

/opt目录用于存储给主机额外安装的软件

/usr 存放应用程序和文件，类似于windows下的program files

/www 用来存放网站相关的文件



上一级目录 cd ..

当前目录  ./

进入当前目录的某个文件cd name  OR cd ./name

less中

/向下寻找，？向上寻找
n在找到的内容中往下翻，N在找到的内容中往上翻

shell编程

vim下q！强制退出  w!强制写入

无法写入的可能原因：当前用户的权限不够



x删除光标指向的字符

ndd删除光标所在行及其以下n-1行

nyy在光标所在行及其以下n-1行

p在光标所在行之下粘贴复制的内容

一般模式下:set nu显示行号，set nonu取消行号显示

增加用户useradd -m name

删除用户userdel -r name

当前的用户名（username）@主机名（hostname） directory

passwd默认修改当前用户的密码

passwd +name修改name对应的密码



上传文件用xftp

ugoa +-= wrx



mount命令来挂载外接设备

mount /dev/* /mnt/*



进程管理

进程状态process status

ps -aux

pstree -p（显示PID）

47.105.91.99



sql，php





动态页面的一个重要特点：后缀中一般没有.html, .xml，而是[.php,.jsp]并且需要?来传递参数

服务器的类型取决于服务器上的软件类型

特殊ip：本机127.0.0.1

特殊域名：localhost

端口：虚拟端口，物理端口

通过端口号找到对应的提供服务的软件

下载图片

curl -o path url

或者wget功能多一点

外网面板地址: http://47.105.91.99:8888/ea0b1f23
内网面板地址: http://172.17.22.1:8888/ea0b1f23
username: kjtlqu4g
password: c73b549c
If you cannot access t







mysql root pwd 123456

**连接数据库语句 :** mysql -h 服务器主机地址 -u 用户名 -p 用户密码

utf-8   utf-8-general-ci

# 基本操作

## 关机

sync，将内存中的数据写入磁盘

shutdown -h time什么时候关机

shutdown -h 10/now

shutdown -r time什么时候重启

shutdown -r 10/now

建议不要在服务器上这样用，如果是远程连接，关了咋开？还得用阿里云的控制台打开。

## 目录概览

```sql
/bin：bin是Binary的缩写, 这个目录存放着最经常使用的命令。

/boot： 这里存放的是启动Linux时使用的一些核心文件，包括一些连接文件以及镜像文件。

/dev ： dev是Device(设备)的缩写, 存放的是Linux的外部设备，在Linux中访问设备的方式和访问文件的方式是相同的。

/etc： 这个目录用来存放所有的系统管理所需要的配置文件和子目录。

/home：用户的主目录，在Linux中，每个用户都有一个自己的目录，一般该目录名是以用户的账号命名的。

/lib：这个目录里存放着系统最基本的动态连接共享库，其作用类似于Windows里的DLL文件。

/lost+found：这个目录一般情况下是空的，当系统非法关机后，这里就存放了一些文件。

/media：linux系统会自动识别一些设备，例如U盘、光驱等等，当识别后，linux会把识别的设备挂载到这个目录下。

/mnt：系统提供该目录是为了让用户临时挂载别的文件系统的，我们可以将光驱挂载在/mnt/上，然后进入该目录就可以查看光驱里的内容了。

/opt：这是给主机额外安装软件所摆放的目录。比如你安装一个ORACLE数据库则就可以放到这个目录下。默认是空的。

/proc：这个目录是一个虚拟的目录，它是系统内存的映射，我们可以通过直接访问这个目录来获取系统信息。

/root：该目录为系统管理员，也称作超级权限者的用户主目录。

/sbin：s就是Super User的意思，这里存放的是系统管理员使用的系统管理程序。

/srv：该目录存放一些服务启动之后需要提取的数据。

/sys：这是linux2.6内核的一个很大的变化。该目录下安装了2.6内核中新出现的一个文件系统 sysfs 。

/tmp：这个目录是用来存放一些临时文件的。

/usr：这是一个非常重要的目录，用户的很多应用程序和文件都放在这个目录下，类似于windows下的program files目录。

/usr/bin： 系统用户使用的应用程序。

/usr/sbin： 超级用户使用的比较高级的管理程序和系统守护程序。

/usr/src： 内核源代码默认的放置目录。

/var：这个目录中存放着在不断扩充着的东西，我们习惯将那些经常被修改的目录放在这个目录下。包括各种日志文件。

/run：是一个临时文件系统，存储系统启动以来的信息。当系统重启时，这个目录下的文件应该被删掉或清除。
```

重点：

/bin，命令

/sbin，超级用户使用的命令

/etc，配置文件

/home，每个用户在这里都有一个自己的目录

/lib，动态链接库

/root，root用户的家目录

/tmp，临时文件

/usr，存放应用程序及其缓存，类似program files

/var，经常变动被修改的文件

## 目录管理

以/根目录开头，为绝对路径

.用来指代当前目录

..用来指代上一级目录

![image-20210311094652474](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210311094652474.png)

## ls: 列出目录

ls -a列出所有文件包括隐藏文件

ls -l以详细列表的形式列出文件

## cd：切换目录

cd -跳转到上一次所在的目录

## pwd：显示目前的目录

-P显示确实的路径，而非使用连接（link）的路径

可能当前工作目录只是一个快捷方式

![image-20210311104439827](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210311104439827.png)

bin是根据/usr/bin创建的link

![image-20210311104550006](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210311104550006.png)

## mkdir：创建一个新的目录

mkdir -m xxx配置文件权限 -p递归创建目录 目录名

## rmdir：删除一个空的目录

## cp: 复制文件或目录

cp -options 【sourc1，source2】 des

- **-r：**递归持续复制，用於目录的复制行为；(常用)

  如果是目录，在非空的情况下，-r。

  ![image-20210311103721645](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210311103721645.png)



​		![image-20210311103809382](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210311103809382.png)



- **-i：**若目标档(destination)已经存在时，在覆盖时会先询问动作的进行(常用)

  防止覆盖

- **-p：**连同文件的属性一起复制过去，而非使用默认属性(备份常用)；

  没有使用-p，发现文件的修改时间变了

  用上-p，发现二者相同

  ![image-20210311103436983](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210311103436983.png)

  

  

  

## rm: 移除文件或目录

## mv: 移动文件与目录，或修改文件与目录的名称

mv 要移动的文件名或目录名 移动到的位置/文件名

mv test.txt test1.txt   -- 重命名

mv test.txt ./test1.txt --重命名

mv test.txt ../test.txt --放到上级目录

## whereis:查找安装文件

cd

## find:查找文件

find 搜索路径 -options 参数

- 按照名称，区分大小写，精确匹配。find / -name filename
- 按照名称，不区分大小写，精确匹配。find / -iname filename



## 

# vim

- 命令模式 vim file.name

如果存在file.name这个文件，则进入编辑模式

如果不存在，则创建并编辑

- vim有三个模式。

一开始都是命令模式，可以i进入输入模式，:command进行底线命令（此时命令比命令模式多）

切换至输入模式，esc退出

切换至底线命令模式，w保存，q退出

![1](https://gitee.com/hit_whr/pic_2.0/raw/master/1.png)

## 命令模式的快捷键（区分大小写,数字不能是小键盘的）

### 光标移动

| h 或 向左箭头键(←) | 光标向左移动一个字符                                         |
| ------------------ | ------------------------------------------------------------ |
| j 或 向下箭头键(↓) | 光标向下移动一个字符                                         |
| k 或 向上箭头键(↑) | 光标向上移动一个字符                                         |
| l 或 向右箭头键(→) | 光标向右移动一个字符                                         |
| ***n< space>***    | ***那个 n 表示『数字』，例如 20 。按下数字后再按空格键，光标会向右移动这一行的 n 个字符。*** |
| 0 或功能键[Home]   | 这是数字『 0 』：移动到这一行的最前面字符处 (常用)           |
| $ 或功能键[End]    | 移动到这一行的最后面字符处(常用)                             |
| G                  | 移动到这个档案的最后一行(常用)                               |
| nG                 | n 为数字。移动到这个档案的第 n 行。例如 20G 则会移动到这个档案的第 20 行(可配合 :set nu) |
| gg                 | 移动到这个档案的第一行，相当于 1G 啊！(常用)                 |
| n< Enter>          | n 为数字。光标向下移动 n 行(常用)                            |

### 搜索替换

| /word | 向光标之下寻找一个名称为 word 的字符串。例如要在档案内搜寻 vbird 这个字符串，就输入 /vbird 即可！(常用) |
| ----- | ------------------------------------------------------------ |
| ?word | 向光标之上寻找一个字符串名称为 word 的字符串。               |
| n     | 这个 n 是英文按键。代表重复前一个搜寻的动作。举例来说， 如果刚刚我们执行 /vbird 去向下搜寻 vbird 这个字符串，则按下 n 后，会向下继续搜寻下一个名称为 vbird 的字符串。如果是执行 ?vbird 的话，那么按下 n 则会向上继续搜寻名称为 vbird 的字符串！ |

### 复制粘贴删除

| x, X     | 在一行字当中，x 为向后删除一个字符 (相当于 [del] 按键)， X 为向前删除一个字符(相当于 [backspace] 亦即是退格键) (常用) |
| -------- | ------------------------------------------------------------ |
| nx       | n 为数字，连续向后删除 n 个字符。举例来说，我要连续删除 10 个字符， 『10x』。 |
| dd       | 删除游标所在的那一整行(常用)                                 |
| ndd      | n 为数字。删除光标所在的向下 n 行，例如 20dd 则是删除 20 行 (常用) |
| d1G      | 删除光标所在到第一行的所有数据                               |
| dG       | 删除光标所在到最后一行的所有数据                             |
| d$       | 删除游标所在处，到该行的最后一个字符                         |
| d0       | 那个是数字的 0 ，删除游标所在处，到该行的最前面一个字符      |
| yy       | 复制游标所在的那一行(常用)                                   |
| nyy      | n 为数字。复制光标所在的向下 n 行，例如 20yy 则是复制 20 行(常用) |
| y1G      | 复制游标所在行到第一行的所有数据                             |
| yG       | 复制游标所在行到最后一行的所有数据                           |
| y0       | 复制光标所在的那个字符到该行行首的所有数据                   |
| y$       | 复制光标所在的那个字符到该行行尾的所有数据                   |
| p, P     | p 为将已复制的数据在光标下一行贴上，P 则为贴在游标上一行！举例来说，我目前光标在第 20 行，且已经复制了 10 行数据。则按下 p 后， 那 10 行数据会贴在原本的 20 行之后，亦即由 21 行开始贴。但如果是按下 P 呢？那么原本的第 20 行会被推到变成 30 行。(常用) |
| J        | 将光标所在行与下一行的数据结合成同一行                       |
| c        | 重复删除多个数据，例如向下删除 10 行，[ 10cj ]               |
| u        | 复原前一个动作。(常用)                                       |
| [Ctrl]+r | 重做上一个动作。(常用)                                       |

### 底线命令模式

| :w!                                                          | 若文件属性为『只读』时，强制写入该档案。不过，到底能不能写入， 还是跟你对该档案的档案权限有关啊！ |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| :q                                                           | 离开 vi (常用)                                               |
| :q!                                                          | 若曾修改过档案，又不想储存，使用 ! 为强制离开不储存档案。    |
| 注意一下啊，那个惊叹号 (!) 在 vi 当中，常常具有『强制』的意思～ |                                                              |
| :wq                                                          | 储存后离开，若为 :wq! 则为强制储存后离开 (常用)              |
| :w [filename]                                                | 将编辑的数据储存成另一个档案（类似另存为）                   |
| :r [filename]                                                | 在编辑的数据中，读入另一个档案的数据。亦即将 『filename』 这个档案内容加到游标所在行后面 |
| :n1,n2 w [filename]                                          | 将 n1 到 n2 的内容储存成 filename 这个档案。                 |
| :! command                                                   | 暂时离开 vi 到指令行模式下执行 command 的显示结果！例如 『:! ls /home』即可在 vi 当中看 /home 底下以 ls 输出的档案信息！ |
| :set nu                                                      | 显示行号，设定之后，会在每一行的前缀显示该行的行号           |
| :set nonu                                                    | 与 set nu 相反，为取消行号！                                 |

# nginx

No package nginx available.
Error: Nothing to do

遇到这种没有源的，先yum -y update进行一下更新，然后yum install

yum install

yum remove

查看安装是否成功whereis 

开始启动

systemctl  start  nginx	启动

systemctl restart nginx  重启

systemctl stop nginx  停止

systemctl enable nginx  将nginx设置为自启

nginx -> /www/server/nginx/sbin/nginx:;

![image-20210311150655046](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210311150655046.png)

首先，没安装上（不是没配置好）时的界面是这样的，为了这个截图，我把nginx又卸载了一遍

![image-20210311151652692](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210311151652692.png)

开始安装yum install nginx

如果说没源，就yum -y update

还不行，手动指定

vim /etc/yum.repos.d/nginx.repo

写入

```bash
[nginx]
name=nginx repo
baseurl=http://nginx.org/packages/centos/$releasever/$basearch/
gpgcheck=0
enabled=1
```

然后yum install nginx -y

应该行了。

看看安装上了没有

nginx -v或者whereis nginx

要是还不成功，https://developer.aliyun.com/article/699966

之后，

>  默认html挂载在/usr/share/nginx/html
>
> 默认conf挂载在/etc/nginx/nginx.conf
>
> 自定义配置文件为/etc/nginx/conf.d2
>
> 日志文件放在/var/log/nginx/access.log
>
> 

确实，配置文件在/etc里面

之后，为了方便处理，最好来个soft link，方便加资源文件

最后，防火墙放行80端口，打开nginx服务。

```bash
systemctl start nginx;
systemctl enable nginx;
```

当然上面这些路径都写在配置文件里面，可以自行更改。

# python

检查python的版本

ls /usr/bin/python*看有没有python3.x

再通过python命令，看默认执行的哪个版本的python

假设只有python2.x

先yum -y install python3

然后

ls /usr/bin/python*

或python3检查安装结果

安装上之后，更改命令的别名

比如 alias python='/usr/bin/python3.6'

安装好之后，发现windows上可以运行，服务器上缺少相关的库

- 下载pip

>  wget https://bootstrap.pypa.io/get-pip.py *--no-check-certificate*

- 安装pip

> python get-pip.py



# 用户管理

## 增

useradd name

创建用户及/home/name目录

passwd name

添加用户密码

pwd:

retype the pwd:

## 切换

su switch user用户切换

exit切回之前的用户

exit相对于切换的好处在于，之前的用户进程可以被杀死

## 删

userdel name

无法删除/home/name与/var/spool/mail/

![image-20210313103232989](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210313103232989.png)



name失去了登录权限

可以手动删除

`rm -rf /home/name`

`rm -rf /var/spool/mail/name`

可以`userdel -r name`将配置文件和登录权限都删除干净

![image-20210313104102748](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210313104102748.png)





## 查看

查看用户id，所属的用户组

id user_name

查看所有用户vim /etc/passed



# sudo

功能：给在/etc/sudoers文件中出现的用户提供sbin，而不用root pwd

> allows particular users to run various commands as root user, without needing the root password

该文件规定了能执行sudo的用户，只能通过visudo命令进行内容修改

而visudo的权限是

rwxr-xr-x，只有管理员能执行visudo并修改文件内容



# linux下软件包安装

## 安装位置

- /usr/bin系统级可执行文件
- /usr/local/bin用户级可执行文件
- /usr/src系统级源码
- /usr/local/src用户级源码

## 安装方法

### 源码安装

本机编译，需要make，gcc,automake,autoconf

没有package management软件，手动升级

### rpm

一个包，主机需要联网

redhad package management

提供编译好的bin文件

规定了文件在本机的安装位置

```bash
rpm -i name.rpm
//安装install
rpm -e name.rpm
//卸载erase
rpm -U name.rpm
//更新update
```

## yum

yum是一个软件包管理器，能够进行依赖关系管理，需要联网

> yum [options] [command] [package ...]

- options 选项，-y all yes，安装时的选项都为yes；-q不显示安装过程
- command以单词的格式，命令
- package包名，与rpm完整的文件名，不同，这是包名

- \1. 列出所有可更新的软件清单命令：**yum check-update**

- \2. 更新所有软件命令：**yum update**

- \3. 仅安装指定的软件命令：**yum install <package_name>**

- \4. 仅更新指定的软件命令：**yum update <package_name>**

- \5. 列出所有可安裝的软件清单命令：**yum list**

  - .noarch，no architecture，没有架构，这个包可以在各种架构的cpu上跑起来
  - .x86_64，即win平台的x64t架构
  - yum list py*

  ![image-20210313112128661](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210311124910259.png)

- \6. 删除软件包命令：**yum remove <package_name>**

- \7. 查找软件包命令：**yum search <keyword>**

- \8. 清除缓存命令:

  - **yum clean packages**: 清除缓存目录下的软件包
  - **yum clean headers**: 清除缓存目录下的 headers
  - **yum clean oldheaders**: 清除缓存目录下旧的 headers
  - **yum clean, yum clean all (= yum clean packages; yum clean oldheaders)** :清除缓存目录下的软件包及旧的 headers

  ### 换源

  源的配置文件：/etc/yum.repos.d/CentOS-Base.repo

  本机用的阿里云的源，垃圾

  在替换之前，先进行备份

  `mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup`

  下载

  wget http://mirrors.163.com/.help/CentOS7-Base-163.repo

  改名

  ```bash
  mv CentOS7-Base-163.repo CentOS-Base.repo
  ```

  运行以下命令生成缓存

  ```bash
  yum clean all
  yum makecache
  ```

  软件的启动程序放在/usr/bin或/usr/local/bin里面

  /usr不是user的缩写，其实usr是Unix Software Resource的缩写， 也就是Unix操作系统软件资源所放置的目录，而不是用户的数据；所有系统默认的软件都会放置到/usr, 系统安装完时，这个目录会占用最多的硬盘容量

  

# wget

# 进程管理

名字ps -aux|grep nginx 出来进程号

端口号ps -ef|grep 端口号  出来进程号

进程号ps -aux|grep 进程号   出来进程

端口号netstat -anp|grep 9000

## 查看

- 查看进程的详细信息，并实时更新

  top

- 树形结构并查看pstree

- 查看进程ps

- htop进行进程管理，进行命令行的管理

  ## 杀死进程

  - kill id_process
    - kill -STOP id 停止一个进程
  - kill name_process
    - 强制杀死 kill -9 name_process

lsb_release -a，列出linux的所有版本信息



# crontab

这个命令是用来设置定时执行的任务。

crontab -u user默认当前用户，如果不是当前用户，需要有root权限 

-l list查看当前的时程表

-r 删除当前的时程表

-e 编辑当前的时程表

```bash
# 时程表的格式
minute(0-59) hour(0-23) day(1-31) month(1-12) 星期几 command
*表示每分钟/小时/天/月/星期几都要执行
a-b表示时间段内都执行
*/n 表示间隔n分钟/小时/天/月执行
a,b,c是或的关系
```



![image-20210916164713358](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210916164713358.png)



```bash
[root@whr ~]# crontab -l
53 * * * * touch /root/test.txt
[root@whr ~]# ls
ad_project        nginx-1.20.1.tar.gz  project
code_plat.backup  not_forget           requirements.txt
nginx-1.20.1      novel   
[root@whr ~]# ls
ad_project           not_forget        test
code_plat.backup     novel             test.txt
nginx-1.20.1         project
nginx-1.20.1.tar.gz  requirements.txt
```

