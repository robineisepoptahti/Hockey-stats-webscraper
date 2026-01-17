from datetime import datetime
from menu import Main
from season_stats_nhl import nhl_season_stats
from season_stats_liiga import liiga_season_stats
from daily_stats_liiga import liiga_daily_stats


########################
#######ALIOHJELMAT######
########################


##MENU PROGRAM###

def menu_loop(valinta):
    while valinta != '0':
        print()
        print()
        print("1) Näytä pelaajien viime kierroksen pisteet")
        print("2) Lisää pelaaja seurantalistaan")
        print("3) Seurattavien kauden kokonaispisteet sarjoittain")
        print("0) Lopeta ohjelma")
        valinta = int(input("Syötä luku: "))
        return valinta
    
##MAIN PROGRAM###

def main():
    print(datetime.now())
    print("Ohjelma alkaa.")
    app = Main()

    #Päivittää kauden pistetilastot 
    nhl_season_stats()
    liiga_season_stats()
    
    valinta = -1
    while valinta != 0:
        try:
            valinta = menu_loop(valinta)
            if valinta == 1:
                liiga_daily_stats()
            #Valinta  2). Syöttää pelaajan tietokantaan.
            elif valinta == 2:
                app.create()
            #Valinta  3). Näyttää listan pelaajista ja kauden pistemääristä.
            elif valinta == 3:
                nhl_season_stats()
                liiga_season_stats()
                app.show()
            elif valinta == 0:
                break
            else:
                print("Kelvoton valinta, syötä numero.")
        except ValueError:
            print("Valinnan on oltava numero.")
    print()
    print("Ohjelma lopetetaan")
    return None


#Kytkin
if __name__ == '__main__':
    main()