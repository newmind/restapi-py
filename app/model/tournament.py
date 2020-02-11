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
        return dict(
            (c.name, getattr(self, c.name))
            for c in self.__table__.columns)
