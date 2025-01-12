import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7377114796:AAEzY-mSqoPvlQ77MMxFZPUYckbVYHQAMhg")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "21702337"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "f496651f4624395e1290dbfe5d8595db")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "6581573267"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://Ujakari:ujujuj@storybot.yqnyo.mongodb.net/?retryWrites=true&w=majority&appName=storybot") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "storybot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
