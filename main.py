from flask import request, redirect, make_response, render_template, session,flash
from app import startApp
from app.forms import LoginForm
from app.firestore_service import get_users,get_todos
from flask_login import login_required

app = startApp()


todos=['Estudiar ... ','Trabajar ... ', 'Triunfar ... ']

@app.errorhandler(500)
def internal_error(error):
    return render_template("500.html",error=error)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.route("/")
def index():
    user_ip = request.remote_addr
    response = make_response(redirect("/hello"))
    session['user_ip'] =user_ip
    return response

@app.route("/hello", methods=['GET'])
@login_required
def hello():
    user_ip = session.get("user_ip")
    username = current_user.id

    context = {
        'user_ip':user_ip,
        'username': username,
        'todos':get_todos(user_id=username),  
    }
    
    return render_template("hello.html",**context)

