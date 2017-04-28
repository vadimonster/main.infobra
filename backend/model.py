from sqlalchemy import Integer, Column, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

import config

Base = declarative_base()
engine = config.engine
metadata = MetaData()

class Diez(Base):
    __tablename__ = 'hashtag'

    id = Column(Integer, primary_key=True, autoincrement=True)
    hashtag = Column(String(255))

    def __init__(self, hashtag):
        self.hashtag = hashtag

    def __repr__(self):
        return "<Diez(id={}, hashtag={})>".format(self.id, self.hashtag)

class Data(Base):
    __tablename__ = 'data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_hash = Column(Integer)
    societe = Column(Integer)
    date = Column(String(50))
    photo = Column(String(500))
    text = Column(String(2056))

    def __init__(self, id_hash, societe, date, photo, text):
        self.id_hash = id_hash
        self.societe = societe
        self.date = date
        self.photo = photo
        self.text = text

    def __repr__(self):
        return "<Data(id={}, id_hash={}, societe={}, date={}, photo={}, text={})>".format(self.id, self.id_hash, self.societe,
                                                                                 self.date, self.photo, self.text)



Base.metadata.create_all(engine)

