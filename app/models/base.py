from flask_sqlalchemy import SQLAlchemy

# Flask sqlalchemy
from sqlalchemy import Column, SmallInteger

db = SQLAlchemy()


class Base(db.Model):
    __abstract__=True
    status = Column(SmallInteger,default = 1)


    def set_attrs(self,arrts_dict):
        for k,v in arrts_dict.items():
            if hasattr(self,k) and k != 'id':
                setattr(self,k,v)