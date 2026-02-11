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
    _initialized = False
    DB_FILEPATH: Path
    conn: Connection
    def __init__(self) -> None:
        if self._initialized:
            return
        self.DB_FILEPATH = Path(__file__).parent.parent.parent / "data" / "players.db"
        self.conn = sqlite3.connect(self.DB_FILEPATH)
        self._initialized = True
        return None
    def __new__(cls: type[Self]) -> Self:
        if cls.__instance == None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    def close(self) -> None:
        self.conn.close()
        return None
    