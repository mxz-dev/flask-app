from flask import Flask
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "secret_key_for_cookie_session_and_etc.:D"
    from .views import views
    from .auth import auth

    app.register_blueprint(views,url_perfix='/')
    app.register_blueprint(auth,url_perfix='/')

    return app