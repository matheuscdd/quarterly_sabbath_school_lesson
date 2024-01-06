from week import week
from intro import get_title, get_lessons_numbers, get_intro
from word import Writer
from time import time

def lesson(url):
    start = time()
    print('\033[33mSistema iniciando...\033[m')
    title = get_title(url)
    doc = Writer(title)
    max_lesson = get_lessons_numbers(url)
    endpoints = ['%02d' % el for el in range(1, max_lesson+1)]
    weeks = []
    for endpoint in endpoints:
        res = week(url + endpoint)
        weeks.append(res)
    intro = get_intro(url + 'intro')
    doc.lesson(intro, weeks)
    print('\033[33mSistema finalizado')
    end_time = time() - start
    print(f'\033[37mTempo de execução {int(end_time/60)} minutos')
