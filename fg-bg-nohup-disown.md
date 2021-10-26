前台、后台、nohup、disown

# 解释

## 前台

前台就是程序在shell里面运行，输入输出都放到shell里面。此时用户只能看着程序运行，而不能做别的事情。

如果当前的shell关闭了，那么shell下属的所有进程都被杀死。

比如用scp传文件。无论是前台运行还是后台运行，一旦退出当前的shell，所有的进程都结束了。‘



## 后台

如果要后台运行，需要在运行command后台加上 &，之后，可以在shell里面做别的事情、



## nohup/不挂起

无论前台、后台，一旦退出shell，开启的进程都挂了。nohup一般需要将输出重定向到一个文件。





# 切换

先开启一个任务

![image-20210829165945843](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210829165945843.png)

ctrl+z，stop这个前台任务，并放到后台，处于暂停状态。



## jobs -l

查看当前shell正在执行的任务。

![image-20210829170112157](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210829170112157.png)

[1]即为任务的num



## fg %num 切换到前台

![image-20210829170221329](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210829170221329.png)



## bg %num切换到后台

![image-20210829170302557](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210829170302557.png)



## 问题

一个关键的问题是，如果启动了一个进程，运行很久后，还没结束。

但现在必须得退出终端了，如何保证程序能在退出后继续执行？（现在再将程序挂起显然不显示，得重新执行）

### disown

这个命令让进程忽略退出终端时HUP信号的影响，即使这个进程已经在运行了。

- 用disown -h jobspec来使某个作业忽略HUP信号。
- 用disown -ah 来使所有的作业都忽略HUP信号。
- 用disown -rh 来使正在运行的作业忽略HUP信号。

```bash
[root@whr ~]# jobs -l
[1]+ 20741 Running                 scp -Cp /root/centos7-base.tar root@47.113.179.166:/root &
[root@whr ~]# disown -h %1
[root@whr ~]# jobs -l
[1]+ 20741 Running                 scp -Cp /root/centos7-base.tar root@47.113.179.166:/root &
[root@whr ~]# ps -aux|grep scp
root     20741  0.1  0.1 175976  2800 pts/0    S    16:59   0:01 scp -Cp /root/centos7-base.tar root@47.113.179.166:/root
root     20742  7.9  0.4 182200  7588 pts/0    S    16:59   1:02 /usr/bin/ssh -x -oForwardAgent=no -oPermitLocalCommand=no -oClearAllForwardings=yes -C -l root -- 47.113.179.166 scp -p -t /root
root     21419  0.0  0.0 112812   972 pts/0    R+   17:12   0:00 grep --color=auto scp
```



现在先退出终端。

![image-20210829172032553](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210829172032553.png)



![image-20210829172045963](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210829172045963.png)

数据还在传输，这个进程确实忽略了HUP信号，在后台运行。