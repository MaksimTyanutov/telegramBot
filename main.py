import config
import telebot
import requests
from bs4 import BeautifulSoup as BS


def formatFilmName(filmName):
    for symb in filmName:
        if symb == ' ':
            filmName = filmName.replace(symb, '+')
        if symb == '+':
            filmName = filmName.replace(symb, '%2B')
    return filmName

def getFindFilmRefIMDB(filmName):
    return ('https://www.imdb.com/find?q=' + filmName + '&ref_=nv_sr_sm')

def getFindFilmRefKP(filmName):
    return ('https://www.kinopoisk.ru/index.php?kp_query=' + filmName)


def getFilmRefIMDB(filmRef):
    r = requests.get(filmRef)
    html = BS(r.content, 'html.parser')
    for elem in html.select('#main'):
        ref = elem.select('.result_text')[0].a['href']
    return 'https://www.imdb.com' + ref

def getFilmRefKP(filmRef):
    r = requests.get(filmRef)
    html = BS(r.content, 'html.parser')
    for elem in html.select('#block_left_pad'):
        ref = elem.select('.search_results .name')[0].a['data-url']
    return 'https://www.kinopoisk.ru' + ref

def getRaitingIMDB(filmRef):
    r = requests.get(filmRef)
    html = BS(r.content, 'html.parser')
    print(filmRef)
    for elem in html.select('#__next'):
        return elem.select('.ipc-button__text .AggregateRatingButton__RatingScore-sc-1ll29m0-1')[0].text

def getRaitingKP(filmRef):
    r = requests.get(filmRef)
    html = BS(r.content, 'html.parser')
    #print(html.text)
    print(filmRef)
    for elem in html.select('#__next'):
        return elem.select('.film-rating-value')[0].text

def print_raiting(message):
    film = formatFilmName(message.text)
    refIMDB = getFindFilmRefIMDB(film)
    refKP = getFindFilmRefKP(film)
    bot.send_message(message.chat.id, 'Рейтинг на IMDB - ' + getRaitingIMDB(getFilmRefIMDB(refIMDB))
                     + '\nРейтинг на кинопоиске - ' + getRaitingKP(getFilmRefKP(refKP)))
    pass

filmName = "Крестный отец"
film = formatFilmName(filmName)
ref = getFindFilmRefKP(film)
print(getRaitingKP(getFilmRefKP(ref)))

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "Список команд:")

@bot.message_handler(commands=['getRaiting'])
def _command_(message):
    bot.send_message(message.chat.id, "Введите название фильма: ")
    bot.register_next_step_handler(message, print_raiting)



@bot.message_handler(commands=['topFilm'])
def send_welcome(message):
    bot.reply_to(message, "Вот твой список фильмов:")

if __name__ == '__main__':
    bot.polling(none_stop=True)

