qt的菜单里面，不能直接输入中文，但可以进行拷贝，然后进行显示

在action editor区域点击一个选项，可以设置选项的名称，图标（资源文件），快捷键



菜单下面是工具栏（快捷菜单）

001：猜数

输入一个数，按下猜数按钮，把数传进去，比较，进行信息提示

知识点：

- 随机数生成
- 槽pushbutton
- 改变label的文本

002：菜单栏

在最上方显示菜单栏

对选项进行转到槽，控制label的输出

- 选项可以生成快捷键



003：比较冒泡排序和快速排序的时间

输入：数字的个数，输出，冒泡或者快速排序的用时







![image-20210320192533333](https://raw.githubusercontent.com/whr819987540/pic/main/image-20210320192533333.png)

![image-20210320192740678](https://raw.githubusercontent.com/whr819987540/pic/main/image-20210320192740678.png)

冒泡排序和快速排序的结果差别（100000个数据）

![image-20210320200601956](https://raw.githubusercontent.com/whr819987540/pic/main/image-20210320200601956.png)

![image-20210320200625764](https://raw.githubusercontent.com/whr819987540/pic/main/image-20210320200625764.png)



![image-20210320200659502](https://raw.githubusercontent.com/whr819987540/pic/main/image-20210320200659502.png)











在qt里面，类的命名尽量首字母大写，不然qt认为这和构造函数产生了二义性



undefined reference是说，这个函数找不到定义，一看，原来是给lineEdit设置了槽函数（不想要的），又没有删除，所以只有声明，没有定义，产生了报错。

E:\qt\build-003-Desktop_Qt_5_9_9_MinGW_32bit-Debug\debug\moc_mainwindow.cpp:81: error: undefined reference to `MainWindow::on_lineEdit_cursorPositionChanged(int, int)'







coding过程：

先在命令行界面下调试程序（必须用类来封装），去年用c&&qt开发，属实痛苦。

用类封装好后，再放到qt里面调试。（必须把功能实现好，把接口写标准）

此时在qt里面，关键是研究业务逻辑（用户会怎样点击，怎样输入，然后程序应该按照怎样的顺序来执行。



005：

绘图(QPainter)，键盘响应(QKeyEvent），计时器（QDebug，QTimeEvent），

（#include < QObject >)

Qwidget，用于绘图，键盘响应

经过这个开发，越来越发现熟悉框架的重要

不过对于qt，了解就好，毕竟不会是以后常用的框架



006：

qt中的光标自动聚焦到某个位置（组件）

listwidget加内容时ui->listwidget->additem()

而ui->listwidget->item(row)->settext(s)是对第row行（从0开始）进行内容上的修改





007：

信息：学号+姓名，分列显示（table widget）

add，增加信息，先在文本框中输入一组信息，然后add，会检查学号是否重复

mod，修改，点击任意一个条款，文本框中显示当前内容，进行修改，条件：不与除本记录之外的任何记录中的id重复

del，删除，删除所选记录，当记录数为0时，显示空行（qt不允许删除完）

sort，先清空表格里面的数据（clear），然后显示表头，最后将排序好的数据，按照下标的顺序放进去



008:

先得到了一个词典，然后将这个词典逐个读入到listwidget中（构造函数）

对lineedit的词进行检索

如果找到了，返回一行的内容（正则）

没找到，返回提示信息 



子串匹配

```cpp
QString test(QString s)
{
    int index=s.indexOf(" ");
    QString tmp=s.mid(0,index);
    return tmp;
}
void Dialog::on_pushButton_clicked()
{
    QString target=ui->lineEdit->text();
    QString current;
    int i;
    for( i=0;i<n;i++){
        current=ui->listWidget->item(i)->text();
        if(target==test(current))
        {
            ui->lineEdit_2->setText(current);
            ui->listWidget->setCurrentRow(i);
            break;
        }
    }
    if(i==n)
        ui->lineEdit_2->setText("not found");
}

```