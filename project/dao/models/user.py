from project.dao.models.base import BaseMixin
from project.setup_db import db


class User(BaseMixin, db.Model):
    __tablename__ = "users"

    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100))
    surname = db.Column(db.String(100))
    favourite_genre = db.Column(db.Integer)

    def __repr__(self):
        return f"<User '{self.name.title()}'>"