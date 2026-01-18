# Displays the stats in CLI
from datetime import datetime, timedelta


aika = datetime.now()
yesteday_unmodified = aika - timedelta(days=1)
yesterday = yesteday_unmodified.strftime("%Y-%m-%d")


def display_season_stats(lista) -> None:
    league = "first"
    for player in lista:
        if player.games != 0:
            if player.league != league:
                print(3 * "\n")
                print(f"{player.league}\n")
                print("_" * 20)
            print()
            print(f"{player.name}:   Ottelut: {player.games} Pisteet: {player.goals} + {player.assists} = {player.season_points}")
            print(f"Joukkue: {player.team}  Laukaisuprosentti: {player.sp:.2f}  Plus-miinus: {player.pm}  Peliaika (avg): {player.toi}")
            league = player.league
    return None


def display_liiga_daily_stats(games, lista) -> None:
    for entry in games:
        game = entry["start"]
        if game[0:10] == yesterday:
            home = entry["homeTeam"]["teamId"]
            away = entry["awayTeam"]["teamId"]
            for player in lista:
                where = "ignore"
                if player.team_id == home[0:9]:
                    where = "homeTeam"
                if player.team_id == away[0:9]:
                    where = "awayTeam"   
                if where != "ignore":         
                    goals = 0
                    Passists = 0
                    Sassists = 0
                    for goal in entry[where]["goalEvents"]:
                        if str(goal["scorerPlayerId"]) == player.player_id:  
                            goals = goals + 1
                        for assist in goal["assistantPlayerIds"]:
                            if str(assist) == player.player_id:
                                if goal["assistantPlayerIds"].index(assist) == 1:
                                    Sassists = Sassists + 1
                                else:
                                    Passists = Passists + 1 
                        assist = Passists + Sassists
                    print(f"{player.name}: {goals} + {assist}, primary assists: {Passists}")
    return None



