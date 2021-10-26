shell脚本

# shell script

shell是在用户和linux系统内核之间的一个桥梁

shell script就是用户在shell里面编写的脚本



# shell的环境变量

## 可写

可写的环境变量就是可以对其进行修改。



### 系统级

放在/etc/profile文件中

在登录过程中由系统进行初始化、加载

由root进行设置，作用于系统上的所有用户



### 用户级

在~/.bash_profile中

用户定制自己的运行环境，可以覆盖系统级的环境变量



## 只读

系统预先设定好的，不能修改

详见echo-特殊变量



## 查看

env查看所有的环境变量

```bash
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ env
XDG_SESSION_ID=1526
HOSTNAME=iZm5e98zphj5y525q4v5k4Z
TERM=xterm
SHELL=/bin/bash
HISTSIZE=1000
SSH_CLIENT=222.175.198.2 3551 22
SSH_TTY=/dev/pts/0
USER=whr2190300211
LS_COLORS=rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=01;05;37;41:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.Z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.jpg=01;35:*.jpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.axv=01;35:*.anx=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=01;36:*.au=01;36:*.flac=01;36:*.mid=01;36:*.midi=01;36:*.mka=01;36:*.mp3=01;36:*.mpc=01;36:*.ogg=01;36:*.ra=01;36:*.wav=01;36:*.axa=01;36:*.oga=01;36:*.spx=01;36:*.xspf=01;36:
MAIL=/var/spool/mail/whr2190300211
PATH=/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/usr/local/go/bin:/home/whr2190300211/.local/bin:/home/whr2190300211/bin
PWD=/home/whr2190300211/shell_script
LANG=en_US.UTF-8
HISTCONTROL=ignoredups
SHLVL=1
HOME=/home/whr2190300211
GOROOT=/usr/local/go
LOGNAME=whr2190300211
SSH_CONNECTION=222.175.198.2 3551 172.17.22.1 22
GOPATH=/home/admin/go
LESSOPEN=||/usr/bin/lesspipe.sh %s
XDG_RUNTIME_DIR=/run/user/1002
_=/usr/bin/env
OLDPWD=/home/whr2190300211
```



set查看所有的shell变量，包括用户自定义的变量（下面的username）

```bash
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ username=111
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ set
BASH=/bin/bash
BASHOPTS=checkwinsize:cmdhist:expand_aliases:extquote:force_fignore:histappend:hostcomplete:interactive_comments:login_shell:progcomp:promptvars:sourcepath
BASH_ALIASES=()
BASH_ARGC=()
BASH_ARGV=()
BASH_CMDS=()
BASH_LINENO=()
BASH_SOURCE=()
BASH_VERSINFO=([0]="4" [1]="2" [2]="46" [3]="2" [4]="release" [5]="x86_64-redhat-linux-gnu")
BASH_VERSION='4.2.46(2)-release'
COLUMNS=134
DIRSTACK=()
EUID=1002
GOPATH=/home/admin/go
GOROOT=/usr/local/go
GROUPS=()
HISTCONTROL=ignoredups
HISTFILE=/home/whr2190300211/.bash_history
HISTFILESIZE=1000
HISTSIZE=1000
HOME=/home/whr2190300211
HOSTNAME=iZm5e98zphj5y525q4v5k4Z
HOSTTYPE=x86_64
ID=1002
IFS=$' \t\n'
LANG=en_US.UTF-8
LESSOPEN='||/usr/bin/lesspipe.sh %s'
LINES=30
LOGNAME=whr2190300211
LS_COLORS='rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=01;05;37;41:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.Z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.jpg=01;35:*.jpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.axv=01;35:*.anx=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=01;36:*.au=01;36:*.flac=01;36:*.mid=01;36:*.midi=01;36:*.mka=01;36:*.mp3=01;36:*.mpc=01;36:*.ogg=01;36:*.ra=01;36:*.wav=01;36:*.axa=01;36:*.oga=01;36:*.spx=01;36:*.xspf=01;36:'
MACHTYPE=x86_64-redhat-linux-gnu
MAIL=/var/spool/mail/whr2190300211
MAILCHECK=60
OLDPWD=/home/whr2190300211
OPTERR=1
OPTIND=1
OSTYPE=linux-gnu
PATH=/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/usr/local/go/bin:/home/whr2190300211/.local/bin:/home/whr2190300211/bin
PIPESTATUS=([0]="0")
PPID=5121
PROMPT_COMMAND='printf "\033]0;%s@%s:%s\007" "${USER}" "${HOSTNAME%%.*}" "${PWD/#$HOME/~}"'
PS1='[\u@\h \W]\$ '
PS2='> '
PS4='+ '
PWD=/home/whr2190300211/shell_script
SHELL=/bin/bash
SHELLOPTS=braceexpand:emacs:hashall:histexpand:history:interactive-comments:monitor
SHLVL=1
SSH_CLIENT='222.175.198.2 6488 22'
SSH_CONNECTION='222.175.198.2 6488 172.17.22.1 22'
SSH_TTY=/dev/pts/1
TERM=xterm
UID=1002
USER=whr2190300211
XDG_RUNTIME_DIR=/run/user/1002
XDG_SESSION_ID=1560
_=
colors=/home/whr2190300211/.dircolors
username=111
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ set |grep username
username=111
```



## 删除

unset

```bash
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ unset username
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ set |grep username
_=username
```





# 通配符

## *

匹配任意数量的任意字符，不包括文件名开头的.（隐藏文件）和文件末尾的/（子文件夹的内容）



```bash
# 不包括隐藏文件
[whr2190300211@iZm5e98zphj5y525q4v5k4Z ~]$ ls -l
total 24
-rwxr-xr-- 1 whr2190300211 root 1004 Jul 19 15:20 1.py
-rw-r--r-- 1 whr2190300211 root    0 Jul 19 16:46 22.txt
-rw-r--r-- 1 whr2190300211 root   77 Jul 19 16:46 2.txt
-rwxr--r-- 1 whr2190300211 root  668 Jul 19 15:51 manage.py
drwxr-xr-x 8 whr2190300211 root 4096 Jul 19 15:59 not_forget
drwxr-xr-x 2 whr2190300211 root 4096 Jul 25 15:34 shell_script
drwxr-xr-x 2 whr2190300211 root 4096 Jul 19 16:48 test
-rw-r--r-- 1 whr2190300211 root    0 Jul 19 16:49 test.txt
# 包括隐藏文件
[whr2190300211@iZm5e98zphj5y525q4v5k4Z ~]$ ls -al
total 60
drwx------  6 whr2190300211 1002 4096 Jul 25 15:34 .
drwxr-xr-x. 7 root          root 4096 Jul 24 23:13 ..
-rwxr-xr--  1 whr2190300211 root 1004 Jul 19 15:20 1.py
-rw-r--r--  1 whr2190300211 root    0 Jul 19 16:46 22.txt
-rw-r--r--  1 whr2190300211 root   77 Jul 19 16:46 2.txt
-rw-------  1 whr2190300211 root 1924 Jul 25 15:10 .bash_history
-rw-r--r--  1 whr2190300211 1002   18 Apr  1  2020 .bash_logout
-rw-r--r--  1 whr2190300211 1002  193 Apr  1  2020 .bash_profile
-rw-r--r--  1 whr2190300211 1002  231 Apr  1  2020 .bashrc
-rwxr--r--  1 whr2190300211 root  668 Jul 19 15:51 manage.py
drwxr-xr-x  8 whr2190300211 root 4096 Jul 19 15:59 not_forget
drwxr-xr-x  2 whr2190300211 root 4096 Jul 25 15:34 shell_script
drwx------  2 whr2190300211 root 4096 Jul 25 11:17 .ssh
drwxr-xr-x  2 whr2190300211 root 4096 Jul 19 16:48 test
-rw-r--r--  1 whr2190300211 root    0 Jul 19 16:49 test.txt
-rw-------  1 whr2190300211 root 4544 Jul 25 15:34 .viminfo
# echo *
[whr2190300211@iZm5e98zphj5y525q4v5k4Z ~]$ echo *
1.py 22.txt 2.txt manage.py not_forget shell_script test test.txt
# echo.*（此时只输出了隐藏文件）
[whr2190300211@iZm5e98zphj5y525q4v5k4Z ~]$ echo .*
. .. .bash_history .bash_logout .bash_profile .bashrc .ssh .viminfo
```



## ?

匹配任意一个字符



## []

范围

```bash
[whr2190300211@iZm5e98zphj5y525q4v5k4Z ~]$ ls
1.py  22.txt  2.txt  manage.py  not_forget  shell_script  test  test.txt
[whr2190300211@iZm5e98zphj5y525q4v5k4Z ~]$ echo [1-9].txt
2.txt
```

范围否定

```bash
[whr2190300211@iZm5e98zphj5y525q4v5k4Z ~]$ ls
1.py  22.txt  2.txt  3.txt  manage.py  not_forget  shell_script  test  test.txt
[whr2190300211@iZm5e98zphj5y525q4v5k4Z ~]$ echo [!0-2].txt
3.txt
```



# 引号

## 反引号

### 命令

对于反引号括起来的内容，shell会将这个字符串视为命令

```bash
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ cat 1
echo `pwd`
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ sh 1
/home/whr2190300211/shell_script
```



### 命令赋值给变量

前面将命令用反引号括起来，也可以将这个字符串赋值给一个变量

```bash
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ cat 2
cmd=`pwd`
echo "the cmd result is ${cmd}"
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ sh 2
the cmd result is /home/whr2190300211/shell_script
```



### 嵌套使用

将命名赋值给变量，命令中嵌套命令。

```bash
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ cat 3
cmd=`echo now the dir is \`pwd\``
echo ${cmd}
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ sh 3
now the dir is /home/whr2190300211/shell_script
```





## 单引号

在单引号中，所有字符都视为普通字符，没有特殊含义，比如反引号括起来的内容不被视为命令并执行，${var}也不被视为变量

```bash
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ cat 4
cmd=`pwd`
var="001"
echo 'now the dir is ${cmd} or `pwd`,var is ${var}'
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ sh 4
now the dir is ${cmd} or `pwd`,var is ${var}
```



## 双引号

反引号括起来的内容被视为命令进行执行，${var}被视为变量，\转义字符可以使用。

```bash
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ cat 5
cmd=`ls -l`
var="now the ls cmd result is:"
echo -e "${var}\n${cmd}"
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ sh 5
now the ls cmd result is:
total 20
-rw-r--r-- 1 whr2190300211 root 11 Jul 25 15:56 1
-rw-r--r-- 1 whr2190300211 root 42 Jul 25 16:00 2
-rw-r--r-- 1 whr2190300211 root 46 Jul 25 16:03 3
-rw-r--r-- 1 whr2190300211 root 72 Jul 25 16:06 4
-rw-r--r-- 1 whr2190300211 root 69 Jul 25 16:12 5
```



```bash
学习shell 特殊字符的使用包括双引号、单引号、倒引号和” \”的作用；
学习系统环境变量的使用，包括$HOME、$PATH、$PWD等；
学习用户变量的定义和赋值方法；
学习内部变量的作用和使用方法，包括$#、$*、$0、$?；
以上题目自己使用不同的方式和方法学习各种符号和变量的用法，给出具体命令或者程序，体现学习内容；
创建一个shell脚本程序：创建Centos7的5个用户名和密码，所创建的用户名和密码由参数输入；要求用户名的第2位和第4位为[0-9]，不符要求则放弃，同时提示信息。
删除上述的用户
编程求解n个数的和，要求n由键盘输入，使用循环语句完成；
编写shell脚本，完成在命令行参数一指定的文件中搜索参数二指定的单词，并将结果存入目录/home/test/temp；
利用for循环将当前目录下的指定扩展名（由输入决定）文件转移到指定的目录下，并按照文件大小排序，并显示移动后指定目录的内容。
```



# 运行shell脚本



## 后缀

无论是什么脚本，都需要指定脚本的解释器。比如python脚本，后缀为.py；php脚本，后缀为.php；shell脚本，==后缀为.sh==。



## 运行

- 当前目录

```bash
chmod +7xx ./name.sh
./name.sh
```



首先要将文件的权限修改为可执行

```bash
[root@iZm5e98zphj5y525q4v5k4Z shell_script]# ls -al
total 12
drwxr-xr-x   2 root root 4096 Jul 12 23:41 .
dr-xr-x---. 12 root root 4096 Jul 12 23:41 ..
-rw-r--r--   1 root root   32 Jul 12 23:41 1.sh
[root@iZm5e98zphj5y525q4v5k4Z shell_script]# chmod +722 ./1.sh 
[root@iZm5e98zphj5y525q4v5k4Z shell_script]# ls -al
total 12
drwxr-xr-x   2 root root 4096 Jul 12 23:41 .
dr-xr-x---. 12 root root 4096 Jul 12 23:41 ..
-rwxrw-rw-   1 root root   32 Jul 12 23:41 1.sh
```

这样就是可执行程序了。

并且需要在脚本的第一行，显式的声明用哪个解释器解释这个脚本。

```bash
#! /bin/bash
echo "hello world"
```

然后就可以用./name.sh执行这个脚本了。

```bash
[root@iZm5e98zphj5y525q4v5k4Z shell_script]# ./1.sh 
hello world
```



==注意==

- 必须要用./加文件名，./表明是当前目录的文件。
- 如果不加，系统会去PATH路径里面找nane.sh，显然是找不到的。

```bash
[root@iZm5e98zphj5y525q4v5k4Z shell_script]# 1.sh
-bash: 1.sh: command not found
```



==其他的二进制可执行文件也是一样，在执行时需要加上./==

```bash
[root@iZm5e98zphj5y525q4v5k4Z shell_script]# ls
1.sh
```



- 指定解释器

/bin/bash name.sh

上面那种方法比较麻烦，首先要在脚本里面指明解释器的类型，然后再修改文件的权限，其实就是为了让os能自己找到合适的解释器。

这样的效率不如自己显示的指定用什么解释器。

```
[root@iZm5e98zphj5y525q4v5k4Z shell_script]# /bin/bash 1.sh
hello world



# 变量

## 定义

name=value

## 使用

${var_name}

{}是将变量名和一般的字符串或者关键字给隔开

​```bash
[root@iZm5e98zphj5y525q4v5k4Z shell_script]# vim 3.sh

file="name"
echo ${file}

[root@iZm5e98zphj5y525q4v5k4Z shell_script]# /bin/bash 3.sh 
name
```

- 直接用sh 脚本名即可

```bash
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ cat test7-1 
ls -l
cal
who
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ sh test7-1 
total 8
-rw-r--r-- 1 whr2190300211 root 87 Jul 25 12:29 1.sh
-rwxr--r-- 1 whr2190300211 root 14 Jul 25 12:34 test7-1
      July 2021     
Su Mo Tu We Th Fr Sa
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30 31

whr2190300211 pts/0        2021-07-25 11:18 (127.0.0.1)
root     pts/1        2021-07-25 11:14 (222.175.198.2)
root     pts/2        2021-07-25 11:19 (221.2.164.30)
```



## 只读变量

声明：readonly var_name

```bash
[root@iZm5e98zphj5y525q4v5k4Z shell_script]# vim 4.sh

file="again"
readonly file
echo ${file}
file="time"
echo ${file}

[root@iZm5e98zphj5y525q4v5k4Z shell_script]# /bin/bash 4.sh 
again
4.sh: line 4: file: readonly variable
again
```

声明为只读变量后，不能再修改变量的值，由于是解释型语言，即使尝试对readonly类型的变量进行修改，也不会终止脚本的执行。

可以看到，尝试对readonly的变量进行修改值后，值不变。



## 删除变量

unset var_name

unset不能删除只读变量

```bash
[root@iZm5e98zphj5y525q4v5k4Z shell_script]# vim 1.sh

#! /bin/bash
echo "hello world"
tmp="111"
echo ${tmp}
unset tmp
echo ${tmp}
[root@iZm5e98zphj5y525q4v5k4Z shell_script]# /bin/bash 1.sh 
hello world
111
```







# 字符串



## 单引号

用单引号括起来的字符串，里面的变量都无效

```bash
[root@iZm5e98zphj5y525q4v5k4Z shell_script]# vim 1.sh

tmp="hello"
echo 'why ${tmp}'
[root@iZm5e98zphj5y525q4v5k4Z shell_script]# /bin/bash 1.sh 
why ${tmp}
```

不能出现单独的单引号



## 双引号

可以使用变量

```bash
[root@iZm5e98zphj5y525q4v5k4Z shell_script]# cat 1.sh 
tmp="hello"
echo "why ${tmp}"
[root@iZm5e98zphj5y525q4v5k4Z shell_script]# /bin/bash 1.sh 
why hello
```



```bash
[root@iZm5e98zphj5y525q4v5k4Z shell_script]# cat 1.sh 
tmp="hello"
echo "why \"${tmp}"
[root@iZm5e98zphj5y525q4v5k4Z shell_script]# /bin/bash 1.sh 
why "hello
```



## 字符串长度

```bash
[root@iZm5e98zphj5y525q4v5k4Z shell_script]# cat 2.sh 
string="1111"
echo ${#string}
[root@iZm5e98zphj5y525q4v5k4Z shell_script]# /bin/bash 2.sh 
4
```



# 数组

数组中的元素类型可以不相同

array[@]访问数组的所有元素

```bash
[root@iZm5e98zphj5y525q4v5k4Z shell_script]# cat 1.sh
array=(1 2 3 "111")
echo "array[0]=${array[0]}"
echo "all array=${array[@]}"

[root@iZm5e98zphj5y525q4v5k4Z shell_script]# /bin/bash 1.sh
array[0]=1
all array=1 2 3 111
```



## 数组元素个数

```bash
[root@iZm5e98zphj5y525q4v5k4Z shell_script]# cat 1.sh 
array=(1 2 3 "111")
echo "array[0]=${array[0]}"
echo "all array=${array[@]}"
echo "array size=${#array[@]}"
[root@iZm5e98zphj5y525q4v5k4Z shell_script]# /bin/bash 1.sh
array[0]=1
all array=1 2 3 111
array size=4
```



# 传递参数

$n，n为一个数字

$0，默认为脚本文件的名称

```bash
[root@iZm5e98zphj5y525q4v5k4Z shell_script]# cat 0.sh 
echo "第一个参数为$0"
echo "第二个参数为$1"
echo "第三个参数为$2"
[root@iZm5e98zphj5y525q4v5k4Z shell_script]# /bin/bash 0.sh 
第一个参数为0.sh
第二个参数为
第三个参数为
[root@iZm5e98zphj5y525q4v5k4Z shell_script]# /bin/bash 0.sh 1 2
第一个参数为0.sh
第二个参数为1
第三个参数为2
```



# 获取输入

read var

在要求用户输入前，最好有提示性的语句

```bash
[root@iZm5e98zphj5y525q4v5k4Z shell_script]# cat 1.sh
echo "输入数据"
read data
echo "data=${data}"
[root@iZm5e98zphj5y525q4v5k4Z shell_script]# /bin/bash 1.sh
输入数据
1111 jilj
data=1111 jilj
```





# echo

## echo *(通配符)



```bash
# 输出当前目录的所有文件名
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ ls
1.sh  test7-1
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ echo *
1.sh test7-1
# 通配符
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ echo *.sh
1.sh
```



## 特殊变量

| $0   | 当前脚本的文件名                                             |
| ---- | ------------------------------------------------------------ |
| $n   | 传递给脚本或函数的参数。n 是一个数字，表示第几个参数。例如，第一个参数是$1，第二个参数是$2。 |
| $#   | 传递给脚本或函数的参数个数。                                 |
| $*   | 传递给脚本或函数的所有参数。                                 |
| $@   | 传递给脚本或函数的所有参数。被双引号(" ")包含时，与 $* 稍有不同，下面将会讲到。 |
| $?   | 上个命令的退出状态，或函数的返回值。                         |
| $$   | 当前Shell进程ID。对于 Shell 脚本，就是这些脚本所在的进程ID。 |

```bash
# $n
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ cat test
echo "filename:$0"
echo "1:$1"
echo "2:$2"
echo "n:$#"
echo "total:$*"
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ sh test a b c
filename:test
1:a
2:b
n:3
total:a b c

# $$
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ cat test2
echo "当前shell的进程号$$"
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ sh test2
当前shell的进程号25968

# $?
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ cat test3
echo "上一个命令的退出状态$?"
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ sh test3
上一个命令的退出状态0
```





## 启用转移字符

-e 启用转义字符

```bash
[root@iZm5e98zphj5y525q4v5k4Z shell_script]# cat 2.sh 
echo -e "test\ntest"
[root@iZm5e98zphj5y525q4v5k4Z shell_script]# /bin/bash 2.sh
test
test
```

## 输出命令执行的结果

```bash
[root@iZm5e98zphj5y525q4v5k4Z shell_script]# cat 2.sh
echo `docker images`
[root@iZm5e98zphj5y525q4v5k4Z shell_script]# /bin/bash 2.sh 
REPOSITORY TAG IMAGE ID CREATED SIZE nginx latest 4cdc5dd7eaad 6 days ago 133MB my_tomcat 1.0 82119924df85 2 weeks ago 672MB nginx <none> 4f380adfc10f 2 weeks ago 133MB mysql 5.7 09361feeb475 2 weeks ago 447MB mysql latest 5c62e459e087 2 weeks ago 556MB tomcat latest 5505f7218e4d 3 weeks ago 667MB centos 7 8652b9f0cb4c 8 months ago 204MB
```



# 命令的执行顺序

## ;

以分号;连接的命令进行顺序执行，下一条命令是否执行和上一条命令是否执行成功（状态码为0）无关

```bash
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ pwd;cd /;ls;cd -
/home/whr2190300211/shell_script
bin  boot  dev  etc  home  lib  lib64  lost+found  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
/home/whr2190300211/shell_script
```



## &&

如果前一条命令执行成功，则继续执行后一条命令，否则不执行。

```bash
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ ls &&mkdir 1 &&mkdir 6
1  2  3  4  5
mkdir: cannot create directory ‘1’: File exists

[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ ls &&mkdir 7 &&mkdir 6
1  2  3  4  5
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ ls
1  2  3  4  5  6  7
```



## ||

如果前一条命令执行成功，则不执行后一条命令；只有前一条命令执行失败才执行后一条命令。

```bash
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ mkdir 6||ls
mkdir: cannot create directory ‘6’: File exists
1  2  3  4  5  6  7
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ ls || mkdir 6
1  2  3  4  5  6  7
```



## &

在命令的最后边加上&可以让命令在后台执行，不占用shell终端。

这个命令在后台执行，但是当前用户退出后，该进程还是会被杀死。

想要查看时，可以用jobs查看后台进程，然后用fg将后台进程回到前台。

```bash
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ cat 1.py 
import time
for i in range(10):
	time.sleep(10)
	print(i)
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ python 1.py &
[1] 29970
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ ls
1  1.py  2  3  4  5
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ pwd
/home/whr2190300211/shell_script
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ 0
pwd
/home/whr2190300211/shell_script
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ 1
2
3
4
5
6
7
8
9
ls
1  1.py  2  3  4  5
[1]+  Done                    python 1.py

```



## nohop

意思是不要挂起，当前用户退出后，命令仍然被执行。

nohup command >out.file 2>&1

不挂起地执行command，同时将2（标准错误）重定向到1（标准输入），然后将标准输出都重定向到out.file里面，作为结果。

执行：

![image-20210725165049355](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210725165049355.png)

断开连接：

![image-20210725165114516](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210725165114516.png)

查看程序的执行结果：

```bash
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ ls
1  1.py  2  3  4  5  out.txt
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ cat out.txt 
nohup: ignoring input
0
1
2
3
4
5
6
7
8
9
```



## nohup+&

nohup command >out.file 2>$1 &

在用户没有退出时，后台执行，并且标准输出都重定向到log文件了，所以在界面上也不会出现输出。

当用户退出时，由于hohup不挂起，所以该进程还能继续执行。

执行命令：

此时shell终端没有被占用(只是nohup在用户没有退出时，还是会被占用)

```bash
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ nohup python 1.py >out.txt 2>&1 &
[1] 30541

```

退出：

![image-20210725165645169](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210725165645169.png)

查看执行结果：

```bash
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ ls
1  1.py  2  3  4  5  out.txt
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ cat out.txt 
nohup: ignoring input
0
1
2
3
4
5
6
7
8
9
```

# 输入输出

## 标准文件

进程运行时自动打开三个标准文件

- stdin，标准输入文件，文件编号0，默认是键盘
- stdout，标准输出文件（错误不属于输出，正确的执行结果是输出），文件编号1，默认是显示器
- stderr，标准错误文件，文件编号2，默认是显示器

python文件：

```bash
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ cat 2.py 
for i in range(10):
	print(i)
print(10/0)
```



对于输出和错误，默认输出到显示器

**command**

```bash
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ python 2.py
0
1
2
3
4
5
6
7
8
9
Traceback (most recent call last):
  File "2.py", line 3, in <module>
    print(10/0)
ZeroDivisionError: integer division or modulo by zero
```



将输出重定向到文件中，将错误显示到显示器上

**command 1>right.txt**

```bash
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ python 2.py 1>right.txt 
Traceback (most recent call last):
  File "2.py", line 3, in <module>
    print(10/0)
ZeroDivisionError: integer division or modulo by zero
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ cat right.txt 
0
1
2
3
4
5
6
7
8
9

```



分别将stdout，stderr重定向到不同的文件中

**command 1>right.txt 2>wrong.txt**

```bash
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ python 2.py 1>right.txt 2>wrong.txt
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ ls
1  1.py  2  2.py  3  4  5  out.txt  right.txt  wrong.txt
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ cat right.txt 
0
1
2
3
4
5
6
7
8
9
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ cat wrong.txt 
Traceback (most recent call last):
  File "2.py", line 3, in <module>
    print(10/0)
ZeroDivisionError: integer division or modulo by zero
```



将stdout，stderr重定向到同一个文件中

**command >out.txt 2>&1**

```bash
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ python 2.py >out.txt 2>&1
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ cat out.txt 
0
1
2
3
4
5
6
7
8
9
Traceback (most recent call last):
  File "2.py", line 3, in <module>
    print(10/0)
ZeroDivisionError: integer division or modulo by zero
```



上面用的都是\>，会覆盖一个文件。

如果想追加，用>>



## 读取输入

用`read var_name`从标准输入中读取数据，然后赋值给var_name



# 变量的算术运算

- Shell中变量没有明确的类型，变量值都以字符串的形式存储
- 算术运算需要使⽤命令将变量中的字符串转换为数值。Shell中的运算⼀般通过两个命令实现：let和expr。

## 算术运算符

- 加+
- 减-
- 乘\\*
- 除/
- 取模%
- 只能对整数进行运算
- 在算数运算符前后都要有空格



## let

```bash
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ cat 1
i="1"
echo "i=${i}"
let i=i+1
echo "i+1=${i}"
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ sh 1
i=1
i+1=2
```



## (())

```bash
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ cat 2
i="1"
echo "i=${i}"
echo "i+1=$((i+1))"
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ sh 2
i=1
i+1=2
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ cat 9
a=9
((a=a + a))
echo $a
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ sh 9
18
```



## expr



# 流程控制



## if

```bash
if condition
then
	command
elif condition
then
	command
else
	command
fi
```

condition可以是命令语句，也可以是测试语句。



### 命令语句

```bash
编写一个 shell 脚本,查找给定的某用户是否在系统中工作。如果在系统中就发一个问候。
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ cat 3
echo "输入要查找的用户"
read username 
echo "`who|grep ${username}`"
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ sh 3
输入要查找的用户
root
root     pts/2        2021-07-25 19:14 (221.2.164.30)

[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ cat 3
echo "输入要查找的用户"
read username 
if who|grep ${username}
then echo "${username}登录了"
else echo "${username}没有登录"
fi 
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ sh 3
输入要查找的用户
ri^Hoot^H
roo没有登录
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ sh 3
输入要查找的用户
root
root     pts/2        2021-07-25 19:14 (221.2.164.30)
root登录了
```





### 测试语句

- 文件测试
- 字符串测试
- 数值测试



### test

#### 文件测试

![image-20210725193645673](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210725193645673.png)

-a 判断文件或者文件夹是否存在

```bash
编写一个 shell 脚本，利用位置参数携带一个文件名，判断该文件在当前目录下是否存在且是一个普通文件

[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ cat 1
echo "输入文件名" 
read filename
if test -f ${filename}
then echo "${filename}是一般文件"
elif test -d ${filename}
then echo "${filename}是目录"
else
echo "unknown"
fi
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ sh 1
输入文件名
1
1是一般文件
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ sh 1
输入文件名
6
6是目录
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ sh 1
输入文件名
9
unknown
```





#### 字符串测试

![image-20210725194307617](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210725194307617.png)

```bash
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ cat 1
echo "1:$1"
echo "2:$2"
if [ $1 = $2 ]
then echo "一样"
else echo "不一样"
fi
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ sh 1 md md5
1:md
2:md5
不一样
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ sh 1 md md
1:md
2:md
一样
```



#### 数值测试

![image-20210725194756568](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210725194756568.png)

-eq equivalent

-ne not equivalent

-lt less than

-le less or equivalent

-gt greater

-ge greater equivalent

```bash
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ cat 2
a=1
b=2
if test ${a} -le ${b}
then echo "yes"
else echo "not"
fi
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ sh 2
yes
```



![image-20210725195437278](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210725195437278.png)

```bash
表达式0<a<10且a<>5
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ cat 3
read a
if test \( ${a} -gt 0 -a ${a} -lt 10 \) -a ${a} -ne 5
then echo 'yes'
else echo 'no'
fi
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ sh 3
1
yes
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ sh 3
5
no
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ sh 3
10
no
```



#### 逻辑连接

![image-20210725195544750](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210725195544750.png)

-a and

-o or

()进行分组，确定优先级

括号前后都需要有空格，并且用转义字符`\( \)`



### 方括号[]

也有三种测试，注意=前后都必须有空格隔开



## case

```bash
case string in 
re pattern)
	command list;;
re pattern)
	commandd list;;
esac
```

- case用来进行字符串的匹配
- re pattern是正则表达式，后边必须跟上)。
- 如果正则表达式匹配上了，则执行后边的命令，命令最后以两个分后结束
- 如果不同的正则表达式对应于同一组command list，则用|隔开，表示或的关系

```bash
 case 语句的通配符及多个模式组合实例
 [whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ cat 1
a=$1
echo $1
case $a in
[Dd]ate) echo "the date is `date`";;
dir|pwd|path) echo "pwd is `pwd`";;
esac
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ sh 1 date
date
the date is Sun Jul 25 20:20:25 CST 2021
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ sh 1 dir
dir
pwd is /home/whr2190300211/shell_script
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ sh 1 3
3
```



```bash
编写一个 shell 脚本，根据键盘可以循环输入学生成绩（百分制），并显示对应的成绩标准（及格和不及格）按“q”键退出，按其他键提示重新输入。
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ cat 4
while echo "输入成绩：q退出"
do
read mark
if test $mark = "q"
then break
elif test $mark -ge 60
then echo "及格"
elif test $mark -lt 60
then echo "不及格"
else echo "未知"
fi
done
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ sh 4
输入成绩：q退出
11
不及格
输入成绩：q退出
100
及格
输入成绩：q退出
q
```







## for

```sh
for var [in params]
do
	command list
done
```

in params可选，有三种形式



### 显式指出

```bash
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ cat 1
for i in 1 2 3 a bc
do
echo $i
done
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ sh 1
1
2
3
a
bc
```



### 取某个目录下的所有文件名（进行匹配）

```bash
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ cat 2
for i in `ls /`
do
echo $i
done
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ sh 2
bin
boot
dev
etc
home
lib
lib64
lost+found
media
mnt
opt
proc
root
run
sbin
srv
sys
tmp
usr
var
```



###  为空

为空的时候参数取自位置参数

```bash
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ cat 3
for i
do
echo $i
done
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ sh 3 1 2 3 aaa
1
2
3
aaa
```



```bash
编写shell脚本，第一个位置参数为指定的目录,其后指定的位置参数为第一个位置参数指定目录下的文件，显示这些文件的内容 

先读取指定目录的所有文件，目录以位置参数给出。如果是文件，输出文件的内容，否则输出不是一个文件。
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ cat -n 1
     1	dir=$1
     2	echo "you enter $dir"
     3	if test -d $dir
     4	then 
     5		cd $dir
     6		echo "now in `pwd`"
     7		for file in `ls`
     8		do
     9			echo $file
    10			if test -f $file
    11			then 
    12				cat $file
    13				echo "---------------"
    14			else
    15				echo "$file not a readable file"
    16			fi
    17		done
    18	else
    19		echo "$dir not a dir"
    20	fi
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ ls ../
1.py    2.txt  manage.py   shell_script  test.txt
22.txt  3.txt  not_forget  test
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ sh 1 /home/whr2190300211/
you enter /home/whr2190300211/
now in /home/whr2190300211
1.py
import requests
from bs4 import BeautifulSoup as bs
url="https://www.biqooge.com/14_14051/"
base_url="https://www.biqooge.com"
#url="http://www.baidu.com"
request=requests.get(url)
request.encoding="GB2312"
soup=bs(request.text,features="lxml")
# < dd > < a href = "/14_14051/9026334.html" > 第1章地狱灵芝 < / a > < / dd >
dds=soup.find_all("dd")
for dd in dds[1:10]:
    a=dd.find("a")
    print(base_url+a.get("href"))
    print(a.text)import requests
from bs4 import BeautifulSoup as bs
url="https://www.biqooge.com/14_14051/9026334.html"
base_url="https://www.biqooge.com"
request=requests.get(url)
request.encoding="GB2312"
soup=bs(request.text,features="lxml")
# 标题
title=soup.find("h1").text
print(title)
# 内容
content="   "+soup.find("div",attrs={"id":"content"}).text
content=content.encode("gbk",errors="ignore")
content=content.decode("gbk")
content=content.replace("\n","\n    ")
print(content)
with open(title+".txt",'w') as f:
    f.write(content)---------------
22.txt
---------------
2.txt
this is a test for vim
now in insert mode
we can write in something
ok done

---------------
3.txt
---------------
manage.py
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning_log.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
---------------
not_forget
not_forget not a readable file
shell_script
shell_script not a readable file
test
test not a readable file
test.txt
---------------

然后再判断用户指定的文件名是不是一个文件，如果是，输出该文件的内容
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ ls -l
total 12
-rw-r--r-- 1 whr2190300211 root  267 Jul 25 23:17 1
-rw-r--r-- 1 whr2190300211 root  253 Jul 25 23:24 2
drwxr-xr-x 2 whr2190300211 root 4096 Jul 25 23:24 3
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ cat -n 2
     1	dir=$1;shift
     2	if test -d $dir
     3	then
     4		echo "$dir is a dir"
     5		for file
     6		do 
     7			if test -f $file
     8			then 
     9				echo "$dir$file is a file"
    10				cat $file
    11				echo "------------------"
    12			else
    13				echo "$file is not a file"
    14			fi	
    15		done
    16	else
    17		echo "$dir is not a dir"
    18	fi
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ sh 2 /home/whr2190300211/shell_script/ 1 3
/home/whr2190300211/shell_script/ is a dir
/home/whr2190300211/shell_script/1 is a file
dir=$1
echo "you enter $dir"
if test -d $dir
then 
	cd $dir
	echo "now in `pwd`"
	for file in `ls`
	do
		echo $file
		if test -f $file
		then 
			cat $file
			echo "---------------"
		else
			echo "$file not a readable file"
		fi
	done
else
	echo "$dir not a dir"
fi
------------------
3 is not a file
```



## while

```bash
while expression
do
	command list
done
```



```bash
编写程序，这段程序对各个给定的位置参数，首先判断其是否是普通文件，若是，则显示其内容；否则，显示它不是文件名的信息
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ cat -n 5
     1	for file
     2	do
     3		if [ -a $file ]
     4		then
     5			if [ -f $file ]
     6			then
     7				echo "$file is a file"
     8				cat $file
     9				echo "------------------"
    10			else
    11				echo "$file is not a file"
    12				echo "------------------"
    13			fi
    14		else 
    15			echo "$file not exists"
    16		fi
    17	done
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ sh 5 /root 1 2 3 4
/root is not a file
------------------
1 is a file
dir=$1
echo "you enter $dir"
if test -d $dir
then 
	cd $dir
	echo "now in `pwd`"
	for file in `ls`
	do
		echo $file
		if test -f $file
		then 
			cat $file
			echo "---------------"
		else
			echo "$file not a readable file"
		fi
	done
else
	echo "$dir not a dir"
fi
------------------
2 is a file
dir=$1;shift
if test -d $dir
then
	echo "$dir is a dir"
	for file
	do 
		if test -f $file
		then 
			echo "$dir$file is a file"
			cat $file
			echo "------------------"
		else
			echo "$file is not a file"
		fi	
	done
else
	echo "$dir is not a dir"
fi
------------------
3 is not a file
------------------
4 is a file
dir=$1
if [ -a $dir ]
then echo "exists"
fi
------------------

```



```bash
利用while循环输出0到10之间的整数
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ cat -n 6
     1	data="0"
     2	while [ $data -le 10 ]
     3	do
     4		echo $data
     5		let data=data+1
     6	done
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ sh 6
0
1
2
3
4
5
6
7
8
9
10
```



### break

从循环体中跳出来

```bash
用while和break输出1-10之间的整数。
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ cat -n 7
     1	data=0
     2	while true
     3	do
     4		if [ $data -gt 10 ]
     5		then break
     6		fi
     7		echo $data
     8		let data=data+1
     9	done
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ sh 7
0
1
2
3
4
5
6
7
8
9
10
```



### continue

```bash
输入一组数，输出除了值为3的所有数。
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ cat 8
for i
do
	if [ $i -eq 3 ]
	then continue
	fi
	echo $i
done
[whr2190300211@iZm5e98zphj5y525q4v5k4Z shell_script]$ sh 8 3 4 3 54
5
```



# 自定义函数

```bash
function()
{
	command list
}
```

先定义函数，调用时直接使用函数名进行调用

