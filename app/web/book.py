from flask import jsonify,request
from app.libs.helper import is_isbn_oe_key
from app.spider.yushu_book import YuShuBook
from app.forms.book import SearchForm
# 引入 init 中 web
from . import web


# # 测试非隔离
# @web.route('/test')
# def test1():
#     from flask import  request
#     from app.libs.non_local import n
#     print(n.v)
#     n.v = 2
#     print('--------------------')
#     print(getattr(request,'v',None))
#     setattr(request,'v',2)
#     print('-------------------------')
#     return ''



@web.route('/book/search/')
def search():
    '''
            q 普通关键字 isbn
            page
    '''
    # Request 查询参数 http 请求信息 到request里找
    # q = request.args['q']
    # page = request.args['page']
    # 验证 q page 合法性
    # 验证层
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key =is_isbn_oe_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q,page)
        return jsonify(result)
    else:
        return  jsonify(form.errors)