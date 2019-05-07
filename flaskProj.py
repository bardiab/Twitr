from datetime import datetime
from flask import Flask, render_template, url_for, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'efc8c0504858d673cfedcb19002ff421'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(60), nullable=False)
#     posts = db.relationship('Post', backref='author', lazy=True)
#
#     def __repr__(self):
#         return f"User('{self.username}', '{self.email}', '{self.image_file}')"
#
# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     content = db.Column(db.Text, nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#
#     def __repr__(self):
#         return f"Post('{self.title}', '{self.date_posted}')"
#
# class Log(db.Model):
#     __tablename__ = 'logs'
#     id = db.Column(db.Integer, primary_key=True)
#     logger = db.Column(db.String(100)) #name of logger
#     level = db.Column(db.String(100)) # info, debug, or error
#     trace = db.Column(db.String(4096))
#     msg = db.Column(db.String(4096))
#     created_at = db.Column(db.DateTime, default=db.func.now())
#
#     def __init__(self, logger=None, level=None, trace=None, msg=None):
#         self.logger = logger
#         self.level = level
#         self.trace = trace
#         self.msg = msg
#
#     def __unicode__(self):
#         return self.__repr__()
#
#     def __repr__(self):
#         return "<Log: %s - %s>" % (self.created_at.strftime('%m/%d/%Y-%H:%M:%S'), self.msg[:50])

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
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
