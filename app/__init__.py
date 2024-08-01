from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "secret_key_for_cookie_session_and_etc.:D"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app) # initial database 
    from .views import views
    from .auth import auth

    app.register_blueprint(views,url_perfix='/')
    app.register_blueprint(auth,url_perfix='/')
    
    from .models import Users, Notes
    
    with app.app_context():
        db.create_all()

    return app
