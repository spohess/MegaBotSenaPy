from src.data_process import DataProcess
from src.database.database_manager import DatabaseManager
from src.scraping import Scraping
from src.loteria_model import MegaSenaModel

dbm = DatabaseManager()
dbm.migrate()

model = MegaSenaModel()

scraping = Scraping('Mega-Sena', model=model)
scraping.execute()

data_process = DataProcess(model=model)
data_process.execute()
