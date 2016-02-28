from flask import abort
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from chemy import app
from chemy import db

from models import Game
from models import Round
from models import User


@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()


def get_game_or_abort(game_id):
    current_game = db.session.query(Game).get(game_id)

    if not current_game:
        abort(404)


@app.route('/')
def index():
    return render_template('static/index.html')


@app.route('/game/<game_id>')
def game(game_id):
    current_game = get_game_or_abort(game_id)
    if not current_game.current_round:
        redirect(url_for('results', game_id), 303)

    if request.method == 'POST':
        # TODO(There should be a lot more cases for safety, and security.)
        if 'round_id' not in request.form or 'winner_id' not in request.form:
            abort(406)

        current_round = (
            db.session
            .query(Round).get(request.form['round_id'])
        )

        if not current_round:
            abort(404)

        winner_id = request.form['winner_id']
        winner = db.session.query(User).get(winner_id)

        if not winner:
            abort(404)

        current_round.winner = winner

        if (
            current_game.index(current_round) + 1 >=
            len(current_game.rounds)
        ):
            current_game.current_round = None
            redirect(url_for('results', game_id), 303)
        current_game.current_round = (
            current_game.rounds[current_game.index(current_round) + 1]
        )

    current_round = current_game.current_round
    return render_template('static/game.html', {
        'round': current_round, 'game': current_game
    })


@app.route('/results/<game_id>')
def results(game_id):
    current_game = get_game_or_abort(game_id)

    return render_template('static/results.html', current_game)
