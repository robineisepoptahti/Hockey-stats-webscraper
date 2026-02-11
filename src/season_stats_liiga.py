import sys
import requests
from player import PlayerDAO
from datetime import datetime

def liiga_season_stats():
    date = datetime.now()
    stat_list = []
    url = f'https://www.liiga.fi/api/v2/players/stats/summed/{date.year}/{date.year}/runkosarja/true?dataType=basicStats'
    player_dao = PlayerDAO()
    lista = player_dao.getAll()
    #Gets the page and saves the content
    page = requests.get(url)
    if page.status_code == 403:
        print("Pyyntö epäonnistui, tarkista käyttökertojen määrä.")
        sys.exit(0)
    stats = page.json()
    league = "Liiga"
    #Parsing the stats
    for player in lista:
        for entry in stats:
            fullname = f"{entry['firstName']} {entry['lastName']}"
            if entry.get("timeOnIceAvg") is not None:
                peliaika = ((str(round(entry.get("timeOnIceAvg")) or "Unknown")[:-2]) + ":" + str(round(entry.get("timeOnIceAvg")) or "Unknown")[-2:])
            if fullname == player.name:
                player_stats = {
                    "league": league,
                    "name": fullname,
                    "goals": int(entry.get("goals") or 0),
                    "assists": int(entry.get("assists") or 0),
                    "points": int(entry.get("points") or 0),
                    "games": int(entry.get("playedGames") or 0),
                    "team": entry.get("teamShortName") or "Unknown",
                    "sp": float(entry.get("shotPercentage") or 0),
                    "pm": int(entry.get("plusMinus") or 0),
                    "toi": peliaika,
                    "tId": entry.get("teamId") or "Unknown",
                    "pId": entry.get("playerId") or "Unknown"
                }
                stat_list.append(player_stats)
    player_dao.update(stat_list)
    return None

if __name__ == '__main__':
    liiga_season_stats()
