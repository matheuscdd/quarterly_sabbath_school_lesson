import os 
from dotenv import load_dotenv
from week import week
from intro import get_title, get_lessons_numbers, get_intro
from word import Writer


def lesson(url: str = input('Digite a url da lição do site inVerse: ').strip()):
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
    print('Sistema finalizado')

lesson()