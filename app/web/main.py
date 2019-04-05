from . import web


__author__ = '七月'


@web.route('/')
def index():
    return 'sdas'


@web.route('/personal')
def personal_center():
    pass
