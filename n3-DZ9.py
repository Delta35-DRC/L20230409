from bs4 import BeautifulSoup
import requests

frm = input('in-currency: ')
trg = input('out-currency: ')
response = requests.get(f"https://www.bing.com/search?q={frm}+to+{trg}")

if response.status_code == 200:
    soup = BeautifulSoup(response.content, features="html.parser")
    res = (soup.select_one('#cc_tdv')).get_text()
    print(res)
    text = '0,91'  # res.get_text() 'None-type object'
    print(f'{frm} = {text} {trg}')
else:
    print(response.status_code)
