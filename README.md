安装方法：
---

假设你已经安装好edx平台
那么安装步骤是：

```
sudo su edxapp -s /bin/bash
cd ~
source edxapp_env
pip install git+https://github.com/lxy2222/CccXBlock.git
```
在/edx/app/edxapp/cms.envs.json 添加 `"ALLOW_ALL_ADVANCED_COMPONENTS": true, 到FEATURES`
然后重新启动你的studio

在studio中的配置：
----
然后在`studio中settings--->advanced settings--->`将文件名添加到此，记得加双引号
好了，然后你添加新的unit的时候，就会出现advance选项，然后你就可以选择ccblock了
好了现在你可以根据你的userid 和video_id上传，
这只是一个简易版本，嗯后期还是会完善
如果有好的建议，欢迎大神们发邮箱到
liangxiaoyu0129@163.com，请你们吃好吃的哟~
