from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt= Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view = 'login' # type: ignore
login_manager.login_message_category = 'info' 


from flask_blog import routes

from .models import User, Post

with app.app_context():
    db.create_all()