from flask import request, redirect, make_response, render_template, session,flash, url_for
from app import startApp
from app.forms import LoginForm, TodoForm, DeleteTodoForm
from app.firestore_service import get_users,get_todos,put_todo,delete_todo
from flask_login import login_required,current_user

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

@app.route("/hello", methods=['GET','POST'])
@login_required
def hello():
    user_ip = session.get("user_ip")
    username = current_user.id
    todo_form = TodoForm()
    delete_form = DeleteTodoForm()
    context = {
        'user_ip':user_ip,
        'username': username,
        'todos':get_todos(user_id=username),
        'todo_form': todo_form,
        'delete_form': delete_form,
    }
    if (todo_form.validate_on_submit()):
        put_todo(user_id=username,description=todo_form.description.data)
        flash('Task added successfully')
    return render_template("hello.html",**context)

@app.route('/todos/delete/<todo_id>', methods=['POST'])
def delete(todo_id):
    user_id = current_user.id
    delete_todo(user_id=user_id,todo_id=todo_id)
    return redirect(url_for('hello'))




