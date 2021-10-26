# redis配置文件

## 查看redis服务的相关信息

```bash
systemctl status redis
[root@whr etc]# systemctl status redis
● redis.service - Redis persistent key-value database
   Loaded: loaded (/usr/lib/systemd/system/redis.service; disabled; vendor preset: disabled)
  Drop-In: /etc/systemd/system/redis.service.d
           └─limit.conf
   Active: inactive (dead)
```





## 查看reids-server的路径、当前redis服务加载配置文件的位置

```bash
cat /usr/lib/systemd/system/redis.server
[root@whr etc]# cat /usr/lib/systemd/system/redis.service
[Unit]
Description=Redis persistent key-value database
After=network.target
After=network-online.target
Wants=network-online.target

[Service]
ExecStart=/usr/bin/redis-server /etc/redis.conf --supervised systemd
ExecStop=/usr/libexec/redis-shutdown
Type=notify
User=redis
Group=redis
RuntimeDirectory=redis
RuntimeDirectoryMode=0755

[Install]
WantedBy=multi-user.target
```

可以看到，redis-server的路径是/usr/bin/redis-server。加载的配置文件在/etc/redis.conf。



## 重启redis，指定配置文件



