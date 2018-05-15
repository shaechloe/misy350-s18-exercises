import os
from flask import Flask, render_template, request, flash, redirect, url_for
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

@app.route('/artists')
def all_artists():
    artists = Artist.query.all()
    return render_template('all-artists.html', artists=artists)


@app.route('/')
def index():
    ## return "<h1>hello shae</h1>" ##this returns html
    return render_template('index.html')


@app.route('/artist/add', methods=['GET', 'POST'])
def add_artists():
    if request.method == 'GET':
        return render_template('artist-add.html')
    if request.method == 'POST':
        # get data from the form
        name = request.form['name']
        about = request.form['about']

        # insert the data into the database
        artist = Artist(name=name, about=about)
        db.session.add(artist)
        db.session.commit()
        return redirect(url_for('all-artists'))


@app.route('/api/artist/add', methods=['POST'])
def add_ajax_artists():
    # get data from the form
    name = request.form['name']
    about = request.form['about']

    # insert the data into the database
    artist = Artist(name=name, about=about)
    db.session.add(artist)
    db.session.commit()
    # flash message type: success, info, warning, and danger from bootstrap
    flash('Artist Inserted', 'success')
    return jsonify({"id": str(artist.id), "name": artist.name})


@app.route('/artist/edit/<int:id>', methods=['GET', 'POST'])
def edit_artist(id):
    artist = Artist.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('artist-edit.html', artist=artist)
    if request.method == 'POST':
        # update data based on the form data
        artist.name = request.form['name']
        artist.about = request.form['about']
        # update the database
        db.session.commit()
        return redirect(url_for('all-artists'))


@app.route('/artist/delete/<int:id>', methods=['GET', 'POST'])
def delete_artist(id):
    artist = Artist.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('artist-delete.html', artist=artist)
    if request.method == 'POST':
        # delete the artist by id
        # all related songs are deleted as well
        db.session.delete(artist)
        db.session.commit()
        return redirect(url_for('all-artists'))


@app.route('/api/artist/<int:id>', methods=['DELETE'])
def delete_ajax_artist(id):
    artist = Artist.query.get_or_404(id)
    db.session.delete(artist)
    db.session.commit()
    return jsonify({"id": str(artist.id), "name": artist.name})


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


@app.route('/artist/edit/<int:id>/')
def artist_edit(id):
    artist = Artist.query.filter_by(id=id).first()
    artist.about = "this is shae"
    db.session.commit()

    return "this is artist %d updated" % id
    #return render_template('all-artists.html')
    # return render_template('user.html', uname=username)


@app.route('/user')
def user():
        return "this is the page for users"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
