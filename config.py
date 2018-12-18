import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG=True
    SECRET_KEY='123'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
            'sqlite:///' + os.path.join( basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
