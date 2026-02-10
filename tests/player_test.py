from player import Player

def test_create_player():
    player = Player(1, "Test Player", 10, 5, 5, 8, "Team", "t1", "p1", 1.25, "20:00", "NHL", 2)
    assert player.name == "Test Player"
    assert player.season_points == 10
    assert player.goals == 5
