from datetime import datetime
from ..extensions import db

class Room(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(20), nullable=False)
    date=db.Column(db.DateTime, default=datetime.now(), nullable=False)
    chats=db.relationship('Chat', backref="room")
    users=db.relationship('User', secondary='user_room', backref='rooms')

    def __init__(self, name):  
        self.name=name