from flask import Blueprint

admin_app=Blueprint('admin',__name__)

from app.admin import admin