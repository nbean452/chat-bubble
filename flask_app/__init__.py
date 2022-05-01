from flask import Flask
from .extensions import db
from .routes.root import root
from .routes.users import users
from .routes.rooms import rooms

def create_app():

    # instantiate Flask object named 'app'
    app=Flask(__name__)
    # database location
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    # silence cmd pop-ups when running the app
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # random key
    app.config['SECRET_KEY'] = 'justakey'

    # initiate the database with this app
    db.init_app(app)

    # recreate the table
    # db.drop_all(app=app)
    db.create_all(app=app)

    # connect other views into one app
    app.register_blueprint(root)
    app.register_blueprint(users)
    app.register_blueprint(rooms)

    return app