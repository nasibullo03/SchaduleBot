from Message import Send
from pprint import pprint
from SchaduleTimes import listOfTimes
from Check import WeekType
import week
import time
import threading


def Start():
    listOfTimes.GetValues()
    WeekType.Set()


def GetTimeNow():
    t = time.localtime()
    return [t.tm_hour, t.tm_min]

# отправка рассписание через через таймер


def SendWithTimer(timersValue, lessons_hour):
    time.sleep(timersValue)
    # 
    message_Text = Send.SchaduleByHours('first', week.Name.Today(), lessons_hour)
    if message_Text != 'empty':
        print(message_Text)


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
            th = threading.Thread(target=SendWithTimer, args=(
                listOfTimesInSecond[time_value], time_value+1))
            th.start()
        elif LessonsTimesList[time_value][0] == currentTime[0]:
            if LessonsTimesList[time_value][1] >= currentTime[1]:
                th = threading.Thread(target=SendWithTimer, args=(
                    listOfTimesInSecond[time_value], time_value))
                th.start()


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
                    F'Thread started at {currentTimeInSecond} and would be at sleep ({s_time})')
                th.start()

                
        elif currentTime[0] < 8:
            Start()
            th = threading.Thread(target=StartTimer, args=())
            th.start()
            s_time = updateTimeInSecond - currentTimeInSecond
            print(
                F'Thread started at {currentTimeInSecond} and would be at sleep ({s_time})')
            time.sleep(s_time)
            
        else:
            s_time = updateTimeInSecond-currentTimeInSecond
            time.sleep(s_time)
            Start()
            th = threading.Thread(target=StartTimer, args=())
            print(
                F'Thread started at {currentTimeInSecond} and would be at sleep ({s_time})')
            th.start()
            
            


Start()
threadingTask = threading.Thread(target=UpdatingDatas, args=())
threadingTask.start()
threadingTask.join()
print("Всех фоновых задач остановились")


# StartTimer()

# pprint(listOfTimes.StartTimesArray)
# pprint(listOfTimes.StartTimesArray)
