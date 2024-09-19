import sys

from data import calculator
import requests
from models.team_model import *
from models.player_model import *
from models.details_model import *
from models.composition_model import *

BASE_URL = "http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?pageSize=1000&&season="

def get_data_by_year(year: int):
    response = requests.get(BASE_URL + str(year))
    if response.status_code == 200:
        data = response.json()
        return data
    return None


def get_player_from_db(name):
    return Player.query.filter_by(player_name=name).first()

def get_team_from_db(name):
    return Team.query.filter_by(team_name=name).first()

def insertDataToDB(player_dict: dict):
    new_player = get_player_from_db(player_dict["playerName"])
    if new_player == None:
        new_player = Player(player_name = player_dict ["playerName"])
        db.session.add(new_player)
        db.session.commit()
    new_team = get_team_from_db( player_dict["team"])
    if new_team == None:
        new_team = Team(team_name = player_dict["team"])
        db.session.add(new_team)
        db.session.commit()
    new_details = Details(
        team_id = new_team.team_id,
        player_id = new_player.player_id,
        season = player_dict["season"],
        points = player_dict["points"],
        position = player_dict["position"],
        games = player_dict["games"],
        two_Percent = player_dict["twoPercent"],
        three_Percent = player_dict["threePercent"],
        atr = calculator.get_atr(player_dict["assists"], player_dict["turnovers"]),
        ppg_ratio = None
      )
    try:
        db.session.add(new_details)
        db.session.commit()
    except:
        db.session.rollback()
        # print(f"an error occured, id: {player_dict['playerId']}  season: {player_dict['season']} ")
        # print(sys.exc_info())
        # print()
    return

def trans_data_api_to_db(year: int):
    json = get_data_by_year(year)
    if json == None:
        raise Exception("the return vallue from get_data_by_year() is None")
    for player_dict in json:
        insertDataToDB(player_dict)
    return True


# if __name__ == '__main__':
#     lst = get_data_by_year(2024)
#     print(f"total: {len(lst)}")
#     lst2 = list(filter(lambda x: x["twoPercent"] == None, lst))
#     print(f"without twoPercent: {len(lst2)}")
#     lst3 = list(filter(lambda x: x["season"] != 2022, lst))
#     print(f"different year: {len(lst3)}")
#     lst4 = list(filter(lambda x: x["threePercent"] == None, lst))
#     print(f"without threePercent: {len(lst4)}")


