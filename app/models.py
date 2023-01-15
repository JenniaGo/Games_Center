from app import db

class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    game = db.Column(db.String(20))
    score = db.Column(db.Integer)

    def __init__(self, user_id, game, score):
        self.user_id = user_id
        self.game = game
        self.score = score


class Guess(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    guess = db.Column(db.String(20))
    result = db.Column(db.String(20))

    def __init__(self, user_id, guess, result):
        self.user_id = user_id
        self.guess = guess
        self.result = result


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    email = db.Column(db.String(20))
    scores = db.relationship('Score', backref='user', lazy=True)
    guesses = db.relationship('Guess', backref='user', lazy=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email
