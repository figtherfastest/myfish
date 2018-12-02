from . import web

@web.route('/register',methods=['GET','POST'])
def register():
    form = request.form
    return "register"