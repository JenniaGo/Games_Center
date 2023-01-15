from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

from app.games.guessgame import guessgame
from app.games.memorygame import memorygame
from app.scores import scores

app.register_blueprint(guessgame)
app.register_blueprint(memorygame)
app.register_blueprint(scores)

