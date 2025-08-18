""" Return auth variables for appropriate API """
import os
from dotenv import load_dotenv

load_dotenv()

def get_auth(api_name):
    """ .env variables should have capitalized names
        Convention: name of api followed by _ID or _KEY without spaces """
    api_name = api_name.upper()

    if os.getenv(f"{api_name}_ID") is None:
        return {"app_key": os.getenv(f"{api_name}_KEY")}

    return {"app_id": os.getenv(f"{api_name}_ID"),
            "app_key": os.getenv(f"{api_name}_KEY")}        #naming convention of .env variables

