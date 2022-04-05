import os
import sqlite3

from src.database.migration import Migrate


class DatabaseManager:
    con = None

    def migrate(self):
        os.remove('loteria.db')
        self.con = sqlite3.connect('loteria.db')
        migrate = Migrate(self.con)
        migrate.execute()

    def connect(self):
        self.con = sqlite3.connect('loteria.db')

    def close(self):
        self.con.close()
