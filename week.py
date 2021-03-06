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
    'Суббота',
    'Воскресение'
]


KemSU_SchadulePageUrl = 'https://kemsu.ru/education/schedule/'


def GetWeekDayNumber(intWeekDayNumber):
    return weekDaysArray[intWeekDayNumber]


class Name:
    
    def Today():
        return weekDaysArray[time.localtime().tm_wday]

    def WeekDay(weekDayInt):
        return weekDaysArray[weekDayInt]
    def Tomorrow():
        tomorrow = time.localtime().tm_wday+1
        if time.localtime().tm_wday == 6:
            tomorrow = 0
        
        return weekDaysArray[tomorrow]

def GetOddOrEvenWeek():
    return BeautifulSoup(requests.get(KemSU_SchadulePageUrl).text, "html.parser").find('div', class_="calendar-week").find('div').find_next_sibling('div').text.split(' ')[2]
