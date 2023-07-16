from bs4.element import Tag
from search_bible import search_local, search_web
from file import save
from requests import get

def day(content: Tag):
    INDICATIVE_PASSAGE_DEFAULT = 'Read This Week’s Passage: '
    if INDICATIVE_PASSAGE_DEFAULT in content.text:
        element = content.find('div', class_='c-block__content')
        paragraphs = element.find_all('p')
        paragraph = paragraphs[1]
        week_passage_indicative = paragraph.text.split(INDICATIVE_PASSAGE_DEFAULT)[1]
        week_passage_text = search_local(week_passage_indicative)
        # Talvez precise de algo depois para indicar o negrito pro word
        paragraph.string = f'{INDICATIVE_PASSAGE_DEFAULT}{week_passage_indicative}\n{week_passage_text}'
    
    verses = content.find_all('a', class_='rtBibleRef')
    if len(verses):
        for verse in verses:
            # Talvez precise de algo depois para indicar o negrito pro word
            verse.string += ' ' + search_web(verse['href'])
    save(content)
    return content


