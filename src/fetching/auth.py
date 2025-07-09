""" Return authentication variables for specific API """
import os
from dotenv import load_dotenv

load_dotenv()

def get_auth(name):
    """ Return .env variables for 'name' API """
    
    if os.getenv(f"{name}_ID") is None:
        return {"app_key": os.getenv(f"{name}_KEY")}

    return {"app_id": os.getenv(f"{name}_ID"),
            "app_key": os.getenv(f"{name}_KEY")}
