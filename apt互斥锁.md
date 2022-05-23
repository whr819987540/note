apt互斥锁

```bash
E:Could not get lock /var/lib/apt/lists/lock - open (11: Resource temporarily unavailable)

ps -e | grep apt
kill -9pid
```



