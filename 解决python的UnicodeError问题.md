解决python的UnicodeError问题

```bash
apt-get install -y locales
# 生成本地的字符集
locale-gen en_US.UTF-8
# 这里选择en_US即可，选择4,3
dpkg-reconfigure locales
# 查看本地的字符集
cat /etc/default/locale
```

