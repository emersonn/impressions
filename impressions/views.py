from flask import abort
from flask import redirect
from flask import render_template
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
    return render_template('static/game.html')


@app.route('/game/<game_id>/<round_id>')
def round(game_id, round_id):
    current_game = db.session.query(Game).get(game_id)
    if not current_game:
        abort(404)
    if not current_game.current_round:
        redirect(url_for('results', game_id), 303)
    # if they don't have the right round
    # if this is a post request to submit the winner
    # otherwise return the request
    pass


@app.route('/results/<game_id>')
def results(game_id):
    return render_template('static/results.html')
