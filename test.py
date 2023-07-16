from navigator import browser
from bs4 import BeautifulSoup as bs
from requests import get
from search_bible import search_web


url = 'https://biblia.com/bible/nlt/john/6/35-38'
res = get(url)
print(search_web(res))