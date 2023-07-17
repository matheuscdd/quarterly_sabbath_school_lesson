from day import day
from navigator import browser
from bs4 import BeautifulSoup as bs
from common import titles

def week(url: str):
    res = browser(url)
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
        results_text.append(day(el))
        print('Dia finalizado')
    print(f'Semana finalizada: {title}')
    return {
        'title': title,
        'week': results_text
    }
        
