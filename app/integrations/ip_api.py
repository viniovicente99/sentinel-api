import requests

from dotenv import load_dotenv
import os

load_dotenv()

IP_API = os.getenv("IP_API_URL")

def get_geo_location(ip: str):

    response = requests.get(f"{IP_API}/{ip}")

    response.raise_for_status()

    return response.json()