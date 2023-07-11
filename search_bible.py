import requests
from data import books
import pythonbible as bible
from bs4 import BeautifulSoup as bs

# api_abrv = requests.get('https://www.abibliadigital.com.br/api/books').json()
def search_local(location: str): 
    reference = bible.get_references(
        location.replace('–', '-')
    )
    ids_ = bible.convert_references_to_verse_ids(reference)
    text = ''
    for id_ in ids_:
        text += bible.get_verse_text(id_) 
    return text

    
def search_web(location: str):
    new_version = 'ncv'
    old_version = 'nlt'
    location = location.replace(old_version, new_version)
    res = requests.get(location)
    soup = bs(res, 'html.parser')
    ## continuar


