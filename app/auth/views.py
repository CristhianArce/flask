from flask import render_template
from app.forms import LoginForm
from flask import session
from flask import flash

from . import auth

@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form':LoginForm()
    }
    if(login_form.validate_on_submit()):
        username = login_form.username.data
        session['username'] = username
        flash('El usuario ha sido registrado con éxito')
    return render_template('login.html',**context)