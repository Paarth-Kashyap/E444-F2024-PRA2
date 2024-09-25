from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from datetime import datetime


app = Flask(__name__, template_folder='templates')
bootstrap=Bootstrap(app)

time_now = datetime.now()
date_time = time_now.strftime("%A, %B %d, %Y, %I:%M %p")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name, date_time=date_time)