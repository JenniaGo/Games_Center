from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import INTEGER

db = SQLAlchemy()

class MemoryGame(db.Model):
    id = db.Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    score = db.Column(db.Integer)

    def __init__(self, name, score):
        self.name = name
        self.score = score

class Score(db.Model):
    id = db.Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    user_id = db.Column(db.String(255))
    score = db.Column(db.Integer)

    def __init__(self, user_id, score):
        self.user_id = user_id
        self.score = score

    def update(self):
        db.session.commit()
