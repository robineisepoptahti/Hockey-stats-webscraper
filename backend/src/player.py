from dataclasses import dataclass
from db.db_conn import DB
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

    
    def getAll(self, league=None) -> list[Player]:
        cursor = self.db.conn.cursor()
        #Which league to fetch from, everything if no league param is sent
        if league is not None:
            cursor.execute(PlayerQueries.SELECT_LEAGUE_STATEMENTS, (league,))
        else:
            cursor.execute(PlayerQueries.SELECT_STATEMENTS)
        records = cursor.fetchall()
        players: list[Player] = []
        for record in records:
            player = Player(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10], record[11], record[12])
            players.append(player)
        cursor.close()
        return players
    
    #Updates stats to db, but doesnt bring back anything.
    def updateDB(self, l) -> None:
        cursor = self.db.conn.cursor()
        for player in l:
            record_data = (player["points"], player["goals"], player["assists"], player["games"], player["league"], player["team"], player["sp"], player["pm"], player["toi"], player["tId"], player["pId"], player["name"])
            cursor.execute(PlayerQueries.UPDATE_STATEMENT, record_data)
            self.db.conn.commit()
        cursor.close()
        return None 
    

    def add_to_db(self, name: None) -> None:
        lista = self.getAll()
        if lista:
            for player in lista:
                #Name already in list
                if player.name == name:
                    return None
        cursor = self.db.conn.cursor()
        #Adds a new player with "empty" stats
        record_data = (name, 0, 0, 0, 0 ,"-" ,"-" ,"-" ,0 ,"-" ,"-" ,0)
        cursor.execute(PlayerQueries.ADD_STATEMENT, record_data)
        self.db.conn.commit()
        cursor.close()
        return None
    
    
    def remove_from_db(self, id) -> None:
        cursor = self.db.conn.cursor()
        #The comma after name makes it a Tuple, otherwise it is handled as a char array
        cursor.execute(PlayerQueries.DELETE_STATEMENT, (id,))
        self.db.conn.commit()
        cursor.close()
        return None