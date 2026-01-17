import sys
import requests
from player import PlayerDAO
from datetime import datetime, timedelta

aika = datetime.now()
eilen_muokkaamaton = aika - timedelta(days=1)
muokattu_aika = aika.strftime("%Y-%m-%d")
eilen = eilen_muokkaamaton.strftime("%Y-%m-%d")
year = aika.year
month = aika.month
day = aika.day
day = day-1

def liiga_daily_stats():
    print(eilen)
    print(f"Game stats from {day}.{month}.{year}:")
    print()
    url = 'https://api-web.nhle.com/v1/score/{eilen}'
    player_dao = PlayerDAO()
    lista = player_dao.getAll("NHL")
    
    #Gets the page and saves the content
    page = requests.get(url)
    if page.status_code == 403:
        print("Pyyntö epäonnistui.")
        sys.exit(0)
    games = page.json()
    for entry in games:
        game = entry["start"]
        if game[0:10] == eilen:
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


liiga_daily_stats()