from flaskProj import app

from logging.config import dictConfig
from flaskProj import logging_config

if __name__ == '__main__':
    dictConfig(logging_config)
    app.run(debug=True)
