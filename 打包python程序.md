```bash
# 安装python的pyinstaller模块
pip install pyinstaller
# 以管理员身份进入cmd窗口，然后进入代码的src目录
pyinstaller 
-F 打包成单文件 
-p python安装路径即python.exe所在目录(环境变量查看或者cmd窗口，where python查看)
C:\Users\user\Desktop\数据库课设\src>where python
C:\Users\user\AppData\Local\Programs\Python\Python36\python.exe
main.py(入口函数)

# 完整命令
C:\Users\user\Desktop\数据库课设\src>pyinstaller -F -p C:\Users\user\AppData\Local\Programs\Python\Python36 main.py
```
