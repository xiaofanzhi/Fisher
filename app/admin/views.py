from flask import render_template
from flask_login import current_user, login_required
from flask_admin.contrib import sqla
from wtforms import TextAreaField

from app.forms.auth import LoginForm
from app.web import web
from flask_admin import Admin, BaseView, expose, AdminIndexView





from app.models.base import db
from app.models.user import User
from app.libs.email import send_mail
from flask import render_template, request, redirect, url_for, flash
from app.forms.auth import RegisterForm, LoginForm, EmailForm, ResetPasswordForm
from flask_login import login_user, logout_user

import flask_admin as admin

class MyView(admin.AdminIndexView):
    @expose('/')
    def index(self):
        if not current_user.is_authenticated:
            return redirect(url_for('.login_view'))
        return super(MyView, self).index()

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        form = LoginForm(request.form)
        if request.method == 'POST' and form.validate():
            user = User.query.filter_by(email=form.email.data).first()
            if user and user.check_password(form.password.data):
                login_user(user,remember=True)
            else:
                flash('账号不存在或密码错误')
        if current_user.is_authenticated:
            return redirect(url_for('.index'))
        self._template_args['form'] = form
        # self._template_args['link'] = link
        return super(MyView, self).index()

    @expose('/logout/')
    def logout_view(self):
        logout_user()
        return redirect(url_for('.index'))





class UserAdmin(sqla.ModelView):
    column_list = ('nickname', 'phone_number', 'email','beans','send_counter','receive_counter')

    form_overrides = dict(about_me=TextAreaField)

    column_labels = dict(
        email=('邮箱'),
        nickname=('用户名'),
        beans=('鱼币'),
    )
    column_descriptions = dict(
        email = ('输入游戏')
    )
    def is_accessible(self):
        return current_user.is_authenticated