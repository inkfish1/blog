from flask import Blueprint
#定义蓝图
login_app=Blueprint('login',__name__)
from app.login import login