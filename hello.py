from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()]) #Email() is a validator that checks the field’s value against a regular expression to ensure that it is a valid email address.
    submit = SubmitField('Submit')


app = Flask(__name__, template_folder='templates')
bootstrap=Bootstrap(app)
app.config['SECRET_KEY'] = 'True'

time_now = datetime.now()
date_time = time_now.strftime("%A, %B %d, %Y, %I:%M %p")


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    
    return render_template('index.html', form=form, 
                            name=session.get('name'),
                            date_time=date_time)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name, date_time=date_time)