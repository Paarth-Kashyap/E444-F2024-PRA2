from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = EmailField('What is your UofT email?', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')

app = Flask(__name__, template_folder='templates')
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'True'

time_now = datetime.now()
date_time = time_now.strftime("%A, %B %d, %Y, %I:%M %p")

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        email = form.email.data
        if 'utoronto' not in email:
            flash('Please enter a valid UofT email address.', 'warning')
            return redirect(url_for('index'))

        old_name = session.get('name')
        old_email = session.get('email')

        # Check for name change
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')

        # Check for email change
        if old_email is not None and old_email != email:
            flash('Looks like you have changed your email!')

        session['name'] = form.name.data
        session['email'] = email
        return redirect(url_for('success'))

    return render_template('index.html', form=form, 
                           name=session.get('name'),
                           date_time=date_time)

@app.route('/success')
def success():
    name = session.get('name')
    email = session.get('email')
    return render_template('success.html', name=name, email=email, date_time=date_time)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name, date_time=date_time)

if __name__ == '__main__':
    app.run(debug=True)
