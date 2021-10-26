bash版本

bash --version

```bash
[root@iZm5e98zphj5y525q4v5k4Z ~]# bash --version
GNU bash, version 4.2.46(2)-release (x86_64-redhat-linux-gnu)
Copyright (C) 2011 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>

This is free software; you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

```

![image-20210713160203866](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210713160203866.png)



mkdir

```bash
[root@iZm5e98zphj5y525q4v5k4Z ~]# mkdir --help
Usage: mkdir [OPTION]... DIRECTORY...
Create the DIRECTORY(ies), if they do not already exist.

Mandatory arguments to long options are mandatory for short options too.
  -m, --mode=MODE   set file mode (as in chmod), not a=rwx - umask
默认权限都是属主rwx，属组r-x，其他用户r-x
[root@iZm5e98zphj5y525q4v5k4Z ~]# mkdir 1
[root@iZm5e98zphj5y525q4v5k4Z ~]# ls -l
total 20
drwxr-xr-x 2 root root 4096 Jul 13 16:07 1
drwxr-xr-x 9 root root 4096 Jun 17 21:31 code_plat.backup
drwxr-xr-x 6 root root 4096 Apr 19 15:30 env
drwxr-xr-x 8 root root 4096 Apr 18 22:51 not_forget
drwxr-xr-x 2 root root 4096 Jul 13 00:00 shell_script

  -p, --parents     no error if existing, make parent directories as needed
递归创建文件夹
[root@iZm5e98zphj5y525q4v5k4Z ~]# mkdir -p 1/2/3
[root@iZm5e98zphj5y525q4v5k4Z ~]# ls
1  code_plat.backup  env  not_forget  shell_script
[root@iZm5e98zphj5y525q4v5k4Z ~]# cd 1
[root@iZm5e98zphj5y525q4v5k4Z 1]# ls
2
[root@iZm5e98zphj5y525q4v5k4Z 1]# cd 2
[root@iZm5e98zphj5y525q4v5k4Z 2]# ls
3
  -v, --verbose     print a message for each created directory
这个和递归创建连起来，看到底新建了哪些文件夹
[root@iZm5e98zphj5y525q4v5k4Z ~]# ls
1  code_plat.backup  env  not_forget  shell_script
[root@iZm5e98zphj5y525q4v5k4Z ~]# mkdir -pv 1/2/3
mkdir: created directory ‘1/2’
mkdir: created directory ‘1/2/3
  -Z                   set SELinux security context of each created directory
                         to the default type
      --context[=CTX]  like -Z, or if CTX is specified then set the SELinux
                         or SMACK security context to CTX
      --help     display this help and exit
      --version  output version information and exit
```



du -sh *查看当前目录下（不递归）所有文件和目录的大小

```bash
[root@iZm5e98zphj5y525q4v5k4Z ~]# pwd
/root
[root@iZm5e98zphj5y525q4v5k4Z ~]# ls
1  code_plat.backup  env  not_forget  shell_script
[root@iZm5e98zphj5y525q4v5k4Z ~]# du -sh *
12K	1
10M	code_plat.backup
259M	env
94M	not_forget
20K	shell_script
```



clear清屏



# who，查看当前登录的用户

```bash
[root@iZm5e98zphj5y525q4v5k4Z ~]# who --help
Usage: who [OPTION]... [ FILE | ARG1 ARG2 ]
Print information about users who are currently logged in.
  -a, --all         same as -b -d --login -p -r -t -T -u
  -b, --boot        time of last system boot
  -d, --dead        print dead processes
  -H, --heading     print line of column headings
  -l, --login       print system login processes
      --lookup      attempt to canonicalize hostnames via DNS
  -m                only hostname and user associated with stdin
  -p, --process     print active processes spawned by init
  -q, --count       all login names and number of users logged on
  -r, --runlevel    print current runlevel
  -s, --short       print only name, line, and time (default)
  -t, --time        print last system clock change
  -T, -w, --mesg    add user's message status as +, - or ?
  -u, --users       list users logged in
      --message     same as -T
      --writable    same as -T
      --help     display this help and exit
      --version  output version information and exit

```



# 中文乱码问题：

![image-20210713164404779](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210713164404779.png)

## 常用的字符集

中文：LANG=”zh_CN.UTF-8”

英文：LANG=”en_US.UTF-8”



## 查看系统的字符集

locale或者echo $LANG

```bash
[root@iZm5e98zphj5y525q4v5k4Z ~]# locale
LANG=en_US.UTF-8
LC_CTYPE="en_US.UTF-8"
LC_NUMERIC="en_US.UTF-8"
LC_TIME="en_US.UTF-8"
LC_COLLATE="en_US.UTF-8"
LC_MONETARY="en_US.UTF-8"
LC_MESSAGES="en_US.UTF-8"
LC_PAPER="en_US.UTF-8"
LC_NAME="en_US.UTF-8"
LC_ADDRESS="en_US.UTF-8"
LC_TELEPHONE="en_US.UTF-8"
LC_MEASUREMENT="en_US.UTF-8"
LC_IDENTIFICATION="en_US.UTF-8"
LC_ALL=
[root@iZm5e98zphj5y525q4v5k4Z ~]# echo $LANG
en_US.UTF-8
```



## 查看是否安装中文字符集

locale -a|grep zh

```bash
[root@iZm5e98zphj5y525q4v5k4Z ~]# locale -a|grep zh
zh_CN
zh_CN.gb18030
zh_CN.gb2312
zh_CN.gbk
zh_CN.utf8
zh_HK
zh_HK.big5hkscs
zh_HK.utf8
zh_SG
zh_SG.gb2312
zh_SG.gbk
zh_SG.utf8
zh_TW
zh_TW.big5
zh_TW.euctw
zh_TW.utf8
```



如果没有安装，安装之。

## 安装中文字符集

 yum -y groupinstall chinese-support



## 修改系统字符集

echo ”export LANG=zh_CN.UTF-8” >> /etc/profile

```bash
[root@iZm5e98zphj5y525q4v5k4Z ~]# echo "export LANG=zh_CN.UTF-8" >> /etc/profile
env
PWD=/root
LANG=zh_CN.UTF-8
HISTCONTROL=ignoredups
SHLVL=1
HOME=/root
GOROOT=/usr/local/go
LOGNAME=root
[root@iZm5e98zphj5y525q4v5k4Z ~]# echo $LANG
zh_CN.UTF-8
```





# profile

## 简介

profile是存放环境变量的文件，分为用户级、系统级两个层次。

## /etc/profile

/etc/profile⽂件。这是系统最重要的shell配置⽂件，也是⽤户登录系统最先检查的⽂件，系统的环境变量多定义在此⽂件中。

系统级的环境变量在/etc/profile中

```bash
[root@iZm5e98zphj5y525q4v5k4Z ~]# vim /etc/profile


# By default, we want umask to get set. This sets it for login shell
# Current threshold for system reserved uid/gids is 200
# You could check uidgid reservation validity in
# /usr/share/doc/setup-*/uidgid file
if [ $UID -gt 199 ] && [ "`/usr/bin/id -gn`" = "`/usr/bin/id -un`" ]; then
    umask 002
else
    umask 022
fi

for i in /etc/profile.d/*.sh /etc/profile.d/sh.local ; do
    if [ -r "$i" ]; then
        if [ "${-#*i}" != "$-" ]; then
            . "$i"
        else
            . "$i" >/dev/null
        fi
    fi
done

unset i
unset -f pathmunge
export GOROOT=/usr/local/go
export PATH=$PATH:$GOROOT/bin
export GOPATH=/home/admin/go
"/etc/profile" 79L, 1906C           
```

可以用env命令查看系统环境变量

```bash
MAIL=/var/spool/mail/root
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/usr/local/go/bin:/root/bin
PWD=/root
LANG=en_US.UTF-8
HISTCONTROL=ignoredups
SHLVL=1
HOME=/root
GOROOT=/usr/local/go
LOGNAME=root
SSH_CONNECTION=223.104.193.57 63879 172.17.22.1 22
GOPATH=/home/admin/go
LESSOPEN=||/usr/bin/lesspipe.sh %s
XDG_RUNTIME_DIR=/run/user/0
_=/usr/bin/env
```

可以看到上面那个字符集是英文的



## 生效

source /etc/profile

对文件的修改立刻生效



## ~/.bash_profile

~/.bash_profile⽂件。每个⽤户的BASH环境配置⽂件，存在于⽤户的主⽬录中，当系统运⾏/etc/profile后，将读取此⽂件的内容。

```bash
[root@iZm5e98zphj5y525q4v5k4Z ~]# pwd
/root
[root@iZm5e98zphj5y525q4v5k4Z ~]# vim .bash_profile

# .bash_profile

# Get the aliases and functions
if [ -f ~/.bashrc ]; then
        . ~/.bashrc
fi

# User specific environment and startup programs

PATH=$PATH:$HOME/bin

export PATH
```



## ~/.bashrc

~/.bashrc⽂件。前两个⽂件仅在系统登录时读取，此⽂件将在每次运⾏bash时读取，此⽂件主要定义的是⼀些终端设置以及shell提⽰符等，⽽不定义环境变量等内容。

```bash
[root@iZm5e98zphj5y525q4v5k4Z ~]# pwd
/root
[root@iZm5e98zphj5y525q4v5k4Z ~]# vim .bashrc

# .bashrc

# User specific aliases and functions

alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'

# Source global definitions
if [ -f /etc/bashrc ]; then
        . /etc/bashrc
fi
```



## ~/.bash_history

记录用户bash的历史使用命令

```bash
[root@iZm5e98zphj5y525q4v5k4Z ~]# pwd
/root
[root@iZm5e98zphj5y525q4v5k4Z ~]# vim .bashrc
[root@iZm5e98zphj5y525q4v5k4Z ~]# vim .bash_history 

go
go version
vim profile
vim /etc/profile
source ./profile
```



这里记录的命令数由用户环境变量中的HISTSIZE决定

也可以直接在命令行中输入history

```bash
[root@iZm5e98zphj5y525q4v5k4Z ~]# history
   31  ls
   32  pip install eventlet
   33  als
   34  ls
   35  cd code_plat/
   36  ls
   37  cd env/
   38  cd bin/
 1023  vim .bash_history 
 1024  du -sh .bash_history 
 1025  du -c .bash_history 
 1026  du -sh .bash_history 
 1027  du -sh *
 1028  ls
 1029  vim ~/.bash_history 
 1030  history
[root@iZm5e98zphj5y525q4v5k4Z ~]# 
```







# 管道符

command A|command B

将A命令的输出作为命令B的执行对象

比如上面的locale -a就是列出所有的字符集

太长了，就不列出来了

grep string是字符串匹配，如果某一行里面有string，就选中这一行

所以locale -a|grep zh就是对locale -a的结果进行是否含有zh判断，如果有就显示出来，否则不显示。

```bash
[root@iZm5e98zphj5y525q4v5k4Z ~]# locale -a|grep zh
zh_CN
zh_CN.gb18030
zh_CN.gb2312
zh_CN.gbk
zh_CN.utf8
zh_HK
zh_HK.big5hkscs
zh_HK.utf8
zh_SG
zh_SG.gb2312
zh_SG.gbk
zh_SG.utf8
zh_TW
zh_TW.big5
zh_TW.euctw
zh_TW.utf8
```



# rm

```bash
[root@iZm5e98zphj5y525q4v5k4Z ~]# rm --help
Usage: rm [OPTION]... FILE...
Remove (unlink) the FILE(s).

  -f, --force           ignore nonexistent files and arguments, never prompt
  强制执行删除，并且在删除某个文件或目录时，不询问用户是否删除
[root@iZm5e98zphj5y525q4v5k4Z ~]# rm -rf 2
[root@iZm5e98zphj5y525q4v5k4Z ~]# 
  -i                    prompt before every removal
  删除文件时，会询问用户y或n
[root@iZm5e98zphj5y525q4v5k4Z ~]# rm -ri 2
rm: remove directory ‘2’? 
  -I                    prompt once before removing more than three files, or
                          when removing recursively; less intrusive than -i,
                          while still giving protection against most mistakes
      --interactive[=WHEN]  prompt according to WHEN: never, once (-I), or
                          always (-i); without WHEN, prompt always
      --one-file-system  when removing a hierarchy recursively, skip any
                          directory that is on a file system different from
                          that of the corresponding command line argument
      --no-preserve-root  do not treat '/' specially
      --preserve-root   do not remove '/' (default)
  -r, -R, --recursive   remove directories and their contents recursively
  递归删除，删除目录及目录里面的内容
[root@iZm5e98zphj5y525q4v5k4Z ~]# mkdir -p 1/2/3
[root@iZm5e98zphj5y525q4v5k4Z ~]# tree 1
1
└── 2
    └── 3

2 directories, 0 files
[root@iZm5e98zphj5y525q4v5k4Z ~]# rm -rf 1
  -d, --dir             remove empty directories
  -v, --verbose         explain what is being done
  显示删除的细节
[root@iZm5e98zphj5y525q4v5k4Z ~]# rm -rfv 1*
removed directory: ‘1’
removed ‘1.txt’

      --help     display this help and exit
      --version  output version information and exit

```



# mv

两个用途：Rename SOURCE to DEST, or move SOURCE(s) to DIRECTORY.

重命名和移动文件



# touch

用于修改指定的文件或者目录的时间，包括存取时间和更改时间

```bash
[root@iZm5e98zphj5y525q4v5k4Z ~]# ls -l
total 16
drwxr-xr-x 9 root root 4096 Jun 17 21:31 code_plat.backup
drwxr-xr-x 6 root root 4096 Apr 19 15:30 env
drwxr-xr-x 8 root root 4096 Apr 18 22:51 not_forget
drwxr-xr-x 2 root root 4096 Jul 13 00:00 shell_script
[root@iZm5e98zphj5y525q4v5k4Z ~]# touch *
[root@iZm5e98zphj5y525q4v5k4Z ~]# ls -l
total 16
drwxr-xr-x 9 root root 4096 Jul 13 18:41 code_plat.backup
drwxr-xr-x 6 root root 4096 Jul 13 18:41 env
drwxr-xr-x 8 root root 4096 Jul 13 18:41 not_forget
drwxr-xr-x 2 root root 4096 Jul 13 18:41 shell_script
```



如果文件不存在，则新建之

```bash
[root@iZm5e98zphj5y525q4v5k4Z ~]# touch 1.txt
[root@iZm5e98zphj5y525q4v5k4Z ~]# ls
1.txt  code_plat.backup  env  not_forget  shell_script
```



# date

用来显示和时间有关的信息，特点是时间的格式可以充分的自定义。

date ‘+format’

```bash
[root@iZm5e98zphj5y525q4v5k4Z ~]# date '+%c'
Tue 13 Jul 2021 06:46:30 PM CST
[root@iZm5e98zphj5y525q4v5k4Z ~]# date '+now:%c'
now:Tue 13 Jul 2021 06:47:47 PM CST
```



# cp



# cal

```bash
[root@iZm5e98zphj5y525q4v5k4Z ~]# cal --help

Usage:
 cal [options] [[[day] month] year]

Options:
 -1, --one        show only current month (default)
 -3, --three      show previous, current and next month
 -s, --sunday     Sunday as first day of week
 -m, --monday     Monday as first day of week
 -j, --julian     output Julian dates
 -y, --year       show whole current year
 -V, --version    display version information and exit
 -h, --help       display this help text and exit
```



# uname

查看和系统有关的信息

```bash
[root@iZm5e98zphj5y525q4v5k4Z ~]# uname --help
Usage: uname [OPTION]...
Print certain system information.  With no OPTION, same as -s.

  -a, --all                print all information, in the following order,
                             except omit -p and -i if unknown:
  -s, --kernel-name        print the kernel name
Linux
  -n, --nodename           print the network node hostname
  网络结点主机名
[root@iZm5e98zphj5y525q4v5k4Z ~]# uname -n
iZm5e98zphj5y525q4v5k4Z
  -r, --kernel-release     print the kernel release
  内核的发行版本
[root@iZm5e98zphj5y525q4v5k4Z ~]# uname -r
3.10.0-1160.31.1.el7.x86_64
  -v, --kernel-version     print the kernel version
  -m, --machine            print the machine hardware name
  -p, --processor          print the processor type or "unknown"
  -i, --hardware-platform  print the hardware platform or "unknown"
处理器类型
[root@iZm5e98zphj5y525q4v5k4Z ~]# uname -i
x86_64
  -o, --operating-system   print the operating system
      --help     display this help and exit
      --version  output version information and exit

GNU coreutils online help: <http://www.gnu.org/software/coreutils/>
For complete documentation, run: info coreutils 'uname invocation'
```



# wc

显示对文本的统计信息，包括bytes字节数，chars字符数，lines行数



```bash
[root@iZm5e98zphj5y525q4v5k4Z env]# vim pyvenv.cfg 

home = /usr
implementation = CPython
version_info = 3.6.8.final.0
virtualenv = 20.4.3
include-system-site-packages = false
base-prefix = /usr
base-exec-prefix = /usr
base-executable = /usr/bin/python3


[root@iZm5e98zphj5y525q4v5k4Z env]# wc --help
Usage: wc [OPTION]... [FILE]...
  or:  wc [OPTION]... --files0-from=F
Print newline, word, and byte counts for each FILE, and a total line if
more than one FILE is specified.  With no FILE, or when FILE is -,
read standard input.  A word is a non-zero-length sequence of characters
delimited by white space.
The options below may be used to select which counts are printed, always in
the following order: newline, word, character, byte, maximum line length.
  -c, --bytes            print the byte counts
  字节数
[root@iZm5e98zphj5y525q4v5k4Z env]# wc -c pyvenv.cfg 
201 pyvenv.cfg
  -m, --chars            print the character counts
[root@iZm5e98zphj5y525q4v5k4Z env]# wc -m pyvenv.cfg 
201 pyvenv.cfg
  -l, --lines            print the newline counts
[root@iZm5e98zphj5y525q4v5k4Z env]# wc -l pyvenv.cfg 
8 pyvenv.cf
      --files0-from=F    read input from the files specified by
                           NUL-terminated names in file F;
                           If F is - then read names from standard input
  -L, --max-line-length  print the length of the longest line
  -w, --words            print the word counts
      --help     display this help and exit
      --version  output version information and exit
```



# useradd

系统上所有用户都在/etc/passwd目录中存放

```bash
[root@iZm5e98zphj5y525q4v5k4Z env]# vim /etc/passwd

bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
games:x:12:100:games:/usr/games:/sbin/nologin
ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin
nobody:x:99:99:Nobody:/:/sbin/nologin
systemd-network:x:192:192:systemd Network Management:/:/sbin/nologin
dbus:x:81:81:System message bus:/:/sbin/nologin
polkitd:x:999:998:User for polkitd:/:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
postfix:x:89:89::/var/spool/postfix:/sbin/nologin
chrony:x:998:996::/var/lib/chrony:/sbin/nologin
ntp:x:38:38::/etc/ntp:/sbin/nologin
tcpdump:x:72:72::/:/sbin/nologin
nscd:x:28:28:NSCD Daemon:/:/sbin/nologin
admin:x:1000:1000::/home/admin:/bin/bash
nginx:x:997:995:Nginx web server:/var/lib/nginx:/sbin/nologin
uwsgi:x:996:994:uWSGI daemon user:/run/uwsgi:/sbin/nologin
tss:x:59:59:Account used by the trousers package to sandbox the tcsd daemon:/dev/null:/sbin/nologin
mysql:x:27:27:MySQL Server:/var/lib/mysql:/bin/false
```

比较重要的option

```bash
1、-p, --password PASSWORD       encrypted password of the new account
输入的时候密码在屏幕上明文显示，可能不安全；存储时还是密文存储
也可以用passwd手动指定密码
2、-d, --home-dir HOME_DIR       home directory of the new account
给新用户指定家目录，如果没有指明，默认以用户名在/home下新建一个目录
3、-g, --gid GROUP               name or ID of the primary group of the new account
给新用户指定属组
4、-s, --shell SHELL             login shell of the new account
登录时的shell，默认为PATH里面的shell

```



# userdel

删除某个用户，但是该用户的home directory还在

# passwd

给相应用户设置密码

```bash
[root@iZm5e98zphj5y525q4v5k4Z env]# useradd user
Creating mailbox file: File exists
[root@iZm5e98zphj5y525q4v5k4Z env]# passwd user
Changing password for user user.
New password: 
Retype new password: 
passwd: all authentication tokens updated successfully.

tss:x:59:59:Account used by the trousers package to sandbox the tcsd daemon:/dev/null:/sbin/nologin
mysql:x:27:27:MySQL Server:/var/lib/mysql:/bin/false
user:x:1001:1001::/home/user:/bin/bash
```





# whoami

查看当前登录的用户（用户名）

# su和sudo

su：switch user

su username

root到其他用户不需要输入密码，反之需要输入密码

常用：

 su [options] [-] [USER [arg]...]

```bash
1、-c, --command <command>         pass a single command to the shell with -c
以某个用户的身份执行-c后的一条命令
[root@iZm5e98zphj5y525q4v5k4Z user]# su -c pwd - user
/home/user
2、在su的options后面跟-自动进入跳转用户的家目录
[root@iZm5e98zphj5y525q4v5k4Z env]# pwd
/root/env
[root@iZm5e98zphj5y525q4v5k4Z env]# su - user
Last login: Tue Jul 13 19:29:23 CST 2021 on pts/6
[user@iZm5e98zphj5y525q4v5k4Z ~]$ pwd
/home/user

```



# cat



# which



# find



# grep



# chmod



# more



# tar

```bash
Examples:
  tar -cf archive.tar foo bar  # Create archive.tar from files foo and bar.
  tar -tvf archive.tar         # List all files in archive.tar verbosely.
  tar -xf archive.tar          # Extract all files from archive.tar.
```



## 打包

tar -cf file.tar file01 file02

create file

```python
[root@iZm5e98zphj5y525q4v5k4Z not_forget]# tar -cf learning_log.tar learning_log
[root@iZm5e98zphj5y525q4v5k4Z not_forget]# ls
collected_static  db.sqlite3  learning_log  learning_logs  learning_log.tar  ll_env  manage.py  requirements.txt  users
[root@iZm5e98zphj5y525q4v5k4Z not_forget]# du -sh *
8.0M	collected_static
148K	db.sqlite3
40K	learning_log
6.4M	learning_logs
20K	learning_log.tar
62M	ll_env
4.0K	manage.py
4.0K	requirements.txt
88K	users
```





##  解打包 

tar -xf file.tar

extract file

```python
[root@iZm5e98zphj5y525q4v5k4Z ~]# ls
ad_project  code_plat.backup  env  learning_log.tar  not_forget  novel  Python-3.7.4  Python-3.7.4.tar.xz  shell_script
[root@iZm5e98zphj5y525q4v5k4Z ~]# tar -xf *.tar
[root@iZm5e98zphj5y525q4v5k4Z ~]# ls
ad_project        env           learning_log.tar  novel         Python-3.7.4.tar.xz
code_plat.backup  learning_log  not_forget        Python-3.7.4  shell_script
[root@iZm5e98zphj5y525q4v5k4Z ~]# du -sh *
119M	ad_project
10M	code_plat.backup
259M	env
40K	learning_log
20K	learning_log.tar
94M	not_forget
301M	novel
215M	Python-3.7.4
17M	Python-3.7.4.tar.xz
16K	shell_script
```

## 查看文件包的文件

tar -tf

list files

```bash
[root@iZm5e98zphj5y525q4v5k4Z ~]# tar -tf learning_log.tar 
learning_log/
learning_log/asgi.py
learning_log/__pycache__/
learning_log/__pycache__/wsgi.cpython-38.pyc
learning_log/__pycache__/settings.cpython-38.pyc
learning_log/__pycache__/__init__.cpython-38.pyc
learning_log/__pycache__/urls.cpython-38.pyc
learning_log/wsgi.py
learning_log/__init__.py
learning_log/urls.py
learning_log/settings.py
```



## 压缩

gzip file.tar

生成的压缩包的后缀为tar.gz

```bash
[root@iZm5e98zphj5y525q4v5k4Z ~]# ls -l
-rw-r--r--  1 root root    20480 Jul 15 15:22 learning_log.tar
[root@iZm5e98zphj5y525q4v5k4Z ~]# gzip learning_log.tar 
[root@iZm5e98zphj5y525q4v5k4Z ~]# ls -l
-rw-r--r--  1 root root     3665 Jul 15 15:22 learning_log.tar.gz
```

发现确实压缩了

## 解压缩

gzip -d file.tar.gz

-d decompress

```bash
[root@iZm5e98zphj5y525q4v5k4Z ~]# gzip -d learning_log.tar.gz 
[root@iZm5e98zphj5y525q4v5k4Z ~]# ls -l learning_log.tar 
-rw-r--r-- 1 root root 20480 Jul 15 15:22 learning_log.tar
```

## 打包和压缩

打包：tar -cf  打包+压缩：tar -zcf

解打包：tar -xf   解打包+解压缩：tar -zxf

```bash
[root@iZm5e98zphj5y525q4v5k4Z ~]# ls
ad_project  code_plat.backup  env  learning_log  not_forget  novel  Python-3.7.4  Python-3.7.4.tar.xz  shell_script
[root@iZm5e98zphj5y525q4v5k4Z ~]# tar -zcf learning_log.tar.gz learning_log/
[root@iZm5e98zphj5y525q4v5k4Z ~]# ls
ad_project        env           learning_log.tar.gz  novel         Python-3.7.4.tar.xz
code_plat.backup  learning_log  not_forget           Python-3.7.4  shell_script
[root@iZm5e98zphj5y525q4v5k4Z ~]# rm -rf learning_log
[root@iZm5e98zphj5y525q4v5k4Z ~]# tar -zxf learning_log.tar.gz 
[root@iZm5e98zphj5y525q4v5k4Z ~]# ls
ad_project        env           learning_log.tar.gz  novel         Python-3.7.4.tar.xz
code_plat.backup  learning_log  not_forget           Python-3.7.4  shell_script
```



# chgrp



# zip



shell命令的一般格式：

command+option+parameter

option是可选的，option前面必须有-，用来区分选项和参数

man命令名，查看命令的帮助文档，

空格--下一页，回车--下一行，q退出



# shell重定向

## 输入重定向

用户从文件中输入命令，相当于将输入的命令保存下来

## 输出重定向

命令执行的结果默认输出到显示器上，让我们看到，但也可以输出到文件中（重定向）



## 错误



# 桌面环境

有两种：GNOME，KDE

switchdesk GNOME/KDE

