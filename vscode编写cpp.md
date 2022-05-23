vscode编写cpp



一开始没有隐藏文件，即没有配置文件

![image-20211108224248278](https://raw.githubusercontent.com/whr819987540/pic/main/image-20211108224248278.png)

# 生成配置文件

## cpp_properties

点击查看->命令面板，输入edit configurations（UI）

![](https://raw.githubusercontent.com/whr819987540/pic/main/image-20211108224355645.png)



注意一定要选对编译器的路径和编译器的类型。

对于编译器的路径，首先应该放到系统环境变量中，并且PATH中只能由一个编译器的路径，。

如果修改了PATH，应该重启vscode

![image-20211109153757990](https://raw.githubusercontent.com/whr819987540/pic/main/image-20211109153757990.png)

![image-20211108224422265](https://raw.githubusercontent.com/whr819987540/pic/main/image-20211108224422265.png)

```bash
{
    "configurations": [
        {
            "name": "Win32",
            "includePath": [
                "${workspaceFolder}/**"
            ],
            "defines": [
                "_DEBUG",
                "UNICODE",
                "_UNICODE"
            ],
            "windowsSdkVersion": "10.0.22000.0",
            "compilerPath": "C:/Program Files/mingw-w64/x86_64-8.1.0-posix-seh-rt_v6-rev0/mingw64/bin/g++.exe",
            "cStandard": "c17",
            "cppStandard": "c++17",
            "intelliSenseMode": "windows-gcc-x64"
        }
    ],
    "version": 4
}
```



## tasks.json

tasks.json这个配置文件里面放的是如何编译的信息，产生该文件后可以编译文件（run code)

输入configure default built task 

![image-20211108224537053](https://raw.githubusercontent.com/whr819987540/pic/main/image-20211108224537053.png)



然后选择g++编译器

![image-20211108224657024](https://raw.githubusercontent.com/whr819987540/pic/main/image-20211108224657024.png)



![image-20211108224710514](https://raw.githubusercontent.com/whr819987540/pic/main/image-20211108224710514.png)

```cpp
{
    "version": "2.0.0",
    "tasks": [
        {
            "type": "cppbuild",
            "label": "C/C++: g++.exe 生成活动文件",
            "command": "C:/Program Files/mingw-w64/x86_64-8.1.0-posix-seh-rt_v6-rev0/mingw64/bin/g++.exe",
            "args": [
                "-fdiagnostics-color=always",
                "-g",
                "${file}",
                "-o",
                "${fileDirname}\\${fileBasenameNoExtension}.exe"
            ],
            "options": {
                "cwd": "C:/Program Files/mingw-w64/x86_64-8.1.0-posix-seh-rt_v6-rev0/mingw64/bin"
            },
            "problemMatcher": [
                "$gcc"
            ],
            "group": "build",
            "detail": "编译器: \"C:/Program Files/mingw-w64/x86_64-8.1.0-posix-seh-rt_v6-rev0/mingw64/bin/g++.exe\""
        },
        {
            "type": "cppbuild",
            "label": "C/C++: g++.exe 生成活动文件 ver(1)",
            "command": "C:/Program Files/mingw-w64/x86_64-8.1.0-posix-seh-rt_v6-rev0/mingw64/bin/g++.exe",
            "args": [
                "-fdiagnostics-color=always",
                "-g",
                "${file}",
                "-o",
                "${fileDirname}\\${fileBasenameNoExtension}.exe"
            ],
            "options": {
                "cwd": "C:/Program Files/mingw-w64/x86_64-8.1.0-posix-seh-rt_v6-rev0/mingw64/bin"
            },
            "problemMatcher": [
                "$gcc"
            ],
            "group": "build",
            "detail": "调试器生成的任务。"
        },
        {
            "type": "cppbuild",
            "label": "C/C++: g++.exe 生成活动文件 ver(2)",
            "command": "C:/Program Files/mingw-w64/x86_64-8.1.0-posix-seh-rt_v6-rev0/mingw64/bin/g++.exe",
            "args": [
                "-fdiagnostics-color=always",
                "-g",
                "${file}",
                "-o",
                "${fileDirname}\\${fileBasenameNoExtension}.exe"
            ],
            "options": {
                "cwd": "C:/Program Files/mingw-w64/x86_64-8.1.0-posix-seh-rt_v6-rev0/mingw64/bin"
            },
            "problemMatcher": [
                "$gcc"
            ],
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "detail": "调试器生成的任务。"
        }
    ]
}
```



## launch.json（路径中不能有中文）

  这个配置文件里面放的是如何进行调试的信息。

![image-20211109162111931](https://raw.githubusercontent.com/whr819987540/pic/main/image-20211109162111931.png)



选择GDB调试

![image-20211109162247442](https://raw.githubusercontent.com/whr819987540/pic/main/image-20211109162247442.png)

![image-20211109162328612](https://raw.githubusercontent.com/whr819987540/pic/main/image-20211109162328612.png)



```bash
{
    // 使用 IntelliSense 了解相关属性。 
    // 悬停以查看现有属性的描述。
    // 欲了解更多信息，请访问: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "g++.exe - 生成和调试活动文件",
            "type": "cppdbg",
            "request": "launch",
            "program": "${fileDirname}\\${fileBasenameNoExtension}.exe",
            "args": [],
            "stopAtEntry": false,
            "cwd": "C:/Program Files/mingw-w64/x86_64-8.1.0-posix-seh-rt_v6-rev0/mingw64/bin",
            "environment": [],
            "externalConsole": false,
            "MIMode": "gdb",
            "miDebuggerPath": "C:\\Program Files\\mingw-w64\\x86_64-8.1.0-posix-seh-rt_v6-rev0\\mingw64\\bin\\gdb.exe",
            "setupCommands": [
                {
                    "description": "为 gdb 启用整齐打印",
                    "text": "-enable-pretty-printing",
                    "ignoreFailures": true
                }
            ],
            "preLaunchTask": "C/C++: g++.exe 生成活动文件"
        }
    ]
}
```

