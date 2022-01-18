vscode ssh连接服务器

# 下载remote-ssh扩展

![image-20211106223603041](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20211106223603041.png)



# 配置扩展

![image-20211106224319158](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20211106224319158.png)



第一行是别名，第二行是ip，第三行是用户名

![image-20211106224430150](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20211106224430150.png)

# 本地生成rsa秘钥

用`ssh-keygen`命令生成rsa秘钥

![image-20211106223708161](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20211106223708161.png)

进入上面的路径后

![image-20211106223921002](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20211106223921002.png)

id_rsa.pub是rsa对应的公钥，需要上传到指定服务器的指定用户。

比如最终要以root登录47.105.91.99，就将公钥放到root的家目录/root/.shh/下面，然后`cat id_rsa.pub >> authorized_keys`将公钥放到认证秘钥文件中。



# 最后

配置好上面的东西后，就可以无密码直接登录

记得重新开一个终端，直接进行linux命令行操作