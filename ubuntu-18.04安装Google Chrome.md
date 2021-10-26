ubuntu(18.04)下安装chrome driver

# 安装Google Chrome

```bash
apt update
apt -y upgrade
apt-get update
apt install -y build-essential lsof wget vim zlib* libffi-dev
apt-get install -y libxss1 libappindicator1 libindicator7 fonts-liberation libcurl3 xvfb unzip libgconf-2-4 manpages-dev
cd /home
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
dpkg -i google-chrome*.deb
apt-get install google-chrome-stable
apt --fix-broken install -y
dpkg -i google-chrome*.deb
```



# 安装ChromeDriver(版本可能会更新)

https://chromedriver.storage.googleapis.com/index.html?path=93.0.4577.15/

```bash
wget https://chromedriver.storage.googleapis.com/93.0.4577.15/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
mv -f chromedriver /usr/local/share/chromedriver
ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
```



# 安装python3及依赖

```bash
cd /usr/local/src
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



```python
oss2==2.15.0
pydantic==1.8.2
requests==2.26.0
uvicorn==0.14.0
beautifulsoup4==4.9.3
fastapi==0.68.1
Pillow==8.3.1
html5lib==1.0.1
lxml==4.2.1
selenium==3.141.0
pydantic=1.8.2
```



# 运行测试

pythth3 /home/test.py

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

