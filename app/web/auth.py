from app.models.base import db
from app.models.user import User
from . import web
from app.libs.email import send_mail
from flask import render_template, request, redirect, url_for, flash
from app.forms.auth import RegisterForm, LoginForm, EmailForm, ResetPasswordForm
from flask_login import login_user, logout_user




@web.route('/register',methods=['GET', 'POST'])
def register():
    # 通过request.form 拿到用户post 提交的表单信息 还需要作校验

    # 验证form
    # 错误信息在form.error
    form = RegisterForm(request.form)
    if request.method  == 'POST' and form.validate():
        with db.auto_commit():
            user = User()
            # 用动态方法不需要一个个赋值
            user.set_attrs(form.data)
            # user.nickname = form.nickname.dataGift
            db.session.add(user)
        # db.session.commit()
        return redirect(url_for('web.login'))
    return render_template('auth/register.html',form=form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user,remember=True)
            next = request.args.get('next')
            if not next or not next.startswith('/'):
                next = url_for('web.index')
            return redirect(next)
        else:
            flash('账号不存在或密码错误')
        pass
    return  render_template('auth/login.html',form=form)



@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    form = EmailForm(request.form)
    if request.method=='POST':
        if form.validate():
            account_email = form.email.data
            # 1
            # try:
            #     user = User.query.filter_by(email = account_email).first_or_404()
            # except Exception as e:
            #     return  render_template('404.html')
            #2
            # init.py 中集中编写
            user = User.query.filter_by(email=account_email).first_or_404()

            send_mail(form.email.data,'重置密码',
                      'email/reset_password.html',user = user,token = user.generate_token())
            flash('邮件已发送到邮箱' + account_email + ',及时查收')
            # return redirect(url_for('web.login'))
    return render_template('auth/forget_password_request.html',form=form)



@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    form = ResetPasswordForm(request.form)
    if request.method == 'POST' and form.validate():
        sucess = User.reset_password(token,form.password1.data)
        if sucess:
            flash('密码更新')
            return redirect(url_for('web.login'))
        else:
            flash('重置失败')
    return render_template('auth/forget_password.html',form =form)


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():

    pass


@web.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('web.index'))
