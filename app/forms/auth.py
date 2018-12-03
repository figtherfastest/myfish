from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired, Length,Email

class RegisterFoem(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64), Email(message='电子邮件不符合规范')])
    password = PasswordField(validators=[DataRequired(message='密码不为空'), Length(6, 32)])
    nickname = StringField(validators=[DataRequired(), Length(2, 30, message='2-10')])