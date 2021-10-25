import requests
from bs4 import BeautifulSoup as BS

def getFindFilmRefIMDB(filmName):
    return ('https://www.imdb.com/find?q=' + filmName + '&ref_=nv_sr_sm')

def getFilmRefIMDB(filmRef):
    r = requests.get(filmRef)
    html = BS(r.content, 'html.parser')
    for elem in html.select('#main'):
        ref = elem.select('.result_text')[0].a['href']
    return 'https://www.imdb.com' + ref

def getRaitingIMDB(filmRef):
    r = requests.get(filmRef)
    html = BS(r.content, 'html.parser')
    print(filmRef)
    for elem in html.select('#__next'):
        return elem.select('.ipc-button__text .AggregateRatingButton__RatingScore-sc-1ll29m0-1')[0].text