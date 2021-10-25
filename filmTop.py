import requests
from bs4 import BeautifulSoup as BS

def getAllTop():
    filmList = ''
    r = requests.get('https://www.imdb.com/chart/top/')
    html = BS(r.content, 'html.parser')
    for elem in html.select('#main'):
        for i in range(20):
            filmList = filmList + str(i + 1) + ') ' + elem.select('.titleColumn')[i].a.text + '\n'
    return filmList


def getYearTop(year):
    filmList = ''
    r = requests.get('https://www.imdb.com/search/title/?year=' + year + '&title_type=feature&')
    html = BS(r.content, 'html.parser')
    for elem in html.select('#main'):
        for i in range(20):
            filmList = filmList + str(i + 1) + ') ' + elem.select('.lister-item-content')[i].a.text + '\n'
    return filmList


def getGenresTop(genre):
    filmList = ''
    r = requests.get(
        'https://www.imdb.com/search/keyword/?sort=moviemeter,asc&mode=detail&page=1&genres=' + genre + '&ref_=kw_ref_gnr')
    html = BS(r.content, 'html.parser')
    for elem in html.select('#main'):
        for i in range(20):
            filmList = filmList + str(i + 1) + ') ' + elem.select('.lister-item-content')[i].a.text + '\n'
    return filmList


