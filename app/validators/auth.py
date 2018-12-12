from wtforms import StringField, PasswordField
from app.validators.base import BaseForm as Form
from wtforms.validators import DataRequired, Length, Email, ValidationError
from app.model.user import User


class RegisterForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64),
                                    Email(message='电子邮箱不符合规范')])
    nickname = StringField('昵称', validators=[DataRequired(),
                                             Length(2, 100, message='昵称至少需要两个字符，最多10个字符')])
    password = PasswordField('密码', validators=[ DataRequired(message='至少两位'), Length(6, 32)])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮件已被注册')

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('昵称已存在')