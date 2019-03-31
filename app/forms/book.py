from wtforms import Form,StringField,IntegerField
from wtforms.validators import Length,number_range,DataRequired

# 验证器


class SearchForm(Form):
    q = StringField(validators=[DataRequired(), Length(min=1,max=30)])
    page = IntegerField(validators=[number_range(min=1,max=99)],default=1)