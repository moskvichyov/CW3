from project.dao.models.base import BaseMixin
from project.setup_db import db


class Movie(BaseMixin, db.Model):
    __tablename__ = "movies"

    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    trailer = db.Column(db.String(100), nullable=False)
    year = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    genre = db.relationship("Genre")
    genre_id = db.Column(db.Integer, db.ForeignKey("genres.id"), nullable=False)
    director = db.relationship("Director")
    director_id = db.Column(db.Integer, db.ForeignKey("directors.id"), nullable=False)

    def __repr__(self):
        return f"<Movie '{self.name.title()}'>"