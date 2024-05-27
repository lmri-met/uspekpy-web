from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/uspekpy')
def uspekpy():
    return render_template('uspekpy.html')


@app.route('/user-guide')
def user_guide():
    return render_template('user_guide.html')
