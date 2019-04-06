from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from contextlib import contextmanager
# Flask sqlalchemy
from sqlalchemy import Column, SmallInteger, Integer
from datetime import datetime


# db = _SQLAlchemy()

class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e

db = SQLAlchemy()

class Base(db.Model):
    __abstract__=True
    create_time = Column('create_time',Integer)
    status = Column(SmallInteger,default = 1)

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())


    def set_attrs(self,arrts_dict):
        for k,v in arrts_dict.items():
            if hasattr(self,k) and k != 'id':
                setattr(self,k,v)