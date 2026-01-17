from datetime import datetime
from menu import Operations
from season_stats_nhl import nhl_season_stats
from season_stats_liiga import liiga_season_stats
from daily_stats_liiga import liiga_daily_stats
from utilities import menu_loop

##MAIN PROGRAM###

def main():
    print(datetime.now())
    print("Ohjelma alkaa.")
    app = Operations()

    #Päivittää kauden pistetilastot 
    #nhl_season_stats()
    #liiga_season_stats()
    
    choice = -1
    while choice != 0:
        try:
            choice = menu_loop(choice)
            if choice == 1:
                liiga_daily_stats()
            #Choice  2). Inserts player to DB
            elif choice == 2:
                app.create()
            #Choice  3). Shows player season stats
            elif choice == 3:
                nhl_season_stats()
                liiga_season_stats()
                app.show()
            elif choice == 0:
                break
            else:
                print("Kelvoton valinta, syötä numero.")
        except ValueError:
            print("Valinnan on oltava numero.")
    print()
    app.end_operationn()
    print("Ohjelma suljetaan")
    return None


#Switch
if __name__ == '__main__':
    main()