# ubuntu安装go

```bash
wget https://golang.google.cn/dl/go1.18.linux-amd64.tar.gz
tar -xzf go1.18.linux-amd64.tar.gz -C /usr/local/bin
vim /etc/profile
export GOPATH=/root/go
export GOROOT=/usr/local/go
export PATH=$PATH:/usr/local/go/bin
source /etc/profile

go env -w GOPROXY=https://proxy.golang.com.cn,direct
```

