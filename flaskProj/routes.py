from flask import render_template, url_for, request, flash, redirect
from flaskProj import app
from flaskProj.forms import RegistrationForm, LoginForm
from flaskProj.models import User, Post, Log

twits = [
    {
        'user': 'Bardia',
        'handle': 'bardiab',
        'content' : 'wow f lask is cool',
        'date_posted': 'May 7, 2019'
    },
    {
        'user': 'Kimia',
        'handle': 'kimkam',
        'content': 'i know right',
        'date_posted': 'May 22, 2019'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=twits)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    # generate a flash message to send a one time alert
    if form.validate_on_submit():
        flash(f'Succesfully registered an account for {form.username.data}.', 'success')
        # redirect user to home page
        return redirect(url_for('home'))
    else:
        flash('Failed to log in.', 'danger')
        app.logger.info(f'Failed to register user {form.username.data}.')
        abort(401)
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Sucessfully logged in.', 'success')
        return redirect(url_for('home'))
    else:
        flash('Unsuccessful login. Please check username and password', 'danger')
        app.logger.info(f'Failed to log in to user {form.username.data}.')
        abort(401)
    return render_template('login.html', title='Login', form=form)
