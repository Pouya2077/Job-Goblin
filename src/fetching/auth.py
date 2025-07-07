""" Return authentication variables for specific API """
import os 
from dotenv import load_dotenv

load_dotenv()

def get_auth(name):
    return {"app_id": os.getenv("ADZUNA_ID"), 
            "app_key": os.getenv("ADZUNA_KEY")}