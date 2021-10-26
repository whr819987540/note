系统迁移

# 系统文件打包



```bash
cd /root/
tar --numeric-owner --exclude=/proc --exclude=/sys -cvf centos7-base.tar /
```



# scp上传文件到另一台服务器

```bash
scp 本机文件路径 另一台服务器的用户名@另一台服务器ip:复制到哪个路径
scp -Cp /root/centos7-base.tar root@47.113.179.166:/root
-C压缩
-p保留原文件的时间戳
-r递归复制文件夹
之后需要输入另一台服务器root用户的密码
```

如果比较慢不想等，可以去看看`fg-bg-nohup-disown.md`里面有详细的后台运行方法。



# 另一台服务器安装docker

```bash
curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun
```



# 将镜像导入到docker images

```bash
cat centos7-base.tar | docker import - centos7-mini2
docker images
```



# 运行系统容器

```bash
docker run -itd --name os7.6 centos7-mini2:latest /bin/bash
docker ps
docker exec os7.6 cat /etc/redhat-release
docker exec os7.6 ifconfig
```

