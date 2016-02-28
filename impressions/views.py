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
    # return render_template('')


@app.route('/game/<game_id>')
def game(game_id):
    pass


@app.route('/game/<game_id>/<round_id>')
def round(game_id, round_id):
    pass
