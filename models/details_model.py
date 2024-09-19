from data.db import db
from sqlalchemy import UniqueConstraint

class Details(db.Model):
    __tablename__ = 'details'
    details_id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('players.player_id'), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.team_id'), nullable=False)
    season = db.Column(db.Integer, nullable=False)
    points =db.Column(db.Integer, nullable=True)
    position = db.Column(db.String(20), nullable=True)
    games = db.Column(db.Integer, nullable=True)
    two_Percent = db.Column(db.Float, nullable=True)
    three_Percent = db.Column(db.Float, nullable=True)
    atr = db.Column(db.Float, nullable = True)
    ppg_ratio = db.Column(db.Float, nullable = True)

    __table_args__ = (
        UniqueConstraint('player_id', 'season', name='uq_player_season'),
    )

    def to_dict(self):
        return {
            'player_id': self.player_id,
            'team_id': self.team_id,
            'season': self.season,
            'points': self.points,
            'position': self.position,
            'games': self.games,
            'two_Percent': self.two_Percent,
            'three_Percent': self.three_Percent,
            'atr': self.atr,
            'ppg_ratio': self.ppg_ratio
        }