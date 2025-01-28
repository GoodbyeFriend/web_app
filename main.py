from flask import Flask, redirect, url_for, render_template, request, session, flash
from app.forms import LoginForm


app = Flask (__name__) 
# app.secret_key = "die"

@app.route("/")
def home ():
    return render_template("index.html", content = ["max", "tanya", "zhora", "kira"]) #запуск html страницы


@app.route ("/login", methods=['POST',"GET"])
def login ():
    if request.method == "POST":
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect (url_for ("user"))
        return render_template ("login.html")
    
@app.route ("/login1", methods = ['POST',"GET"])
def login1 ():
    form = LoginForm ()
    return render_template("login1.html", form=form)

@app.route ("/user")
def user ():
    if "user" in session:
        user = session["user"]
        # return f"<h1>{user}</h1>"
        return render_template ("account_main.html", name=user)
    else:
        return redirect (url_for ("login"))
    

@app.route ("/logout")
def logout ():
    session.pop ("user", None)
    return redirect (url_for ("login")) 
# @app.route ("/<name>")
# def user (name):
#     return f"Hello {name}!"


# @app.route("/admin/")
# def admin ():
#     return redirect(url_for("user", name="Admin")) #перенаправление в адресной странице на обработчик user с параметром который мы передаем


if __name__ == "__main__":
    app.run (debug=True, host='0.0.0.0') #запуск приложения