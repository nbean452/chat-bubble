from flask import Blueprint, render_template
from werkzeug.exceptions import HTTPException

root = Blueprint('root', __name__)

@root.route('/')
def index():
    return render_template('index.html')

@root.route('/login')
def login():
    return render_template('login.html')

@root.route('/register')
def register():
    return render_template('register.html')

@root.errorhandler(HTTPException)
def error(e):
    if e.code<400:
        return e
    elif e.code>=500:
        print(e)
    return render_template('error404.html')

