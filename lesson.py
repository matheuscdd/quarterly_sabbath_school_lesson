import os 
from dotenv import load_dotenv
from week import week

load_dotenv()
def lesson(url: str):
    print('\033[33mSistema iniciando...\033[m')
    # Fazer a intro
    endpoints = ['%02d' % el for el in range(1, 13)]
    for endpoint in endpoints:
        res = week(url + endpoint)
        break
    return res

lesson(
    os.getenv('BASE_URL') or ''
)