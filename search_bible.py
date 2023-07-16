import requests
import pythonbible as bible
from bs4 import BeautifulSoup as bs
from common import SYMBOL_BIBLE_VERSE_CONTAINER as SBVC, SYMBOL_BIBLE_VERSE_START as SBVS

def search_local(location: str): 
    reference = bible.get_references(
        location.replace('–', '-')
    )
    ids_ = bible.convert_references_to_verse_ids(reference)
    text = ''
    for id_ in ids_:
        text += bible.get_verse_text(id_) 
    return set_container(text)

    
def search_web(location: str):
    new_version = 'ncv'
    old_version = 'nlt'
    location = location.replace(old_version, new_version)
    res = requests.get(location)
    soup = bs(res.text, 'html.parser')
    verse = soup\
        .findAll('div', class_='resourcetext')[0]\
        .findAll('p')[-1]\
        .findAll('span')[-1].text
    return set_container(verse)
    

def set_container(text):
    return f'{SBVC}{SBVS}{text}{SBVC}'

