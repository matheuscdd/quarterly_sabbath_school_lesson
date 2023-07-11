from navigator import browser
from bs4 import BeautifulSoup as bs

url = 'https://www.inversebible.org/3am13'
res = browser(url)
soup = bs(res, 'html.parser')
print(type(soup))