from requests import get
from bs4 import BeautifulSoup as bs


def get_title(url: str):
    res = get(url)
    soup = bs(res.text, 'html.parser')
    title = soup.findAll('h1')[0].a.text
    return title

def get_lessons_numbers(url: str):
    res = get(url)
    soup = bs(res.text, 'html.parser')
    lessons = soup.find_all(lambda tag: tag.name == 'a' and 'Week' in tag.get_text())
    return len(lessons)

def get_intro(url: str):
    res = get(url)
    soup = bs(res.text, 'html.parser')
    content = soup.findAll('div', 'u-padding--double--bottom')[0].text
    return content




