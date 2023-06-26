from day import day
import requests 
from bs4 import BeautifulSoup as bs
titles = {'inTro', 'inGest', 'inTerpret', 'inSpect', 'inVite', 'inSight', 'inQuire'}

def week(url: str):
    res = requests.get(url)
    soup = bs(res.text, 'html.parser')
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
        break
