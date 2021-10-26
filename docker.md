一键安装脚本

```bash
curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun
```



# 安装

## 更新yum包

`yum update`

## 卸载旧版本

`yum -y remove docker-ce docker-ce-cli containerd.io`

ce即为community engine

cli表示客户端

io是容器的镜像



## 设置yum源

`yum install -y yum-utils device-mapper-persistent-data lvm2`

`yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo`

阿里源的镜像

`yum list docker-ce --showduplicates | sort -r`

查看可安装的docker版本



## 阿里云镜像加速

防止下载镜像太过缓慢

![image-20210623204844863](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210623204844863.png)



## 安装

`yum install -y docker-ce`

![image-20210623204917994](https://gitee.com/hit_whr/pic_2.0/raw/master/5Nel6xwIW3zvsLt.png)



## 启动docker

类似于开启一个windows的服务

`systemctl start docker`

![image-20211025231743507](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20211025231743507.png)



![image-20211025231757855](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20211025231757855.png)

## 帮助文档

https://docs.docker.com/reference/

# docker镜像

## 查看本机的所有镜像

docker images

![image-20211025231809301](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20211025231809301.png)

docker images --help

-a将所有的镜像都显示出来

-q只显示镜像的id

## 搜索镜像

要寻找某个镜像，可以去docker hub上搜索并下载

![image-20211025231817881](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20211025231817881.png)



![image-20210623205758468](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210623205758468.png)





![image-20210623205817215](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210623205817215.png)

也可以用docker search来进行搜索，结果是一样的

![image-20210623205847503](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210623205847503.png)



对于比较冷门的镜像，过滤掉

docker search xxx -f=condition

![image-20210623210110822](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210623210110822.png)

## 下载镜像

docker pull 镜像名[:tag]

tag（版本）是可选的，如果不加，默认最新（latest）版本

也就是default tag（latest）

![image-20210623210328623](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210623210328623.png)



下载的时候出现了多个下载项和id，这是docker的镜像采用分层下载，节省带宽和资源占用，进行文件共享。

下面查找存在的mysql镜像版本，比如5.7，然后进行下载

![image-20210623210554605](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210623210554605.png)

docker pull mysql:5.7

![image-20210623233504475](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20211025231950496.png)



## 镜像的存储位置

可以用`docker info`查看相关的配置，比如image的默认存储位置

 ![image-20211025231950496](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20211025231950496.png)

```bash
[root@iZm5e98zphj5y525q4v5k4Z ~]# cd /var/lib/docker/
[root@iZm5e98zphj5y525q4v5k4Z docker]# ls
buildkit  containers  image  network  overlay2  plugins  runtimes  swarm  tmp  trust  volumes
[root@iZm5e98zphj5y525q4v5k4Z docker]# cd image
[root@iZm5e98zphj5y525q4v5k4Z image]# ls
overlay2
[root@iZm5e98zphj5y525q4v5k4Z image]# find -name /var/lib/docker/ mysql
find: warning: Unix filenames usually don't contain slashes (though pathnames do).  That means that '-name ‘/var/lib/docker/’' will probably evaluate to false all the time on this system.  You might find the '-wholename' test more useful, or perhaps '-samefile'.  Alternatively, if you are using GNU grep, you could use 'find ... -print0 | grep -FzZ ‘/var/lib/docker/’'.
find: paths must precede expression: mysql
Usage: find [-H] [-L] [-P] [-Olevel] [-D help|tree|search|stat|rates|opt|exec] [path...] [expression]
[root@iZm5e98zphj5y525q4v5k4Z image]# find /var/lib/docker/ -name mysql
/var/lib/docker/overlay2/827a9a120bc0e4a56aff72feb0255250c54bc6c0ddcb72e8715dfc7446026b60/diff/usr/bin/mysql
/var/lib/docker/overlay2/827a9a120bc0e4a56aff72feb0255250c54bc6c0ddcb72e8715dfc7446026b60/diff/usr/lib/mysql
/var/lib/docker/overlay2/827a9a120bc0e4a56aff72feb0255250c54bc6c0ddcb72e8715dfc7446026b60/diff/etc/mysql
/var/lib/docker/overlay2/827a9a120bc0e4a56aff72feb0255250c54bc6c0ddcb72e8715dfc7446026b60/diff/var/lib/mysql
/var/lib/docker/overlay2/457fd84819c3d802631384b09b5fdb9cd726fdb62f5af6b44629111e6eacc9b4/diff/usr/share/mysql
/var/lib/docker/overlay2/457fd84819c3d802631384b09b5fdb9cd726fdb62f5af6b44629111e6eacc9b4/diff/usr/bin/mysql
/var/lib/docker/overlay2/457fd84819c3d802631384b09b5fdb9cd726fdb62f5af6b44629111e6eacc9b4/diff/usr/lib/mysql
/var/lib/docker/overlay2/457fd84819c3d802631384b09b5fdb9cd726fdb62f5af6b44629111e6eacc9b4/diff/etc/init.d/mysql
/var/lib/docker/overlay2/457fd84819c3d802631384b09b5fdb9cd726fdb62f5af6b44629111e6eacc9b4/diff/etc/mysql
/var/lib/docker/overlay2/457fd84819c3d802631384b09b5fdb9cd726fdb62f5af6b44629111e6eacc9b4/diff/var/log/mysql
/var/lib/docker/overlay2/457fd84819c3d802631384b09b5fdb9cd726fdb62f5af6b44629111e6eacc9b4/diff/var/lib/mysql
/var/lib/docker/overlay2/71a04aa313d3ea99452a8d8765766a8819f6a4e0b1b750d3680915103e87eb15/diff/etc/mysql
[root@iZm5e98zphj5y525q4v5k4Z image]# pwd
/var/lib/docker/image
[root@iZm5e98zphj5y525q4v5k4Z image]# ls
overlay2
[root@iZm5e98zphj5y525q4v5k4Z image]# cd overlay2/
[root@iZm5e98zphj5y525q4v5k4Z overlay2]# ls
distribution  imagedb  layerdb  repositories.json
[root@iZm5e98zphj5y525q4v5k4Z overlay2]# ls -al
total 24
drwx------ 5 root root 4096 Jun 23 21:06 .
drwx------ 3 root root 4096 Jun 23 20:49 ..
drwx------ 4 root root 4096 Jun 23 21:02 distribution
drwx------ 4 root root 4096 Jun 23 20:49 imagedb
drwx------ 4 root root 4096 Jun 23 21:02 layerdb
-rw------- 1 root root  511 Jun 23 21:06 repositories.json

```



## 查看所有的镜像

因为上面看存储位置，看到的其实也只是一堆小文件（分层传送），所以直接看镜像吧。

`docker images -a`

![image-20210623234124003](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210623234124003.png)

repository是镜像对应的仓库名称（docker hub）

tag是版本号，image id是对镜像的标识

`docker images -aq`

显示所有镜像的id

![image-20211025232022863](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20211025232022863.png)



## 卸载镜像

根据镜像id删除对应的镜像

`docker rmi -f image_id image_id`

![image-20210623234550964](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210623234550964.png)

下载的时候是分层下载，删除的时候同样如此，并不是全部删除（mysql:latest的依赖还在里面）

删除后，就只有最新的mysql了

![image-20210623234645346](https://i.loli.net/2021/06/23/o6E84uptmjONiTW.png)

而镜像的id可以根据`docker images -aq`来进行查询，所以删除所有的镜像

`docker rmi $(docker images -aq)`

![image-20210623234724884](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210623234724884.png)

删除后没有镜像了

![image-20211026184832435](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20211026184832435.png)



# docker容器

这里用一个centos的镜像来做测试

`docker search centos`

![image-20210623235046930](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210623235046930.png)



`docker pull centos:7 `

![image-20210623235230217](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210623235230217.png)



## 根据镜像创建容器

`docker run [选项] image_name[:tag] command`

如果不指定tag，则默认为latest

command比如bash，ssh等等

![image-20211026184900862](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20211026184900862.png)



## 启动容器

有点诧异

![image-20211026184910338](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20211026184910338.png)

-i是说交互模式

![image-20210624000053509](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210624000053509.png)

但只是-i似乎不行

还得-it

![image-20211026184930857](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20211026184930857.png)

tty是与i/o有关的一个东西



进入后，就像开启了一个新的系统一样，只不过命令不是那么充分

![image-20210624000547209](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210624000547209.png)



## -d

-d是detach分离，将容器在后台运行，但如果容器没有前台进程，这个容器会自己docker kill掉

```bash
[root@iZm5e98zphj5y525q4v5k4Z ~]# docker run -d centos:7 /bin/bash --name="back_centos"
60526787dd1d763adb9ceedcd0c97706daa7cefef505e873dbebf4e08b60cc8e
[root@iZm5e98zphj5y525q4v5k4Z ~]# docker ps -a
CONTAINER ID   IMAGE      COMMAND                  CREATED          STATUS                     PORTS     NAMES
60526787dd1d   centos:7   "/bin/bash --name=ba…"   4 seconds ago    Exited (2) 3 seconds ago             wonderful_leakey
43adb17d06de   nginx      "/docker-entrypoint.…"   22 minutes ago   Up 7 minutes               80/tcp    nginx
```



## -v

-v是将容器内的某个



## -p

-p 服务器的端口:容器的端口

进行端口映射。

如果有多个-p选项，就是进行多个端口的映射。

```bash
[root@whr ~]# docker images
REPOSITORY            TAG       IMAGE ID       CREATED        SIZE
20210827/python3      1.0       e6e028e98b1d   35 hours ago   982MB
819987540/python3.6   v1        f9c67e0d4dcc   37 hours ago   936MB
python3.6             v1        f9c67e0d4dcc   37 hours ago   936MB
ubuntu                18.04     39a8cfeef173   4 weeks ago    63.1MB
[root@whr ~]# docker run -itd --name test_port -p 8001:8001 -p 8002:8002 ubuntu:18.04 /bin/bash
cffc9f0535f95557443978318983cc1af2b1c995d9d357fcf0503f7f0e22e1b5
[root@whr ~]# docker ps -a
CONTAINER ID   IMAGE                  COMMAND       CREATED          STATUS                        PORTS                              NAMES
cffc9f0535f9   ubuntu:18.04           "/bin/bash"   3 seconds ago    Up 2 seconds                  0.0.0.0:8001-8002->8001-8002/tcp   test_port
1b2c37397f6f   ubuntu:18.04           "/bin/bash"   13 minutes ago   Exited (0) 9 minutes ago                                         ubuntu
e71cf569f9df   20210827/python3:1.0   "/bin/bash"   34 hours ago     Exited (137) 15 minutes ago      
```







## 退出容器（-it打开）

exit是直接退出，此时容器也会被stop

ctrl+pq是后台运行

![image-20211026184953184](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20211026184953184.png)





## 查看容器的状态

![image-20210624000800075](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210624000800075.png)

容器id

使用的镜像

用什么命令启动

status值得注意，由于刚才是ctrl+pq退出的，所以这个容器还在运行->up

ports：容器和公网是隔离的，如果要通信，首先服务器和公网通信，然后服务器和容器通过一个端口通信，就好像容器和公网直接通信。

names可以指定



现在看看有没有其他的status

![image-20210624001407020](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210624001407020.png)

刚才创建的container已经没了

查看当前正在运行的容器和历史上运行过的容器

`docker ps -a `

![image-20210624001531747](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210624001531747.png)

只显示容器id

`docker ps -aq `

![image-20210624001723292](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210624001723292.png)



如果历史上创建的容器太多了，利用-n进行数目的筛选

![image-20210624001946955](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210624001946955.png)

可以看出来，无论是-a，-aq，-aq -n=，都是根据created time来排序的



## 查看相应镜像的所有容器

docker ps --filter ancestor=

- image[:tag]  ==如果不指定tag，默认为latest==
- image id

```bash
[root@iZm5e98zphj5y525q4v5k4Z ~]# docker ps --filter ancestor=nginx
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS     NAMES
43adb17d06de   nginx     "/docker-entrypoint.…"   27 minutes ago   Up 12 minutes   80/tcp    nginx
[root@iZm5e98zphj5y525q4v5k4Z ~]# docker ps --filter ancestor=centos
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
[root@iZm5e98zphj5y525q4v5k4Z ~]# docker ps --filter ancestor=centos -a
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
[root@iZm5e98zphj5y525q4v5k4Z ~]# docker ps --filter ancestor=centos:7 -a
CONTAINER ID   IMAGE      COMMAND                  CREATED         STATUS                     PORTS     NAMES
60526787dd1d   centos:7   "/bin/bash --name=ba…"   5 minutes ago   Exited (2) 5 minutes ago             wonderful_leakey

```



## 删除容器

根据容器id来删除容器

`docker rm [-f] container_id`

![image-20210624002158350](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210624002158350.png)



如果是正在运行的（up）需要-f强制删除

报错说，==不能删除正在运行的容器，要么把容器停了，要么强制删除==

![image-20210624002324383](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210624002324383.png)

删除全部容器

`docker rm -f $(docker ps -aq)`

![image-20210624002506632](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210624002506632.png)



## 容器保存

### 将容器保存为镜像

docker commit container_id/name image_name:image:tag



### 保存在远程仓库

#### 登录到dockerhub

docker login -puser_name

然后输入密码

#### 将镜像发布到dockerhub

发布到dockerhub需要将docker镜像的名称修改一下，修改为user_name/image_name:image_tag

```bash
docker tag image_id/image_name:tag new_image_name:tag

docker tag image_id/image_name:tag new_image_name:tag
docker push 
```



### 将镜像打包为tar文件

将镜像打包为tar文件，主要用于内网，（网络不好，访问dockerhub比较慢，也可以构建私人仓库）。

```bash
docker save -o image_name/id:tag file_name.tar
```



### tar文件加载为镜像

```bash
docker load -i file_
```



# 日志

docker logs option container_id



```bash
[root@ca39e3df0cd5 /]# [root@iZm5e98zphj5y525q4v5k4Z ~]# docker logs --help

Usage:  docker logs [OPTIONS] CONTAINER

Fetch the logs of a container

Options:
      --details        Show extra details provided to logs
  -f, --follow         Follow log output
  对日志的输出进行实时更新
  [root@iZm5e98zphj5y525q4v5k4Z ~]# docker ps -a
CONTAINER ID   IMAGE      COMMAND                  CREATED             STATUS             PORTS     NAMES
ca39e3df0cd5   centos:7   "/bin/bash"              About an hour ago   Up About an hour             test_exited
43adb17d06de   nginx      "/docker-entrypoint.…"   2 hours ago         Up 2 hours         80/tcp    nginx
[root@iZm5e98zphj5y525q4v5k4Z ~]# docker logs --follow ca39e3df0cd5
[root@ca39e3df0cd5 /]# ls
anaconda-post.log  bin  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
[root@ca39e3df0cd5 /]# p     
bash: p: command not found
[root@ca39e3df0cd5 /]# ps
  PID TTY          TIME CMD
    1 pts/0    00:00:00 bash
   17 pts/0    00:00:00 ps
[root@ca39e3df0cd5 /]# d^H^H
d
^C
[root@iZm5e98zphj5y525q4v5k4Z ~]#
可以看到在显示日志后，并不会马上停止显示日志，因为root的标识为ca39e3df0cd5，而不是iZm5e98zphj5y525q4v5k4Z
  
  
  
      --since string   Show logs since timestamp (e.g. 2013-01-02T13:23:37Z) or relative (e.g. 42m for 42 minutes)
  -n, --tail string    Number of lines to show from the end of the logs (default "all")
  -n 数字从日志的末尾往上数，来n行日志记录
[root@iZm5e98zphj5y525q4v5k4Z ~]# docker logs ca39e3df0cd5
[root@ca39e3df0cd5 /]# ls
anaconda-post.log  bin  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
[root@ca39e3df0cd5 /]# p     
bash: p: command not found
[root@ca39e3df0cd5 /]# ps
  PID TTY          TIME CMD
    1 pts/0    00:00:00 bash
   17 pts/0    00:00:00 ps
[root@ca39e3df0cd5 /]# [root@iZm5e98zphj5y525q4v5k4Z ~]# docker logs -n 5 ca39e3df0cd5
第一行：[root@ca39e3df0cd5 /]# ps
第二行：  PID TTY          TIME CMD
第三行：    1 pts/0    00:00:00 bash
第四行：   17 pts/0    00:00:00 ps
第五行：[root@ca39e3df0cd5 /]#



  -t, --timestamps     Show timestamps
[root@iZm5e98zphj5y525q4v5k4Z ~]# docker logs -t ca39e3df0cd5
2021-07-12T14:11:42.123901735Z [root@ca39e3df0cd5 /]# ls
2021-07-12T14:11:42.129214461Z anaconda-post.log  bin  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
2021-07-12T14:11:51.191831942Z [root@ca39e3df0cd5 /]# p     
2021-07-12T14:11:51.194244827Z bash: p: command not found
2021-07-12T14:11:52.312255741Z [root@ca39e3df0cd5 /]# ps
2021-07-12T14:11:52.357539136Z   PID TTY          TIME CMD
2021-07-12T14:11:52.357588735Z     1 pts/0    00:00:00 bash
2021-07-12T14:11:52.357595034Z    17 pts/0    00:00:00 ps
2021-07-12T14:12:42.025072304Z [root@ca39e3df0cd5 /]#


      --until string   Show logs before a timestamp (e.g. 2013-01-02T13:23:37Z) or relative (e.g. 42m for 42 minutes)
```



# 查看容器的元数据

docker inspect 



## 启动，停止，重启

启动`docker start container_id`

停止 `docker stop container_id`

重启 `docker restart container_id`

强制停止 `docker kill container_id`

### 启动(重新进入容器)

![image-20210624002959800](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210624002959800.png)

那么问题来了：如何以交互模式进入容器？

`docker exec -it container_id command`

这个命令的前提是这个container必须是up状态，也就是必须在运行

```bash
[root@iZm5e98zphj5y525q4v5k4Z ~]# docker ps -a
CONTAINER ID   IMAGE      COMMAND                  CREATED          STATUS                       PORTS     NAMES
ca39e3df0cd5   centos:7   "/bin/bash"              3 minutes ago    Exited (137) 2 minutes ago             test_exited
43adb17d06de   nginx      "/docker-entrypoint.…"   50 minutes ago   Up 36 minutes                80/tcp    nginx
[root@iZm5e98zphj5y525q4v5k4Z ~]# docker start ca39e3df0cd5
ca39e3df0cd5
[root@iZm5e98zphj5y525q4v5k4Z ~]# docker ps -a
CONTAINER ID   IMAGE      COMMAND                  CREATED          STATUS          PORTS     NAMES
ca39e3df0cd5   centos:7   "/bin/bash"              3 minutes ago    Up 1 second               test_exited
43adb17d06de   nginx      "/docker-entrypoint.…"   51 minutes ago   Up 36 minutes   80/tcp    nginx
[root@iZm5e98zphj5y525q4v5k4Z ~]# docker exec -it ca39e3df0cd5 /bin/bash
[root@ca39e3df0cd5 /]# ls
anaconda-post.log  bin  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
```



![image-20210624003321769](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210624003321769.png)



### 停止

![image-20210624003626205](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210624003626205.png)



停止所有的容器

`docker stop $(docker ps -aq)`

![image-20210624004438823](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210624004438823.png)



### exit code

137

```bash
Any of these events result in a 137 status:
the init process of the container is killed manually
容器的初始进程被手动kill了（在服务器层面杀进程）
kill -9 process_id


docker kill kills the container
容器被手动kill了
docker kill container_id
[root@iZm5e98zphj5y525q4v5k4Z ~]# docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS         PORTS     NAMES
43adb17d06de   nginx     "/docker-entrypoint.…"   11 minutes ago   Up 2 minutes   80/tcp    nginx
[root@iZm5e98zphj5y525q4v5k4Z ~]# docker kill 43adb17d06de
43adb17d06de
[root@iZm5e98zphj5y525q4v5k4Z ~]# docker ps -a
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS                       PORTS     NAMES
43adb17d06de   nginx     "/docker-entrypoint.…"   12 minutes ago   Exited (137) 7 seconds ago             nginx

Docker daemon restarts which kills all running containers
手动重启容器
docker restart container_id

```



2。没有前台进程退出

```bash
[root@iZm5e98zphj5y525q4v5k4Z ~]# docker run -d centos:7 /bin/bash --name="back_centos"
60526787dd1d763adb9ceedcd0c97706daa7cefef505e873dbebf4e08b60cc8e
[root@iZm5e98zphj5y525q4v5k4Z ~]# docker ps -a
CONTAINER ID   IMAGE      COMMAND                  CREATED          STATUS                     PORTS     NAMES
60526787dd1d   centos:7   "/bin/bash --name=ba…"   4 seconds ago    Exited (2) 3 seconds ago             wonderful_leakey
43adb17d06de   nginx      "/docker-entrypoint.…"   22 minutes ago   Up 7 minutes               80/tcp    nginx


```



### 重启



### 强制关闭



### 后台启动



### 后台日志



### 容器进程

`docker top container_id`

根据容器id来查看容器内的进程信息





## 给容器改名

![image-20210624003403271](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210624003403271.png)

这种name不具备实际含义，所以进行改名

![image-20210624003524119](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210624003524119.png)



# 数据交换

## 将容器内的数据复制到服务器上

`docker cp container_id:path path`

![image-20210624004227032](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210624004227032.png)



## 将服务器的数据复制到容器里

docker cp path container_id/name:path



## 目录挂载



## 数据卷

# 容器外执行容器内的命令



docker exec option container_id/name command args

option中，-d是后台运行命令，-t分配一个为终端

一般用-d或者-it

command是在容器内用什么来执行命令，比如/bin/bash，args是执行文件。

如果是很多命令，建议把命令写到一个脚本中，然后用/bin/bash执行该脚本。

# 实例

docker安装nginx

```bash
#搜索镜像
[root@iZm5e98zphj5y525q4v5k4Z test]# docker search nginx
NAME                               DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
nginx                              Official build of Nginx.                        15051     [OK]       
jwilder/nginx-proxy                Automated Nginx reverse proxy for docker con…   2039                 [OK]
#安装镜像
[root@iZm5e98zphj5y525q4v5k4Z test]# docker pull nginx
Using default tag: latest
latest: Pulling from library/nginx
b4d181a07f80: Already exists 
edb81c9bc1f5: Pull complete 
b21fed559b9f: Pull complete 
03e6a2452751: Pull complete 
b82f7f888feb: Pull complete 
5430e98eba64: Pull complete 
Digest: sha256:47ae43cdfc7064d28800bc42e79a429540c7c80168e8c8952778c0d5af1c09db
Status: Downloaded newer image for nginx:latest
docker.io/library/nginx:latest
#查看镜像
[root@iZm5e98zphj5y525q4v5k4Z test]# docker images
REPOSITORY   TAG       IMAGE ID       CREATED        SIZE
nginx        latest    4f380adfc10f   10 hours ago   133MB
mysql        latest    5c62e459e087   10 hours ago   556MB
centos       7         8652b9f0cb4c   7 months ago   204MB
#运行一个容器
[root@iZm5e98zphj5y525q4v5k4Z test]# docker run -it nginx /bin/bash
root@3fd04066a9c0:/# ls
bin   dev		   docker-entrypoint.sh  home  lib64  mnt  proc  run   srv  tmp  var
boot  docker-entrypoint.d  etc			 lib   media  opt  root  sbin  sys  usr
root@3fd04066a9c0:/# nginx
2021/06/23 16:48:14 [notice] 8#8: using the "epoll" event method
2021/06/23 16:48:14 [notice] 8#8: nginx/1.21.0
2021/06/23 16:48:14 [notice] 8#8: built by gcc 8.3.0 (Debian 8.3.0-6) 
2021/06/23 16:48:14 [notice] 8#8: OS: Linux 3.10.0-957.21.3.el7.x86_64
2021/06/23 16:48:14 [notice] 8#8: getrlimit(RLIMIT_NOFILE): 1048576:1048576
root@3fd04066a9c0:/# 2021/06/23 16:48:14 [notice] 9#9: start worker processes
2021/06/23 16:48:14 [notice] 9#9: start worker process 10
#退出，查看容器的状态
exit
[root@iZm5e98zphj5y525q4v5k4Z test]# docker ps -a
CONTAINER ID   IMAGE      COMMAND                  CREATED          STATUS                       PORTS     NAMES
3fd04066a9c0   nginx      "/docker-entrypoint.…"   54 seconds ago   Exited (0) 25 seconds ago              friendly_ride
5d7642c3a13d   centos:7   "/bin/bash"              21 minutes ago   Exited (137) 4 minutes ago             my_centos
02f8ae1edaaa   centos:7   "/bin/bash"              21 minutes ago   Exited (0) 21 minutes ago              suspicious_jepsen
35a9abf67902   centos:7   "/bin/bash"              21 minutes ago   Exited (137) 4 minutes ago             elegant_mirzakhani
#运行
[root@iZm5e98zphj5y525q4v5k4Z test]# docker ps -a
CONTAINER ID   IMAGE      COMMAND                  CREATED          STATUS                       PORTS     NAMES
3fd04066a9c0   nginx      "/docker-entrypoint.…"   4 minutes ago    Exited (0) 3 minutes ago               friendly_ride
5d7642c3a13d   centos:7   "/bin/bash"              24 minutes ago   Exited (137) 8 minutes ago             my_centos
02f8ae1edaaa   centos:7   "/bin/bash"              24 minutes ago   Exited (0) 24 minutes ago              suspicious_jepsen
35a9abf67902   centos:7   "/bin/bash"              24 minutes ago   Exited (137) 8 minutes ago             elegant_mirzakhani
[root@iZm5e98zphj5y525q4v5k4Z test]# docker start 3fd04066a9c0
3fd04066a9c0
[root@iZm5e98zphj5y525q4v5k4Z test]# docker ps -a
CONTAINER ID   IMAGE      COMMAND                  CREATED          STATUS                       PORTS     NAMES
3fd04066a9c0   nginx      "/docker-entrypoint.…"   4 minutes ago    Up 2 seconds                 80/tcp    friendly_ride
5d7642c3a13d   centos:7   "/bin/bash"              25 minutes ago   Exited (137) 8 minutes ago             my_centos
02f8ae1edaaa   centos:7   "/bin/bash"              25 minutes ago   Exited (0) 25 minutes ago              suspicious_jepsen
35a9abf67902   centos:7   "/bin/bash"              25 minutes ago   Exited (137) 8 minutes ago             elegant_mirzakhani

```



# 内网搭建docker私人仓库

这个主要是提高docker hub的下载速度，同时也是为了安全。



# 常用镜像

```python
# 基于Debian的python3.6，自制镜像
docker pull 819987540/python3.6:tag
    
   
```

