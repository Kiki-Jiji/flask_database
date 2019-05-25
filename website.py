import os

from flask import Flask, render_template, request

from flask_sqlalchemy import SQLAlchemy


# figure out where our project path is and set up a database file with
# its full path and the sqlite:/// prefix to tell SQLAlchemy which database engine we're using.
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "bookdatabase.db"))

app = Flask(__name__)

# tell our web application where our database will be stored.
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

# we initialize a connection to the database and keep this in the db variable.
# We'll use this to interact with our database.
db = SQLAlchemy(app)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.form:
        print(request.form)
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)

# we create a new class which inherits from a basic database model, provided by SQLAlchemy.
# This will also make SQLAlchemy create a table called book, which it will use to store our Book objects.

class Book(db.Model):
    title = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)

    def __repr__(self):
        return "<Title: {}>".format(self.title)
