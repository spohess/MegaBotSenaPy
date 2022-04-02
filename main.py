from src.database.database_manager import DatabaseManager
from src.database.loteria_model import MegaSenaModel
from src.scraping import Scraping

dbm = DatabaseManager()
dbm.migrate()

model = MegaSenaModel()
scraping = Scraping('Mega-Sena', model)
scraping.execute()
