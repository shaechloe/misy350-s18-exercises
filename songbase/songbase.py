from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    ## return "<h1>hello shae</h1>" ##this returns html
    return render_template('index.html')


@app.route('/users/<string:username>/')
def users(username):
    #return "hello" + username
    ##return "<h1>hello %s</h1>" % username
    return render_template('user.html', uname=username)


@app.route('/songs')
def shaw_all_songs():
        songs = [
        'Paradise',
        'Yellow',
        'Viva La Vida'
        ]
        return render_template ('song-all.html', songs=songs)


@app.route('/user')
def user():
        return "this is the page for users"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
