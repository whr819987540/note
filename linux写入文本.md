# linux写入文本

## 单行文本

### 覆盖

echo content > filename

```bash
root@ubuntu:~# echo 11 > 1.txt
root@ubuntu:~# cat 1.txt 
11
root@ubuntu:~# echo 22 > 1.txt
root@ubuntu:~# cat 1.txt 
22
```



### 追加

```bash
root@ubuntu:~# cat 1.txt 
22
root@ubuntu:~# echo 33 >> 1.txt 
root@ubuntu:~# cat 1.txt 
22
33
```



## 多行文本

### 覆盖

```bash
root@ubuntu:~# cat 1.txt 
22
33
root@ubuntu:~# cat >1.txt<<EOF
> 44
> 55
> EOF
root@ubuntu:~# cat 1.txt 
44
55
```

