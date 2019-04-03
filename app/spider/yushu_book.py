
from app.libs.httper import HTTP
from  flask import current_app
class YuShuBook:
    # 模型层
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'
    @classmethod
    def search_by_isbn(cls,isbn):
        url = cls.isbn_url.format(isbn)
        # result是json格式 在Python中json转化为字典
        result = HTTP.get(url)
        #在这可以存入数据 缓存数据 减少api访问
        return result
    @classmethod
    def search_by_keyword(cls,keyword,page=1):
        url = cls.keyword_url.format(keyword,current_app.config['PER_PAGE'],cls.calculate_start(page))
        result = HTTP.get(url)
        return result

    @staticmethod
    def calculate_start(page):
        return (page-1)*current_app.config['PER_PAGE']