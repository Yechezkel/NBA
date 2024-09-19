from flask import request

from data.db import db
from flask import Blueprint, jsonify

from models.details_model import Details
from models.player_model import Player

player_bp = Blueprint('players', __name__)

@player_bp.route('/player', methods=['GET'])
def get_by_position():
    position = request.args.get('position')
    season = request.args.get('season')
    if position == None:
        return jsonify({"error": "must provide position"}), 400
    if season is None:
        result = Details.query.all()
    else:
        result = Details.query.filter_by(season=season).all()
    result_list = [d.to_dict() for d in result]
    result_list = list(map(lambda d: {
            'player_id': Player.query.filter_by(player_id = d["player_id"]).first().player_name,
            'team_id': Player.query.filter_by(team_id = d["team_id"]).first().team_name,
            'season': d["season"],
            'points': d["points"],
            'position': d["position"],
            'games': d["games"],
            'two_Percent': d["two_Percent"],
            'three_Percent': d["three_Percent"],
            'atr': d["atr"],
            'ppg_ratio': d["ppg_ratio"]
        }, result_list))
    return jsonify({"data": result_list}), 200



@player_bp.route('/settings', methods=['POST'])
def add_composition():
    return "User Settings Page"

