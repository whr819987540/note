win ubantu

```bash
安装镜像

docker pull dorowu/ubuntu-desktop-lxde-vnc

运行镜像

C:\Users\user>docker run -p 6080:80 -p 5900:5900 -e VNC_PASSWORD='123456' -v /dev/shm:/dev/shm dorowu/ubuntu-desktop-lxde-vnc
docker: Error response from daemon: Ports are not available: listen tcp 0.0.0.0:5900: bind: An attempt was made to access a socket in a way forbidden by its access permissions.

端口没开
查看哪些端口被禁用了
C:\Users\user>netsh interface ipv4 show excludedportrange protocol=tcp

协议 tcp 端口排除范围

开始端口    结束端口
----------    --------
      5041        5140
      5141        5240
      5241        5340
      5392        5491
      5492        5591
      5592        5691
      5772        5871
      5872        5971
      5972        6071
     50000       50059     *

* - 管理的端口排除。
浏览器
C:\Users\user>docker run -p 3000:80 -p 3001:3001 -e VNC_PASSWORD=123456 -v /dev/shm:/dev/shm dorowu/ubuntu-desktop-lxde-vnc
stored passwd in file: /.password2
2021-07-24 04:15:16,401 CRIT Supervisor is running as root.  Privileges were not dropped because no user is specified in the config file.  If you intend to run as root, you can set user=root in the config file to avoid this message.
2021-07-24 04:15:16,401 INFO Included extra file "/etc/supervisor/conf.d/supervisord.conf" during parsing
2021-07-24 04:15:16,405 INFO RPC interface 'supervisor' initialized
2021-07-24 04:15:16,405 CRIT Server 'unix_http_server' running without any HTTP authentication checking
2021-07-24 04:15:16,405 INFO supervisord started with pid 16
2021-07-24 04:15:17,408 INFO spawned: 'nginx' with pid 18
2021-07-24 04:15:17,409 INFO spawned: 'web' with pid 19
2021-07-24 04:15:17,410 INFO spawned: 'xvfb' with pid 20
2021-07-24 04:15:17,411 INFO spawned: 'wm' with pid 21
2021-07-24 04:15:17,412 INFO spawned: 'lxpanel' with pid 22
2021-07-24 04:15:17,414 INFO spawned: 'pcmanfm' with pid 23
2021-07-24 04:15:17,415 INFO spawned: 'x11vnc' with pid 24
2021-07-24 04:15:17,416 INFO spawned: 'novnc' with pid 25
2021-07-24 04:15:17,558 INFO  Listening on http://localhost:6079 (run.py:87)
2021-07-24 04:15:18,432 INFO success: nginx entered RUNNING state, process has stayed up for > than 1 seconds (startsecs)

Get-AppxPackage -AllUsers|Foreach {Add-AppxPackage-DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}
```

Get-AppxPackage -AllUsers|Foreach {Add-AppxPackage-DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}

