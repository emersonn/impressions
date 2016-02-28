from impressions import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(120))
    picture = db.Column(db.String(420))
    points = db.Column(db.Integer)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)


game_user = db.Table(
    'game_player',
    db.Column('game_id', db.Integer, db.ForeignKey('game.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
)

game_round = db.Table(
    'game_round',
    db.Column('game_id', db.Integer, db.ForeignKey('game.id')),
    db.Column('round_id', db.Integer, db.ForeignKey('round.id'))
)


class Game(db.Model):
    __tablename__ = 'game'

    id = db.Column(db.Integer, primary_key=True)

    start = db.Column(db.DateTime)

    players = db.relationship(
        'User',
        secondary=game_user,
        backref=db.backref('game', lazy='dynamic')
    )

    rounds = db.relationship(
        'Round',
        secondary=game_round,
        backref=db.backref('game', lazy='dynamic')
    )

round_image = db.Table(
    'round_image',
    db.Column('round_id', db.Integer, db.ForeignKey('round.id')),
    db.Column('image_id', db.Integer, db.ForeignKey('image.id'))
)


class Round(db.Model):
    __tablename__ = 'round'

    id = db.Column(db.Integer, primary_key=True)

    impression = db.Column(db.String(420))

    images = db.relationship(
        'Image',
        secondary=round_image,
        backref=db.backref('round', lazy='dynamic')
    )

    voter = db.Column(db.Integer, db.ForeignKey('user.id'))
    winner = db.Column(db.Integer, db.ForeignKey('user.id'))
