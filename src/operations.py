from db.db_conn import DB
from player import PlayerDAO
from utilities import deserialize
from display import display_season_stats
from season_stats_nhl import nhl_season_stats
from season_stats_liiga import liiga_season_stats
from db.queries import PlayerQueries

class Operations:
    db: DB
    def __init__(self) -> None:
        self.db = DB()
        self.__initDatabase()
        name_list = deserialize() 
        self.player_dao = PlayerDAO()
        data_list = self.player_dao.getAll()
        #Check if names are already in database
        temp_name = "placeholder"
        for name in name_list:
            for data in data_list:
                #Adds name if not found
                temp_name = data.name
                if name == temp_name:
                    break
            if name != temp_name:
                self.player_dao.add_to_db(name)
        print("Tietokanta alustettu.")
        return None
    
    def __initDatabase(self) -> None:
        cursor = self.db.conn.cursor()
        cursor.execute(PlayerQueries.TABLE_STATEMENT)
        self.db.conn.commit()
        cursor.close()
        return None
    
    #Takes player name and adds it to table
    def create(self) -> None:
        self.player_dao.add_name()
        return None
    
    #Gets info using a DAO, as a list of player objects.
    def show(self) -> None:
        lista = self.player_dao.getAll()
        display_season_stats(lista)
        return None
    
    def update_stats(self) -> None:
        nhl_season_stats()
        liiga_season_stats()
        return None
    

    #Cleaning up
    def end_operationn(self) -> None:
        self.db.close()
        return None

