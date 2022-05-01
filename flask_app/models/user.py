from flask_login import UserMixin
from ..extensions import db

class User(db.Model, UserMixin):
    username = db.Column(db.String(30), unique=True, nullable=False, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    chats = db.relationship('Chat', backref='sender')
    
    def __init__(self, username, email, password):  
        self.username=username
        self.email=email
        self.password=password