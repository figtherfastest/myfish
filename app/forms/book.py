from wtforms import Form, StringField,IntegerField
from wtforms.validators import DataRequired,length,NumberRange

class searchForm(Form):
    q = StringField(validators=[DataRequired(),length(min=1,max=30)])
    page = IntegerField(validators=[NumberRange(min=1,max=999)],default=1)