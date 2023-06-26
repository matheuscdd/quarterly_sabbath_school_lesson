import requests
from data import books
import pythonbible as bible

# api_abrv = requests.get('https://www.abibliadigital.com.br/api/books').json()
def search(location: str): 
    reference = bible.get_references(
        location.replace('–', '-')
    )
    ids_ = bible.convert_references_to_verse_ids(reference)
    text = ''
    for id_ in ids_:
        text += bible.get_verse_text(id_, version=bible.Version.NEW_INTERNATIONAL) 
    breakpoint()

    




