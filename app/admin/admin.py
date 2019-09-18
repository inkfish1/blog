from app.admin import admin_app
from flask import session,render_template,redirect,url_for,request,jsonify
from app.models import Type
from app import db
'''后台管理'''

@admin_app.before_request
def before_request():
    if session['adminuser']=='cgy':
        pass
    else:
        return '无权访问'


#文章类型管理
@admin_app.route('/articletype')
def articletype():
    page=request.args.get('page',1,int)
    types=Type.query.paginate(page,6,False)
    return render_template('/admin/articletype.html',types=types)

#添加文章类型
@admin_app.route('/addtype/',methods=['POST','GET'])
def addtype():
    type=request.form.get('type')
    try:
        t=Type(name=type)
        db.session.add(t)
        db.session.commit()
        return jsonify({'singal':1})
    except:
        return '添加失败'

#删除文章类型
@admin_app.route('/deletetype/')
def deletetype():
    id=request.args.get('id')
    try:
        type=Type.query.get(id)
        db.session.delete(type)
        db.session.commit()
        return redirect(url_for('admin.articletype'))
    except:
        return "删除失败"
    
  
   