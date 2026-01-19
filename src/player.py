from dataclasses import dataclass
from db.db_conn import DB
from utilities import askName, serialize
from db.queries import PlayerQueries

#Model
@dataclass
class Player:
    id: int | None
    name: str
    season_points: int
    goals: int
    assists: int
    games: int
    team: str
    team_id: str
    player_id: str
    sp: float
    toi: str
    league: str
    pm: int

#Dummy for testing
@staticmethod
def createPlayer() -> "Player":
    player = Player(None, 'Masi', 6)
    return player


#DAO
class PlayerDAO:
    db: DB
    def __init__(self) -> None:
        self.db = DB()
        return None
    def createTable(self) -> None:
        cursor = self.db.conn.cursor()
        cursor.execute(PlayerQueries.TABLE_STATEMENT)
        self.db.conn.commit()
        cursor.close()
        return None
    def insert(self, player: Player) -> None:
        pass

    
    def getAll(self, league=None) -> list[Player]:
        cursor = self.db.conn.cursor()
        #Which league to fetch from, everything if no league param is sent
        if league is not None:
            cursor.execute(PlayerQueries.SELECT_LEAGUE_STATEMENTS, (league,))
        else:
            print("____")
            cursor.execute(PlayerQueries.SELECT_STATEMENTS)
        records = cursor.fetchall()
        #Test print of fetched list (for debug)
        #print(records)
        players: list[Player] = []
        for record in records:
            player = Player(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10], record[11], record[12])
            players.append(player)
        cursor.close()
        return players
    
    
    def update(self, l) -> None:
        cursor = self.db.conn.cursor()
        for player in l:
            record_data = (player["points"], player["goals"], player["assists"], player["games"], player["league"], player["team"], player["sp"], player["pm"], player["toi"], player["tId"], player["pId"], player["name"])
            cursor.execute(PlayerQueries.UPDATE_STATEMENT, record_data)
            self.db.conn.commit()
        cursor.close()
        return None 
    


    def add_name(self) -> None:
        nimi_listaan = askName()    
        #Fetaches names from DB and checks for duplicates
        player_dao = PlayerDAO()
        lista = player_dao.getAll()
        if lista:
            for player in lista:
                if player.name == nimi_listaan:
                    print("Nimi on jo listassa.")
                    return None
        #Serializes the name as a key, and adds to DB
        serialize(nimi_listaan)
        player_dao.add_to_db(nimi_listaan)
        print()
        print(f"Seurataan pelaajaa {nimi_listaan}")
        print("Pelaaja lisätty listaan.")
        return None


    def add_to_db(self, nimi_listaan: None) -> None:
        cursor = self.db.conn.cursor()
        record_data = (nimi_listaan, 0, 0, 0, 0 ,"-" ,"-" ,"-" ,0 ,"-" ,"-" ,0)
        cursor.execute(PlayerQueries.ADD_STATEMENT, record_data)
        self.db.conn.commit()
        cursor.close()
        return None