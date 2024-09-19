from flask import Flask
from models.team_model import *
from models.player_model import *
from models.details_model import *
from models.composition_model import *
from blue_prints.player_bp import player_bp



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nba.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


with app.app_context():
    db.create_all()

app.register_blueprint(player_bp, url_prefix='/p')


@app.route('/', methods=['GET'])
def home():
    return "Home Page"

if __name__ == '__main__':
    app.run()
    # with app.app_context():
    #     new_team = Team(team_name="qqqqqqq")
    #     db.session.add(new_team)
    #     db.session.commit()
