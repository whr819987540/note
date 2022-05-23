# 用virtualenv创建python的虚拟环境

```bash
pip3 install virtualenv
find / -name virtualenv
# 为virtualenv创建软链接
ln -s xxx /usr/local/bin/virtualenv
# 创建虚拟环境
virtualenv [-p python interpreter path] test_env
# 如果要带上系统的库
virtualenv --system-site-packages env_name
# 进入虚拟环境
cd test_env
# 激活虚拟环境
source bin/activate
# 退出虚拟环境
deactivate
```



# 报错，提示没有某个文件

```bash
# pip3 list查看安装的库时报错
# https://blog.csdn.net/p1279030826/article/details/111573774
# File "/usr/local/python3/lib/python3.8/subprocess.py", line 516, in run
#    raise CalledProcessError(retcode, process.args,
# subprocess.CalledProcessError: Command '('lsb_release', '-a')' returned non-zero exit status 1.
# 缺少某个文件
# 首先查找该文件
find / -name 'lsb_release.py'
/usr/lib/python2.7/dist-packages/lsb_release.py
/usr/lib/python3/dist-packages/lsb_release.py
/usr/share/pyshared/lsb_release.py
# 然后将该文件复制到报错的目录下
cp /usr/lib/python3/dist-packages/lsb_release.py /usr/local/python3/lib/python3.8/
```

