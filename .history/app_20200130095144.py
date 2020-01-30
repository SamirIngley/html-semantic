from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name=name)

@app.route('/about')
def about():
    return 'About page'