import config
from Message import Send
from pprint import pprint
from SchaduleTimes import listOfTimes
from Check import WeekType
from Check import UsersData
import week
import time
import threading
import telebot
bot = telebot.TeleBot(config.TOKEN)

def Start():
    WeekType.Set()
    listOfTimes.GetValues()


def GetTimeNow():
    t = time.localtime()
    return [t.tm_hour, t.tm_min]

# отправка рассписание через через таймер

def SendMessage(chatId, text):
    bot.send_message(chatId, F"{text}", parse_mode="HTML")
    
def SendWithTimer(timersValue, lessons_hour):
    time.sleep(timersValue)
    #
    usersData = UsersData.GetUserIdUserGroupAndNotification()
    for id in range(len(usersData[0])):
        if id == 0:
            continue
        message_Text = Send.SchaduleByHours(
        usersData[1][id], week.Name.Today(), lessons_hour)
        if message_Text != 'empty':
            if usersData[2][id] == 'yes':
                threadSend = threading.Thread(
                    target=SendMessage, args=(
                        usersData[0][id],
                        F'Занятие начался\n{message_Text}'
                    )
                )
                threadSend.start()


def SendWithTimer_10MinutBefore(timersValue, lessons_hour):
    time.sleep(timersValue)
    #
    usersData = UsersData.GetUserIdUserGroupAndNotification()
    for id in range(len(usersData[0])):
        if id == 0:
            continue
        message_Text = Send.SchaduleByHours(
        usersData[1][id], week.Name.Today(), lessons_hour)
        if message_Text != 'empty':
            if usersData[2][id] == 'yes':
                threadSend = threading.Thread(
                    target=SendMessage, args=(
                        usersData[0][id],
                        F'Через 10 минут у вас начнется занятие.\n{message_Text}'
                    )
                )
                threadSend.start()

def StartTimer():
    # список время уроков
    LessonsTimesList = listOfTimes.StartTimesArray

    # текушее время
    currentTime = GetTimeNow()
    # текушая время в секундах
    currentTimeInSecond = currentTime[0]*3600 + currentTime[1]*60
    # массив для время урока в секундах
    listOfTimersValueInSecond = []
    # массив для хранение разницы между двумя времям
    listOfTimesInSecond = []
    #  список разницы между времям в hour
    listOfTimesInHour = []

    # процесс обработки разници между времям
    for time_value in listOfTimes.StartTimesArray:
        # значение время урока в секунда
        time_value_inSecond = time_value[0]*3600 + time_value[1]*60
        # массив для время урока в секундах
        listOfTimersValueInSecond.append(time_value_inSecond)
        # разница между двум времям
        difference = time_value_inSecond - currentTimeInSecond
        # массив для хранение разницы между двум времям
        listOfTimesInSecond.append(difference)

        listOfTimesInHour.append(
            [int(difference/3600), int(difference % 3600/60)])

    for time_value in range(len(listOfTimes.StartTimesArray)):
        if listOfTimesInSecond[time_value] < 0:
            continue
        if LessonsTimesList[time_value][0] > currentTime[0]:
            time_sleep = listOfTimesInSecond[time_value]
            if time_sleep-10*60 >= 0:
                th2 = threading.Thread(target=SendWithTimer_10MinutBefore, args=(
                    time_sleep-10*60, time_value+1))
                th2.start()

            th = threading.Thread(target=SendWithTimer, args=(
                time_sleep, time_value+1))
            th.start()
            pprint(
                F'Message would be sent after {int(time_sleep/3600)}:{int(time_sleep%3600/60)}')

        elif LessonsTimesList[time_value][0] == currentTime[0]:
            if LessonsTimesList[time_value][1] >= currentTime[1]:
                time_sleep = listOfTimesInSecond[time_value]
                if time_sleep-10*60 >= 0:
                    th2 = threading.Thread(target=SendWithTimer_10MinutBefore, args=(
                        time_sleep-10*60, time_value+1))
                    th2.start()
                th = threading.Thread(target=SendWithTimer, args=(
                    time_sleep, time_value))
                th.start()
                pprint(
                    F'Message would be sent after {int(time_sleep/3600)}:{int(time_sleep%3600/60)}')


def UpdatingDatas():

    while True:
        currentTime = GetTimeNow()
        # текушая время в секундах
        currentTimeInSecond = currentTime[0]*3600 + currentTime[1]*60

        # врмя обновление данные 00:30
        # время для обновление данные в секундах
        updateTimeInSecond = float(24*3600 + 30*60)
        if currentTime[0] == 0:
            if currentTime[1] <= 40:
                s_time = 30*60-currentTime[1]*60
                time.sleep(s_time)
                Start()
                th = threading.Thread(target=StartTimer, args=())
                print(
                    F'Thread started at {currentTimeInSecond} and would be at sleep after ({int(s_time/3600)}:{int(s_time% 3600/60)}) hour')
                th.start()

        elif currentTime[0] < 8:
            Start()
            th = threading.Thread(target=StartTimer, args=())
            th.start()
            s_time = updateTimeInSecond - currentTimeInSecond
            print(
                F'Thread started at {currentTimeInSecond} and would be at sleep after({int(s_time/3600)}:{int(s_time% 3600/60)} hour)')
            time.sleep(s_time)

        else:
            s_time = updateTimeInSecond-currentTimeInSecond
            time.sleep(s_time)
            Start()
            th = threading.Thread(target=StartTimer, args=())
            print(
                F'Thread started at {currentTimeInSecond} and would be at sleep after ({int(s_time/3600)}:{int(s_time% 3600/60)}) hour')
            th.start()


def StartThreading():
    threadingTask = threading.Thread(target=UpdatingDatas, args=())
    threadingTask.start()
    threadingTask.join()
    print("Всех фоновых задач остановились")


Start()
OnStartThread=threading.Thread(target=StartThreading, args=())
OnStartThread.start()

