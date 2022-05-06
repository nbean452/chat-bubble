from flask import Blueprint, redirect, render_template, url_for
from flask_login import login_required
from werkzeug.exceptions import HTTPException
from ..models.user import User
from ..models.chat import Chat
from ..models.room import Room
from ..models.user_room import user_room
from ..extensions import db

users = Blueprint('users', __name__, url_prefix='/u')

# TODO, remove later!
@users.route('/')
def index():
    return render_template('user-index.html')

@users.route('/<string:username>')
@login_required
def profile(username):
    user=User(username, username+"@mail.com", username)
    db.session.add(user)
    db.session.commit()
    return username+" has been added!"
    # return redirect(url_for('.index'))


# the original function
# @users.route('/<string:username>')
# def profile(username):
#     user=User.query.filter_by(username=username).first()
#     if not user:
#         return render_template('error404.html')
#         # return redirect(url_for('routes.index'))

#     return render_template('user_profile.html')
    
    # return render_template('user_profile.html', user=user)