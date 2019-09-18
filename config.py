import os

BASE_DIR=os.path.abspath(os.path.dirname(__file__))

class Config(object):
    #密钥
    SECRET_KEY='$Iwillsuccess$'
    SQLALCHEMY_DATABASE_URI='sqlite:///'+os.path.join(BASE_DIR,'blog.db')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    
    #分页
    POSTS_PRE_PAGE=6