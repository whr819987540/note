# ubuntu修改dns服务器

- 系统读取的配置文件为/etc/resolv.conf（也就是说后面修改的最终效果都是要修改本文件）

  那么为什么不直接修改本文件呢？因为本文件的内容是读取其他文件之后生成的内容

- 修改/etc/network/interfaces

  在最后一行加上`dns-nameservers 8.8.8.8`

