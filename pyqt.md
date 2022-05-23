# 将ui文件转成py文件

## 命令

```python
pyuic5 .ui -o .py
```



## 转换目录下的所有文件

```python
import os

for root,dir,file in os.walk('./'):
    for i in file:
        if i.endswith('ui'):
            path = root + i
            py_path = f'../{i.split(".")[0]}.py'
            print(f'pyuic5 {path} -o {py_path}')
            os.popen(f'pyuic5 {path} -o {py_path}')
```



# pyqt的表格

[Qt中让tableWidget内容中的每个元素居中（qtablewidget的一些使用） - ww学习笔记 - 博客园 (cnblogs.com)](https://www.cnblogs.com/wang--wei/p/11928234.html)



[(53条消息) PyQt5 tableWidget 居中显示_shiyue41的博客-CSDN博客_pyqt5 tablewidget 居中](https://blog.csdn.net/qq_27694835/article/details/111669093)



[(53条消息) PyQt5 QTableWidget（表单控件）自适应窗口大小、栏位大小调整及布局_独步天秤的博客-CSDN博客_qtablewidget设置大小](https://blog.csdn.net/yl_best/article/details/84070231)



[[ PyQt入门教程 \] PyQt5中数据表格控件QTableWidget使用方法 - 锅边糊 - 博客园 (cnblogs.com)](https://www.cnblogs.com/linyfeng/p/11832237.html)



[Qtablewidget操作,设置表头,填充内容,删除行,获取行内其它元素 - Aloe_n - 博客园 (cnblogs.com)](https://www.cnblogs.com/aloe-n/p/8721590.html)



[(53条消息) PyQt5中动态设置QTableWidget表格添加数据，并且设置表格的行高，列宽_水月灯花的博客-CSDN博客_pyqt5 tablewidget 添加数据](https://blog.csdn.net/u014535666/article/details/104750373)

这里的QT是指`from PyQt5 import QtCore` `QtCore.Qt.AlignCenter`

```python
- 在显示数据之前，要设置行数和列数
self.log_list.setRowCount(len(log_info))
self.log_list.setColumnCount(len(headers))
- 显示行标题
self.log_list.setHorizontalHeaderLabels(headers)
# 设置单元格根据内容进行拉伸
self.log_list.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
# 设置最后一列自动拉伸
self.log_list.horizontalHeader().setStretchLastSection(True)
```

