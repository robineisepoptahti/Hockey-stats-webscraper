from datetime import datetime
from src.operations import Operations
from src.player import PlayerDAO

##MAIN PROGRAM###

def test_main():
    app = Operations()

    player_dao = PlayerDAO()

    player_dao.add_to_db("Connor McDavid")

    data_list = player_dao.getAll()
    assert len(data_list) > 0
    assert any(player.name == "Connor McDavid" for player in data_list)


