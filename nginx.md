```bash
root@whr:~/webmail# nginx -s reopen
nginx: [error] invalid PID number "" in "/run/nginx.pid"
root@whr:~/webmail# cat /run/nginx.pid
root@whr:~/webmail# rm /run/nginx.pid 
root@whr:~/webmail# nginx -s reload
nginx: [error] open() "/run/nginx.pid" failed (2: No such file or directory)
root@whr:~/webmail# nginx -s reopen
nginx: [error] open() "/run/nginx.pid" failed (2: No such file or directory)
# 指定配置文件的路径
root@whr:~/webmail# nginx -c etc/nginx/nginx.conf
nginx: [emerg] open() "/usr/share/nginx/etc/nginx/nginx.conf" failed (2: No such file or directory)
root@whr:~/webmail# nginx -c /etc/nginx/nginx.conf
root@whr:~/webmail# nginx -s reopen
root@whr:~/webmail# lsof -i:80
COMMAND   PID     USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
nginx   53641     root    6u  IPv4 205387      0t0  TCP *:http (LISTEN)
nginx   53641     root    7u  IPv6 205388      0t0  TCP *:http (LISTEN)
nginx   53642 www-data    6u  IPv4 205387      0t0  TCP *:http (LISTEN)
nginx   53642 www-data    7u  IPv6 205388      0t0  TCP *:http (LISTEN)

```

