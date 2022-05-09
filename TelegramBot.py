from pprint import pprint
from time import sleep
import telebot
from telebot import types
import config
from Message import Send
import threading
from Check import WeekType
from Check import UsersData

bot = telebot.TeleBot(config.TOKEN)

# отправить сообщение без кнопки(обычно для отправки расписание используется)

def SendMessage(chatId, text):
    bot.send_message(chatId, F"{text}", parse_mode="HTML")
    
# отправить сообщение используя имя недели(если пользователь выбрал пункт "Другой день")

def SendSchaduleByWeekName(chatId, weekName):
    th = threading.Thread(target=SendMessage, args=(
        chatId,
        Send.GetSchaduleByWeekName(UsersData.GetUserChousedGroupType(chatId), weekName, UsersData.GetUserChousedWeekType(chatId))
    ))
    th.start()

# отправляет расписние на сегодня (выделяет поток для отправки)


def SendTodaysSchadule(chatId):
    th = threading.Thread(target=SendMessage, args=(
        chatId,
        Send.TodaysSchadule(UsersData.GetUserChousedGroupType(chatId))
    ))
    th.start()

# отправляет расписние на завтра (выделяет поток для отправки)
def SendTomorrowsSchadule(chatId):
    th = threading.Thread(target=SendMessage, args=(
        chatId,
        Send.TommorowsSchadule(UsersData.GetUserChousedGroupType(chatId))
    ))
    th.start()

# Главное меню


@bot.message_handler(commands=['start'])
def start_command(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Да", "Нет")
    bot.send_message(message.chat.id, "Здраствуйте {0.first_name}!, Хотите ли Вы получать сообщение о начало занятие?".format(
        message.from_user), reply_markup=markup)
    # bot.send_message(message.chat.id, "Здраствуйте {0.first_name}!, Выбирите подгруппу".format(
    #     message.from_user), reply_markup=markup)
    # проверяет существует ли пользовател в базу данных (если нет тогда добавляет)
    UsersData.CheekUserId(message,message.chat.id)

@bot.message_handler(content_types=['text'])
def bot_message(message):

    textFromUser = message.text
    chatId = message.chat.id
    if message.text == 'Да':
        UsersData.SetNotificationAccept(chatId,'yes')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add("Первая подгруппа")
        markup.add("Вторая подгруппа")
        bot.send_message(message.chat.id,"<i>Уведомление о начало занятие включено</i>\n<b>Вам будет отправлен сообщение о начало занятие</b>", parse_mode="HTML")
        bot.send_message(message.chat.id, "Выбирите подгруппу".format(
        message.from_user), reply_markup=markup)
    elif message.text == 'Нет':
        UsersData.SetNotificationAccept(chatId,'no')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add("Первая подгруппа")
        markup.add("Вторая подгруппа")
        bot.send_message(message.chat.id,"<i>Уведомление о начало занятие отключено</i>\n<b>Вы не будете получить сообещение о начало занятие</b>", parse_mode="HTML")
        bot.send_message(message.chat.id, "Выбирите подгруппу".format(
        message.from_user), reply_markup=markup)
# кнопка первая подгруппа
    elif message.text == 'Первая подгруппа':
        UsersData.CheckGroupType(message.chat.id,'first')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Расписание на сегодня')
        markup.add('Расписание на завтра')
        markup.add('Другой день')
        markup.add('Главное меню')
        bot.send_message(message.chat.id, "Выберите день",
                         reply_markup=markup)
# Кнопка Главное меню
    elif message.text == 'Главное меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add("Показать расписание")
        markup.add("Изменить подгруппу")
        pprint(UsersData.GetNotificationAccept(chatId))
        if UsersData.GetNotificationAccept(chatId)=='yes':
            markup.add("Отключить уведомление")
        elif UsersData.GetNotificationAccept(chatId)=='no':    
            markup.add("Включить уведомление")
        bot.send_message(message.chat.id, "{0.first_name}!, Вы вернулись в главное меню".format(
            message.from_user), reply_markup=markup)
    elif message.text=='Отключить уведомление':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add("Показать расписание")
        markup.add("Изменить подгруппу")
        markup.add("Включить уведомление")
        bot.send_message(message.chat.id,"<i>Уведомление о начало занятие отключено</i>\n<b>Вы не будете получить сообещение о начало занятие</b>", parse_mode="HTML", reply_markup=markup)
    elif message.text=='Включить уведомление':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add("Показать расписание")
        markup.add("Изменить подгруппу")
        markup.add("Отключить уведомление")
        bot.send_message(message.chat.id,"<i>Уведомление о начало занятие включено</i>\n<b>Вам будет отправлен сообщение о начало занятие</b>", parse_mode="HTML", reply_markup=markup)
    elif message.text=='Показать расписание':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Расписание на сегодня')
        markup.add('Расписание на завтра')
        markup.add('Другой день')   
        markup.add('Главное меню')
        bot.send_message(message.chat.id, "Выберите день",
                         reply_markup=markup)
    elif message.text=='Изменить подгруппу':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add("Первая подгруппа")
        markup.add("Вторая подгруппа")
        bot.send_message(message.chat.id, "Здраствуйте {0.first_name}!, Выбирите подгруппу".format(
        message.from_user), reply_markup=markup)
# Кнопка Вторая подгруппа
    elif message.text == 'Вторая подгруппа':
        UsersData.CheckGroupType(message.chat.id,'second')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Расписание на сегодня')
        markup.add('Расписание на завтра')
        markup.add('Другой день')
        markup.add('Главное меню')
        bot.send_message(message.chat.id, "Выберите день",
                         reply_markup=markup)
# Четная неделя первая подгруппа
    elif message.text == 'Четная':
        UsersData.CheckWeekType(message.chat.id,'четная')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Понедельник', 'Вторник', 'Среда')
        markup.add('Четверг', 'Пятница', 'Суббота')
        markup.add('Главное меню')
        bot.send_message(message.chat.id, "Выберите день", reply_markup=markup)

# Нечетная неделя первая подгруппа
    elif message.text == 'Нечетная':
        UsersData.CheckWeekType(message.chat.id,'нечетная')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Понедельник', 'Вторник', 'Среда')
        markup.add('Четверг', 'Пятница', 'Суббота')
        markup.add('Главное меню')
        bot.send_message(message.chat.id, "Выберите день", reply_markup=markup)
# Другой день, первая подгруппа, Четная неделя
    elif message.text == 'Другой день':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Четная', 'Нечетная')
        markup.add('Текущая неделя')
        markup.add('Главное меню')
        bot.send_message(message.chat.id, "Выберите неделю",
                         reply_markup=markup)

    # обработка текст пользователья для отправки рассписание
    elif 'Расписание на сегодня' in textFromUser:
        SendTodaysSchadule(chatId)
    elif 'Расписание на завтра' in textFromUser:
        SendTomorrowsSchadule(chatId)
    elif 'Понедельник' in textFromUser:
        SendSchaduleByWeekName(chatId, 'Понедельник')
    elif 'Вторник' in textFromUser:
        SendSchaduleByWeekName(chatId, 'Вторник')
    elif 'Среда' in textFromUser:
        SendSchaduleByWeekName(chatId, 'Среда')
    elif 'Четверг' in textFromUser:
        SendSchaduleByWeekName(chatId, 'Четверг')
    elif 'Пятница' in textFromUser:
        SendSchaduleByWeekName(chatId, 'Пятница')
    elif 'Суббота' in textFromUser:
        SendSchaduleByWeekName(chatId, 'Суббота')

    elif 'Текущая неделя' in textFromUser:
        UsersData.CheckWeekType(message.chat.id,WeekType.Get())
        bot.send_message(chatId, Send.ThisWeekType(), parse_mode="HTML")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('Понедельник', 'Вторник', 'Среда')
        markup.add('Четверг', 'Пятница', 'Суббота')
        markup.add('Главное меню')
        bot.send_message(message.chat.id, "Выберите день", reply_markup=markup)
#     # кнопка первая подгруппа
#     if message.text == 'Первая подгруппа':
#         UsersData.CheckGroupType(message.chat.id,'first')
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         markup.add('Четная', 'Нечетная')
#         markup.add('Текущая неделя')
#         markup.add('Главное меню')
#         bot.send_message(message.chat.id, "Выберите неделю",
#                          reply_markup=markup)
# # Кнопка Главное меню
#     elif message.text == 'Главное меню':
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         markup.add("Первая подгруппа")
#         markup.add("Вторая подгруппа")
#         bot.send_message(message.chat.id, "{0.first_name}!, Вы вернулись в главное меню".format(
#             message.from_user), reply_markup=markup)
# # Кнопка Вторая подгруппа
#     elif message.text == 'Вторая подгруппа':
#         UsersData.CheckGroupType(message.chat.id,'second')
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         markup.add('Четная', 'Нечетная')
#         markup.add('Текущая неделя')
#         markup.add('Главное меню')
#         bot.send_message(message.chat.id, "Выберите неделю",
#                          reply_markup=markup)
# # Четная неделя первая подгруппа
#     elif message.text == 'Четная':
#         UsersData.CheckWeekType(message.chat.id,'четная')
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         markup.add('Расписание на сегодня')
#         markup.add('Расписание на завтра')
#         markup.add('Другой день')
#         markup.add('Главное меню')
#         bot.send_message(message.chat.id, "Выберите день", reply_markup=markup)
# # Нечетная неделя первая подгруппа
#     elif message.text == 'Нечетная':
#         UsersData.CheckWeekType(message.chat.id,'нечетная')
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         markup.add('Расписание на сегодня')
#         markup.add('Расписание на завтра')
#         markup.add('Другой день')
#         markup.add('Главное меню')
#         bot.send_message(message.chat.id, "Выберите день", reply_markup=markup)
# # Другой день, первая подгруппа, Четная неделя
#     elif message.text == 'Другой день':
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         markup.add('Понедельник', 'Вторник', 'Среда')
#         markup.add('Четверг', 'Пятница', 'Суббота')
#         markup.add('Главное меню')
#         bot.send_message(message.chat.id, "Выберите день", reply_markup=markup)

#     # обработка текст пользователья для отправки рассписание
#     elif 'Расписание на сегодня' in textFromUser:
#         SendTodaysSchadule(chatId)
#     elif 'Расписание на завтра' in textFromUser:
#         SendTomorrowsSchadule(chatId)
#     elif 'Понедельник' in textFromUser:
#         SendSchaduleByWeekName(chatId, 'Понедельник')
#     elif 'Вторник' in textFromUser:
#         SendSchaduleByWeekName(chatId, 'Вторник')
#     elif 'Среда' in textFromUser:
#         SendSchaduleByWeekName(chatId, 'Среда')
#     elif 'Четверг' in textFromUser:
#         SendSchaduleByWeekName(chatId, 'Четверг')
#     elif 'Пятница' in textFromUser:
#         SendSchaduleByWeekName(chatId, 'Пятница')
#     elif 'Суббота' in textFromUser:
#         SendSchaduleByWeekName(chatId, 'Суббота')

#     elif 'Текущая неделя' in textFromUser:
#         UsersData.CheckWeekType(message.chat.id,WeekType.Get())
#         bot.send_message(chatId, Send.ThisWeekType(), parse_mode="HTML")
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         markup.add('Расписание на сегодня')
#         markup.add('Расписание на завтра')
#         markup.add('Другой день')
#         markup.add('Главное меню')
#         bot.send_message(message.chat.id, "Выберите день", reply_markup=markup)

bot.polling(none_stop=True)
