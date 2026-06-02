import requests
import os
from dotenv import load_dotenv
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


load_dotenv()

IP_API = os.getenv("IP_API_URL")

session = requests.Session()

retry = Retry(
    total=3,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["GET"],
)

adapter = HTTPAdapter(max_retries=retry)

session.mount("http://", adapter)
session.mount("https://", adapter)


def get_geo_location(ip: str):
    response = session.get(
        f"{IP_API}/{ip}",
        timeout=5,
    )

    response.raise_for_status()

    return response.json()