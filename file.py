from bs4.element import Tag

def save(soup: Tag, name: str = 'page'):
    with open(name + '.html', 'w') as file:
        try:
            file.write(soup.prettify())
        except:
            file.write(soup)
