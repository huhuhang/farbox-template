## Farbox 2 自动同步模板

### 初始化配置

点击 [Use this template](https://github.com/huhuhang/farbox-template/generate) 按钮基于本模板仓库创建自己的 **私有仓库**。务必使用私有仓库，否则可能会暴露你的私钥地址。当然，如果你需要公开自己的博客内容，可以借助 Actions secrets 功能保护自己的私钥。

然后修改主目录下面的 `sync_from_server.py` 和 `sync_to_server.py` 脚本，替换其中的**私钥**和**服务器 IP** 字段。

### 自动同步

提交到 master 分支下方的 `.md`，`.jade` 等相关文件发生变更将触发自动同步。你可以到 `.github/workflows/sync_to_server.yml` 下的 `path` 字段中修改触发同步的文件类型。
