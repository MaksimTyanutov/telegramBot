import config
import telebot
import filmTop as FT
import utilities as util
import IMDButilities as IMDB
import KPutilities as KP

bot = telebot.TeleBot(config.token)

def printGenresTop(message):
    genre = 'Romance'
    if (message.text == '1'):
        genre = 'Romance'
    elif (message.text == '2'):
        genre = 'Drama'
    elif (message.text == '3'):
        genre = 'Comedy'
    elif (message.text == '4'):
        genre = 'Crime'
    elif (message.text == '5'):
        genre = 'Family'
    elif (message.text == '6'):
        genre = 'Mystery'
    elif (message.text == '7'):
        genre = 'Fantasy'
    elif (message.text == '8'):
        genre = 'Action'
    elif (message.text == '9'):
        genre = 'Thriller'
    elif (message.text == '10'):
        genre = 'Short'
    elif (message.text == '11'):
        genre = 'Adventure'
    elif (message.text == '12'):
        genre = 'Animation'
    elif (message.text == '13'):
        genre = 'Music'
    elif (message.text == '14'):
        genre = 'Sci-Fi'
    elif (message.text == '15'):
        genre = 'History'
    elif (message.text == '16'):
        genre = 'Musical'
    elif (message.text == '17'):
        genre = 'Horror'
    elif (message.text == '18'):
        genre = 'War'
    elif (message.text == '19'):
        genre = 'Sport'
    else:
        bot.send_message(message.chat.id, 'Попробуй вбить только цифру от 1 до 19')
        bot.register_next_step_handler(message, printGenresTop)
        return
    filmList = FT.getGenresTop(genre)
    bot.send_message(message.chat.id, filmList)

def printYearTop(message):
    filmList = FT.getYearTop(message.text)
    bot.send_message(message.chat.id, filmList)

def print_top(message):
    if message.text == '1':
        bot.send_message(message.chat.id, FT.getAllTop())
        return
    if message.text == '2':
        send = bot.send_message(message.chat.id, 'Введите год')
        bot.register_next_step_handler(send, printYearTop)
        return
    if message.text == '3':
        send = bot.send_message(message.chat.id, 'Выберите жанр(введите только цифру):\n\n'
                                                 '1)Романтика\n'
                                                 '2)Драма\n'
                                                 '3)Комедия\n'
                                                 '4)Преступление\n'
                                                 '5)Семейный\n'
                                                 '6)Мистика\n'
                                                 '7)Фантастика\n'
                                                 '8)Экшн\n'
                                                 '9)Триллеры\n'
                                                 '10)Короткие\n'
                                                 '11)Приключение\n'
                                                 '12)Анимационные\n'
                                                 '13)Музыкальные\n'
                                                 '14)Научная фантастика\n'
                                                 '15)Исторические\n'
                                                 '16)Мюзиклы\n'
                                                 '17)Хорроры\n'
                                                 '18)Военные\n'
                                                 '19)Спортивные\n')
        bot.register_next_step_handler(send, printGenresTop)
        return
    bot.send_message(message.chat.id, 'Попробуй вбить только цифру: 1, 2 или 3')
    bot.register_next_step_handler(message, print_top)


def print_film_info(message):
    film = util.formatFilmName(message.text)
    ref_IMDB = IMDB.getFilmRefIMDB(IMDB.getFindFilmRefIMDB(film))
    ref_KP = KP.getFilmRefKP(KP.getFindFilmRefKP(film))
    img_url = IMDB.getPhotoIMDB(ref_IMDB)
    bot.send_photo(message.chat.id, img_url)
    bot.send_message(message.chat.id, IMDB.getDescriptionIMDB(ref_IMDB) + '\n\nРейтинг на IMDB - ' + IMDB.getRaitingIMDB(ref_IMDB)
                     + '\nРейтинг на кинопоиске - ' + KP.getRaitingKP(ref_KP))
    pass


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "Список команд:")


@bot.message_handler(commands=['getFilmInfo'])
def _command_(message):
    bot.send_message(message.chat.id, "Введите название фильма: ")
    bot.register_next_step_handler(message, print_film_info)


@bot.message_handler(commands=['topFilm'])
def _command_(message):
    bot.send_message(message.chat.id, "Чтобы получить топ фильмов за все время напишите \"1\"\n"
                                      "Чтобы получить топ фильмов по годам напишите \"2\"\n"
                                      "Чтобы получить топ фильмов по жанрам напишите \"3\"\n")
    bot.register_next_step_handler(message, print_top)

#text = IMDB.getDescriptionIMDB(IMDB.getFilmRefIMDB(IMDB.getFindFilmRefIMDB(util.formatFilmName("Крестный отец"))))


if __name__ == '__main__':
    bot.polling(none_stop=True)
