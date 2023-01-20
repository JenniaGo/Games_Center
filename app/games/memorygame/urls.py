from flask import render_template, request, redirect, url_for, flash, make_response
from .models import MemoryGame, Score
from .forms import MemoryForm
import random
from . import app

@app.route('/memorygame', methods=['GET', 'POST'])
def memorygame():
    form = MemoryForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            selected_cards = form.selected_cards.data
            secret_cards = request.cookies.get('secret_cards')
            if selected_cards == secret_cards:
                flash('Congratulations! You have matched all the cards.', 'success')
                score = Score.query.filter_by(user_id=request.cookies.get('user_id')).first()
                score.score += 1
                score.update()
                secret_cards = random.sample(range(1,9), 4)
                return redirect(url_for('memorygame'))
            else:
                flash('Sorry! The cards you have selected are not matching. Please try again.', 'danger')
        else:
            flash('Invalid Input', 'danger')
    secret_cards = random.sample(range(1,9), 4)
    resp = make_response(render_template('memorygame.html', form=form, cards=range(1,9)))
    resp.set_cookie('secret_cards', str(secret_cards))
