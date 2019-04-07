from threading import Thread

from flask import current_app, render_template, app, flash

from app import mail
from flask_mail import Message

def send_async_email(app,msg):
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            flash('发送错误')
            raise e




def send_mail(to, subject, template,**kwargs):
    # msg = Message('邮件测试',sender='648215109@qq.com',body='test',recipients=['fzx_930129@163.com'])
    msg = Message('fzx'+' '+subject, sender=current_app.config['MAIL_USERNAME'] ,recipients=[to])
    msg.html = render_template(template,**kwargs)
    app = current_app._get_current_objiect()
    thr = Thread(target=send_async_email,args=[app,msg])
    thr.start()
