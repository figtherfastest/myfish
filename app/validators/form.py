from app.validators.base import BaseForm as Form
from wtforms import StringField, IntegerField, PasswordField, ValidationError
from wtforms.validators import DataRequired, NumberRange, Length, Email, ValidationError, Regexp
from app.model.user import User



class ClientForm(Form):
    account = StringField(validators=[DataRequired(message='账号不能为空'), Length(
        min=6,max=30
    )])
    password = StringField()

    type= IntegerField(validators=[DataRequired()])


class searchForm(ClientForm):
    q = StringField(validators=[DataRequired(), Length(min=1,max=30)])
    page = IntegerField(validators=[NumberRange(min=1,max=99)],default=1)


class RegisterForm(ClientForm):
    account = StringField(validators=[DataRequired(), Length(min=8,max=64),
                                    Email(message='电子邮箱不符合规范')])
    nickname = StringField('昵称', validators=[DataRequired(),
                                             Length(min=2,max=100, message='昵称至少需要两个字符，最多10个字符')])
    password = PasswordField('密码', validators=[DataRequired(message='至少两位'), Length(min=6,max=32)])

    def validate_account(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮件已被注册')

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('昵称已存在')


class UserEmailForm(ClientForm):
    account = StringField(validators=[
        Email(message='invalidate email')
    ])
    password = StringField(validators=[
        DataRequired(),
        # password can only include letters , numbers and "_"
        Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$')
    ])
    nickname = StringField(validators=[DataRequired(),
                                       Length(min=2, max=22)])

    def validate_account(self, value):
        if User.query.filter_by(email=value.data).first():
            raise ValidationError()


class searchForm(ClientForm):
    q = StringField(validators=[DataRequired(),Length(min=1,max=30)])
    page = IntegerField(validators=[NumberRange(min=1,max=99)],default=1)


class resetPsd(ClientForm):
    account = StringField(validators=[DataRequired(), Length(min=8, max=64),
                                      Email(message='电子邮箱不符合规范')])
    password = PasswordField('密码', validators=[DataRequired(message='至少两位'), Length(min=6, max=32)])

