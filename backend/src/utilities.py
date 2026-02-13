import unicodedata

#Apufunktioita / Utilities
from pathlib import Path

def ask_name() -> str:
    while(True): 
        name_to_list = input("Anna pelaajan nimi (Etunimi Sukunimi): ")
        if name_to_list.isalnum() == True:
            print("Muista kirjoittaa sekä etu ja sukunimi, välilyöntiä käyttäen.")
        else:
            return name_to_list

    

def normalize_string(s) -> str:
    #.encode - > .decode poistaa turhia merkkejä, tosin tässä takoituksessa niitä tuskin esiintyy.
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode("ascii")

