import sys
import requests
from player import PlayerDAO
from datetime import datetime
from display import display_liiga_daily_stats

aika = datetime.now()
year = aika.year
month = aika.month
day = aika.day
day = day-1

def liiga_daily_stats():
    print(f"Game stats from {day}.{month}.{year}:")
    print()
    url = 'https://liiga.fi/api/v2/games'
    player_dao = PlayerDAO()
    lista = player_dao.getAll("Liiga")
    
    #Gets the page and saves the content
    page = requests.get(url)
    if page.status_code == 403:
        print("Pyyntö epäonnistui.")
        sys.exit(0)
    games = page.json()
    display_liiga_daily_stats(games, lista)
    return None


if __name__ == '__main__':
    liiga_daily_stats()



