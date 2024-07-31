from flask import Blueprint, render_template, flash, request

auth = Blueprint("auth",__name__)

@auth.route("/sign-in")
def sign_in():
    return render_template('signin.html')

@auth.route("/sign-up", methods=['GET','POST'])
def sign_up():
    if request.method  == "POST":
        data = request.form
        fullName = data.get('fullName')
        username = data.get('username')
        password = data.get('password')
        passwordConfirm = data.get('passwordConfirm')
        
        if len(fullName) < 2:
            flash("FullName must be greather than 1 charachter.", category="error")
        elif len(username) < 3:
            flash("username must be greather than 2 charachters.", category="error")
        elif password != passwordConfirm:
            flash("passwords is not equal.", category="error")
        elif len(password) < 7:
            flash("password length must be greather than 6 charachter.", category="error")
        else:
            flash("Account Created!",category="success")

             

    return render_template('signup.html')
@auth.route("/sign-out")
def sign_out():
    pass
