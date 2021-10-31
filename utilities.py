import requests
from bs4 import BeautifulSoup as BS

def formatFilmName(filmName):
    for symb in filmName:
        if symb == ' ':
            filmName = filmName.replace(symb, '+')
        if symb == '+':
            filmName = filmName.replace(symb, '%2B')
    return filmName

