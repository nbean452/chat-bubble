from datetime import datetime
from ..extensions import db

class Room(db.Model):
    name=db.Column(db.String(20), unique=True, primary_key=True, nullable=False)
    date=db.Column(db.DateTime, default=datetime.now(), nullable=False)
    chats=db.relationship('Chat', backref="room")
    users=db.relationship('User', secondary='user_room', backref='rooms')

    def __init__(self, name):  
        self.name=name