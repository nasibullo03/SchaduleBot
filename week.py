import time
from array import *
import requests
from bs4 import BeautifulSoup

weekDaysArray = [
    'Понедельник',
    'Вторник',
    'Среда',
    'Четверг',
    'Пятница',
    'Суббота'
]

KemSU_SchadulePageUrl = 'https://kemsu.ru/education/schedule/'


def GetWeekDayNumber(intWeekDayNumber):
    return weekDaysArray[intWeekDayNumber]


def GetTodaysWeekName():
    return weekDaysArray[time.localtime().tm_wday]


def GetOddOrEvenWeek():
    return BeautifulSoup(requests.get(KemSU_SchadulePageUrl).text, "html.parser").find('div', class_="calendar-week").find('div').find_next_sibling('div').text.split(' ')[2]
