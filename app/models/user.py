from flask import current_app
from sqlalchemy import Column, Integer, String, Boolean, Float
from werkzeug.security import generate_password_hash,check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from math import floor

from app.libs.enums import PendingStatus
from app.libs.helper import is_isbn_or_key
from app.models.drift import Drift
from app.models.gift import Gift
from app.models.wish import Wish
from app.spider.yushu_book import YuShuBook
from .base import Base,db
from flask_login import UserMixin
from app import login_manager


class User(UserMixin,Base):
    # __tablename__ = 'user1'
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    email = Column(String(50), unique=True, nullable=False)
    _password = Column('password', String(500))
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))



    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,raw):
        self._password = generate_password_hash(raw)


    def can_send_drift(self):
        if self.beans<1:
            return False
        success_gifts_count = Gift.query.filter_by(
            uid = self.id,launched = True
        ).count()
        success_receive_count = Drift.query.filter_by(
            requester_id = self.id,pending=PendingStatus.success
        ).count()

        return  True if floor(success_receive_count/2)<=floor(success_gifts_count) \
            else False


    def check_password(self, raw):
        if not self._password:
            return False
        return check_password_hash(self._password, raw)


    def can_save_to_list(self,isbn):
        if is_isbn_or_key(isbn) != 'isbn':
            return False
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(isbn)
        if not yushu_book.first:
            return False
        # 既不在礼物清单也不再心愿清单
        gifting =Gift.query.filter_by(uid = self.id,isbn=isbn,launched = False).first()
        wishing = Wish.query.filter_by(uid=self.id,isbn=isbn,launched =False).first()
        if not gifting and not wishing:
            return  True
        else:
            return False



    def generate_token(self,expiration=600):
        s = Serializer(current_app.config['SECRET_KEY'],expiration)
        temp = s.dumps({'id':self.id})
        return temp.decode('utf-8')

    @staticmethod
    def reset_password(token,new_password):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except:
            return False
        uid = data.get('id')
        with db.auto_commit():
            user = User.query.get(uid)
            user.password = new_password
        return True


    @property
    def summary(self):
        return dict(
            nickname = self.nickname,
            beans = self.beans,
            email = self.email,
            send_receive = str(self.send_counter) + '/' + str(self.receive_counter)
        )



@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))


