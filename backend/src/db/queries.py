class PlayerQueries:
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
    UPDATE_STATEMENT = """
        UPDATE players
        SET season_points = ?, goals = ?, assists = ?, games = ?, league = ?, team = ?, sp = ?, pm = ?, toi = ?, team_id = ?, player_id = ?
        WHERE name = ?;
        """
    ADD_STATEMENT = "INSERT INTO players(name, season_points, goals, assists, games, team, team_id, player_id, sp, toi, league, pm) VALUES(?, ?, ?, ?, ?, ?, ? ,? ,? ,? ,? ,?)"
    
    SELECT_STATEMENTS = """SELECT * FROM players
                ORDER BY league ASC, season_points DESC;"""
    
    SELECT_LEAGUE_STATEMENTS ="""SELECT * FROM players
                WHERE league = ?
                ORDER BY season_points DESC;"""
    
    DELETE_STATEMENT = "DELETE FROM players WHERE player_id = ?;"