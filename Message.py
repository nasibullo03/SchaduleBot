from array import array
from pprint import pprint
import threading

from Schadule import Schadule
from SchaduleTimes import listOfTimes
from Check import WeekType

import week
import enum


class MessageTypes(enum.Enum):
    Today = 0
    Tomorrow = 1
    ByWeekDay = 2
    ByHour = 3
    Now = 4


def MakeText(listofSchadules):
    text = ''
    for list in range(len(listofSchadules)):
        text += F"{listofSchadules[list][0]}-{listofSchadules[list][1]} {listofSchadules[list][2]}\n"
    return text


def MakeMassage(listofSchadules, MessageType):

    if MessageType == MessageTypes.Today:
        if listofSchadules == []:
            return "Сегодня у вас нет расписание"
        else:
            return MakeText(listofSchadules)
    elif MessageType == MessageTypes.Tomorrow:
        if listofSchadules == []:
            return "Завтра у вас нет расписание"
        else:
            return MakeText(listofSchadules)
    elif MessageType == MessageTypes.Now:
        if listofSchadules == []:
            return "У вас нет рассписание сейчас"
        else:
            return MakeText(listofSchadules)
    elif MessageType == MessageTypes.ByWeekDay:
        if listofSchadules == []:
            return "У вас нет расписание в этот день"
        else:
            return MakeText(listofSchadules)
    elif MessageType == MessageTypes.ByHour:
        if listofSchadules == []:
            return "empty"
        else:
            return MakeText(listofSchadules)

    # if listofSchadules == []:
    #     return "У вас нет расписание"


def ProcessingSchadule(_schaduleList, MessageType, hour=0):
    arraySchadule = []
    if MessageType == MessageTypes.ByHour:
       if _schaduleList[2][0][0] != 'empty':
            arraySchadule.append(
                [
                    _schaduleList[0][hour][0],
                    _schaduleList[1][hour][0],
                    _schaduleList[2][0][0]
                ]
            )
            return MakeMassage(arraySchadule, MessageType)
        
    
    for list in range(len(_schaduleList[2])):
        if _schaduleList[2][list][0] != 'empty':
            arraySchadule.append(
                [
                    _schaduleList[0][list][0],
                    _schaduleList[1][list][0],
                    _schaduleList[2][list][0]
                ]
            )
    return MakeMassage(arraySchadule, MessageType)


class Send:

    def TodaysSchadule(group):
        if week.Name.Today() != "Воскресение":
            if WeekType.Get() == "четная":
                if group == "first":
                    return ProcessingSchadule([
                        listOfTimes.Start['values'],
                        listOfTimes.End['values'],
                        Schadule.EvenWeek.FirstGroup.GetTodaysSchadule()[
                            'values']
                    ], MessageTypes.Today
                    )

                else:
                    return ProcessingSchadule([
                        listOfTimes.Start['values'],
                        listOfTimes.End['values'],
                        Schadule.EvenWeek.SecondGroup.GetTodaysSchadule()[
                            'values']
                    ], MessageTypes.Today
                    )
            elif WeekType.Get() == "четная":
                if group == "first":
                    return ProcessingSchadule([
                        listOfTimes.Start['values'],
                        listOfTimes.End['values'],
                        Schadule.OddWeek.FirstGroup.GetTodaysSchadule()[
                            'values']
                    ], MessageTypes.Today)
                else:
                    return ProcessingSchadule([
                        listOfTimes.Start['values'],
                        listOfTimes.End['values'],
                        Schadule.OddWeek.SecondGroup.GetTodaysSchadule()[
                            'values']
                    ], MessageTypes.Today)
        else:
            return 'empty'

    def TommorowsSchadule(group):
        if week.Name.Tomorrow() != "Воскресение":
            if WeekType.Get() == "четная":
                if group == "first":
                    return ProcessingSchadule([
                        listOfTimes.Start['values'],
                        listOfTimes.End['values'],
                        Schadule.EvenWeek.FirstGroup.GetTomorrowsSchadule()[
                            'values']
                    ], MessageTypes.Tomorrow)
                else:
                    return ProcessingSchadule([
                        listOfTimes.Start['values'],
                        listOfTimes.End['values'],
                        Schadule.EvenWeek.SecondGroup.GetTomorrowsSchadule()[
                            'values']
                    ], MessageTypes.Tomorrow)
            elif WeekType.Get() == "нечетная":
                if group == "first":
                    return ProcessingSchadule([
                        listOfTimes.Start['values'],
                        listOfTimes.End['values'],
                        Schadule.OddWeek.FirstGroup.GetTomorrowsSchadule()[
                            'values']
                    ], MessageTypes.Tomorrow)
                else:
                    return ProcessingSchadule([
                        listOfTimes.Start['values'],
                        listOfTimes.End['values'],
                        Schadule.OddWeek.SecondGroup.GetTomorrowsSchadule()[
                            'values']
                    ], MessageTypes.Tomorrow)
        else:
            return 'empty'

    def GetSchaduleByWeekName(group, weekName):
        if weekName != "Воскресение":
            if WeekType.Get() == "четная":
                if group == "first":
                    return ProcessingSchadule([
                        listOfTimes.Start['values'],
                        listOfTimes.End['values'],
                        Schadule.EvenWeek.FirstGroup.GetSchaduleByWeekName(weekName)[
                            'values']
                    ], MessageTypes.ByWeekDay)
                else:
                    return ProcessingSchadule([
                        listOfTimes.Start['values'],
                        listOfTimes.End['values'],
                        Schadule.EvenWeek.SecondGroup.GetSchaduleByWeekName(weekName)[
                            'values']
                    ], MessageTypes.ByWeekDay)
            elif WeekType.Get() == "нечетная":
                if group == "first":
                    return ProcessingSchadule([
                        listOfTimes.Start['values'],
                        listOfTimes.End['values'],
                        Schadule.OddWeek.FirstGroup.GetSchaduleByWeekName(weekName)[
                            'values']
                    ], MessageTypes.ByWeekDay)
                else:
                    return ProcessingSchadule([
                        listOfTimes.Start['values'],
                        listOfTimes.End['values'],
                        Schadule.OddWeek.SecondGroup.GetSchaduleByWeekName(weekName)[
                            'values']
                    ], MessageTypes.ByWeekDay)
        else:
            return 'empty'

    def SchaduleByHours(group, weekName, hour):
        if weekName != "Воскресение":
            if WeekType.Get() == "четная":
                if group == "first":
                    return ProcessingSchadule([
                        listOfTimes.Start['values'],
                        listOfTimes.End['values'],
                        Schadule.EvenWeek.FirstGroup.SchaduleByHours(weekName, hour)[
                            'values']
                    ], MessageTypes.ByHour, hour)
                else:
                    return ProcessingSchadule([
                        listOfTimes.Start['values'],
                        listOfTimes.End['values'],
                        Schadule.EvenWeek.SecondGroup.GetTomorrowsSchadule()[
                            'values']
                    ], MessageTypes.ByHour, hour)
            elif WeekType.Get() == "нечетная":
                if group == "first":
                    return ProcessingSchadule([
                        listOfTimes.Start['values'],
                        listOfTimes.End['values'],
                        Schadule.OddWeek.FirstGroup.GetTomorrowsSchadule()[
                            'values']
                    ], MessageTypes.ByHour, hour)
                else:
                    return ProcessingSchadule([
                        listOfTimes.Start['values'],
                        listOfTimes.End['values'],
                        Schadule.OddWeek.SecondGroup.GetTomorrowsSchadule()[
                            'values']
                    ], MessageTypes.ByHour, hour)
        else:
            return 'empty'


WeekType.Set()
listOfTimes.GetValues()
# def ptin():
print(Send.SchaduleByHours('first', 'Понедельник', 0))
# 'values'])

# for i in range(5):
#     print(F"Start({i})")
#     th = threading.Thread(target=ptin, args=())
#     th.start()
#     th.join()


