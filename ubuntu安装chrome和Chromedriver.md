ubuntu安装chrome和Chromedriver

# chrome

[chrome的历史版本](https://www.ubuntuupdates.org/package/google_chrome/stable/main/base/google-chrome-stable)

```bash
cd root && wget https://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_94.0.4606.54-1_amd64.deb
# 依赖
apt install fonts-liberation libasound2 libatk-bridge2.0-0 libatspi2.0-0 libgbm1 libgtk-3-0 libxkbcommon0 xdg-utils 
dpkg -i google-chrome-stable_94.0.4606.54-1_amd64.deb && rm google-chrome-stable_94.0.4606.54-1_amd64.deb
google-chrome -V
```



# 版本关系

chrome和chromedriver的版本号命名方式相同，二者的主版本号、次要版本号、内部版本号需要相同：` major, minor, and build version numbers. For example, ChromeDriver 73.0.3683.20 supports all Chrome versions that start with 73.0.3683.`



# chromedriver

```bash
sudo apt update -y && sudo apt-get install -y libxss1 libappindicator1 libindicator7 xvfb unzip libnss3

cd /root && wget https://chromedriver.storage.googleapis.com/94.0.4606.41/chromedriver_linux64.zip && unzip chromedriver_linux64.zip && rm chromedriver_linux64.zip
 && chmod +x chromedriver

sudo mv -f chromedriver /usr/local/share/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
chromedriver -V
```



# demo

```python
from selenium import webdriver
from datetime import datetime
import time

# 配置
options = webdriver.ChromeOptions()
options.add_argument('window-size=1920x1080')  # 窗口分辨率
options.add_argument('--disable-gpu')  # 禁用gpu
options.add_argument('--headless')  # 不开启可视化界面
options.add_argument('--no-sandbox')  # 最高权限

driver = webdriver.Chrome(options=options)
url = "http://www.baidu.com/"

driver.get(url)
print(driver.get_cookies())

now_time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
# 截图之前需要等待一段时间，让浏览器渲染出图片
time.sleep(2)
driver.get_screenshot_as_file(f'{now_time}.png')
driver.quit()

```



