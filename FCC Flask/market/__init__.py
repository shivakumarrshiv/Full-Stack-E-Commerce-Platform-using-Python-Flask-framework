from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app=Flask(__name__)
login_manager = LoginManager(app)
login_manager.login_view='login_page'
login_manager.login_message_category='info'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///market_data.db'
app.config['SECRET_KEY']='826c9ea4520cdaa5b8546492'
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)

from market import routes

