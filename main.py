import config
import telebot
import requests
from bs4 import BeautifulSoup as BS


def formatFilmNameIMDB(filmName):
    for symb in filmName:
        if symb == ' ':
            filmName = filmName.replace(symb, '+')
        if symb == '+':
            filmName = filmName.replace(symb, '%2B')
    return filmName

def getFindFilmRefIMDB(filmName):
    return ('https://www.imdb.com/find?q=' + filmName + '&ref_=nv_sr_sm')


def getFilmRefIMDB(filmRef):
    r = requests.get(filmRef)
    html = BS(r.content, 'html.parser')
    for elem in html.select('#main'):
        ref = elem.select('.result_text')[0].a['href']
    return 'https://www.imdb.com/' + ref

def getRaitingIMDB(filmRef):
    r = requests.get(filmRef)
    html = BS(r.content, 'html.parser')
    print(filmRef)
    for elem in html.select('#__next'):
        print(elem.select('.ipc-button__text .AggregateRatingButton__RatingScore-sc-1ll29m0-1')[0].text)


filmName = "Крестный отец"
film = formatFilmNameIMDB(filmName)
ref = getFindFilmRefIMDB(film)
getRaitingIMDB(getFilmRefIMDB(ref))

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "Список команд:")


@bot.message_handler(commands=['topFilm'])
def send_welcome(message):
    bot.reply_to(message, "Вот твой список фильмов:")

if __name__ == '__main__':
    bot.polling(none_stop=True)

