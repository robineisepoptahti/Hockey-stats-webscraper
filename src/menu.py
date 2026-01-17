from db_conn import DB
from player import PlayerDAO
from utilities import deserialize

TABLE_STATEMENT = """
CREATE TABLE IF NOT EXISTS players(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(128) NOT NULL,
    season_points INTEGER NOT NULL,
    goals INTEGER NOT NULL,
    assists INTEGER NOT NULL,
    games INTEGER NOT NULL,
    team VARCHAR(128) NOT NULL,
    team_id VARCHAR(128) NOT NULL,
    player_id VARCHAR(128) NOT NULL,
    sp FLOAT NOT NULL,
    toi VARCHAR(128) NOT NULL,
    league VARCHAR(128) NOT NULL,
    pm INTEGER NOT NULL
);
"""
class Main:
    db: DB
    def __init__(self) -> None:
        self.db = DB()
        self.__initDatabase()
        name_list = deserialize() 
        player_dao = PlayerDAO()
        data_list = player_dao.getAll()
        #Tarkistaa onko serialisoitu nimi jo tietokannassa
        temp_name = "placeholder"
        for name in name_list:
            for data in data_list:
                #Lisätään muuttujaan, että voidaan käsitellä loopin ulkopuolellA
                temp_name = data.name
                if name == temp_name:
                    break
            if name != temp_name:
                player_dao.add_to_db(name)
        print("Initialized")
        return None
    
    def __initDatabase(self) -> None:
        cursor = self.db.conn.cursor()
        cursor.execute(TABLE_STATEMENT)
        self.db.conn.commit()
        cursor.close()
        return None
    
    #Takes player name and adds it to table
    def create(self) -> None:
        player_dao = PlayerDAO()
        player_dao.add_name()
        return None
    
    #Gets info using a DAO, as a list of player objects.
    def show(self) -> None:
        league = "first"
        player_dao = PlayerDAO()
        lista = player_dao.getAll()
        for player in lista:
            if player.games != 0:
                if player.league != league:
                    print(3 * "\n")
                    print(f"{player.league}\n")
                    print("_" * 20)
                print()
                print(f"{player.name}:   Ottelut: {player.games} Pisteet: {player.goals} + {player.assists} = {player.season_points}")
                print(f"Joukkue: {player.team}  Laukaisuprosentti: {player.sp:.2f}  Plus-miinus: {player.pm}  Peliaika (avg): {player.toi}")
                league = player.league
        return None

