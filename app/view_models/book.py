
# 可以在这调整数据
class BookViewModel:
    # 处理单本情况 data原始数据
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
        pass

    # 字段裁剪 变成我们需要的
    @classmethod
    def __cut_book_data(cls,data):
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'pages': '、'.join(data['pages']),
            'author': data['author'],
            'price': data['price'],
            'summary': data['summary'],
            'image': data['image']
        }
        return book
