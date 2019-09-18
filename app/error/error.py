from app.error import error_app
from flask import render_template

@error_app.app_errorhandler(404)
def not_found_error(error):
    return render_template("404.html"),404
@error_app.app_errorhandler(500)
def internal_error(error):
    return render_template("500.html"),500