- python获取字典内的某个值

  - dict.get(key)
  - 如果不存在这个key，返回None

- pandas中将数据类型转化为字典

  - 将dataframe转化为字典，dataframe.to_dict()
    - orient='dict'，格式为{column:{row:value}}
  - 将series转化为字典，series.to_dict()
    - 格式为{index:value}

- python第三方库安装

  - 在线安装
    - pip install xx
  - 离线安装
    - python setup.py install
    - pip install xx.whl

- pandas的map、apply、applymap

  - 区别在于应用的对象不同

- 增加一行

  - df.loc[index,:]
  - df.append()
    - ignore_index
      - true，重新设置index
      - false，拷贝原index
  - df.concat()

- 增加一列

  - df[column]
  - df.loc[:,column]

- series.value_counts()

  - 统计series中出现过的值的频率

    ![image-20220406231419839](https://gitee.com/hit_whr/pic_2.0/raw/main/image-20220406231419839.png)

- jupyter notebook显示所有数据

  ```python
  pd.set_option('display.max_columns', None)  # 设置最大显示列数的多少
  pd.set_option('display.width', 1000)  # 设置宽度,就是说不换行,比较好看数据
  pd.set_option('display.max_rows', None)  # 设置行数的多少
  ```

  

series的最大值、最小值

series.max()

series.min()

skipna



