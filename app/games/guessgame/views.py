from flask import Flask, render_template, request, redirect, url_for, flash
from .models import GuessGame, Score
from .forms import GuessForm
import random

app = Flask(__name__)

@app.route('/guessgame', methods=['GET', 'POST'])
def guessgame():
    form = GuessForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            guess_number = form.guess_number.data
            secret_number = request.cookies.get('secret_number')
            if guess_number == secret_number:
                flash('Congratulations! You guessed the correct number.', 'success')
                score = Score.query.filter_by(user_id=request.cookies.get('user_id')).first()
                score.score += 1
                score.update()
                secret_number = random.randint(1,100)
                return redirect(url_for('guessgame'))
            elif guess_number > secret_number:
                flash('Your guess is too high. Please try again.', 'danger')
            else:
                flash('Your guess is too low. Please try again.', 'danger')
        else:
            flash('Invalid Input', 'danger')
    secret_number = random.randint(1,100)
    resp = make_response(render_template('guessgame.html', form=form))
    resp.set_cookie('secret_number', str(secret_number))
    return resp

if __name__ == '__main__':
    app.run(debug=True)
