from data.db import db

class Player(db.Model):
    __tablename__ = 'players'
    player_id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(80), unique=True, nullable=False)
    details = db.relationship('Details', backref='player', foreign_keys='Details.player_id')

    def to_dict(self):
        return {
            'player_id': self.player_id,
            'player_name': self.player_name
        }