
from . import web
from flask_login import login_required


@web.route('/my/gifts')
@login_required
def my_gifts():
    return 'asdas'


@web.route('/gifts/book/<isbn>')
def save_to_gifts(isbn):
    # 赠书视图逻辑从这开始
    pass


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass



