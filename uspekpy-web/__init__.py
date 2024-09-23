from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/single-case')
def single():
    return render_template('single.html')


@app.route('/batch-cases')
def batch():
    return render_template('batch.html')
