from wtforms import Form,StringField,IntegerField,PasswordField
from wtforms.validators import Length, number_range, DataRequired, Email, ValidationError, EqualTo

# 校验
from app.models.user import User


class RegisterForm(Form):
    email = StringField(validators=[DataRequired(),Length(3,64),Email(message='电子邮件格式错误')])

    password = PasswordField(validators=[DataRequired(message='密码不能为空'),Length(1,128)])

    nickname = StringField('昵称', validators=[DataRequired(), Length(1, 10, message='昵称至少需要两个字符，最多10个字符')])


    def validate_email(self,field):
        # 用模型做数据库查询 都用db.session

        # 下面是简单方法
        if User.query.filter_by(email = field.data).first():
            raise ValidationError('电子邮件已被注册')

    def validate_nickname(self, field):
        if User.query.filter_by(nickname =field.data).first():
            raise ValidationError('昵称存在')


class LoginForm(Form):
    email = StringField(validators=[DataRequired(),Length(3,64),Email(message='电子邮件格式错误')])

    password = PasswordField(validators=[DataRequired(message='密码不能为空'),Length(1,128)])


class EmailForm(Form):
    email = StringField(validators=[DataRequired(), Length(3, 64), Email(message='电子邮件格式错误')])


class ResetPasswordForm(Form):
    password1 = PasswordField('新密码', validators=[
        DataRequired(), Length(1, 20, message='密码长度至少需要在6到20个字符之间'),
        EqualTo('password2', message='两次输入的密码不相同')])
    password2 = PasswordField('确认新密码', validators=[
        DataRequired(), Length(1, 20)])