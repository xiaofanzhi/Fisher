from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, desc, func
from sqlalchemy.orm import relationship


from app.spider.yushu_book import YuShuBook
from .base import Base,db


class Wish(Base):
    id = Column(Integer, primary_key=True)
    launched = Column(Boolean, default=False)

    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15),nullable=False )

    @property
    def book(self):
        yushubook = YuShuBook()
        yushubook.search_by_isbn(self.isbn)
        return yushubook.first


    @classmethod
    def get_user_wishes(cls,uid):
        wishes = Wish.query.filter_by(uid=uid,launched = False).order_by(
            desc(Wish.create_time)).all()
        return wishes


    @classmethod
    def get_gifts_counts(cls,isbn_list):
    #     db.session 做查询
    # filter 接受条件表达式
        count_list = db.session.query(func.count(Gift.id),Gift.isbn).filter(
            Gift.launched == False,Gift.isbn.in_(isbn_list),
                                   Gift.status==1).group_by(Gift.isbn).all()
        # 1返回一个对象
        # 2返回字典
        count_list = [{'count':w[0],'isbn':w[1]} for w in count_list]
        return count_list

from app.models.gift import Gift