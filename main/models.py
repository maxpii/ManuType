from main import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False) #string of 20 characters, and cannot be duplicated
    email = db.Column(db.String(120), unique=True, nullable=False) #string of 120 characters, and cannot be duplicated
    image_file = db.Column(db.String(20),nullable=False, default='default.jpg') #string of 20 characters, and cannot be duplicated
    password = db.Column(db.String(60), nullable=False)
    typing = db.relationship("Typing",backref="player",lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.id}')"

class Typing(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    speed = db.Column(db.Integer,nullable=False)
    accuracy = db.Column(db.Integer,nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey("user.id"),nullable=False)
    #TODO:create columns for typing-specific data

    def __repr__(self):
        return f"User('{self.speed}','{self.accuracy}','{self.user_id}')"