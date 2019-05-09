from flask import Flask, render_template, request, redirect, url_for, flash, session, g
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
import jwt
import logging
from logr import *

app = Flask(__name__)

app.config['SECRET_KEY'] = 'efc8c0504858d673cfedcb19002ff421'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Must import the models after we create the database
from models import *

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Please log in first!', 'info')
            return redirect(url_for('login'))
    return decorated_function

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/home')
@login_required
def home():
    posts = db.session.query(Post).all()
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] !=  'bardia' or request.form['password'] != 'lol':
            error = 'Invalid username/password. Please try again.'
            logger.error('Invalid Credentials.')
            flash (error, 'danger')
        else:
            flash ('Successful login', 'success')
            session['logged_in'] =  True
            return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        db.session.add(Post(request.form['title'], request.form['content']))
        flash ('Posted!', 'success')
        return redirect(url_for('home'))
    return render_template('post.html')

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('Successfully logged out.', 'info')
    return redirect(url_for('welcome'))


from flask_wtf.csrf import CSRFProtect
import traceback
import logging

if __name__ == '__main__':
    # Customizing logging handler to store into database
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    #ch = console handler
    ch = SQLAlchemyHandler()
    ch.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)

    loggers = [logger,
               logging.getLogger('werkzeug'),
               logging.getLogger('sqlalchemy'),
               logging.getLogger('flask.app')]

    #add ch to logger
    for l in loggers:
        l.addHandler(ch)

    csrf = CSRFProtect()
    csrf.init_app(app)

    app.run(debug=True)
