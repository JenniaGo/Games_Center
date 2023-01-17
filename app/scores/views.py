from flask import render_template, request, redirect, url_for
from flask.views import MethodView
from app import db
from app.models import Score
from app.auth.models import User

class ScoreView(MethodView):

    def get(self, user_id):
        user = User.query.get(user_id)
        scores = Score.query.filter_by(user_id=user_id).all()
        return render_template('scores.html', user=user, scores=scores)

    def post(self):
        game = request.form['game']
        score = request.form['score']
        user_id = request.form['user_id']
        score = Score(user_id=user_id, game=game, score=score)
        db.session.add(score)
        db.session.commit()
        return redirect(url_for('scores.score_view', user_id=user_id))
