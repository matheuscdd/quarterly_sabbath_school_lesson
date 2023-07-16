import os 
from dotenv import load_dotenv
from week import week
from intro import get_title, get_lessons_numbers
from word import Writer


load_dotenv()
def lesson(url: str):
    print('\033[33mSistema iniciando...\033[m')
    title = get_title(url)
    doc = Writer(title)
    max_lesson = get_lessons_numbers(url)
    endpoints = ['%02d' % el for el in range(1, max_lesson+1)]
    results = []
    for endpoint in endpoints:
        res = week(url + endpoint)
        results.append(res)
        break
    doc.lesson(results)

lesson(
    os.getenv('BASE_URL') or ''
)