from pprint import pprint
import telebot
from telebot import types
import config
from Message import Send
import threading

bot = telebot.TeleBot(config.TOKEN)


studentGroup = ''

# неделя которую выберает пользователь чтобы получить расписание
userChousedWeekType = ''

# добавить гзначение группы по умолчанию чтобы получит доступ
def GlobalAddGroup(group):
    global studentGroup
    studentGroup = group


def GetGloablGroupName(group):
    return studentGroup

#  добавить гзначение тип недели чтобы получит доступ

def GlobalAddWeekType(weekType):
    global userChousedWeekType
    userChousedWeekType = weekType


def GetGlobalWeekType():
    return userChousedWeekType

# отправить сообщение без кнопки(обычно для отправки расписание используется)
def SendMessage(chatId, text):
    pprint(text)
    bot.send_message(chatId, F"{text} 111")

# отправить сообщение используя имя недели(если пользователь выбрал пункт "Другой день")
def SendSchaduleByWeekName(chatId, weekName):
    pprint(weekName)
    pprint(GetGlobalWeekType())
    pprint(studentGroup)
    th = threading.Thread(target=SendMessage, args=(
        chatId,
        Send.GetSchaduleByWeekName(studentGroup, weekName, GetGlobalWeekType())
    ))
    th.start()

# отправляет расписние на сегодня (выделяет поток для отправки)
def SendTodaysSchadule(chatId):

    pprint(studentGroup)
    th = threading.Thread(target=SendMessage, args=(
        chatId,
        Send.TodaysSchadule(studentGroup)
    ))
    th.start()

# отправляет расписние на завтра (выделяет поток для отправки)


def SendTomorrowsSchadule(chatId):
    pprint(studentGroup)
    th = threading.Thread(target=SendMessage, args=(
        chatId,
        Send.TommorowsSchadule(studentGroup)
    ))
    th.start()

# Главное меню
@bot.message_handler(commands=['start'])
def start_command(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Первая подгруппа")
    markup.add("Вторая подгруппа")
    bot.send_message(message.chat.id, "Здраствуйте {0.first_name}!, Выбирите подгруппу".format(
        message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):

    textFromUser = message.text
    chatId = message.chat.id

    # кнопка первая подгруппа
    if message.text == 'Первая подгруппа':
        GlobalAddGroup('first')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Четная','Нечетная')
        markup.add('Текущая неделя')
        markup.add('Главное меню')
        bot.send_message(message.chat.id, "Выберите неделю",
                         reply_markup=markup)
# Кнопка Главное меню
    elif message.text == 'Главное меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add("Первая подгруппа")
        markup.add("Вторая подгруппа")
        bot.send_message(message.chat.id, "{0.first_name}!, Вы вернулись в главное меню".format(
            message.from_user), reply_markup=markup)
# Кнопка Вторая подгруппа
    elif message.text == 'Вторая подгруппа':
        GlobalAddGroup('second')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('|Четная', '|Нечетная')
        markup.add('|Текущая неделя')
        markup.add('Главное меню')
        bot.send_message(message.chat.id, "Выберите неделю",
                         reply_markup=markup)
# Четная неделя первая подгруппа
    elif message.text == 'Четная':
        GlobalAddWeekType('четная')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('*Расписание на сегодня')
        markup.add('*Расписание на завтра')
        markup.add('*Другой день')
        markup.add('Главное меню')
        bot.send_message(message.chat.id, "Выберите день", reply_markup=markup)
# Нечетная неделя первая подгруппа
    elif message.text == 'Нечетная':
        GlobalAddWeekType('нечетная')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('-Расписание на сегодня')
        markup.add('-Расписание на завтра')
        markup.add('-Другой день')
        markup.add('Главное меню')
        bot.send_message(message.chat.id, "Выберите день", reply_markup=markup)
# Четная неделя вторая подгруппа
    elif message.text == '|Четная':
        GlobalAddWeekType('четная')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('|Расписание на сегодня')
        markup.add('|Расписание на завтра')
        markup.add('|Другой день')
        markup.add('Главное меню')
        bot.send_message(message.chat.id, "Выберите день", reply_markup=markup)
# Нечетная вторая подгруппа
    elif message.text == '|Нечетная':
        GlobalAddWeekType('нечетная')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('.Расписание на сегодня')
        markup.add('.Расписание на завтра')
        markup.add('.Другой день')
        markup.add('Главное меню')
        bot.send_message(message.chat.id, "Выберите день", reply_markup=markup)
# Другой день, первая подгруппа, Четная неделя
    elif message.text == '*Другой день':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('*Понидельник')
        markup.add('*Вторник')
        markup.add('*Среда')
        markup.add('*Четверг')
        markup.add('*Пятница')
        markup.add('*Суббота')
        markup.add('Главное меню')
        bot.send_message(message.chat.id, "Выберите день", reply_markup=markup)
# Другой день, первая подгруппа, Нечетная неделя
    elif message.text == '-Другой день':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('-Понедельник')
        markup.add('-Вторник')
        markup.add('-Среда')
        markup.add('-Четверг')
        markup.add('-Пятница')
        markup.add('-Суббота')
        markup.add('Главное меню')
        bot.send_message(message.chat.id, "Выберите день", reply_markup=markup)
    # Другой день, вторая подгруппа, Четная неделя
    elif message.text == '|Другой день':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('|Понедельник')
        markup.add('|Вторник')
        markup.add('|Среда')
        markup.add('|Четверг')
        markup.add('|Пятница')
        markup.add('|Суббота')
        markup.add('Главное меню')
        bot.send_message(message.chat.id, "Выберите день", reply_markup=markup)
    # Другой день, вторая подгруппа, Нечетная неделя
    elif message.text == '.Другой день':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('.Понедельник')
        markup.add('.Вторник')
        markup.add('.Среда')
        markup.add('.Четверг')
        markup.add('.Пятница')
        markup.add('.Суббота')
        markup.add('Главное меню')
        bot.send_message(message.chat.id, "Выберите день", reply_markup=markup)

    # обработка текст пользователья для отправки рассписание
    elif 'Расписание на сегодня' in textFromUser:
        pprint('Расписание на сегодня')
        SendTodaysSchadule(chatId)
    elif 'Расписание на завтра' in textFromUser:
        pprint('Расписание на завтра')
        SendTomorrowsSchadule(chatId)
    elif 'Понедельник' in textFromUser:
        pprint('Другой день')
        SendSchaduleByWeekName(chatId, 'Понедельник')
    elif 'Вторник' in textFromUser:
        pprint('Другой день')
        SendSchaduleByWeekName(chatId, 'Вторник')
    elif 'Среда' in textFromUser:
        pprint('Другой день')
        SendSchaduleByWeekName(chatId, 'Среда')
    elif 'Четверг' in textFromUser:
        pprint('Другой день')
        SendSchaduleByWeekName(chatId, 'Четверг')
    elif 'Пятница' in textFromUser:
        pprint('Другой день')
        SendSchaduleByWeekName(chatId, 'Пятница')
    elif 'Суббота' in textFromUser:
        pprint('Другой день')
        SendSchaduleByWeekName(chatId, 'Суббота')



bot.polling(none_stop=True)

