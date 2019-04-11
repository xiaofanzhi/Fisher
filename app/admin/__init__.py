from app.models.base import db
from flask_admin import Admin
from .views import MyView,UserAdmin

from app.models.book import Book
from app.models.gift import Gift
from app.models.user import User
from app.models.wish import Wish




admin = Admin(name="后台管理系统", index_view=MyView(), base_template='admin/my_master.html')

# add views
admin.add_view(UserAdmin(User, db.session, name='分类'))
