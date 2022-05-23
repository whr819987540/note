# ubuntu将原始python3.5升级为高版本

```bash
# ubuntu将原始python3.5升级为高版本
apt update
apt-get install -y zlib1g-dev libbz2-dev libssl-dev libncurses5-dev libsqlite3-dev libreadline-dev tk-dev libgdbm-dev libdb-dev libpcap-dev xz-utils libexpat1-dev liblzma-dev libffi-dev libc6-dev
apt install -y wget
wget https://www.python.org/ftp/python/3.8.8/Python-3.8.8.tgz
tar -xzf Python-3.8.8.tgz
cd Python-3.8.8
./configure --prefix=/usr/local/python3  --enable-optimizations
make && make install
# rm -rf /usr/bin/python3
# rm -rf /usr/bin/pip3
ln -s /usr/local/python3/bin/python3.8 /usr/bin/python38
ln -s /usr/local/python3/bin/pip3.8 /usr/bin/pip38
python38 -V
pip38 -V
pip38 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```



# 第二步安装依赖可能太慢，更换ubuntu仓库

```bash
# 换源
# 首先备份一下源文件
cp /etc/apt/sources.list /etc/apt/sources.list.bak
rm /etc/apt/sources.list
vim /etc/apt/sources.list
```



```bash
# /etc/apt/sources.list
deb http://mirrors.aliyun.com/ubuntu/ xenial main
deb-src http://mirrors.aliyun.com/ubuntu/ xenial main
deb http://mirrors.aliyun.com/ubuntu/ xenial-updates main
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-updates main
deb http://mirrors.aliyun.com/ubuntu/ xenial universe
deb-src http://mirrors.aliyun.com/ubuntu/ xenial universe
deb http://mirrors.aliyun.com/ubuntu/ xenial-updates universe
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-updates universe
deb http://mirrors.aliyun.com/ubuntu/ xenial-security main
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-security main
deb http://mirrors.aliyun.com/ubuntu/ xenial-security universe
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-security universe

deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial main restricted universe multiverse
deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-updates main restricted universe multiverse
deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse
deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-security main restricted universe multiverse
deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-security main restricted universe multiverse

```



```bash
apt-get update
apt-get -f install
```

