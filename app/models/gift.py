from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, desc,func
from sqlalchemy.orm import relationship

from app.models.wish import Wish
from app.spider.yushu_book import YuShuBook
from .base import Base,db
from flask import current_app

from collections import  namedtuple





class Gift(Base):
    id = Column(Integer, primary_key=True)
    launched = Column(Boolean, default=False)

    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15),nullable=False )

    @classmethod
    def get_user_gifts(cls,uid):
        gifts = Gift.query.filter_by(uid=uid,launched = False).order_by(
            desc(Gift.create_time)).all()
        return gifts


    @classmethod
    def get_wish_counts(cls,isbn_list):
    #     db.session 做查询
    # filter 接受条件表达式
        count_list = db.session.query(func.count(Wish.id),Wish.isbn).filter(
            Wish.launched == False,Wish.isbn.in_(isbn_list),
                                   Wish.status==1).group_by(Wish.isbn).all()
        # 1返回一个对象
        # 2返回字典
        count_list = [{'count':w[0],'isbn':w[1]} for w in count_list]
        return count_list

    @property
    def book(self):
        yushubook = YuShuBook()
        yushubook.search_by_isbn(self.isbn)
        return yushubook.first

    @classmethod
    def recent(cls):
        recent_gift = Gift.query.filter_by(launched=False).group_by(Gift.isbn).order_by(
            desc(Gift.create_time)).distinct().limit(current_app.config['RECENT_BOOK_COUNT']).all()
        return recent_gift