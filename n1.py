from bs4 import BeautifulSoup
import requests, lxml

html = requests.get('https://coinmarketcap.com/')
soup = BeautifulSoup(html.text, 'lxml')

names = soup.select('.LCOyb .kKpPOn')
prices = soup.select('.HgnCe span')

for name, price in zip(names, prices):
    print(name.text, price.text)
