from flask import render_template, url_for,flash,redirect
from game import app,db,bcrypt
from game.forums import RegistrationForm, LoginForm
from game.models import User



@app.route("/")
def home():
        return render_template("home.html")

@app.route("/game")
def game():
    return render_template("game.html")

@app.route("/register",methods=["GET","POST"])
def register():
    form = RegistrationForm()
    if(form.validate_on_submit()):
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Account created for {form.username.data}!","success")
        return(redirect(url_for("home")))
    return render_template("register.html", title="Register", form=form)

@app.route("/login",methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if(form.email.data == "admin@blog.com" and form.password.data =="password"):
            flash("You have been Logged in","success")
            return(redirect(url_for("home")))
        else:
            flash('Login Unsuccesful. Please check Username and Password',"danger")
    return render_template("login.html",title= "login", form=form)
