from flask import Blueprint, render_template, flash, request, redirect, url_for
from .models import Users
from . import db
from werkzeug.security import generate_password_hash , check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
auth = Blueprint("auth",__name__)

@auth.route("/sign-in",methods=['GET','POST'])
def sign_in():
    if request.method == "POST":
        data = request.form
        username = data.get("username")
        password = data.get("password")

        if len(username) < 3:
            flash("username must be greather than 3 charechters.",category='error')
        elif len(password) < 7:
            flash("password must be greather than 7 charechters.",category='error') 
        else:
            user = Users.query.filter_by(username=username).first()
            if user:
                if check_password_hash(user.password,password):
                    flash("Login was successful.", category='success')
                    login_user(user=user,remember=True)
                    return redirect(url_for("views.home"))
                else:
                    flash("Password or Username is incorrect.", category='error')


    return render_template('signin.html',user=current_user  )

@auth.route("/sign-up", methods=['GET','POST'])
def sign_up():
    if request.method  == "POST":
        data = request.form
        fullName = data.get('fullName')
        username = data.get('username')
        fpassword = data.get('password')
        passwordConfirm = data.get('passwordConfirm')
        user = Users.query.filter_by(username=username).first()
        if user:
            flash("username is already exists try aother one.", category="error")
        elif len(fullName) < 2:
            flash("FullName must be greather than 1 charachter.", category="error")
        elif len(username) < 3:
            flash("username must be greather than 2 charachters.", category="error")
        elif fpassword != passwordConfirm:
            flash("passwords is not equal.", category="error")
        elif len(fpassword) < 7:
            flash("password length must be greather than 6 charachter.", category="error")
        else:
            new_user = Users(full_name=fullName,username=username,password=generate_password_hash(fpassword,method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash("Account Created!",category="success")
            return redirect(url_for('views.home'))
             

    return render_template('signup.html',user=current_user)

@auth.route("/sign-out")
@login_required
def sign_out():
    logout_user()
    return redirect(url_for("auth.sign_in"))
