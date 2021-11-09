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

def compareTexts(text1, text2):
    for symb in text1:
        text1 = text1.replace(symb, symb.lower())
        if symb == 'ё':
            text1 = text1.replace(symb, 'е')
    for symb in text2:
        text2 = text2.replace(symb, symb.lower())
        if symb == 'ё':
            text2 = text2.replace(symb, 'е')
    lettersListOne = []
    for symb in text1:
        if lettersListOne.count(symb) == 0:
            lettersListOne.append(symb)

    lettersListTwo = []
    for symb in text2:
        if lettersListTwo.count(symb) == 0:
            lettersListTwo.append(symb)
    lenRight = len(text1)
    countDif = 0
    for symb in lettersListOne:
        if text1.count(symb) != text2.count(symb):
            countDif += 1
    if abs(len(text1) - len(text2))/len(text1) > 0.1 and abs(len(text1) - len(text2)) > 1:
        return False
    if countDif/lenRight > 0.1 and countDif > 1:
        return False
    return True


