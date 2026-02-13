# Displays the stats in CLI
from datetime import datetime, timedelta
aika = datetime.now()
yesteday_unmodified = aika - timedelta(days=1)
yesterday = yesteday_unmodified.strftime("%Y-%m-%d")

#Uses the Player object list to display season stats
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


# Displays the daily stats in CLI. Finds all players for the teams that played yesterday, even those who haven't played.
#That is why we exclude all players with no points in the end.
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
                elif player.team_id == away[0:9]:
                    where = "awayTeam"   
                else:       
                    continue
                goals = 0
                primary_assists = 0
                secondary_assists = 0
                for goal in entry[where]["goalEvents"]:
                    if str(goal["scorerPlayerId"]) == player.player_id:  
                        goals = goals + 1
                    for assist in goal["assistantPlayerIds"]:
                        if str(assist) == player.player_id:
                            if goal["assistantPlayerIds"].index(assist) == 1:
                                secondary_assists = secondary_assists + 1
                            else:
                                primary_assists = primary_assists + 1 
                    assist = primary_assists + secondary_assists
                #The API doesn't provide a roster to compare against (only teams), so we exclude players with no points
                if goals + assist > 0:
                    print(f"{player.name}: {goals} + {assist}, primary assists: {primary_assists}")
    return None



