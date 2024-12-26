from flask import Flask, abort, render_template
from sqlalchemy import desc
from database import Book, db, Genre

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.db"

db.init_app(app)


@app.route("/")
def all_books():
    books = Book.query.order_by(desc(Book.added)).limit(15).all()
    return render_template("all_books.html", books=books)


@app.route("/genre/<string:genre_name>")
def books_by_genre(genre_name):
    genre = Genre.query.filter_by(name=genre_name).first()
    if not genre:
        abort(404)

    books = Book.query.filter_by(genre=genre)
    return render_template(
        "books_by_genre.html",
        genre_name=genre.name,
        books=books,
    )


if __name__ == "__main__":
    app.run()
