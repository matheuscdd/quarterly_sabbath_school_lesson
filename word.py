from docx import Document
from docx.shared import RGBColor, Pt
from common import SYMBOL_BIBLE_VERSE_CONTAINER as SBVC, SYMBOL_BIBLE_VERSE_START as SBVS, titles
from bs4.element import Tag
from file import save

class Writer:
    def __init__(self, title: str) -> None:
        self.title = title
        self.doc = Document()
        self.doc.add_heading(title, 0)
    
    def add_intro(self, text: Tag):
        pass

    def add_day(self, day: Tag):
        # p = self.doc.add_paragraph()
        title = day.find_all(lambda tag: tag.name == 'strong' and tag.get_text() in titles)[0].text
        self.doc.add_heading(title, 2)
        day = day.text.replace(title, '')
        texts = day.split(SBVC)
        for text in texts:
            if text[:2] == SBVS:
                text = text.replace(SBVS, '')
                paragraph = self.doc.add_paragraph()
                run = paragraph.add_run(text)
                run.bold = True
            else:
                paragraph = self.doc.add_paragraph(text)

        # breakpoint()
        # separar os versos
        # split loco
        self.doc.add_page_break()

    def add_week(self, week: list[Tag], title: str):
        self.doc.add_heading(title, 1)
        for day in week:
            self.add_day(day)

    def lesson(self, weeks):
        for week in weeks:
            self.add_week(week['week'], week['title'])
        self.doc.save(self.title + '.docx')

    



# Adiciona o título de acordo com seu nível


# Adiciona paragráfo normal



# run = p.add_run("Este é um texto estilizado")
# run.bold = True
# run.font.size = Pt(11)
# run.font.color.rgb = RGBColor(0xFF, 0x00, 0x00)

# # quebra a página


# # quando quebra a página precisa adicionar um outro parágrafo
# p = doc.add_paragraph('Lorem lorem')

# # p.add_run('This text is colorfull').color = 'red'

# doc.save('text.docx')
