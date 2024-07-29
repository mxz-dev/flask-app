from flask import Blueprint

auth = Blueprint("auth",__name__)

@auth.route("/sign-in")
def sign_in():
    pass
@auth.route("/sign-up")
def sign_up():
    pass
@auth.route("/sign-out")
def sign_out():
    pass
