from wtforms import Form, StringField,IntegerField
from wtforms.validators import DataRequired,Length,NumberRange

class searchForm(Form):
    q = StringField(validators=[DataRequired(),Length(min=1,max=30)])
    page = IntegerField(validators=[NumberRange(min=1,max=99)],default=1)