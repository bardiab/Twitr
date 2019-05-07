import logging
import traceback
from flask_wtf.csrf import CSRFProtect
import transaction

from models import Log
from flaskProj import db

class SQLAlchemyHandler(logging.Handler):
    # A very basic logger that commits a LogRecord to the SQL db
    def emit(self, record):
        trace = None
        exc = record.__dict__['exc_info']
        if exc:
            trace = traceback.format_exc()
        log = Log(
            logger=record.__dict__['name'],
            level=record.__dict__['levelname'],
            trace=trace,
            msg=record.__dict__['msg'],)
        db.session.add(log)
        db.session.commit()

#create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create console handler and set level to INFO
ch = SQLAlchemyHandler()
ch.setLevel(logging.INFO)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# add formatter to ch
ch.setFormatter(formatter)

loggers = [logger,
            logging.getLogger('werkzeug'),
            logging.getLogger('sqlalchemy'),
            logging.getLogger('flask.app')]

# add ch to logger
for l in loggers:
    l.addHandler(ch)

csrf = CSRFProtect()

if __name__ == '__main__':
    csrf.init_app(app)
    logger.critical('TEST CRITICAL ERROR')
    app.run(host=config['ENV']['HOST'])
