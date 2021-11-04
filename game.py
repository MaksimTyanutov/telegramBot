import requests
from bs4 import BeautifulSoup as BS
import random

def getRandomFilm():
    global film
    i = random.randint(1, 100)
    r = requests.get('https://www.imdb.com/chart/top/')
    html = BS(r.content, 'html.parser')
    for elem in html.select('#main'):
        film = elem.select('.titleColumn')[i].a.text
    return film