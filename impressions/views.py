from flask import abort
from flask import render_template

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
    pass
    # return render_template('static/index.html')


@app.route('/game/<game_id>')
def game(game_id):
    current_game = db.session.query(Game).get(game_id)
    if not current_game:
        abort(404)
    if not current_game.current_round:
        pass
        # redirect(url_for('results', game_id))
    return render_template('static/game.html')


@app.route('/game/<game_id>/<round_id>')
def round(game_id, round_id):
    pass


@app.route('/results/<game_id>')
def results(game_id):
    pass
