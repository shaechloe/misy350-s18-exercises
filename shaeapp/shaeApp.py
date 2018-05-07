from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    ## return "<h1>hello shae</h1>" ##this returns html
    return render_template('index.html')


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/users/<string:username>/')
def users(username):
    #return "hello" + username
    ##return "<h1>hello %s</h1>" % username
    return render_template('users.html', uname=username)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
