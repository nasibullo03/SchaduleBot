from tracemalloc import start
from Message import Send
from pprint import pprint
from SchaduleTimes import listOfTimes
from Check import WeekType
import time
import threading

class Start():
    listOfTimes.GetValues();
    WeekType.Set()


def GetTimeNow():
    t = time.localtime()
    return [t.tm_hour, t.tm_min]

# отправка рассписание через через таймер 
def SendWithTimer(timersValue, lessons_hour):
    time.sleep(timersValue)
    # week.Name.Today()
    message_Text = Send.SchaduleByHours('first','Понедельник',lessons_hour)
    if message_Text !='empty':
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
        if LessonsTimesList[time_value][0] > currentTime[0]:
            th = threading.Thread(target=SendWithTimer, args=(
                listOfTimesInSecond[time_value], time_value+1))
            th.start()
        elif LessonsTimesList[time_value][0] == currentTime[0]:
            if LessonsTimesList[time_value][1] >= currentTime[1]:
                th = threading.Thread(target=SendWithTimer, args=(
                     listOfTimesInSecond[time_value], time_value))
                th.start()
        

# Start()     
StartTimer()
    
    
    
    

 

    

# StartTimer()

# pprint(listOfTimes.StartTimesArray)
# pprint(listOfTimes.StartTimesArray)




   






