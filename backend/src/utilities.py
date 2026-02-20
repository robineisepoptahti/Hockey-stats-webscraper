import unicodedata

#Apufunktioita / Utilities
from pathlib import Path



def normalize_string(s) -> str:
    #.encode - > .decode poistaa turhia merkkejä, tosin tässä takoituksessa niitä tuskin esiintyy.
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode("ascii")

