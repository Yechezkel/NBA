from data.db import db
from sqlalchemy import UniqueConstraint

class Details(db.Model):
    __tablename__ = 'details'
    details_id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('players.player_id'), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.team_id'), nullable=False)
    season = db.Column(db.Integer, nullable=False)
    points =db.Column(db.Integer, nullable=False)
    position = db.Column(db.String(20), nullable=False)
    games = db.Column(db.Integer, nullable=False)
    two_Percent = db.Column(db.Float, nullable=False)
    three_Percent = db.Column(db.Float, nullable=False)
    atr = db.Column(db.Float, nullable = True)
    ppg_ratio = db.Column(db.Float, nullable = True)

    __table_args__ = (
        UniqueConstraint('player_id', 'season', name='uq_player_season'),
    )