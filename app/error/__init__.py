from flask import Blueprint

error_app=Blueprint('error',__name__)

from app.error import error