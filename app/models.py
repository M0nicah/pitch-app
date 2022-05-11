from datetime import datetime
from . import db

# database tables
class User(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(150))
    pitch = db.relationship('Pitch', backref='author', lazy=True)

    def __repr__(self) -> str:
        return f"User('{self.username}', '{self.email}')"
 
class Pitch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Pitch('{self.title}', '{self.date_posted}')"