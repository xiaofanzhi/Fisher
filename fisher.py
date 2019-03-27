# coding=utf-8
from flask import Flask,make_response
from helper import is_isbn_oe_key
app = Flask(__name__)
app.config.from_object('config')
# 检索
@app.route('/book/search/<q>/<page>')
def search(q,page):
    '''
            q 普通关键字 isbn
            page
    '''
    # isbn isbn13 isbn10
    isbn_or_key =is_isbn_oe_key(q)



    pass






if __name__=='__main__':
    app.run(debug=app.config['DEBUG'],port='9999')

