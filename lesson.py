import pythonbible as bible
from word import Writer
from time import time
from selenium import webdriver
from time import sleep
from selenium.webdriver import Remote
import requests as req
from bs4 import BeautifulSoup as bs
from bs4.element import Tag
from common import titles, SYMBOL_BIBLE_VERSE_CONTAINER as SBVC, SYMBOL_BIBLE_VERSE_START as SBVS


class Browser:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--ignore-ssl-errors=yes")
        options.add_argument("--ignore-certificate-errors")
        self.driver = Remote(command_executor="http://chrome:4444/wd/hub", options=options)

    def get(self, url: str) -> str:
        self.driver.get(url)
        sleep(5)
        data = self.driver.page_source
        return data

    def close(self):
        self.driver.close()
    

class Bible:
    @classmethod
    def local(cls, location: str): 
        reference = bible.get_references(
            location.replace('–', '-')
        )
        ids_ = bible.convert_references_to_verse_ids(reference)
        text = ''
        for id_ in ids_:
            text += ' ' + bible.get_verse_text(id_) 
        return cls.set_container(text)

    @classmethod
    def web(cls, location: str):
        NEW_VERSION = 'ncv'
        OLD_VERSION = 'nlt'
        location = location.replace(OLD_VERSION, NEW_VERSION)
        res = req.get(location)
        soup = bs(res.text, 'html.parser')
        verse = soup\
            .findAll('div', class_='resourcetext')[0].text
        return cls.set_container(verse)

    @staticmethod
    def set_container(text):
        return f'{SBVC}{SBVS}{text}{SBVC}'


class Lesson:
    browser = Browser()

    def __init__(self, url):
        start = time()
        print('\033[33mSistema iniciando...\033[m')
        title = self.get_title(url)
        intro = self.get_intro(url + 'intro')
        max_lesson = self.get_lessons_numbers(url)
        endpoints = ['%02d' % el for el in range(1, max_lesson+1)]
        weeks = []
        for endpoint in endpoints:
            weeks.append(self.week(url + endpoint))
            print(endpoints)
        Writer(title, intro, weeks)
        self.browser.close()
        print('\033[33mSistema finalizado')
        print(f'\033[37mTempo de execução {int((time() - start)/60)} minutos')
    
    def week(self, url: str):
        res = self.browser.get(url)
        soup = bs(res, 'html.parser')
        title = soup.findAll('h1')[0].a.text
        results_raw, results_handle, results_text = soup.findAll('div', 'c-block'), [], []
        for el in results_raw:
            try: 
                curr_title = el.h2.a.strong.text
                if curr_title in titles:
                    results_handle.append(el)
            except (KeyError, AttributeError):
                pass
        for el in results_handle:
            results_text.append(self.day(el))
            print('\033[34mDia finalizado\033[m')
        print(f'\033[32mSemana finalizada: {title}\033[m')
        return {
            'title': title,
            'week': results_text
        }
    
    def day(content: Tag):
        INDICATIVE_PASSAGE_DEFAULT = 'Read This Week’s Passage: '
        if INDICATIVE_PASSAGE_DEFAULT in content.text:
            element = content.find('div', class_='c-block__content')
            paragraphs = element.find_all('p')
            paragraph = paragraphs[1]
            week_passage_indicative = paragraph.text.split(INDICATIVE_PASSAGE_DEFAULT)[1]
            week_passage_text = Bible.local(week_passage_indicative)
            paragraph.string = f'{INDICATIVE_PASSAGE_DEFAULT}{week_passage_indicative}\n{week_passage_text}'
        
        verses = content.find_all('a', class_='rtBibleRef')
        if len(verses):
            for verse in verses:
                verse.string += ' ' + Bible.web(verse['href'])
        return content
    
    def get_title(self, url: str):
        res = req.get(url)
        soup = bs(res.text, 'html.parser')
        title = soup.findAll('h1')[0].a.text
        return title

    def get_lessons_numbers(self, url: str):
        res = req.get(url)
        soup = bs(res.text, 'html.parser')
        lessons = soup.find_all(lambda tag: tag.name == 'a' and 'Week' in tag.get_text())
        return len(lessons)

    def get_intro(self, url: str):
        res = req.get(url)
        soup = bs(res.text, 'html.parser')
        content = soup.findAll('div', 'u-padding--double--bottom')[0].text
        return content

    
