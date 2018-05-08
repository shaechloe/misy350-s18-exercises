from flask_script import Manager
from songbase import app, db

manager = Manager(app)


# reset the database and create some initial data
@manager.command
def deploy():
    db.drop_all()
    db.create_all()


if __name__ =='__main__':
    manager.run()
