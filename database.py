from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    added = db.Column(db.DateTime, nullable=False, default=func.now())
    genre_name = db.Column(db.String, db.ForeignKey("genre.name", ondelete="SET NULL"))
    genre = relationship("Genre", back_populates="books")

    def __repr__(self):
        return f"Book(fullname={self.fullname!r})"


class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    books = relationship("Book", back_populates="genre")

    def __repr__(self):
        return f"Genre(name={self.name!r})"
