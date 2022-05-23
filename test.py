import re

OLD_PATH_1 = "gitee.com/hit_whr/pic_2.0/raw/main"
OLD_PATH_2 = "gitee.com/hit_whr/pic_2.0/raw/master"
NEW_PATH = "raw.githubusercontent.com/whr819987540/pic/main"

line = "![image-20210904121758844](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20210904121758844.png)"


line_new = re.sub(OLD_PATH_1, NEW_PATH, line)
line_new = re.sub(OLD_PATH_2, NEW_PATH, line_new)
print(line_new)

