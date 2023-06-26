import pandas as pd
import requests
# 	Abbreviations*

table = pd.read_excel('bible.xlsx')
abbrvs, books = table['Abbreviations*'], []
api_abrv = requests.get('https://www.abibliadigital.com.br/api/books').json()

for cel in abbrvs:
    index = table[abbrvs == cel].index[0]
    title = cel \
        .lower() \
        .replace('\xa0', '') \
        .split(',') 
    title = [el.strip() for el in title]
    en_name = api_abrv[index]['abbrev']['en']
    title += [en_name, table['Biblical Book Name'][index]] 
    title.insert(0,
        {'main': en_name},
    )
    books.append(title)

file = open('data.py', 'w') 
file.write(f'books = {books}')