from flask import Flask, request, redirect, make_response, render_template, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'SUPER SECRETO'

todos=['TODO 1','TODO 2', 'TODO 3']

class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField("Enviar")


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

@app.route("/hello")
def hello():
    user_ip = session.get("user_ip")
    login_form = LoginForm()
    context = {
        'user_ip':user_ip,
        'todos':todos,
        'login_form':login_form,
    }
    #return "Hello, Cristhian Arce esta es tu IP: {}.".format(user_ip)
    return render_template("hello.html",**context)

