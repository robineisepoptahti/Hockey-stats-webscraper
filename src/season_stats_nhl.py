import requests
import sys
from player import PlayerDAO
from utilities import normalize_string




def nhl_season_stats():
    league = "NHL"
    stat_list = []
    url = f'https://api.nhle.com/stats/rest/en/skater/summary?limit=-1&cayenneExp=seasonId=20252026'
    player_dao = PlayerDAO()
    player_dao.createTable()

    lista = player_dao.getAll()

    #Gets the page and saves the content
    page = requests.get(url)
    if page.status_code == 403:
        print("Pyyntö epäonnistui, tarkista käyttökertojen määrä.")
        sys.exit(0)
    stats = page.json()

    for player in lista:
        normalized_name = normalize_string(player.name)
        for entry in stats['data']:
            fullname = entry["skaterFullName"]
            if fullname == normalized_name:
                peliaika = ((str(round(entry.get("timeOnIcePerGame")) or "Unknown")[:-2]) + ":" + str(round(entry.get("timeOnIcePerGame")) or "Unknown")[-2:])
                player_stats = {
                    "league": league,
                    "name": fullname,
                    "goals": int(entry.get("goals") or 0),
                    "assists": int(entry.get("assists") or 0),
                    "points": int(entry.get("points") or 0),
                    "games": int(entry.get("gamesPlayed") or 0),
                    "team": entry.get("teamAbbrevs") or "Unknown",
                    "sp": float(entry.get("shootingPct") or 0),
                    "pm": int(entry.get("plusMinus") or 0),
                    "toi": peliaika,
                    "tId": entry.get("teamAbbrevs") or "Unknown",
                    "pId": entry.get("playerId") or "Unknown"
                }
                stat_list.append(player_stats)
    #Lähetetään lista tietoja päivittävään metodiin
    player_dao.update(stat_list)
    return None

if __name__ == '__main__':
    nhl_season_stats()


