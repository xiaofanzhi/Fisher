from app.models.user import User
from . import web
from flask import render_template,request
from app.forms.auth import RegisterForm
__author__ = '七月'


@web.route('/register',methods=['GET', 'POST'])
def register():
    # 通过request.form 拿到用户post 提交的表单信息 还需要作校验

    # 验证form
    form = RegisterForm(request.form)
    if request.method  == 'POST' and form.validate():
        user = User()
        # 用动态方法不需要一个个赋值
        user.set_attrs(form.data)
        # user.nickname = form.nickname.data
    return render_template('auth/register.html',form={'data':{}})


@web.route('/login', methods=['GET', 'POST'])
def login():
    pass


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    pass


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    pass


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    pass
