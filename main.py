from flask import request, redirect, make_response, render_template, session,flash
from app import startApp
from app.forms import LoginForm
from app.firestore_service import get_users,get_todos

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
def hello():
    user_ip = session.get("user_ip")
    #login_form = LoginForm()
    username = session.get('username')

    context = {
        'user_ip':user_ip,
        'username': username,
        'todos':get_todos(user_id=username),
    #    'login_form':login_form,
        
    }

    users = get_users()
    for user in users:
        print(user.id)
    #if(login_form.validate_on_submit()):
    #    username = login_form.username.data
    #    session['username'] = username
    #    flash('El usuario ha sido registrado con éxito')
    #return "Hello, Cristhian Arce esta es tu IP: {}.".format(user_ip)
    return render_template("hello.html",**context)

