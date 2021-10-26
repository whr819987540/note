```bash
apt install -y vsftpd
systemctl enable vsftpd.service
systemctl start vsftpd.service
adduser ftpuser
# passwd=ftp123456
mkdir -p /var/ftp/ftpuser
chown -R ftpuser:ftpuser /var/ftp/ftpuser
# 修改配置文件
vim /etc/vsftpd.conf
```



