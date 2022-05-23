git服务器版

# 配置文件

和win平台上一样，配置文件分为三层

- 仓库级

  对本仓库有效的配置文件

  工作目录的.git/config文件。该配置只对当前仓库有效

  利用git config 进行修改

- 用户级

  对当前登录用户有效的配置文件

  ~/.gitconfig

  利用git config --global进行修改

- 系统级

  对本机上所有用户都有效

  /etc/gitconfig文件

  利用git config --system

  

  利用git config --system/global --list/key_name

  > 有一点值得注意，在linux下，项目文件中，.git文件自动被隐藏了，如果要查看，使用list -a

  与win平台不同，linux下git的配置文件如此简洁

  ![image-20210318224201362](https://raw.githubusercontent.com/whr819987540/pic/main/image-20210318224201362.png)



# 工作流

  

  git有三个区域：

  > - **工作区：**working directory，就是你在电脑里能看到的目录。
  > - **暂存区：**英文叫 stage 或 index。一般存放在 **.git** 目录下的 index 文件（.git/index）中，所以我们把暂存区有时也叫作索引（index）。
  > - **版本库：**工作区有一个隐藏目录 **.git**，这个不算工作区，而是 Git 的版本库。

  ![image-20210318224416943](https://raw.githubusercontent.com/whr819987540/pic/main/image-20210318224416943.png)

  

  ![image-20210318224521435](https://raw.githubusercontent.com/whr819987540/pic/main/image-20210318224521435.png)

  



# clone：远程仓库到本地仓库

> git clone [options] [--] <repo> [<dir>]

将远程仓库repo（url）克隆到当前目录，并默认根据远程仓库名指定本地仓库名，可以用dir指定克隆到哪个目录，本地仓库名是什么。





# pull：远程仓库到工作区



# push：本地仓库到远程仓库