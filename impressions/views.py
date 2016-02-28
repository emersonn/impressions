from flask import abort
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from impressions import app
from impressions import db

from models import Game
from models import Round
from models import User


@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()


def get_game_or_abort(game_id):
    """Gets the game corresponding to the given game_id.

    Args:
        game_id: int id for the game.
            Aborts with 404 error if game does not exist.

    Returns:
        Game: Game in question.
    """

    current_game = db.session.query(Game).get(game_id)

    if not current_game:
        abort(404)

    return current_game


@app.route('/')
def index():
    """Index page of the website."""

    # TODO(Make the game)
    if request.method == 'POST':
        pass

    return render_template('static/index.html')


@app.route('/game/<game_id>')
def game(game_id):
    """Game playing page of the website given the game_id.

    Args:
        game_id: Game to play with.
            Aborts with 404 error if game does not exist.
            Redirects if the game does not have a current round.

    Returns:
        Render of the game page.
    """

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
