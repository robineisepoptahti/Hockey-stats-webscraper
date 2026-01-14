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
    with open("players.txt", 'a', encoding="UTF-8") as f:
        f.write(f"{name}\n")
    return None


def deserialize() -> list[str]:
    with open("players.txt", 'r', encoding="UTF-8") as f:
        lista = [line.strip() for line in f.readlines()]
    return lista


def normalize_string(s) -> str:
    #.encode - > .decode poistaa turhia merkkejä, tosin tässä takoituksessa niitä tuskin esiintyy.
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode("ascii")