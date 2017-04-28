import datetime

from model import Diez, Data
from sqlalchemy.orm import sessionmaker

import config

engine = config.engine
Session = sessionmaker()
session = Session(bind=engine)
now_time = datetime.datetime.now()


class diez:
    def __init__(self):
        pass
    def check(hashTag):
        checker = session.query(Diez).filter_by(hashtag=hashTag).first()
        return checker
    def append(hashTag):
        add_hash = Diez(hashTag)
        session.add(add_hash)
        session.commit()
        return True

class data:
    def __init__(self):
        pass
    def check(id_hash, photo, text):
        checker = session.query(Data).filter_by(id_hash=id_hash,
                                                photo=photo, text=text).first()
        return checker
    def append(id_hash, societe, photo, text):
        add_data = Data(id_hash, societe, now_time.strftime("%d.%m.%Y %I:%M %p"), photo, text)
        session.add(add_data)
        session.commit()
        return True
