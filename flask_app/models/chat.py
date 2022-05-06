from datetime import datetime
from ..extensions import db

class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    msg = db.Column(db.Text, nullable=False)
    sender_username = db.Column(db.String(30), db.ForeignKey('user.username'))
    date = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    room_name=db.Column(db.String(20), db.ForeignKey('room.name'))

    def __init__(self, msg, sender_username, room_name):  
        self.msg=msg
        self.sender_username=sender_username
        self.room_name=room_name