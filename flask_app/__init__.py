from flask import Flask
from .extensions import db, bcrypt, login_manager
from .routes.root import root
from .routes.users import users
from .routes.rooms import rooms
from .routes.static import static

def create_app():

    # instantiate Flask object named 'app', this variable is important!
    app=Flask(__name__)

    # set environment variable
    ENV='dev'

    if ENV=='dev':
        # set database to connect to the local PostgreSQL 'chat-bubble' database
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/chat-bubble'
        app.debug=True
    else:
        # set database to connect to Heroku PostgreSQL dataabase
        app.config['SQLALCHEMY_DATABASE_URI'] = ''
        app.debug=False


    # silence cmd pop-ups when running the app
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # random key
    app.config['SECRET_KEY'] = "b'\xee\x9a+\xca\xf8d\x93\x02\xf3\xb53\x96\x11\xb2\xb4\xe0~av\x89k_\xdf:'"

    # initiate the database with this app
    db.init_app(app)
    bcrypt.init_app(app)
    # csrf.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "root.login"

    @login_manager.user_loader
    def load_user(username):
        from .models.user import User
        return User.query.get(username)


    # recreate the table
    # db.drop_all(app=app)
    db.create_all(app=app)

    # connect other views into one app so the project doesn't look messy!
    app.register_blueprint(root)
    app.register_blueprint(users)
    app.register_blueprint(rooms)
    app.register_blueprint(static)


    return app