import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8752628401:AAEPAuqDBzs56hGXef-y90xFHgNU7e3a6Jo")
    API_ID = int(os.environ.get("API_ID", "22419004"))
    API_HASH = os.environ.get("API_HASH", "34982b52c4a83c2af3ce8f4fe12fe4e1")
    MAX_FILE_SIZE = 2194304000
    
    
