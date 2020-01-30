from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render'Index Page'

@app.route('/about')
def about():
    return 'About page'