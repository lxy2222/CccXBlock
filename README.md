安装方法：
假设你已经安装好edx平台
那么安装步骤是
sudo su edxapp -s /bin/bash
cd ~
source edxapp_env
pip install git+https://github.com/lxy2222/CccXBlock.git
在/edx/app/edxapp/cms.envs.json 添加 "ALLOW_ALL_ADVANCED_COMPONENTS": true, 到FEATURES
然后重新启动你的studio
还有在studio中的配置：
然后在studio中settings--->advanced settings--->将文件名添加到此，记得加双引号
好了，然后你添加新的unit的时候，就会出现advance选项，然后你就可以选择ccblock了
但是有个问题就是
cc返回的播放码是<script src...>
然后我使用了{{video_id|safe}}防止转义后，仍然无法播放视频。。。
所以请路过的大大们帮帮忙=====。=====
邮箱liangxiaoyu0129@163.com
