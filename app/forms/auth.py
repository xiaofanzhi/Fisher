from wtforms import Form,StringField,IntegerField,PasswordField
from wtforms.validators import Length, number_range, DataRequired, Email


class RegisterForm(Form):
    email = StringField(validators=[DataRequired(),Length(8,64),Email(message='电子邮件格式错误')])

    password = PasswordField(validators=[DataRequired(message='密码不能为空'),Length(3,32)])

    nickname = StringField('昵称', validators=[DataRequired(), Length(2, 10, message='昵称至少需要两个字符，最多10个字符')])