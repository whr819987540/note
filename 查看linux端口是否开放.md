端口是否开放

```bash
lsof -i:port
netstat -aptu | grep port
-t tcp
-u udp
-p display pid
```

