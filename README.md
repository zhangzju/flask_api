# flask_api
An lightable RESTful api system based on flask.

这是一个采用flask作为框架的一个api后台系统。

## usage用户指南

将这个仓库下载到你的本地，在config.py中配置好你的数据库。
支持所有sqlalchemy能够连接的数据库，但是要求是关系型数据库，因为模型设计中使用了很多外键。

运行数据库迁移：
```python
python manage.py db migrate
```

然后运行主程序，不建议直接运行main.py，这样的方式在很多时候会报错，以为内你的环境变量加载顺序问题。
应该这样：
```python
python manage.py server
```
