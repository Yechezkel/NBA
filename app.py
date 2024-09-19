import data.loadData
from flask import Flask
from models.team_model import *
from models.player_model import *
from models.details_model import *
from models.composition_model import *
from blue_prints.player_bp import player_bp


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nba3.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()


with app.app_context():
    data.loadData.trans_data_api_to_db(2022)
    data.loadData.trans_data_api_to_db(2023)
    data.loadData.trans_data_api_to_db(2024)

app.register_blueprint(player_bp, url_prefix='/api')


@app.route('/', methods=['GET'])
def home():
    return "wellcome to NBA"

if __name__ == '__main__':
    app.run()
