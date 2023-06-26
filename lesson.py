import os 
from dotenv import load_dotenv
from week import week

load_dotenv()
def lesson(url: str):
    endpoints = ['%02d' % el for el in range(1, 13)]
    for endpoint in endpoints:
        res = week(url + endpoint)
        break
    return res

lesson(
    os.getenv('BASE_URL') or ''
)