from ..models.input_field import LoginForm, RegisterForm
from flask import Blueprint, render_template, redirect, url_for
from werkzeug.exceptions import HTTPException
from ..models.user import User 
from flask_login import current_user, login_required, login_user, logout_user
from ..extensions import db, bcrypt

root = Blueprint('root', __name__)

@root.route('/')
def index():
    return render_template('index.html')

@root.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    msg = ""

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('users.index'))
            else:
                msg = "Username / Password is incorrect."
                return render_template('login.html', form=form, msg=msg)
        else:
            msg = "Username / Password is incorrect."
            return render_template('login.html', form=form, msg=msg)

    return render_template('login.html', form=form)

@root.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('root.index'))

@root.route('/register', methods=['GET', 'POST'])
def register():

    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(form.username.data, form.email.data, hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('root.login'))

    return render_template('register.html', form=form)

# @root.errorhandler(HTTPException)
# def error(e):
#     if e.code<400:
#         return e
#     elif e.code>=500:
#         print(e)
#     return render_template('error404.html')

