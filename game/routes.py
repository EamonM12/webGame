from crypt import methods
from site import USER_BASE
from flask import render_template, url_for,flash,redirect,request,jsonify
from game import app,db,bcrypt
from game.forums import RegistrationForm, LoginForm
from game.models import User
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import login_user,current_user,logout_user, login_required
import json,random


@app.route("/")
def home():
        return render_template("home.html")

@app.route("/game")
def game():
    
    
    return render_template("game.html")

@app.route("/register",methods=["GET","POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegistrationForm()
    if(form.validate_on_submit()):
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        username_check= User.query.filter_by(username=form.username.data).first()
        email_check= User.query.filter_by(email=form.email.data).first()
        if  email_check:
            flash("That email is already being used","danger")
        elif username_check:
            flash("That Username is already being used","danger")
        else:
            db.session.add(user)
            db.session.commit()
            flash(f"Account created for {form.username.data}!","success")
            return(redirect(url_for("home")))
    return render_template("register.html", title="Register", form=form)


@app.route("/login",methods=["GET","POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            flash("You have been Logged in","success")
            return redirect(next_page) if next_page else redirect(url_for("home"))            
        else:
            flash('Login Unsuccesful. Please check email and Password',"danger")
    return render_template("login.html",title= "login", form=form)

@app.route("/logout")
def logout():
    
    logout_user()
    return redirect(url_for("home"))


# #fix this
# @app.route("/result",methods = ["POST","GET"])
# def result():
#     if request.method == "POST":
#         data = request.get_data(True,True,False)
#         print(data)
#         # data = request.get_json(force=True)
#         return(str(data)) 
#     # return(jsonify(data))



# add logout message
@app.route("/account")
@login_required
def account():
        
    return render_template("account.html", title="Account")
