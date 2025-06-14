from bs4 import BeautifulSoup
import requests

product = input()

url = 'https://www.avito.ru/nizhniy_novgorod?q=' + product

request = requests.get(url)
bs = BeautifulSoup(request.text, 'html.parser')

all_links = bs.find_all('a', class_='styles-module-root_underlineOffset_size-m-ce9r8мщ')

for link in all_links:
    print(link)
