from ..extensions import db

user_room = db.Table('user_room',
db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
db.Column('room_id', db.Integer, db.ForeignKey('room.id')))

