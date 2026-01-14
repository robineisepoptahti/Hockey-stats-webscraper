from dataclasses import dataclass
from db_conn import DB
from utilities import askName, serialize

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
        sql_statement = """
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            season_points INTEGER,
            goals INTEGER,
            assists INTEGER,
            games INTEGER,
            team TEXT,
            team_id TEXT,
            player_id TEXT,
            sp REAL,
            toi TEXT,
            league TEXT,
            pm INTEGER
        );
        """
        cursor.execute(sql_statement)
        self.db.conn.commit()
        cursor.close()
        return None
    def insert(self, player: Player) -> None:
        pass

    
    def getAll(self, league=None) -> list[Player]:
        cursor = self.db.conn.cursor()
        #Päättää palautetaanko jokin tietty liiga vai kaikki pelaajat
        if league is not None:
            sql_statement = """SELECT * FROM players
                WHERE league = ?
                ORDER BY season_points DESC;"""
            cursor.execute(sql_statement, (league,))
        else:
            print("____")
            sql_statement = """SELECT * FROM players
                ORDER BY league ASC, season_points DESC;"""
            cursor.execute(sql_statement)
        records = cursor.fetchall()
        #Test print of fetched list
        #print(records)
        players: list[Player] = []
        for record in records:
            player = Player(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10], record[11], record[12])
            players.append(player)
        cursor.close()
        return players
    
    
    def update(self, l) -> None:
        cursor = self.db.conn.cursor()
        sql_statement = """
        UPDATE players
        SET season_points = ?, goals = ?, assists = ?, games = ?, league = ?, team = ?, sp = ?, pm = ?, toi = ?, team_id = ?, player_id = ?
        WHERE name = ?;
        """
        for player in l:
            record_data = (player["points"], player["goals"], player["assists"], player["games"], player["league"], player["team"], player["sp"], player["pm"], player["toi"], player["tId"], player["pId"], player["name"])
            cursor.execute(sql_statement, record_data)
            self.db.conn.commit()
        cursor.close()
        return None 
    


    def add_name(self) -> None:
        nimi_listaan = askName()    
        #Lataa nimet tietokannasta je tarkistaa onko syötetty nimi jo siellä
        player_dao = PlayerDAO()
        lista = player_dao.getAll()
        #Tarkastaa että listassa on jotain, jotta voidaaan verrata tuplauksien varalta
        if lista:
            for player in lista:
                if player.name == nimi_listaan:
                    print("Nimi on jo listassa.")
                    return None
        #Muuten serialisoi nimen avaimeksi ja lisää nimen tietokantaan
        serialize(nimi_listaan)
        player_dao.add_to_db(nimi_listaan)
        print()
        print(f"Seurataan pelaajaa {nimi_listaan}")
        print("Pelaaja lisätty listaan.")
        return None


    def add_to_db(self, nimi_listaan: None) -> None:
        cursor = self.db.conn.cursor()
        sql_statement = "INSERT INTO players(name, season_points, goals, assists, games, team, team_id, player_id, sp, toi, league, pm) VALUES(?, ?, ?, ?, ?, ?, ? ,? ,? ,? ,? ,?)"
        record_data = (nimi_listaan, 0, 0, 0, 0 ,"-" ,"-" ,"-" ,0 ,"-" ,"-" ,0)
        cursor.execute(sql_statement, record_data)
        self.db.conn.commit()
        cursor.close()
        return None