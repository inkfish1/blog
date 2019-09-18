from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app=Flask(__name__)
#导入配置
app.config.from_object(Config)
#数据库和迁移初始化
db=SQLAlchemy(app)
migrate=Migrate(app,db)

# 注册登录登出蓝图
from app.login import login_app
app.register_blueprint(login_app)
# 注册error蓝图
from app.error import error_app
app.register_blueprint(error_app)
#注册main蓝图
from app.main import main_app
app.register_blueprint(main_app)
#注册admin蓝图
from app.admin import admin_app
app.register_blueprint(admin_app)

from app import models
