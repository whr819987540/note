import os
import re

OLD_PATHS = ["gitee.com/hit_whr/pic_2.0/raw/main",
             "gitee.com/hit_whr/pic_3.0/raw/master/img",
             "gitee.com/hit_whr/pic_3.0/raw/master/img"
             "gitee.com/hit_whr/picgo/raw/master"]

NEW_PATH = "raw.githubusercontent.com/whr819987540/pic/main"


def modify_md_content(top):
    for root, dirs, files in os.walk(top):
        for file_name in files:
            if file_name.endswith(".md"):
                try:
                    md_file_path = root + file_name
                    # 打开md文件然后进行替换
                    with open(md_file_path, 'r', encoding='utf8') as fr:
                        readlines = fr.readlines()

                    with open(md_file_path, 'w', encoding='utf8') as f:
                        for line in readlines:
                            for OLD_PATH in OLD_PATHS:
                                line_new = re.sub(OLD_PATH, NEW_PATH, line)
                            f.write(line_new)

                    print(f'{md_file_path} done...')
                except Exception as e:
                    print(e)

        # 递归处理子目录
        for dir in dirs:
            modify_md_content(root+f'{dir}\\')


modify_md_content('C:\\Users\\user\\Desktop\\note\\')
