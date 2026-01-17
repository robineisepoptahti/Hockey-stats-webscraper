"""
Database connection
"""
from pathlib import Path
import sqlite3
from sqlite3 import Connection
from typing import Self

# Singleton patterni
class DB:
    __instance: type[Self] | None = None
    DB_FILEPATH: Path
    conn: Connection
    def __init__(self) -> None:
        self.DB_FILEPATH = Path().joinpath("../data/players.db") 
        self.conn = sqlite3.connect(self.DB_FILEPATH) 
        return None
    def __new__(cls: type[Self]) -> Self:
        if cls.__instance == None:
            cls.__instance = super(DB, cls).__new__(cls)
        return cls.__instance
    