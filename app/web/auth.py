from . import web
from app.forms.auth import RegisterFoem
from flask import request
from app.model.user import User



@web.route('/register',methods=['GET','POST'])
def register():
    form = RegisterFoem(request.form)
    if request.method == 'POST' and form.validate():
        user = User()
    return "register"