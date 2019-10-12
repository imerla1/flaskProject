from datetime import datetime
from flaskapp import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))




class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(70), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    register_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    def __repr__(self):
        return 'Person Info (username): {self.username}\n(is): {self.id}\n password:{self.password}'
    
    def is_active(self):
        """True, as all users are active."""
        return True