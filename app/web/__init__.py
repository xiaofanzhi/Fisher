'''
蓝图也要转移到flak核心对象上
'''
from flask import Blueprint, render_template

web = Blueprint('web',__name__,)
# 要把相关文件导入才能运行
from app.web import book
from app.web import auth
from app.web import drift
from app.web import gift
from app.web import main
from app.web import wish

@web.app_errorhandler(404)
def not_found(e):
    return render_template('404.html'),404