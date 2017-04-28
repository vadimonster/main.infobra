import os
basedir = os.path.abspath(os.path.dirname('backend/'))
from sqlalchemy import create_engine
engine = create_engine('sqlite:///{}'.format(os.path.join(basedir, 'hasher.db')), echo=True, connect_args={'check_same_thread':False})


SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(basedir, 'hasher.db'))
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')