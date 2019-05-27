import os

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# figure out where our project path is and set up a database file with
# its full path and the sqlite:/// prefix to tell SQLAlchemy which database engine we're using.

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "website.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

# we initialize a connection to the database and keep this in the db variable.
# We'll use this to interact with our database.

db = SQLAlchemy(app)

class Book(db.Model):
    title = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)

    def __repr__(self):
        return "<Title: {}>".format(self.title)

@app.route('/', methods=["GET", "POST"])
def home():
    books = None
    if request.form:
 # grab the "title" input from our form, and use it to initialize a new Book object.
 # We save this new Book to a variable named book
        try:
            book = Book(title=request.form.get("title"))
            # We then add the book to our database and commit our changes to persist them
            db.session.add(book)
            db.session.commit()
        # a line to retrieve all of the books just before the end of the home() function and
        # modify the last line to pass these books through to our front-end template.
        except Exception as e:
            print("Failed to add book")
            print(e)
    books = Book.query.all()
    return render_template("home.html", books=books)

if __name__ == "__main__":
    app.run(debug=True)
