import bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
# from flask_wtf import CSRFProtect

# csrf = CSRFProtect()
bcrypt = Bcrypt()
db = SQLAlchemy()

login_manager = LoginManager()