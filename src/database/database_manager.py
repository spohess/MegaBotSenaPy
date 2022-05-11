import os
import sqlite3

from src.database.migration import Migrate


class DatabaseManager:
    con = None

    def migrate(self):
        if os.path.isfile('lottery.db'):
            os.remove('lottery.db')
        self.con = sqlite3.connect('lottery.db')
        migrate = Migrate(self.con)
        migrate.execute()

    def connect(self):
        self.con = sqlite3.connect('lottery.db')

    def close(self):
        self.con.close()
