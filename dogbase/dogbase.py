import os
from flask import Flask, session, render_template, request, flash, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess secure key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# setup SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)


# define database tables
class Group(db.Model):
    __tablename__ = 'group'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    about = db.Column(db.Text)
    breed = db.relationship('Breed', backref='group', cascade="delete")


class Breed(db.Model):
    __tablename__ = 'breed'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    size = db.Column(db.String(64))
    color = db.Column(db.String(64))
    description = db.Column(db.Text)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/group')
def show_all_groups():
    group = Group.query.all()
    return render_template('group-all.html', group=group)


@app.route('/group/add', methods=['GET','POST'])
def add_group():
    if request.method == 'GET':
        return render_template('group-add.html')
    if request.method == 'POST':
        # get data from the form
        name = request.form['name']
        about = request.form['about']

        # insert the data into the database
        group = Group(name=name, about=about)
        db.session.add(group)
        db.session.commit()
        return redirect(url_for('show_all_groups'))


@app.route('/ajax/group/add', methods=['POST'])
def add_ajax_group():
    # get data from the form
    name = request.form['name']
    about = request.form['about']

    # insert the data into the database
    Group = Group(name=name, about=about)
    db.session.add(group)
    db.session.commit()
    # flash message type: success, info, warning, and danger from bootstrap
    flash('Group Inserted', 'success')
    return jsonify({"id": str(group.id), "name": group.name})


@app.route('/group/edit/<int:id>', methods=['GET', 'POST'])
def edit_group(id):
    group = Group.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('group-edit.html', group=group)
    if request.method == 'POST':
        # update data based on the form data
        group.name = request.form['name']
        group.about = request.form['about']
        # update the database
        db.session.commit()
        return redirect(url_for('show_all_groups'))


@app.route('/group/delete/<int:id>', methods=['GET', 'POST'])
def delete_group(id):
    group = Group.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('group-delete.html', group=group)
    if request.method == 'POST':
        # delete the groups by id
        # all related breeds are deleted as well
        db.session.delete(group)
        db.session.commit()
        return redirect(url_for('show_all_groups'))


@app.route('/ajax/group/<int:id>', methods=['DELETE'])
def delete_ajax_group(id):
    group = Group.query.get_or_404(id)
    db.session.delete(group)
    db.session.commit()
    return jsonify({"id": str(group.id), "name": group.name})


@app.route('/breed')
def show_all_breeds():
    breed = Breed.query.all()
    return render_template('breed-all.html', breed=breed)


@app.route('/breed/add', methods=['GET', 'POST'])
def add_breeds():
    if request.method == 'GET':
        group = Group.query.all()
        return render_template('breed-add.html', group=group)
    if request.method == 'POST':
        # get data from the form
        name = request.form['name']
        size = request.form['size']
        colors = request.form['colors']
        description = request.form['description']
        group_name = request.form['group']
        group = Group.query.filter_by(name=group_name).first()
        breed = Breed(name=name, size=size, colors=colors, description=description, group=group )

        # insert the data into the database
        db.session.add(breed)
        db.session.commit()
        return redirect(url_for('show_all_breeds'))


@app.route('/breed/edit/<int:id>', methods=['GET', 'POST'])
def edit_breed(id):
    breed = Breed.query.filter_by(id=id).first()
    group = Group.query.all()
    if request.method == 'GET':
        return render_template('breed-edit.html', breed=breed, group=group)
    if request.method == 'POST':
        # update data based on the form data
        breed.name = request.form['name']
        breed.size = request.form['size']
        breed.colors = request.form['colors']
        breed.description = request.form['description']
        group_name = request.form['group']
        group = Group.query.filter_by(name=group_name).first()
        breed.groups = group
        # update the database
        db.session.commit()
        return redirect(url_for('show_all_breeds'))


@app.route('/breed/delete/<int:id>', methods=['GET', 'POST'])
def delete_breed(id):
    breed = Breed.query.filter_by(id=id).first()
    group = Group.query.all()
    if request.method == 'GET':
        return render_template('breed-delete.html', breed=breed, group=group)
    if request.method == 'POST':
        db.session.delete(breed)
        db.session.commit()
        return redirect(url_for('show_all_breeds'))


@app.route('/ajax/breed/<int:id>', methods=['DELETE'])
def delete_ajax_breed(id):
    breed = Breed.query.get_or_404(id)
    db.session.delete(breed)
    db.session.commit()
    return jsonify({"id": str(breed.id), "name": breed.name})


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':


    app.run()
