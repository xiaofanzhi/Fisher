from flask import jsonify
from helper import is_isbn_oe_key
from yushu_book import YuShuBook
# 引入 init 中 web
from . import web


@web.route('/book/search/<q>/<page>')
def search(q,page):
    '''
            q 普通关键字 isbn
            page
    '''
    isbn_or_key =is_isbn_oe_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)