# qqchat2wordcloud

## 简介

使用python中的jieba,wordcloud库对QQ聊天记录（群聊、好友）进行分析

生成关键词词云图，关键词出现次数，发言次数

## QQ聊天记录获取

登录电脑端，主菜单---消息管理---选择会话---右键导出消息记录---选择txt格式

得到example.txt文件，记录其路径

## 开始

### 输入参数

+ txt_name    聊天消息路径 格式txt
+ dir_name    生成文件夹名
+ checkDate    是否检查日期
+ start_date    开始日期
+ end_date    结束日期
+ common    忽略的常用词

## 输出文件

+ word_count.txt    关键词出现次数
+ people_count.txt    发言次数
+ dir_name.png    关键词词云图
