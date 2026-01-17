import unicodedata

#Apufunktioita / Utilities

def askName() -> str:
    while(True): 
        nimi_listaan = input("Lisää pelaajan nimi (Etunimi Sukunimi): ")
        if nimi_listaan.isalnum() == True:
            print("Muista kirjoittaa sekä etu ja sukunimi, välilyöntiä käyttäen.")
        else:
            return nimi_listaan

def serialize(name) -> None:
    with open("../data/players.txt", 'a', encoding="UTF-8") as f:
        f.write(f"{name}\n")
    return None


def deserialize() -> list[str]:
    with open("../data/players.txt", 'r', encoding="UTF-8") as f:
        lista = [line.strip() for line in f.readlines()]
    return lista


def normalize_string(s) -> str:
    #.encode - > .decode poistaa turhia merkkejä, tosin tässä takoituksessa niitä tuskin esiintyy.
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode("ascii")



##MENU LOOP PROGRAM###
def menu_loop(choice):
    try:
        while choice != '0':
            print()
            print()
            print("1) Näytä pelaajien viime kierroksen pisteet")
            print("2) Lisää pelaaja seurantalistaan")
            print("3) Seurattavien kauden kokonaispisteet sarjoittain")
            print("0) Lopeta ohjelma")
            choice = int(input("Syötä luku: "))
            return choice
    except ValueError:
        print("Valinnan on oltava numero.")
        return None