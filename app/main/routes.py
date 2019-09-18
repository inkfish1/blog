from app.main import main_app
from flask import render_template,request,redirect,session,jsonify,url_for
from app.forms import EditBlogForm
from app.models import Post,Type
import random,base64,os
from functools import wraps
from app import app,db

#访问前验证
def logined_require(func):
    @wraps(func)
    def inner(*args,**kwargs):
        user=session.get('screen_name')
        if not user:
            return redirect(url_for('login.login'))
        return func(*args,**kwargs)
    return inner



# 首页
@main_app.route('/')
@main_app.route('/index')
def index():
    #从数据库随机抽取三篇文章
    num=Post.query.count()
    if num<=3:
        return redirect(url_for('main.editblog'))
    blist=list(range(1,num))
    bid=random.sample(blist,3)
    querydata=Post.query.filter(Post.id.in_(bid)).all()
    #end抽取
    barselect='index'
    sessions={'name':session.get('screen_name'),'headimg':session.get('profile_image_url')}
    return render_template('index.html',barselect=barselect,data=querydata,sessions=sessions)


#博客页
@main_app.route('/blog')
def blog():
    page=request.args.get('page',1,type=int)
    posts=Post.query.order_by(Post.id.desc()).paginate(page,app.config['POSTS_PRE_PAGE'],False)
    barselect='blog'
    sessions={'name':session.get('screen_name'),'headimg':session.get('profile_image_url')}
    return render_template('blog.html',barselect=barselect,sessions=sessions,posts=posts)

#特色页
@main_app.route('/page')
def page():
    barselect='page'
    sessions={'name':session.get('screen_name'),'headimg':session.get('profile_image_url')}
    return render_template('page.html',barselect=barselect,sessions=sessions)

#work页面
@main_app.route('/work')
def work():
    barselect='work'
    sessions={'name':session.get('screen_name'),'headimg':session.get('profile_image_url')}
    return render_template('work.html',barselect=barselect,sessions=sessions)

#contact页面
@main_app.route('/contact')
def contact():
    barselect='contact'
    sessions={'name':session.get('screen_name'),'headimg':session.get('profile_image_url')}
    return render_template('contact.html',barselect=barselect,sessions=sessions)

#single页面
@main_app.route('/single/',methods=['GET','POST'])
def single():
    id=request.args.get('id')     #得到点击页面的id，得到文章
    article=Post.query.filter_by(id=id).first()
    #根据session判断当前阅读的人是否加1
    if not session.get('reding'):
        if article.reding:
            article.reding+=1
        else:
            article.reding=1
    sessions={'name':session.get('screen_name'),'headimg':session.get('profile_image_url')}
    #设置session
    session['reding']='true'   
        
    return render_template('single.html',article=article,sessions=sessions)
    

#编写博客页面 editblog

@main_app.route('/editblog',methods=['POST','GET'])
@logined_require
def editblog():
    barselect='editblog'
    form=EditBlogForm(title='标题',body='输入内容')
    if form.validate_on_submit():
        title=form.title.data
        body=form.body.data
        categoryid=form.category.data
        type=Type.query.get(categoryid)
        keyword=form.keyword.data
        coverpic=request.files['coverpic'].read()   #得到图片二进制流
        coverpic=base64.b64encode(coverpic)
        #将数据写入数据库
        try:
            post=Post(title=title,body=body,keyword=keyword,coverpic=coverpic,category=type)
            db.session.add(post)
            db.session.commit()
            
        except:
            return 'error'
        return 'success' 
    sessions={'name':session.get('screen_name'),'headimg':session.get('profile_image_url')}
    return render_template('editblog.html',form=form,barselect=barselect,sessions=sessions)


#得到最近三个博客的处理方法
@main_app.route('/getrecent',methods=['POST'])
def getrecent():  
    postlist=[]
    # num=Post.query.count()
    # if num<=3:
        
    rectarticale=Post.query.order_by(Post.id.desc()).limit(3).all()
    for post in rectarticale:
        dtime=post.timestamp.strftime('%Y-%m-%d %H:%M')
        pic=post.coverpic.decode('utf-8')
        dic={'id':post.id,'title':post.title,'timestamp':dtime,'pic':pic}
        postlist.append(dic)
    return  jsonify({'signal':1,'posts':postlist})

#得到分类类别
@main_app.route('/getcategory',methods=['POST'])
def getcategory():
    type=Type.query.all()
    catelist=[]
    for t in type:
        id=t.id
        name=t.name
        length=len(t.posts.all())
        dic={'id':id,'name':name,'length':length}
        catelist.append(dic)
    return jsonify({'signal':1,'category':catelist})


#upload富文本图片上传
@main_app.route('/upload',methods=['POST','GET'])
def upload():
    basepath=os.path.abspath(os.path.dirname(__file__))
    if request.method=='POST':
        img=request.files.get('file')
        path=basepath+'/static/upload/'
        img_path=path+img.filename
        img.save(img_path)
        back_url='/static/upload/'+img.filename
    return jsonify({'location': back_url})


#具体分类页
@main_app.route('/categorylist/')
def categorylist():
    id=request.args.get('id')
    posts=Type.query.get(id).posts.all()
    sessions={'name':session.get('screen_name'),'headimg':session.get('profile_image_url')}
    return render_template('categorylist.html',posts=posts,sessions=sessions)
   

#修改博客页
@main_app.route('/revise/',methods=['POST','GET'])
@logined_require
def revise():
    id=request.args.get('id')
    article=Post.query.get(id)
    form=EditBlogForm(title=article.title,body=article.body,category=article.kind,keyword=article.keyword,coverpic=article.coverpic)
    if form.validate_on_submit():
        title=form.title.data
        body=form.body.data
        categoryid=form.category.data
        type=Type.query.get(categoryid)
        keyword=form.keyword.data
        coverpic=request.files['coverpic'].read()   #得到图片二进制流
        coverpic=base64.b64encode(coverpic)
        #将数据写入数据库
        try:
            post=Post(title=title,body=body,keyword=keyword,coverpic=coverpic,category=type)
            db.session.add(post)
            db.session.commit()
        except:
            print('error')
        return 'success' 
    sessions={'name':session.get('screen_name'),'headimg':session.get('profile_image_url')}
    return render_template('editblog.html',article=article,sessions=sessions,form=form)