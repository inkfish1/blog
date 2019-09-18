from app.login import login_app
from flask import redirect,render_template,request,session,url_for
import requests,json
from app.models import User
#-----------------------------------后台登录----------------------------------------------
@login_app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        username=request.form.get('username')
        password=request.form.get('password')
        try:
            user=User.query.filter(User.username==username).first()    
        except :
            return '登录失败'
        if user.password==password:
            if username=='cgy':
                session['adminuser']='cgy'
                return redirect(url_for('admin.articletype'))  #应该访问index====需要改
            else:
                return redirect(url_for('main.index'))   
    return render_template('login.html')


#-----------------------------------微博登录----------------------------------------------
access_token=''
#登录接口
@login_app.route('/weibo_login',methods=['POST','GET'])
def weibo_login():
    url="https://api.weibo.com/oauth2/authorize?client_id=1303717547&response_type=code&redirect_uri=http://127.0.0.1:5000/process"
    return redirect(url)

#回调函数
@login_app.route('/process/')
def process():
    global access_token
    code=request.args.get('code')
    data=''
    if code:
        url = 'https://api.weibo.com/oauth2/access_token?client_id=1303717547&client_secret=715b831a974ff6f769fc0325422e2c9e&code='+str(code)+'&redirect_uri=http://127.0.0.1:5000/process'
        page=requests.post(url)
        access_token=page.json()['access_token']
        uid=page.json()['uid']
        info_url='https://api.weibo.com/2/users/show.json?access_token='+access_token+'&uid='+uid
        data=requests.get(info_url).json()
        session['screen_name']=data['screen_name']
        session['profile_image_url']=data['profile_image_url']
    return redirect(url_for('main.index'))

#登出接口
@login_app.route('/logout')
def logout():
    global access_token
    session['screen_name']=''
    session['profile_image_url']=''
    #同时需要对微博端进行取消授权
    url='https://api.weibo.com/oauth2/revokeoauth2?access_token='+access_token
    requests.get(url)    
    return redirect(url_for('main.index'))

#-----------------------------------github登录----------------------------------------------


#登录接口
@login_app.route('/github_login')
def github_login():
    url='https://github.com/login/oauth/authorize?client_id=9c28d57c1059b69cc6cd&scope=user:email'
    return redirect(url)
#回调函数
@login_app.route('/github_callback/')
def github_callback():
    code=request.args.get('code')
    token_url='https://github.com/login/oauth/access_token?client_id=9c28d57c1059b69cc6cd&client_secret=da523b028b227d596b79a24e4d3656c33a1874f7&code={}'.format(code)
    access_token=requests.post(token_url)
    access_token=access_token.text
    inf_url='https://api.github.com/user?{}'.format(access_token)
    infor=requests.get(inf_url)
    infor=json.loads(infor.text)
    session['screen_name']=infor['login']
    session['profile_image_url']=infor['avatar_url']
    return redirect(url_for('main.index'))