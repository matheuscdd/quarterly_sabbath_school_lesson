from bs4.element import Tag
from search_bible import search

def day(content: Tag):
    INDICATIVE_PASSAGE = 'Read This Week’s Passage: '
    if INDICATIVE_PASSAGE in content.text:
        week_passage = content.div.p.p.text.split(INDICATIVE_PASSAGE)[1]
        search(week_passage)

    
    return content


