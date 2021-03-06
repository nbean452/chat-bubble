from flask import Blueprint, make_response, render_template 
from flask_login import login_required
from werkzeug.exceptions import HTTPException
from ..models.room import Room 
from ..models.user import User 
from ..models.chat import Chat 
from ..extensions import db

rooms = Blueprint('rooms', __name__, url_prefix='/r')

# TODO, remove this file later!
@rooms.route('/')
def index():
    return render_template("rooms-index.html")

# @rooms.route('/create', defaults=)
@rooms.route('/create')
def create():
    # code snippet below is for testing the web application
    room=Room('testing')
    room.users.append(User.query.filter_by(username='nicho').first())
    db.session.add(room)
    db.session.commit()
    return "created " + str(id) + "!"

@rooms.route('/join/<roomname>')
def join(roomname):
    # code snippet below is for testing the web application
    room = Room.query.filter_by(name=roomname).first()
    room.users.append(User.query.filter_by(username='john').first())
    room.users.append(User.query.filter_by(username='steve').first())
    db.session.commit()
    return "joined room " + str(id) + "!"

@rooms.route('/<roomname>')
def open(roomname):
    # code snippet below is for testing the web application
    # return "opening room " + str(id) + "!"
    room = Room.query.filter_by(name=roomname).first()
    print('works')
    user=User.query.filter_by(username='nicho').first()
    chat=Chat('hello there!', user.id, room.id)

    room.chats.append(chat)
    #     # def __init__(self, msg, sender_username, date, room_name):  
    #     # self.msg=msg
    #     # self.sender_username=sender_username
    #     # self.date=date
    #     # self.room_name=room_name
    db.session.add(chat)
    db.session.commit()

    return {"user1": room.users[0].username,
    "user2": room.users[1].username,
    "user3": room.users[2].username,
    "chat1": room.chats[0].msg,
    "chat1sender": room.chats[0].sender.username,
    "chat1room": room.id,
    "chat1date": room.chats[0].date}
    # it works!

    # test={}
    # for i in range(0,len(room.users)):
    #     test['user'+str(i)]=room.users[i].username

    # for i in range(0,len(room.users[0].rooms)):
    #     test[room.users[0].username+'\'s room ' + str(i+1)]=room.users[0].rooms[i].name
    # return test
    # return render_template('chat.html', room_data=room)



# @rooms.errorhandler(HTTPException)
# def error(e):
#     if e.code<400:
#         return e
#     elif e.code>=500:
#         print(e)
#     return render_template('error404.html')

