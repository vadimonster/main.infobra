import os
basedir = os.path.abspath(os.path.dirname(__file__))
from sqlalchemy import create_engine
engine = create_engine('sqlite:///{}'.format(os.path.join(basedir, 'hasher.db')), echo=True, connect_args={'check_same_thread':False})

consumer_key = 'qhDs03lq4a0vcQwMHGFgmHJqy'
consumer_secret = 'P0XhxLjcqpLTDgSqdsbgivflJnAz1APx8DXF7TTvLPK2xfugyI'
access_token_key ='64750534-oIbnXDbTRZy3mG2ERJHdWKpX1kJb8EHICNK1ro8xP'
access_token_secret = 'csNQo14P6Bzvw41TzBfUE5JtknEahGRFskUft7hxISfL2'