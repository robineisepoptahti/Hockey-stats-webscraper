from db.db_conn import DB
from player import PlayerDAO
from display import display_season_stats
from season_stats_nhl import nhl_season_stats
from season_stats_liiga import liiga_season_stats
from db.queries import PlayerQueries

class Operations:
    #Initializing DB and digital access object
    db: DB
    def __init__(self) -> None:
        self.db = DB()
        self.__initDatabase()
        self.player_dao = PlayerDAO()
        return None
    ##Creation if not existing
    def __initDatabase(self) -> None:
        cursor = self.db.conn.cursor()
        cursor.execute(PlayerQueries.TABLE_STATEMENT)
        self.db.conn.commit()
        cursor.close()
        return None
    
    #Takes player name and adds it to table
    def create(self, name) -> None:
        self.player_dao.add_to_db(name)
        return None
    
    #Gets info using a DAO, as a list of player objects.
    def show(self) -> None:
        lista = self.player_dao.getAll()
        display_season_stats(lista)
        return None
    
    def update_stats(self) -> list:
        nhl_stats = nhl_season_stats()
        liiga_stats = liiga_season_stats()
        return nhl_stats + liiga_stats
    
    #Remove player from DB
    def remove(self, id) -> None:
        self.player_dao.remove_from_db(id)
        return None

    #Cleaning up
    def end_operation(self) -> None:
        self.db.close()
        return None

