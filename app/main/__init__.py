from flask import Blueprint

main_app=Blueprint('main',__name__)
from app.main import routes