import datetime
import json

import requests

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

BING_IMAGE = 'https://api.datamarket.azure.com/Bing/Search/v1/Image?$format=json&$top=10&Query=%27{query}%27'
CREDENTIALS = 'Basic ' + (':%s' % app.config['AZURE_KEY']).encode('base64')[:-1]

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


@app.route('/', methods=['GET', 'POST'])
def index():
    """Index page of the website."""

    # TODO(Make the game)
    if request.method == 'POST':
        # print("This is the data.")
        # print(request.get_data())
        # print(request.form)
        category = request.form['category']
        players = []

        current_game = Game(start=datetime.datetime.now())

        for key in request.form.keys():
            if key != 'category':
                print(key)
                current_player = User(name=request.form[key], points=0)
                current_game.players.append(current_player)

                players.append(current_player)
                db.session.add(current_player)
        db.session.add(current_game)

        # Rounds, current_round, and redirect
        r = requests.get(BING_IMAGE.format(query=category), headers={'Authorization': CREDENTIALS})
        response = json.loads(r.text)
        results = response['d']['results']  # MediaUrl

        for result in results[:min(5, len(results))]:
            current_round = Round(
                impression=result['MediaUrl']
            )

            db.session.add(current_round)
            current_game.rounds.append(current_round)
            # print(current_game.rounds)

        db.session.add(current_game)
        db.session.commit()

        current_game.current_round = current_game.rounds[0].id
        db.session.commit()

        # print("Finished making a game.")
        return redirect(url_for('game', game_id=current_game.id))
        # return redirect('/game/' + str(current_game.id))
    return render_template('index.html')


@app.route('/game/<game_id>', methods=['GET', 'POST'])
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
    # print(current_game.rounds)
    # print(current_game.current_round)
    if current_game.current_round is None:
        return redirect(url_for('results', game_id=game_id), 303)

    if request.method == 'POST':
        # TODO(There should be a lot more cases for safety, and security.)
        if 'playervote' not in request.form:
            abort(406)

        current_round = db.session.query(Round).get(current_game.current_round)

        if not current_round:
            abort(404)

        winner_id = request.form['playervote']
        winner = db.session.query(User).get(winner_id)

        if not winner:
            abort(404)

        current_round.winner = winner_id
        winner.points += 1

        if (
            current_game.rounds.index(current_round) + 1 >=
            len(current_game.rounds)
        ):
            current_game.current_round = None
            return redirect(url_for('results', game_id=game_id), 303)
        current_game.current_round = (
            current_game.rounds[current_game.rounds.index(current_round) + 1].id
        )

        db.session.add(current_game)
        db.session.add(winner)
        db.session.add(current_round)
        db.session.commit()

    current_round = db.session.query(Round).get(current_game.current_round)
    print(current_round.impression)
    return render_template(
        'game.html',
        round=current_round,
        game=current_game
    )


@app.route('/results/<game_id>')
def results(game_id):
    return "poop"

    current_game = get_game_or_abort(game_id)

    return render_template('static/results.html', current_game)
