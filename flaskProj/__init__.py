from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging

app = Flask(__name__)

app.config['SECRET_KEY'] = 'efc8c0504858d673cfedcb19002ff421'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

from flaskProj import routes

####
logging_config = dict(
    version=1,
    formatters={
        'simple': {'format':'%(levelname)s %(asctime)s { module name : %(module)s Line no : %(lineno)d} %(message)s'}
    },
    handlers={
        'console': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logger.log',
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'level': 'DEBUG',
            'formatter': 'simple',
            'encoding': 'utf8'
            }
    },

    root={
        'handlers': ['console'],
        'level': logging.DEBUG,
    },
)
