nginx静态资源

注意将include的部分注释掉

root是指资源的根目录，必须是`\path\`格式的绝对路径。

index是指访问的url为`domain_name:port\`格式时，返回的资源。

error page error_no route_path;

指明了某个error_no匹配的路由

```bash
server{
    listen 80;
    server_name localhost;
	# 错误号为404 403 500 502 503 504时，匹配'/'
    error_page  404 403 500 502 503 504  /;
    location / {
        root /var/www/html/;
        index index.html;
    }

    # error page
    # error_page 500 502 503 504 506 /50x.html;
    # location = /50x.html{
    # 	root html;
    # }
}
```



服务器无法用ip访问

- 查看阿里云的安全组规则，看是否放心了80端口
- 检查iptables，`iptables -I INPUT -p tcp --dport 80 -j ACCEPT`放行80端口
- 上述两个防火墙都需要检查