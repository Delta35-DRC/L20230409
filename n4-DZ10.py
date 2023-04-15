import sqlite3
import time
import datetime
from bs4 import BeautifulSoup
import requests

connection = sqlite3.connect('table410w.sl3', 5)
cur = connection.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS data (date TEXT, timeM TEXT, value REAL);')

tag = '.summaryTemperatureHover-DS-EntryPoint1-1'

while True:
    html = requests.get("https://www.msn.com/en-us/weather/forecast/in-Columbus,OH")
    if html.status_code == 200:
        soup = BeautifulSoup(html.content, 'lxml')
        res = soup.select_one(tag, features='html.parser')
        text = '50'  # res.get_text() 'None-type object'
        time = datetime.time
        timeM = time.minute
        cur.execute('INSERT INTO data VALUES (?, ?, ?);', (datetime.date, timeM, text))
        connection.commit()
    else:
        print(html.status_code)

    time.sleep(1800)
