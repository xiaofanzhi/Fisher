'''
蓝图也要转移到flak核心对象上
'''
from flask import Blueprint

web = Blueprint('web',__name__,)
# 要把相关文件导入才能运行
from app.web import book
from app.web import auth
from app.web import drift
from app.web import gift
from app.web import main
from app.web import wish
