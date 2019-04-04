
from app.libs.httper import HTTP
from  flask import current_app
class YuShuBook:
    # 模型层
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        # 增加了描述鱼书book 特征本身的数据
        self.total = 0
        self.books = []




    def search_by_isbn(self,isbn):
        url = self.isbn_url.format(isbn)
        # result是json格式 在Python中json转化为字典
        result = HTTP.get(url)
        #在这可以存入数据 缓存数据 减少api访问
        self.__fill_single(result)


    def __fill_single(self,data):
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_collection(self,data):
            self.total = data['totals']
            self.books = data['books']

    def search_by_keyword(self,keyword,page=1):
        url = self.keyword_url.format(keyword,current_app.config['PER_PAGE'],self.calculate_start(page))
        result = HTTP.get(url)
        self.__fill_collection(result)


    def calculate_start(self,page):
        return (page-1)*current_app.config['PER_PAGE']