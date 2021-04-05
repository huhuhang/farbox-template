## Farbox 2 支持自动同步模板

### 初始化配置

点击 `Use this template` 按钮基于本模板仓库创建自己的 **私有仓库**。务必使用私有仓库，否则可能会暴露你的私钥地址。当然，如果你需要公开自己的博客内容，可以借助 Actions secrets 功能保护自己的私钥。

修改主目录下面的 `sync_from_server.py` 和 `sync_to_server.py` 脚本，替换其中的**私钥**和**服务器 IP** 字段。

### 第一次同步

首次使用时，需要从服务器同步内容到仓库中。点击 Actions 面板，选中「 手动同步来自 Farbox 的内容」，然后手动执行。

![](https://cdn.jsdelivr.net/gh/huhuhang/cdn@master/images/2021/04/1617594412728.png)

如果你的私钥和服务器地址配置无误，稍后仓库中将会同步来自服务端的全部数据。
