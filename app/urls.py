from flask import Blueprint, render_template
from flask_login import login_required
from app.scores.views import ScoreView

scores_bp = Blueprint('scores', __name__)

score_view = ScoreView.as_view('score_view')

scores_bp.add_url_rule('/score/<int:user_id>/', view_func=score_view, methods=['GET'])
scores_bp.add_url_rule('/score/', view_func=score_view, methods=['POST'])
