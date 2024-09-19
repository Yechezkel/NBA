from data.db import db

class Team(db.Model):
    __tablename__ = 'teams'
    team_id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(80), unique=True, nullable=False)


def to_dict(self):
    return {
        'team_id': self.team_id,
        'team_name': self.team_name
    }