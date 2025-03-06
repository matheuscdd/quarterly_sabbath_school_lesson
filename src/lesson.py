from mail import Email
from writer import Writer
import requests as req
from time import time
from bs4 import BeautifulSoup as bs
from bs4.element import Tag
from common import TITLES
from bible import Bible
from browser import Browser
from console import Console


class Lesson:
    def __init__(self, url: str, email: str):
        self.browser = Browser()
        start_time = time()
        Console.log(Console.blue, "System starting")
        title = self.__title(url)
        intro = self.__intro(url + "intro")
        max_lesson = self.__lessons_numbers(url)
        endpoints = ["%02d" % el for el in range(1, max_lesson + 1)]
        weeks = []
        for endpoint in endpoints:
            weeks.append(self.__week(url + endpoint))
        writer = Writer(title, intro, weeks)
        self.browser.close()
        Console.log(Console.blue, "Sending Email")
        Email(email, title, writer.docx()).send()
        Console.log(Console.green, "Email successfully send")

        end_time = int((time() - start_time) / 60)
        Console.log(Console.green, "System finished")
        Console.log(Console.pink, f"Run time {end_time} minutes")

    def __lessons_numbers(self, url: str):
        res = req.get(url)
        soup = bs(res.text, "html.parser")
        lessons = soup.find_all(
            lambda tag: tag.name == "a" and "Week" in tag.get_text()
        )
        return len(lessons)

    def __title(self, url: str):
        res = req.get(url)
        soup = bs(res.text, "html.parser")
        title = soup.findAll("h1")[0].a.text
        return title

    def __intro(self, url: str):
        res = req.get(url)
        soup = bs(res.text, "html.parser")
        content = soup.findAll("div", "u-padding--double--bottom")[0].text
        return content

    def __week(self, url: str):
        res = self.browser.get(url)
        soup = bs(res, "html.parser")
        title = soup.findAll("h1")[0].a.text
        results_raw, results_handle, results_text = (
            soup.findAll("div", "c-block"),
            [],
            [],
        )
        for el in results_raw:
            try:
                curr_title = el.h2.a.strong.text
                if curr_title in TITLES:
                    results_handle.append(el)
            except (KeyError, AttributeError):
                pass
        for el in results_handle:
            results_text.append(self.__day(el))
            Console.log(Console.cyan, "Day finished")
        Console.log(Console.yellow, "Week finished")
        return {"title": title, "week": results_text}

    def __day(self, content: Tag):
        INDICATIVE_PASSAGE_DEFAULT = "Read This Week’s Passage: "
        if INDICATIVE_PASSAGE_DEFAULT in content.text:
            element = content.find("div", class_="c-block__content")
            paragraphs = element.find_all("p")
            paragraph = paragraphs[1]
            week_passage_indicative = paragraph.text.split(INDICATIVE_PASSAGE_DEFAULT)[
                1
            ]
            week_passage_text = Bible.local(week_passage_indicative)
            paragraph.string = f"{INDICATIVE_PASSAGE_DEFAULT}{week_passage_indicative}\n{week_passage_text}"

        verses = content.find_all("a", class_="rtBibleRef")
        if len(verses):
            for verse in verses:
                verse.string += " " + Bible.web(verse["href"])
        return content
