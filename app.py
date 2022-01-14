# from crypt import methods
# import urllib.request
# from urllib im port request
from flask import *
# from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask import render_template


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5433/flaskmovie'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/')
def index():
    return render_template('register.html')


@app.route('/register', methods=['POST'])
def register():
    user = User(request.form['username'], request.form['email'])
    db.session.add(user)
    db.session.commit()


if __name__ == "__main__":
    app.run()
