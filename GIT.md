# **GIT**

作者是Linus

local vcs

将对文件作出的所有修改同步到本地的数据库中，相当于生成了本地的log

One of the most popular VCS tools was a system called RCS, which is still distributed with many computers today. [RCS](https://www.gnu.org/software/rcs/) works by keeping patch sets (that is, the differences between files) in a special format on disk; it can then re-create what any file looked like at any point in time by adding up all the patches.

记住修改，然后把修改整合起来，形成新的文件，即version

![image-20210315214126340](https://gitee.com/hit_whr/picgo/raw/master/image-20210315214126340.png)

有个问题，无法协作

所以有了centralized VCS

![image-20210315214451431](https://gitee.com/hit_whr/picgo/raw/master/image-20210315214451431.png)



可以协作了，方便管理

easier to administer a CVCS than it is to deal with local databases on every client.

缺点是服务器可能存在的单点故障，毕竟主机上只有部分file，无法形成整个versions

snapshot快照[(1 封私信 / 78 条消息) 快照与备份有什么区别？快照是备份的其中一种么？还是两种不同的概念？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/20374919/answer/499376887)

快照原理，将当前虚拟机的虚拟硬盘文件锁定，不再更改，之后新建一个文件，之后所有更改都放到新建的文件中，读取时，优先读取这个中的，没有的话在读取锁定中的数据。所以快照占的空间取决于你做了多少更改

![image-20210315220117757](https://gitee.com/hit_whr/picgo/raw/master/image-20210315221709978.png)



clients don’t just check out the latest snapshot of the files; rather, they fully mirror the repository, including its full history. Thus, if any server dies, and these systems were collaborating via that server, any of the client repositories can be copied back up to the server to restore it. Every clone is really a full backup of all the data.

简单来说就是，任何客户端都不只是存储需要的部分文件了，而是取回服务器里的所有内容。当服务出问题时，任何客户端的存储内容都可以返回至服务器。这就是分布式结构，增强容灾能力，但是也增加了总的存储量。

For most of the lifetime of the Linux kernel maintenance (1991–2002), changes to the software were passed around as patches and archived files. In 2002, the Linux kernel project began using a proprietary DVCS called BitKeeper.



GIT和之前的vcs的区别

The major difference between Git and any other VCS (Subversion and friends included) is the way Git thinks about its data. Conceptually, most other systems store information as a list of file-based changes. These other systems (CVS, Subversion, Perforce, Bazaar, and so on) think of the information they store as a set of files and the changes made to each file over time (this is commonly described as *delta-based* version control).

基于增量进行复制，如果project中的某个文件改变了，ok，是一次改变，对project进行重新复制，成为另一个version。做了很多无用的工作

![image-20210315221709978](https://gitee.com/hit_whr/picgo/raw/master/image-20210315220117757.png)



Git doesn’t think of or store its data this way. Instead, Git thinks of its data more like a series of snapshots of a miniature filesystem. With Git, every time you commit, or save the state of your project, Git basically takes a picture of what all your files look like at that moment and stores a reference to that snapshot. To be efficient, if files have not changed, Git doesn’t store the file again, just a link to the previous identical file it has already stored. Git thinks about its data more like a **stream of snapshots**.

如果文件没有发生改变，Git不会再存储一遍，只会告诉你一个reference，指向之前那个一模一样的文件

![image-20210315221846368](https://gitee.com/hit_whr/picgo/raw/master/areas.png)

另一个好处是，不用频繁去找服务器取数据，project就在本地，直接修改；并且，如果断网了，因为本地有文件，所以还可以工作。

Most operations in Git need only local files and resources to operate — generally no information is needed from another computer on your network. If you’re used to a CVCS where most operations have that network latency overhead, this aspect of Git will make you think that the gods of speed have blessed Git with unworldly powers. Because you have the entire history of the project right there on your local disk, most operations seem almost instantaneous.

安全性

Everything in Git is checksummed before it is stored and is then referred to by that checksum. This means it’s impossible to change the contents of any file or directory without Git knowing about it. This functionality is built into Git at the lowest levels and is integral to its philosophy. You can’t lose information in transit or get file corruption without Git being able to detect it.

The mechanism that Git uses for this checksumming is called a SHA-1 hash. 

以至于在存储时，Git以hash值来命名而不是文件名

You will see these hash values all over the place in Git because it uses them so much. In fact, Git stores everything in its database not by file name but by the hash value of its contents.

When you do actions in Git, nearly all of them only *add* data to the Git database. It is hard to get the system to do anything that is not undoable or to make it erase data in any way. As with any VCS, you can lose or mess up changes you haven’t committed yet, but after you commit a snapshot into Git, it is very difficult to lose, especially if you regularly push your database to another repository.

This makes using Git a joy because we know we can experiment without the danger of severely screwing things up. For a more in-depth look at how Git stores its data and how you can recover data that seems lost, see [Undoing Things](https://git-scm.com/book/en/v2/ch00/_undoing).

Git的工作流程

Modified：在工作区working director被修改了

Staged：被修改后暂存staged在staging area，存的是索引

Committed：被提交到Git Directory

The Three States

Pay attention now — here is the main thing to remember about Git if you want the rest of your learning process to go smoothly. Git has three main states that your files can reside in: *modified*, *staged*, and *committed*:

- Modified means that you have changed the file but have not committed it to your database yet.
- Staged means that you have marked a modified file in its current version to go into your next commit snapshot.
- Committed means that the data is safely stored in your local database.

This leads us to the three main sections of a Git project: the working tree, the staging area, and the Git directory.

![Working tree, staging area, and Git directory.](https://gitee.com/hit_whr/picgo/raw/master/image-20210315221846368.png)

Figure 6. Working tree, staging area, and Git directory

The working tree is a single checkout of one version of the project. These files are pulled out of the compressed database in the Git directory and placed on disk for you to use or modify.

The staging area is a file, generally contained in your Git directory, that stores information about what will go into your next commit. Its technical name in Git parlance is the “index”, but the phrase “staging area” works just as well.

The Git directory is where Git stores the metadata and object database for your project. This is the most important part of Git, and it is what is copied when you *clone* a repository from another computer.

The basic Git workflow goes something like this:

1. You modify files in your working tree.
2. You selectively stage just those changes you want to be part of your next commit, which adds *only* those changes to the staging area.
3. You do a commit, which takes the files as they are in the staging area and stores that snapshot permanently to your Git directory.

If a particular version of a file is in the Git directory, it’s considered *committed*. If it has been modified and was added to the staging area, it is *staged*. And if it was changed since it was checked out but has not been staged, it is *modified*. In [Git Basics](https://git-scm.com/book/en/v2/ch00/ch02-git-basics-chapter), you’ll learn more about these states and how you can either take advantage of them or skip the staged part entirely.



命令行中的命令通常比图形界面的充足，毕竟图形界面是开发后的结果



![image-20210315224632407](https://gitee.com/hit_whr/picgo/raw/master/image-20210315224632407.png)

首先在英文中portable是便携的意思，那么在软件中也是一样，portable版表示软件不需要安装，只要双击就可以打开使用。避免了安装软件的麻烦，也可以让软件不住系统中写入过多的文件，达到干净、绿色的目的。

portable软件，通常采用了一些技术把需要的运行组件整合到一起，而不需要从系统中调用必要的组件，总之就是一个方便。大家可以把便携版的软件放在U盘、移动硬盘中随时使用。

把一些ddl写入程序中

最后终于在googlegroup一个偏僻的角落找到一个关于Git Portable的讨论（还是2008年的）。原来git-core底下的命令大都是硬连接，但是用Portable版本的话，7z不会保留连接，从而都创建成了一样的文件，所以占用了大量的空间。

大家都知道NTFS文件系统现在已经支持创建硬链接和符号链接，但是FAT不支持（大多数U盘都是FAT）。所以如果不是要在U盘上用，还是用安装器版本的好，它会根据当前的文件系统自动创建链接。



开始安装git

先看windows平台，一路下一步

C:\Program Files\Git\etc\gitconfig是全局配置文件

查看全局配置文件的内容

> git config --list

![image-20210316101203594](https://gitee.com/hit_whr/picgo/raw/master/image-20210316111200760.png)

查看配置文件的位置

> git config --list --show--origin





在linux下，git的配置文件放在三个文件中，对应三层权限

一个是对系统上的所有用户的所有存储库

一是在home目录中，对某个用户的所有存储库

最后是对某个特定的存储库

These variables can be stored in three different places:

1. `[path]/etc/gitconfig` file: Contains values applied to every user on the system and all their repositories. If you pass the option `--system` to `git config`, it reads and writes from this file specifically. Because this is a system configuration file, you would need administrative or superuser privilege to make changes to it.
2. `~/.gitconfig` or `~/.config/git/config` file: Values specific personally to you, the user. You can make Git read and write to this file specifically by passing the `--global` option, and this affects *all* of the repositories you work with on your system.
3. `config` file in the Git directory (that is, `.git/config`) of whatever repository you’re currently using: Specific to that single repository. You can force Git to read from and write to this file with the `--local` option, but that is in fact the default. Unsurprisingly, you need to be located somewhere in a Git repository for this option to work properly.

Each level ==overrides== values in the previous level, so values in `.git/config` ==trump== those in `[path]/etc/gitconfig`.

内级目录的优先级比外面的高，所以3>2>1



The first thing you should do when you install Git is to ==set your user name and email address==. This is important because every Git commit uses this information, and it’s immutably baked into the commits you start creating:

清楚文件位置后，开始使用

一开始需要新建一个本机的用户及对应的邮箱地址

> git config --global user.name ””
>
> git config --global user.email 

然后查看配置结果

> git config user.name

![image-20210316104824661](https://gitee.com/hit_whr/picgo/raw/master/image-20210316101203594.png)

一开始配置文件

> diff.astextplain.textconv=astextplain
> filter.lfs.clean=git-lfs clean -- %f
> filter.lfs.smudge=git-lfs smudge -- %f
> filter.lfs.process=git-lfs filter-process
> filter.lfs.required=true
> http.sslbackend=openssl
> http.sslcainfo=C:/Program Files/Git/mingw64/ssl/certs/ca-bundle.crt
> core.autocrlf=true
> core.fscache=true
> core.symlinks=false
> pull.rebase=false
> credential.helper=manager-core
> credential.https://dev.azure.com.usehttppath=true
> init.defaultbranch=master

修改后

> diff.astextplain.textconv=astextplain
> filter.lfs.clean=git-lfs clean -- %f
> filter.lfs.smudge=git-lfs smudge -- %f
> filter.lfs.process=git-lfs filter-process
> filter.lfs.required=true
> http.sslbackend=openssl
> http.sslcainfo=C:/Program Files/Git/mingw64/ssl/certs/ca-bundle.crt
> core.autocrlf=true
> core.fscache=true
> core.symlinks=false
> pull.rebase=false
> credential.helper=manager-core
> credential.https://dev.azure.com.usehttppath=true
> init.defaultbranch=master
> ==user.name=whr==
> ==user.email\=819987540@qq.com==

Again, you need to do this only once if you pass the `--global` option, because then Git will always use that information for anything you do on that system. If you want to override this with a different name or email address for specific projects, you can run the command without the `--global` option when you’re in that project.

加上--global是对所有project生效，如果只想对某个project生效，或者说生成3配置文件，不加global



更换git的编辑器，毕竟git bash确实丑了点

> git --global core.editor name(emacs)



git的存储库与分支

By default Git will create a branch called *master* when you create a new repository with `git init`. From Git version 2.28 onwards, you can set a different name for the initial branch.

> git config --global init.defaultbranch main(name)



git command 的manual

> git help command
>
> git command --help

这样会出来一大堆内容，如果要简单的

> git command -h





git的使用

目标

配置并初始化一个仓库

追踪文件

暂存和递交

浏览project的历史和各个版本发生的变化

从远程仓库中push和pull

By the end of the chapter, you should be able to configure and initialize a repository, begin and stop tracking files, and stage and commit changes. We’ll also show you how to set up Git to ignore certain files and file patterns, how to undo mistakes quickly and easily, how to browse the history of your project and view changes between commits, and how to push and pull from remote repositories.

## 获得一个仓库

### 两种途径

1. You can take a local directory that is currently not under version control, and turn it into a Git repository, or

2. You can *clone* an existing Git repository from elsewhere.

   将一个未被版本控制的目录转变成一个git仓库或者从别处克隆一个

### 实操

#### 本地文件

1. 进入一个本地目录（没有被版本控制，即目录中没有.git文件）

![image-20210316111200760](https://gitee.com/hit_whr/picgo/raw/master/image-20210316104824661.png)

1. 创建一个次级目录，里面有仓库文件。但是！该目录中任何文件都没有被track

   > git init

This creates a new subdirectory named `.git` that contains all of your necessary repository files — a Git repository skeleton.

![image-20210316111213097](https://gitee.com/hit_whr/picgo/raw/master/image-20210316111213097.png)

![image-20210316111225314](https://gitee.com/hit_whr/picgo/raw/master/image-20210316111225314.png)

3. track某个文件

> git add file.name //支持通配符
>
> git add LICENSE//这个玩意儿可有可无，用来声明项目的开源权限的。不过既然都放在开源网站上了，也不担心别人下载传播。
>
> git commit -m ”Initial project version”

![image-20210316111303318](https://gitee.com/hit_whr/picgo/raw/master/image-20210316122406457.png)

![image-20210316111738663](https://gitee.com/hit_whr/picgo/raw/master/image-20210316111738663.png)



```bash
mkdir chatroom
cd chatroom
git init
touch README.md
git add README.md
git commit -m "first commit"
git remote add origin git@gitee.com:hit_whr/chatroom.git
git push -u origin master
```



#### 克隆已有的仓库

1. 获得所有版本的所有文件

> git clone url pro_new_name

默认，获得服务器端所有版本的所有文件

Git receives a full copy of nearly all data that the server has. Every version of every file for the history of the project is pulled down by default when you run `git clone`. 

2. 结果

首先创建一个目录，然后初始化一个.get目录，获得服务器端的所有数据

That creates a directory named `libgit2`, initializes a `.git` directory inside it, pulls down all the data for that repository, and checks out a working copy of the latest version.

![image-20210316122406457](https://gitee.com/hit_whr/picgo/raw/master/image-20210316122429719.png)



![image-20210316122420256](https://gitee.com/hit_whr/picgo/raw/master/image-20210316122420256.png)



![image-20210316122429719](https://gitee.com/hit_whr/picgo/raw/master/image-20210316124412198.png)



## 关于对仓库的修改

### 状态

> git clone 的时候特别注意，不要打开vpn

假设采用的是`git clone`，ok，现在有了一个仓库，查看仓库中文件的状态`git status`

![image-20210316124412198](https://gitee.com/hit_whr/picgo/raw/master/image-20210316111303318.png)

![image-20210316124500983](https://gitee.com/hit_whr/picgo/raw/master/image-20210316124706856.png)



文件有untracked,tracked,unmodified,modified,staged,committed这几个状态

- 本例中，是clone来了，对git而言，所有文件都是最近一次快照的一部分，是tracked，unmodified
- 如果新建一个文件 `echo 'this is a test'>a.txt`

![image-20210316124706856](https://gitee.com/hit_whr/picgo/raw/master/image-20210316124500983.png)

对于git而言，不会自动track这个文件，如图所示，untracked->tracked&&staged

- 如果要track，`git add file_name`

#### 针对状态可以进行的操作

- untracked->tracked&&staged  `git add file_name`

![image-20210316125341700](https://gitee.com/hit_whr/picgo/raw/master/image-20210316141150383.png)

从最后一条可以看出，确实是staged了，因为git提示可以unstage

这个`git add`命令，后面可以跟文件名，也可以跟目录名，如果是目录名，那么目录中的所有文件都被tracked,staged

The `git add` command takes a path name for either a file or a directory; if it’s a directory, the command adds all the files in that directory recursively.

- staged tracked->commint->unmodified tracked

> git commit -a //直接提交 -m message

![image-20210316141150383](https://gitee.com/hit_whr/picgo/raw/master/image-20210316125341700.png)



- unmodified,tracked->modified,tracked `edit the file`

对前面的a.txt文件进行编辑后，发现a.txt由unmodified，变为modified，而且系统提示将它暂存起来

![image-20210316142040976](https://gitee.com/hit_whr/picgo/raw/master/image-20210316142040976.png)

“Changes not staged for commit” — which means that a file that is tracked has been modified in the working directory but not yet staged. 

- modified tracked->staged tracked

To stage it, you run the `git add` command. `git add` is a multipurpose command — you use it to begin tracking new files, to stage files, and to do other things like marking merge-conflicted files as resolved.

> 目前为止，git add命令可以使untracked到tracked，staged，使modifie到staged。
>
> so，add 可以理解为add file to the ==stage area==

![image-20210316142658632](https://gitee.com/hit_whr/picgo/raw/master/image-20210316142658632.png)

可以看出，现在已经是在stage area了，然后`git commit`即可

![image-20210316143045536](https://gitee.com/hit_whr/picgo/raw/master/image-20210316144257643.png)



背景：tracked，staged，to be committed

At this point, suppose you remember one little change that you want to make in `CONTRIBUTING.md` before you commit it. You open it again and make that change, and you’re ready to commit. However, let’s run `git status` one more time:

一开始，CONTRIBUTING.md文件staged了，但是在committed之前，又做出了修改，此时

```console
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

    new file:   README
    modified:   CONTRIBUTING.md

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

    modified:   CONTRIBUTING.md
```

发现CONTRIBUTING.md有两个状态：staged和modified

What the heck? Now `CONTRIBUTING.md` is listed as both staged *and* unstaged. How is that possible? It turns out that Git stages a file exactly as it is when you run the `git add` command. If you commit now, the version of `CONTRIBUTING.md` as it was when you last ran the `git add` command is how it will go into the commit, not the version of the file as it looks in your working directory when you run `git commit`. If you modify a file after you run `git add`, you have to run `git add` again to stage the latest version of the file:

> 启示：每次committed之前，需要add。==什么时候add？==最好是确保该版本下自己不会再做出修改了。如果要订正上面的，也很简单，再add一次

- tracked unmodified ->untracked
- 对`git status`的补充

git status -s

M:staged(green),modified(red)

??:untracked

![image-20210316144257643](https://gitee.com/hit_whr/picgo/raw/master/image-20210316143045536.png)

New files that aren’t tracked have a `??` next to them, new files that have been added to the staging area have an `A`, modified files have an `M` and so on. There are two columns to the output — the left-hand column indicates the status of the staging area and the right-hand column indicates the status of the working tree. So for example in that output, the `README` file is modified in the working directory but not yet staged, while the `lib/simplegit.rb` file is modified and staged. The `Rakefile` was modified, staged and then modified again, so there are changes to it that are both staged and unstaged.

左侧是stage area的状态，右侧是working directory的状态。

所以a是staged，to be committed；b是modified；c是untracked

![image-20210316145259302](https://gitee.com/hit_whr/picgo/raw/master/image-20210316145259302.png)

#### 查看状态时ignore

Often, you’ll have a class of files that you don’t want Git to automatically add or even show you as being untracked. These are generally automatically generated files such as log files or files produced by your build system. In such cases, you can create a file listing patterns to match them named `.gitignore`. Here is an example `.gitignore` file:

```console
$ cat .gitignore
*.[oa]
*~
```

The first line tells Git to ignore any files ending in “.o” or “.a” — object and archive files that may be the product of building your code. The second line tells Git to ignore all files whose names end with a tilde (`~`), which is used by many text editors such as Emacs to mark temporary files. You may also include a log, tmp, or pid directory; automatically generated documentation; and so on. Setting up a `.gitignore` file for your new repository before you get going is generally a good idea so you don’t accidentally commit files that you really don’t want in your Git repository.

需要注意的是，.gitignore默认在add某个文件前生效，所以如果在gitignore存在前，某个文件就已经add了，git status里面仍然有这个文件。此时，gitignore只对后面再创建的文件有效

![image-20210316211549616](https://gitee.com/hit_whr/picgo/raw/master/image-20210316211549616.png)

解决方法：

```bash
清除所有的stage area

user@DESKTOP-GU58S2D MINGW64 ~/py_snake_game (master)
$ git rm -r --cached .
rm '.gitignore'
rm '1.txt'
rm '2.txt'
rm 'README.md'
rm 'retroSnaker.py'

把所有文件加入stage area，此时.gitignore可以生效了

user@DESKTOP-GU58S2D MINGW64 ~/py_snake_game (master)
$ git add .
warning: LF will be replaced by CRLF in .gitignore.
The file will have its original line endings in your working directory

commit结果

user@DESKTOP-GU58S2D MINGW64 ~/py_snake_game (master)
$ git commit -a -m "j"
[master 3381802] j
 3 files changed, 194 insertions(+), 197 deletions(-)
 delete mode 100644 1.txt
 delete mode 100644 2.txt

对1.txt（untracked）进行修改
user@DESKTOP-GU58S2D MINGW64 ~/py_snake_game (master)
$ echo "after rm and add">>1.txt

发现的确没有显示1.txt了
user@DESKTOP-GU58S2D MINGW64 ~/py_snake_game (master)
$ git status
On branch master
Your branch is ahead of 'origin/master' by 20 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

```



>  总结：
>
> 对于.gitignore的使用，最好是在add文件之前。
>
> 如果是写好文件才想起来
>
> 1. git rm -r --cached .
> 2. git add .
> 3. git commit -a -m ””



#### 查看modified not staged

If the `git status` command is too vague for you — you want to know exactly what you changed, not just which files were changed — you can use the `git diff` command. We’ll cover `git diff` in more detail later, but you’ll probably use it most often to answer these two questions: What have you changed but not yet staged? And what have you staged that you are about to commit? Although `git status` answers those questions very generally by listing the file names, `git diff` shows you the exact lines added and removed — the patch, as it were.

status 只能看到modified之后的文件结果，而不能看到做出了什么修改

##### 测试

背景：

- 创建1.txt 2.txt，写入内容，然后add，commit。恢复到tracked,unmodified状态

![image-20210316183856485](https://gitee.com/hit_whr/picgo/raw/master/image-20210316183856485.png)

![image-20210316183942738](https://gitee.com/hit_whr/picgo/raw/master/image-20210316184757622.png)

- 修改1.txt的内容，add，修改2.txt的内容。1.txt- staged，2.txt- modified

![image-20210316184547762](https://gitee.com/hit_whr/picgo/raw/master/image-20210316183942738.png)

- 利用`git diff`查看内容的变化

![image-20210316184718897](https://gitee.com/hit_whr/picgo/raw/master/image-20210316184718897.png)

![image-20210316184757622](https://gitee.com/hit_whr/picgo/raw/master/image-20210316185816042.png)

>  To see what you’ve changed but not yet staged, type `git diff` with no other arguments:

git diff with no arguments

查看modified但未staged的文件具体做出了哪些修改。将工作目录的内容和stage area的对比，即做出了的修改但还没有进入stage area的变化

That command compares what is in your working directory with what is in your staging area. The result tells you the changes you’ve made that you haven’t yet staged.

注意到1.txt做出了修改，并add到stage area，并且没有在`git diff`中显示出来

> 作用：compare the content in the present working directory with the content in the repository

- 对1.txt 2.txt都add，commit，然后对2.txt进行修改：删除line 2，增加line2，不add

![image-20210316185816042](https://gitee.com/hit_whr/picgo/raw/master/image-20210316190505413.png)

可以看到有+-两种符号，表示增删

- 重复上述操作：修改2.txt，modified，not add

![image-20210316190505413](https://gitee.com/hit_whr/picgo/raw/master/image-20210316194418423.png)

发现只显示了当前工作目录和stage area的区别



`git difftool -g filename`

graphical对git diff的变化内容进行图形化的显示：

![image-20210316191840427](https://gitee.com/hit_whr/picgo/raw/master/image-20210316191840427.png)

#### git commit

在此，先设定配置文件

> git config --global core.editor ”vim”
>
> git commit

进入一个vim edit界面，需要加上comment注释，#会作为注释的注释

或者不想进入本界面

> git commit -m ”comment”

For an even more explicit reminder of what you’ve modified, you can pass the `-v` option to `git commit`. Doing so also puts the diff of your change in the editor so you can see exactly what changes you’re committing.

> 最终的结果类似git commit+git diff

![image-20210316194418423](https://gitee.com/hit_whr/picgo/raw/master/image-20210316200115363.png)

显示的结果包括：

所在branch分支：master

commit的校验和：463dc4f

改变了多少文件：1

Now you’ve created your first commit! You can see that the commit has given you some output about itself: which branch you committed to (`master`), what SHA-1 checksum the commit has (`463dc4f`), how many files were changed, and statistics about lines added and removed in the commit.



如果想commit所有tracked且modified，但未在stage area中的文件，直接

> git commit -a -m ”comment”
>
> 直接跳过add

Notice how you don’t have to run `git add` on the `CONTRIBUTING.md` file in this case before you commit. That’s because the `-a` flag includes all changed files. 

##### commit的结果

记录对stage area的快照，进而能够恢复或者以后比对

Every time you perform a commit, you’re recording a snapshot of your project that you can revert to or compare to later.



#### git中移除文件

git rm

要从git中移除一个文件，不能只是从看到的目录中delete（从working directory中删除）。如果这样，git将`从working directory中直接删除` 视为modified，so，这些文件将处于`changes not staged for commit` 

![image-20210316200115363](https://gitee.com/hit_whr/picgo/raw/master/image-20210316204230718.png)

那么问题来了，这些文件是modified，unstaged，但源文件在working area中已经不可见了，如何将空文件放入stage area中，然后commit？（空文件commit视为删除）

==Then, if you run `git rm`, it stages the file’s removal:==

- 将文件从stage area中移除
- commit

To remove a file from Git, you have to remove it from your tracked files (more accurately, remove it from your staging area) and then commit. The `git rm` command does that, and also removes the file from your working directory so you don’t see it as an untracked file the next time around.

If you simply remove the file from your working directory, it shows up under the “Changes not staged for commit” (that is, *unstaged*) area of your `git status` output:

> git rm LICEMSE

![image-20210316204230718](https://gitee.com/hit_whr/picgo/raw/master/image-20210316184547762.png)

作用是将某个文件的remove放到stage area，那么还需要commit操作

![image-20210316204557785](https://gitee.com/hit_whr/picgo/raw/master/image-20210316204654568.png)



然后查看，发现那些文件确实没了

![image-20210316204654568](https://gitee.com/hit_whr/picgo/raw/master/image-20210316204557785.png)

```bash
user@DESKTOP-GU58S2D MINGW64 ~/py_snake_game (master)
$ git add test.txt
warning: LF will be replaced by CRLF in test.txt.
The file will have its original line endings in your working directory

user@DESKTOP-GU58S2D MINGW64 ~/py_snake_game (master)
$ git commit -a -m "directly to stage"
[master 1c366fe] directly to stage
 1 file changed, 1 insertion(+)
 create mode 100644 test.txt

user@DESKTOP-GU58S2D MINGW64 ~/py_snake_game (master)
$ git rm test.txt
rm 'test.txt'

user@DESKTOP-GU58S2D MINGW64 ~/py_snake_game (master)
$ git status
On branch master
Your branch is ahead of 'origin/master' by 12 commits.
  (use "git push" to publish your local commits)

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        deleted:    test.txt


user@DESKTOP-GU58S2D MINGW64 ~/py_snake_game (master)
$ git commit -m -"rm"
[master 719e872] -rm
 1 file changed, 1 deletion(-)
 delete mode 100644 test.txt
 
 
```



> 总结：
>
> 1. rm，从stage到unstage
> 2. commit，是上述结果生效

#### 移除文件，保存在工作区

> git rm --cached file_name

Another useful thing you may want to do is to keep the file in your working tree but remove it from your staging area. In other words, you may want to keep the file on your hard drive but not have Git track it anymore. This is particularly useful if you forgot to add something to your `.gitignore` file and accidentally staged it, like a large log file or a bunch of `.a` compiled files. To do this, use the `--cached` option:



![image-20210316205916025](https://gitee.com/hit_whr/picgo/raw/master/image-20210316205916025.png)



### 本地到服务器

```bash
mkdir chatroom
cd chatroom
git init
touch README.md
git add README.md
git commit -m "first commit"
git remote add origin https://gitee.com/hit_whr/chatroom.git
git push -u origin master
```



### 删除本地仓库

实际上是删除.git文件，rm .git即可，其他自己写的文件会只保留当前working directory里面有的

与git init进行本地仓库的初始化相对应

### 进行版本恢复

git log查看commit日志

```bash
user@DESKTOP-GU58S2D MINGW64 ~/source/repos/算法 (main)
$ git log
commit ebf7c78639a8bafccb13466c4b44f653e36a128f (HEAD -> main, origin/main)
Author: whr <819987540@qq.com>
Date:   Mon Apr 12 22:39:42 2021 +0800//进行了一次delete（rm）

    delete

commit ae0a7f4e444a1459f0b385ebf03eee73ee5c16aa
Author: whr <819987540@qq.com>
Date:   Mon Apr 12 22:37:02 2021 +0800//进行了一次commit

    2021.4.12

user@DESKTOP-GU58S2D MINGW64 ~/source/repos/算法 (main)
$ git reset --hard "ae0a7f4e444a1459f0b385ebf03eee73ee5c16aa"
Updating files: 100% (134/134), done.
HEAD is now at ae0a7f4 2021.4.12

user@DESKTOP-GU58S2D MINGW64 ~/source/repos/算法 (main)
$ ls
input_auto_push.sh  revert  分治/
ok 文件都找回来了
```





## git中文笔记





## 一个实例

现在的目录结构是

```bash
C:.
└─分治
    ├─二分检索
    │  ├─.vs
    │  │  └─二分检索
    │  │      └─v16
    │  │          └─ipch
    │  │              └─AutoPCH
    │  │                  └─293c79dc8489d69b
    │  └─Debug
    │      └─二分检索.tlog
    ├─幂乘算法及其应用
    │  ├─.vs
    │  │  └─幂乘算法及其应用
    │  │      └─v16
    │  │          └─ipch
    │  │              └─AutoPCH
    │  │                  └─fead4cadd62b6861
    │  └─Debug
    │      └─幂乘算法及其应用.tlog
    ├─平面点对
    │  ├─.vs
    │  │  └─平面点对
    │  │      └─v16
    │  │          └─ipch
    │  │              └─AutoPCH
    │  │                  ├─38a5069640bb923f
    │  │                  └─4b0392335a210e5
    │  └─Debug
    │      └─平面点对.tlog
    ├─平面点集的凸包
    │  ├─.vs
    │  │  └─平面点集的凸包
    │  │      └─v16
    │  │          └─ipch
    │  │              └─AutoPCH
    │  │                  ├─a62333eee54e33eb
    │  │                  ├─c36c663357f53fb6
    │  │                  └─d2bcca677b5c23e9
    │  └─Debug
    │      └─平面点集的凸包.tlog
    └─选择
        ├─.vs
        │  └─选择
        │      └─v16
        │          └─ipch
        │              └─AutoPCH
        │                  ├─4b3fab3ab239ce33
        │                  └─a621c27d1f75a3b0
        └─Debug
            └─选择.tlog
```

分治的每一个目录下都只有.cpp和.h文件是需要的

- 首先进入算法的次级目录，然后add所有的.cpp,.h文件
- 直到访问完次级目录

filename是工程文件目录，下面有多个目录，要提交的文件在目录内，不需要找次级目录了（否则还需要深度搜索，不过没必要，因为自己的文件不会放那么深），把所有的.h  .cpp文件提交即可，然后push上去

这里用到了for循环遍历

每行语句用;分割，do表示循环开始，done表示结束

done后面不需要分号了

```bash
echo "要提交的文件夹，次级目录中只提交.h,.cpp文件（防止git空间满了），保证文件夹的名称正确"
read filename
echo "注释"
read com
cd $filename
for file in *;do echo $file; cd $file; git add *.h *.cpp; done
git commit -m $com
git push -u origin
echo "给你点时间看看status，不保证一定成功"
read wait
```



# ssh登录

```bash
# 查看配置的用户名、邮箱
C:\Users\user\Desktop\note>git config --global --list
user.name=whr
user.email=819987540@qq.com
user.main=819987540@qq.com
core.editor=vim
init.defaultbranch=main
# 修改默认的分治为master
git config --global init.defaultbranch “master”
# 配置
xxx

# ssh秘钥申请
ssh-keygen -t rsa -C "user.mail"

C:\Users\user\Desktop\note>ssh-keygen -t rsa -C "819987540@qq.com"
Generating public/private rsa key pair.
Enter file in which to save the key (C:\Users\user/.ssh/id_rsa):
C:\Users\user/.ssh/id_rsa already exists.
Overwrite (y/n)? y
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in C:\Users\user/.ssh/id_rsa.
Your public key has been saved in C:\Users\user/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:+sXOiuinyRNPNGfZtTIz8Aiee3mLpb8HojbQWI9Th6g 819987540@qq.com
The key's randomart image is:

# 在gitee或github中配置ssh秘钥
```

![image-20211026200022613](https://gitee.com/hit_whr/pic_2.0/raw/master/image-20211026200022613.png)



创建一个仓库

```bash
# git仓库配置
git
```

