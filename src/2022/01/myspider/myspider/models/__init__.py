from orator import Model
from orator import DatabaseManager
from ..settings import DB_CONFIG

db = DatabaseManager(DB_CONFIG)
Model.set_connection_resolver(db)
