import telebot
from telebot import types
import config

bot = telebot.TeleBot(config.TOKEN)

#Главное меню
@bot.message_handler(commands=['start'])
def start_command(message):
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  markup.add("Первая подгруппа")
  markup.add("Вторая подгруппа")
  bot.send_message(message.chat.id, "Здраствуйте {0.first_name}!, Выбирите подгруппу".format(
            message.from_user), reply_markup=markup)
@bot.message_handler(content_types=['text'])
def bot_message(message):
#кнопка первая подгруппа
  if message.text == 'Первая подгруппа':
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      markup.add('Четная')
      markup.add('Нечетная')
      markup.add('Главное меню')
      bot.send_message(message.chat.id, "Выберите неделю", reply_markup=markup)
#Кнопка Главное меню
  elif message.text == 'Главное меню':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Первая подгруппа")
    markup.add("Вторая подгруппа")
    bot.send_message(message.chat.id, "{0.first_name}!, Вы вернулись в главное меню".format(
            message.from_user), reply_markup=markup)
#Кнопка Вторая подгруппа
  elif message.text == 'Вторая подгруппа':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('|Четная')
    markup.add('|Нечетная')
    markup.add('Главное меню')
    bot.send_message(message.chat.id, "Выберите неделю", reply_markup=markup)
#Четная неделя первая подгруппа
  elif message.text == 'Четная':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('*Расписание на сегодня')
    markup.add('*Расписание на завтра')
    markup.add('*Другой день')
    markup.add('Главное меню')
    bot.send_message(message.chat.id, "Выберите день", reply_markup=markup)
#Нечетная неделя первая подгруппа
  elif message.text == 'Нечетная':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('-Расписание на сегодня')
    markup.add('-Расписание на завтра')
    markup.add('-Другой день')
    markup.add('Главное меню')
    bot.send_message(message.chat.id, "Выберите день", reply_markup=markup)
#Четная неделя вторая подгруппа
  elif message.text == '|Четная':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('|Расписание на сегодня')
    markup.add('|Расписание на завтра')
    markup.add('|Другой день')
    markup.add('Главное меню')
    bot.send_message(message.chat.id, "Выберите день", reply_markup=markup)
#Нечетная вторая подгруппа 
  elif message.text == '|Нечетная':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('.Расписание на сегодня')
    markup.add('.Расписание на завтра')
    markup.add('.Другой день')
    markup.add('Главное меню')
    bot.send_message(message.chat.id, "Выберите день", reply_markup=markup)
#Другой день, первая подгруппа, Четная неделя
  elif message.text == '*Другой день':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('*Понидельник')
    markup.add('*Вторник')
    markup.add('*Среда')
    markup.add('*Четвегр')
    markup.add('*Пятница')
    markup.add('*Суббота')
    markup.add('Главное меню')
    bot.send_message(message.chat.id, "Выберите день", reply_markup=markup)
#Другой день, первая подгруппа, Нечетная неделя
  elif message.text == '-Другой день':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('-Понидельник')
    markup.add('-Вторник')
    markup.add('-Среда')
    markup.add('-Четвегр')
    markup.add('-Пятница')
    markup.add('-Суббота')
    markup.add('Главное меню')
    bot.send_message(message.chat.id, "Выберите день", reply_markup=markup)
  #Другой день, вторая подгруппа, Четная неделя
  elif message.text == '|Другой день':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('|Понидельник')
    markup.add('|Вторник')
    markup.add('|Среда')
    markup.add('|Четвегр')
    markup.add('|Пятница')
    markup.add('|Суббота')
    markup.add('Главное меню')
    bot.send_message(message.chat.id, "Выберите день", reply_markup=markup)
  #Другой день, вторая подгруппа, Нечетная неделя
  elif message.text == '.Другой день':
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('.Понидельник')
    markup.add('.Вторник')
    markup.add('.Среда')
    markup.add('.Четвегр')
    markup.add('.Пятница')
    markup.add('.Суббота')

    markup.add('Главное меню')
    bot.send_message(message.chat.id, "Выберите день", reply_markup=markup)
bot.polling(none_stop=True)