from flask import Flask
from flask import render_template
from livereload import Server


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index3.html')

if __name__ == '__main__':
    server = Server(app.wsgi_app)
    server.serve()