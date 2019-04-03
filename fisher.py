# coding=utf-8

from app import create_app

app = create_app()

if __name__=='__main__':
    app.run(debug=app.config['DEBUG'],port='9999',threaded = True,)
#     processes = 1 多线程

