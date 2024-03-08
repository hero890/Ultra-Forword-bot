from os import environ 

class Config:
    API_ID = int(environ.get("API_ID", "26451624"))
    API_HASH = environ.get("API_HASH", "1dc5e466048e7e45c37aa284d32caef6")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6498000890:AAEk4NmVE0mDH_QMcINZJfIhpSuuGOz9A6Y") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://Sohanrazz:Sohanrazz@cluster0.tg5fu9r.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = environ.get("DATABASE_NAME", "i")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '5897793065').split()]
    
class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
