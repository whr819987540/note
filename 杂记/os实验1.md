要求：

- 各个实验程序的流程图
- 运行结果截图
- 分析运行结果
- 提交源代码、exe、实验报告
- 学号+姓名命名
- 程序的可读性好，要有注释；测试数据和结果
- 每个实验单独打印实验报告，左侧装订



至少完成前四个实验，要检查实验结果

附加实验根据质量给予加分



# 实验1

- 创建进程，CreateProcess()
- 结束进程
  - 正常退出，ExitProcess()
  - 强行终止，TerminateProcess()



```cpp
typedef wchar_t WCHAR;    // wc,   16-bit UNICODE character
一个字长度的字符
typedef WCHAR TCHAR, *PTCHAR;
#define MAX_PATH          260
```

