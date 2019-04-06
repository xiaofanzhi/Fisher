from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, SmallInteger, desc
from sqlalchemy.orm import relationship

from app.spider.yushu_book import YuShuBook
from .base import Base
from flask import current_app


class Gift(Base):
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
    def recent(cls):
        recent_gift = Gift.query.filter_by(launched=False).group_by(Gift.isbn).order_by(
            desc(Gift.create_time)).distinct().limit(current_app.config['RECENT_BOOK_COUNT']).all()
        d = recent_gift
        return recent_gift