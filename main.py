from flask import Flask, request, redirect, make_response, render_template

app = Flask(__name__)

todos=['TODO 1','TODO 2', 'TODO 3']

@app.errorhandler(500)
def internal_error(error):
    return render_template("505.html",error=error)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.route("/")
def index():
    user_ip = request.remote_addr
    response = make_response(redirect("/hello"))
    response.set_cookie("user_ip",user_ip)
    return response

@app.route("/hello")
def hello():
    user_ip = request.cookies.get("user_ip")
    context = {
        'user_ip':user_ip,
        'todos':todos,
    }
    #return "Hello, Cristhian Arce esta es tu IP: {}.".format(user_ip)
    return render_template("hello.html",**context)

