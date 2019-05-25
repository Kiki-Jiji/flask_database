# FLASK

This is a test app which sets up a SQL database

# Data Base setup
Most of our code needs to be run every time we use our application. We need to run some one-off setup code though. Run the following commands in a Python shell in your project directory in order to create our database and create the book table where we'll store our books. You can start a Python shell by running python3 in your console (making sure you are in the project directory).

>>> from website import db
>>> db.create_all()
>>> exit()
