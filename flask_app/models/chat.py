from datetime import datetime
from ..extensions import db

class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    msg = db.Column(db.Text, nullable=False)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    room_id=db.Column(db.Integer, db.ForeignKey('room.id'))

    def __init__(self, msg, sender_id, room_id):  
        self.msg=msg
        self.sender_id=sender_id
        self.room_id=room_id