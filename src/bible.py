import pythonbible as bible
import requests as req
from bs4 import BeautifulSoup as bs
from common import (
    SYMBOL_BIBLE_VERSE_CONTAINER as SBVC,
    SYMBOL_BIBLE_VERSE_START as SBVS,
)


class Bible:
    @classmethod
    def local(cls, location: str):
        reference = bible.get_references(location.replace("–", "-"))
        ids_ = bible.convert_references_to_verse_ids(reference)
        text = ""
        for id_ in ids_:
            text += " " + bible.get_verse_text(id_)
        return cls.set_container(text)

    @classmethod
    def web(cls, location: str):
        NEW_VERSION = "ncv"
        OLD_VERSION = "nlt"
        location = location.replace(OLD_VERSION, NEW_VERSION)
        res = req.get(location)
        soup = bs(res.text, "html.parser")
        verse = soup.findAll("div", class_="resourcetext")
        if not verse:
            return ""
        verse = verse[0].text
        return cls.set_container(verse)

    @staticmethod
    def set_container(text):
        return f"{SBVC}{SBVS}{text}{SBVC}"
