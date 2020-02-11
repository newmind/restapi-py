from model import db
from datetime import datetime
from sqlalchemy.dialects.mysql import INTEGER


class Tournament(db.Model):
    __tablename__ = 'tournament'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    gameName = db.Column(db.String(100), nullable=False)
    playerCount = db.Column(INTEGER(unsigned=True), nullable=False, default=0)
    location = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100))
    startAt = db.Column(db.DateTime)
    endAt = db.Column(db.DateTime)

    def as_dict(self):
        return dict((c.name,
                     getattr(self, c.name))
                     for c in self.__table__.columns)


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    author_email = db.Column(db.String(100), nullable=False)
    created_time = db.Column(db.DateTime, nullable=False, default=datetime.now)


class Cats(db.Model):
    __tablename__ = 'cats'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Integer)
    breed = db.Column(db.String(100))
