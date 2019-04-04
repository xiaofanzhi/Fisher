# 处理单本
class BookViewModel:
    # book 来自于yushu_book 这个文件
    def __init__(self,book):
        self.title = book['title'],
        self.publisher = book['publisher'],
        self.author = '、'.join(book['author']),
        self.image = book['image'],
        self.summary = book['summary'],
        self.pages = book['pages']

class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = None

    #     接受鱼叔book
    def fill(self,yushu_book,keyword):
        self.total = yushu_book.total
        self.keyword = keyword
        # 列表推导式
        self.books = [BookViewModel(book) for book in yushu_book.books]




# 可以在这调整数据
class _BookViewModel:
    # 处理单本情况 data原始数据
    # 一个类 类变量， 行为（方法） 只有方法没有变了 本质是面向过程
    @classmethod
    def package_single(cls,data,keyword):
        returned = {
            'books': [],
            'total': 0,
            'keywoed': keyword
        }
        if data:
            returned['total'] = 1
            returned['books'] = [cls.__cut_book_data(data)]

        return returned
    @classmethod
    def package_collectioms(cls,data,keyword):
        returned = {
            'books':[],
            'total':0,
            'keyword':keyword
        }
        if data:
            returned['total'] = data['books'].total
            returned['books'] = [cls.__cut_book_data(book) for book in data['books']]
        return  returned

    # 字段裁剪 变成我们需要的  处理一本 在这里做复杂设计
    @classmethod
    def __cut_book_data(cls,data):
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'pages': data['pages'] or '',
            'author': '、'.join(data['author']),
            'price': data['price'],
            'summary': data['summary'] or '',
            'image': data['image']
        }
        return book
