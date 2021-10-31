import requests
from bs4 import BeautifulSoup as BS
import translate

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
    for elem in html.select('#__next'):
        return elem.select('.ipc-button__text .AggregateRatingButton__RatingScore-sc-1ll29m0-1')[0].text

def getDescriptionIMDB(filmRef):
    r = requests.get(filmRef)
    html = BS(r.content, 'html.parser')
    translator = translate.Translator(to_lang="Russian")
    for elem in html.select('#__next'):
        return translator.translate(elem.select('.GenresAndPlot__Plot-cum89p-6 .GenresAndPlot__TextContainerBreakpointXS_TO_M-cum89p-0')[0].text)

def getPhotoIMDB(filmRef):
    r = requests.get(filmRef)
    html = BS(r.content, 'html.parser')
    url = ''
    img_url = 'a'
    for elem in html.select('#__next'):
        url = 'https://www.imdb.com' + elem.select('.ipc-poster')[0].a['href']
    r = requests.get(url)
    html = BS(r.content, 'html.parser')
    for elem in html.select('#__next'):
        img_url = elem.select('.MediaViewerImagestyles__PortraitContainer-sc-1qk433p-2')[0].img['src']
    return img_url