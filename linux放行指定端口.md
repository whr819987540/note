linux放行指定端口



# 查看防火墙状态

```bash
firewall-cmd --state
```

# 查看某个端口是否放行

```bash
firewall-cmd --query-port=端口号/tcp
```

# 放行指定端口

```bash
firewall-cmd --zone=public --add-port=8080/tcp --permanent
```

# 重启防火墙

```bash
systemctl restart firewalld.service
```

# 重新载入配置

```bash
firewall-cmd --reload
```

