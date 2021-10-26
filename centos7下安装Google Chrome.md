centos7安装chrome driver

# 安装Google Chrome

安装到/usr/bin/下面

```bash
yum update -y
yum 
yum install -y wget unzip glib2 
cd /usr/local/src/
wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
yum install -y google-chrome-stable_current_x86_64.rpm
ln -s /usr/bin/google-chrome /usr/bin/chrome
ln -s /usr/bin/google-chrome /usr/local/bin/chrome
```



# 下载对应的chrome driver

https://chromedriver.chromium.org/downloads

```bash
cd /usr/local/src/
wget https://chromedriver.storage.googleapis.com/93.0.4577.15/chromedriver_linux64.zip
unzip chromedriver_linux64.zip -d /usr/bin/
```



# python3

```bash
yum -y install gcc automake autoconf libtool make
yum install -y gcc gcc-c++
cd /usr/local/src
yum install -y zlib* libffi-dev
wget https://www.python.org/ftp/python/3.6.8/Python-3.6.8.tgz
tar -zxf Python-3.6.8.tgz
mv Python-3.6.8 ../
cd ../Python-3.6.8
./configure --prefix=/usr/local
make && make install
ln -s /usr/local/bin/python3.6 /usr/bin/python3
ln -s /usr/local/bin/pip3 /usr/bin/pip
export LANG="en_US.UTF-8"
source /etc/profile

pip install scipy -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com
pip config set global.index-url http://mirrors.aliyun.com/pypi/simple
pip config set install.trusted-host mirrors.aliyun.com
pip install --upgrade pip
pip install -r requirements.txt
```



# 测试

cd /home/

python3 /home/test.py

```python
#coding=utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_opt = Options()  # 创建参数设置对象.
chrome_opt.add_argument('--headless')  # 无界面化.
chrome_opt.add_argument('--disable-gpu')  # 配合上面的无界面化.
chrome_opt.add_argument('--window-size=1366,768')  # 设置窗口大小, 窗口大小会有影响.
chrome_opt.add_argument("--no-sandbox") #使用沙盒模式运行
# 创建Chrome对象并传入设置信息.
browser = webdriver.Chrome(chrome_options=chrome_opt)
url = "https://www.baidu.com/"
browser.get(url)
print(browser.page_source)
browser.quit()
```

