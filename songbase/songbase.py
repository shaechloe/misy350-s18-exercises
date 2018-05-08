import os
from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

# setup SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)

# define database tables
class Artist(db.Model):
    __tablename__ = 'artists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    about = db.Column(db.Text)
    songs = db.relationship('Song', backref='artist', cascade="delete")


class Song(db.Model):
    __tablename__ = 'songs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    year = db.Column(db.Integer)
    lyrics = db.Column(db.Text)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))


@app.route('/')
def index():
    ## return "<h1>hello shae</h1>" ##this returns html
    return render_template('index.html')


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    if request.method == 'POST':
        first_name = request.form["first_name"]
        return render_template('form.html', first_name="first_name")


@app.route('/users/<string:username>/')
def users(username):
    #return "hello" + username
    ##return "<h1>hello %s</h1>" % username
    return render_template('user.html', uname=username)


@app.route('/user')
def user():
        return "this is the page for users"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
