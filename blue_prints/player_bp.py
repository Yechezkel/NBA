
from flask import Blueprint

player_bp = Blueprint('players', __name__)

@player_bp.route('/pr')
def profile():
    return "User Profile Page"

@player_bp.route('/settings')
def settings():
    return "User Settings Page"

