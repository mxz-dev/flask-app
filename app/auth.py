from flask import Blueprint, render_template

auth = Blueprint("auth",__name__)

@auth.route("/sign-in")
def sign_in():
        return render_template('signin.html')

@auth.route("/sign-up")
def sign_up():
    return render_template('signup.html')
@auth.route("/sign-out")
def sign_out():
    pass
