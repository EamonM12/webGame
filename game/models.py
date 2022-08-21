from locale import windows_locale
from game import db,login_manager
from flask_login import UserMixin

@login_manager.user_loader


def load_user(user_id):
    return(User.query.get(int(user_id)))

class User(db.Model, UserMixin):
    id =db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=True, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)
    win_count = db.Column(db.Integer(),nullable=False,default=0)
    trial_count = db.Column(db.Integer(),nullable=False,default=0)
def __repr__(self):
    return f"User('{self.username}','{self.email}','{self.image_file}')"
