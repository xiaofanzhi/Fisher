from flask import jsonify,request,render_template,flash
from app.libs.helper import is_isbn_oe_key
from app.spider.yushu_book import YuShuBook
from app.forms.book import SearchForm
from  app.view_models.book import BookViewModel,BookCollection
# 引入 init 中 web
from . import web

import json


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


# 视图函数一点要有返回
@web.route('/book/search')
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
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key =is_isbn_oe_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
            # 老式调用
            # result = YuShuBook.search_by_isbn(q)
            # result = BookViewModel.package_single(result,q)
        else:
            yushu_book.search_by_keyword(q,page)
            # result = YuShuBook.search_by_keyword(q,page)
            # result = BookViewModel.package_collectioms(result, q)

        books.fill(yushu_book,q)
        # return json.dumps(books,default=lambda x: x.__dict__)
        # return jsonify(books.__dict__)
    else:
        flash('搜索关键字不服个要求，请重新输入')
        # return  jsonify(form.errors)
    return render_template('search_result.html', books=books)

@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)
    return render_template('book_detail.html',book=book,wishes=[],gifts=[])







# @web.route('/test')
# def test():
#     r = {
#         'name':'fzx',
#         'age':18
#     }
#     flash('fzx fzzf')
#     # 模板html
#     return render_template('test.html',data = r, )