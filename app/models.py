from app import db
from datetime import datetime



#文章分类,它是一文章是多
class Type(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(32))
    posts=db.relationship('Post',backref='category',lazy='dynamic')
#帖子
class Post(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(64))
    keyword=db.Column(db.String())
    body=db.Column(db.String())
    coverpic=db.Column(db.LargeBinary(length=2048))
    timestamp=db.Column(db.DateTime,index=True,default=datetime.now())
    reding=db.Column(db.Integer)
    kind=db.Column(db.String(),db.ForeignKey('type.id'))

#后台用户
class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String())
    password=db.Column(db.String())


    
