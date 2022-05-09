from flask_login import UserMixin
from ..extensions import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(20), nullable=False)
    l_name = db.Column(db.String(20))
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    # TODO, add default profile picture and upload profile picture
    profile_pic = db.Column(db.Text)
    status_msg = db.Column(db.String(50))
    chats = db.relationship('Chat', backref='sender')
    
    def __init__(self, f_name, l_name, username, email, password):
        self.f_name=f_name  
        self.l_name=l_name  
        self.username=username
        self.email=email
        self.password=password
    
    def __repr__(self):
        return f'user id: {self.id}, username: {self.username}, email: {self.email}, status msg: {self.status_msg}'