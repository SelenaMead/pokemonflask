from enum import unique
from unicodedata import name
import uuid
from datetime import datetime as dt
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login


class User(db.Model, UserMixin):
    id = db.Column(db.String(32), primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(300))
    pokemons = db.relationship('Pokemon', backref='pokemons', cascade='all, delete-orphan')

    def generate_password(self, password_from_form):
        self.password = generate_password_hash(password_from_form)

    def check_password(self, password_from_form):
        return check_password_hash(self.password, password_from_form)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = uuid.uuid4().hex

    def __repr__(self):
        return f'<User: {self.email}>'


class Pokemon(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    name = db.Column(db.Text)
    description = db.Column(db.Text)
    type = db.Column(db.Text)
    date_created = db.Column(db.DateTime, default=dt.utcnow)
    owner = db.Column(db.ForeignKey('user.id'))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'type': self.type,
            'date_created': self.date_created,
            'owner': User.query.get(self.owner)
        }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = uuid.uuid4().hex

    def __repr__(self):
        return f'<pokemon: {self.body[30]}...>'


# causing an error at this time, don't know why 
@login.user_loader
def load_user(user_id):
     return User.query.get(user_id)