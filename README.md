# flask-celery-sample

尽管flask的官网给出了celery的相关函数，但那个似乎只对单独实例有效，如果flask的实例是使用工厂函数创建，则celery很容易会遇到循环导入，或者是没有上下文等情况。
celery需要启动两个实例，一个是使用命令行启动worker，一个则由flask实例在创建时celery实例。

## 所需package包
* Flask
* Celery
* Redis

安装程序环境
```
python -m venv venv
venv\Scripts\activate.bat   //windows下激活虚拟环境
pip install -r requirements.txt
```

## 测试项目
1. 开启redis服务器
```
redis-server.exe redis.windows.conf
```

2. 开启celery工作池
```
celery -A app.celery worker --loglevel=info --pool=solo
```

3. 运行项目程序
```
flask run
```

4. 打开浏览器测试
前往http://localhost:5000,
点击`test celery function`链接，正常情况下会返回65。



## English Version

## Dependent
* Flask
* Celery
* Redis

set up a virtual enviroment
```
python -m venv venv
venv\Scripts\activate.bat   //The command is worked for windows
pip install -r requirements.txt
```

## Running the example.
1. Set up redis.

2. Start celery worker.
```
celery -A app.celery worker --loglevel=info --pool=solo
```

3. Start the app.
```
flask run
```

4. Open browser and test
go to: http://localhost:5000 and click `test celery function` link. The browser will return 65 if everything is running right.
