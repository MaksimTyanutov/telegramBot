import requests
from bs4 import BeautifulSoup as BS

def getCinemaFilms():
    filmList = ''
    r = requests.get('https://spb.kinoafisha.info/')
    html = BS(r.content, 'html.parser')
    for elem in html.select('#site'):
        global index
        index = 0
        elem = elem.select('.movieList')[0]
        for i in elem.select('.movieItem_info'):
            filmList = filmList + str(index + 1) + ') ' + i.select('.movieItem_title')[0].text + '\n'
            index+=1
    return filmList