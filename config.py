import os

class Config(object):
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6872825009:AAETLKD9mHVQKS_SDxLa_Udfdl3OUK_dQXU")

    APP_ID = int(os.environ.get("APP_ID", 8754146))

    API_HASH = os.environ.get("API_HASH", "8b56a6989f6d04f6f4fe78133ade02fd")    
    
    CAPTION_TEXT = os.environ.get("CAPTION_TEXT", "")

    CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "bottom")

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
