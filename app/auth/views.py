from flask import render_template
from app.forms import LoginForm
from flask import session
from flask import flash
from flask import redirect,url_for
from app.firestore_service import get_user,user_put
from app.models import UserData,UserModel
from flask_login import login_user,login_required,logout_user
from werkzeug.security import generate_password_hash,check_password_hash
from . import auth

@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form':LoginForm()
    }
    if(login_form.validate_on_submit()):
        username = login_form.username.data
        password = login_form.password.data
        user_doc = get_user(username)
        if (user_doc.to_dict() is not None):
            password_from_db = user_doc.to_dict()['password']
            if(check_password_hash(password_from_db,password)):
                user_data = UserData(username,password)
                user = UserModel(user_data)
                login_user(user)
                flash('Welcome Back')
                redirect(url_for('hello'))
            else:
                flash('Wrong password')
        else:
            flash('The user does not exists')
        return redirect(url_for('index'))
    return render_template('login.html',**context)

@auth.route('logout')
@login_required
def logout():
    logout_user()
    flash('come back soon!')
    return redirect(url_for('auth.login'))

@auth.route('/signup',methods=['GET','POST'])
def sign_up():
    signup_form = LoginForm()
    context = {
        'signup_form': signup_form,
    }
    if (signup_form.validate_on_submit()):
        username = signup_form.username.data
        password = signup_form.password.data

        user_doc = get_user(username)
        if user_doc.to_dict() is None:
            password_hash = generate_password_hash(password)
            user_data = UserData(username,password_hash)
            user_put(user_data)
            user = UserModel(user_data)
            login_user(user)
            flash('Welcome for the first time!')
            return redirect(url_for('hello'))
        else:
            flash('User already exists')

    return render_template('signup.html',**context)
     