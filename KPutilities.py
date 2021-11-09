import requests
from bs4 import BeautifulSoup as BS

def getFindFilmRefKP(filmName):
    return ('https://www.kinopoisk.ru/index.php?kp_query=' + filmName)

def getFilmRefKP(filmRef):
    r = requests.get(filmRef)
    html = BS(r.content, 'html.parser')
    ref = ''
    for elem in html.select('#block_left_pad'):
        ref = elem.select('.search_results .name')[0].a['data-url']
    return 'https://www.kinopoisk.ru' + ref

def getRaitingKP(filmRef):
    r = requests.get(filmRef)
    html = BS(r.content, 'html.parser')
    # print(html.text)
    print(filmRef)
    for elem in html.select('#__next'):
        return elem.select('.film-rating-value')[0].text