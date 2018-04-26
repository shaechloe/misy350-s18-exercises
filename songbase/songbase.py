from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>hello shae</h1>" ##this returns html


@app.route('/user')
def user():
    return "this is the page for users"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
