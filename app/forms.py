from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,TimeField,SubmitField,SelectMultipleField,RadioField
from wtforms.validators import DataRequired,Length
from flask_wtf.file import  FileField,FileAllowed,FileRequired
from datetime import datetime
from app.models import Type

class EditBlogForm(FlaskForm):
    choices=[]
    for t in Type.query.all():
        choices.append((str(t.id),t.name))
   
    title=StringField('标题',validators=[DataRequired(message='输入标题'),Length(1,100)])
    body=TextAreaField('正文',validators=[DataRequired(message='内容不能为空')])
    category=RadioField('文章类型',choices=choices,validators=[DataRequired()])
    keyword=StringField('文章说明',validators=[DataRequired(),Length(1,64)])
    coverpic=FileField('上传图片',validators=[FileRequired(),FileAllowed(['jpg','png','bmp','gif'],'image only!')])
    submit=SubmitField('send')
    cancel=SubmitField('cancel')
 
