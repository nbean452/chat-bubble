from ..extensions import db

user_room = db.Table('user_room',
db.Column('user_name', db.String, db.ForeignKey('user.username')),
db.Column('room_name', db.String, db.ForeignKey('room.name')))

