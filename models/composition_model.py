from data.db import db

class Composition(db.Model):
    __tablename__ = 'compositions'
    compo_id = db.Column(db.Integer, primary_key=True)
    compo_team = db.Column(db.Integer, db.ForeignKey('teams.team_id'), nullable=False)
    pos_pg = db.Column(db.Integer, db.ForeignKey('players.player_id'), nullable=False)
    pos_sg = db.Column(db.Integer, db.ForeignKey('players.player_id'), nullable=False)
    pos_sf = db.Column(db.Integer, db.ForeignKey('players.player_id'), nullable=False)
    pos_pf = db.Column(db.Integer, db.ForeignKey('players.player_id'), nullable=False)
    pos_c  = db.Column(db.Integer, db.ForeignKey('players.player_id'), nullable=False)
