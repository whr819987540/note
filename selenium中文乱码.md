# 创建中文字体目录
mkdir -p /usr/share/fonts/chinese/

# 将字体文件拷贝到中文字体目录中
cp songti.ttf /usr/share/fonts/chinese/

cd /usr/share/fonts/chinese/

# 为刚加入的字体设置缓存使之有效
fc-cache -fv

# 查看系统中的字体
fc-list