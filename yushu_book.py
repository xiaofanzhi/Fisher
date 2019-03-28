
from httper import HTTP
class YuShuBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'
    @classmethod
    def search_by_isbn(cls,isbn):
        url = cls.isbn_url.format(isbn)
        # result是json格式 在Python中json转化为字典
        result = HTTP.get(url)
        return result
    @classmethod
    def search_by_keyword(cls,keyword,count = 15,start =0):
        url = cls.keyword_url.format(keyword,count,start)
        result = HTTP.get(url)
        return result