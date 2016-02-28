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


@app.route('/')
def index():
    return render_template('static/index.html')


@app.route('/game/<game_id>')
def game(game_id):
    current_game = db.session.query(Game).get(game_id)
    if not current_game:
        abort(404)
    if not current_game.current_round:
        redirect(url_for('results', game_id), 303)
    if request.method == 'POST':
        # TODO(There should be a lot more cases for safety, and security.)
        if 'round_id' in request.form and 'winner_id' in request.form:
            current_round = (
                db.session
                .query(Round).get(request.form['round_id'])
            )
            if not current_round:
                abort(404)
            # TODO(Should check whether the winner ID exists in both ways)
            winner_id = request.form['winner_id']
            current_round.winner = current_game.players[winner_id]

            # current_round needs .indexFor()
            if current_game.current_round + 1 >= len(current_game.rounds):
                redirect(url_for('results', game_id), 303)
            current_game.current_round = pass
        else:
            abort(406)

    current_round = current_game.current_round
    return render_template('static/game.html')

"""
@app.route('/game/<game_id>/<round_id>')
def round(game_id, round_id):
    current_game = db.session.query(Game).get(game_id)
    if not current_game:
        abort(404)
    if not current_game.current_round:
        redirect(url_for('results', game_id), 303)

    current_round = db.session.query(Round).get(round_id)
    if not current_round:
        abort(404)
    if current_game.current_round != current_round:
    # if this is a post request to submit the winner
    # otherwise return the request
    pass
"""


@app.route('/results/<game_id>')
def results(game_id):
    return render_template('static/results.html')
