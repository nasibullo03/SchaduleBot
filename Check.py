from pprint import pp, pprint
import week
import Sheets
import time


_weekName = ""


class WeekType:

    def Get():
        return _weekName

    def Set():
        global _weekName
        _weekName = week.GetOddOrEvenWeek()

    def GetFromKemsu():
        return week.GetOddOrEvenWeek()


class UsersData:
    #  Возврашает список id пользователей
    def GetUsersId():
        return Sheets.GetUsersData('A:A')['values'][0]
    #  возврашает список id  полӣзователей и имя группы пользователей
    def SetUsersData(range,values):
       Sheets.SetUsersData(range, values)
        
    def GetUsersData():
        return Sheets.GetUsersData('A:B')['values']

    def CheekUserId(message, chatId):
        UsersId = UsersData.GetUsersId()
        containsId = False
        for id in range(len(UsersId)):
            if UsersId[id] == str(chatId) :
                containsId = True
                break
        if containsId == False:
            UsersData.AddUserId(message,chatId,len(UsersId))
              
                
    def AddUserId(message,chatId, lastId):
        todaysTime = time.localtime()
        UsersData.SetUsersData(
            F'A{lastId+1}', [[chatId]]
        )
        UsersData.SetUsersData(
            F'C{lastId+1}:G{lastId+1}', 
            [[message.from_user.id],
             [message.from_user.first_name],
             [message.from_user.last_name],
             [message.from_user.username],
             [F"{todaysTime.tm_mday}.{todaysTime.tm_mon}.{todaysTime.tm_year} {todaysTime.tm_hour}:{todaysTime.tm_min}:{todaysTime.tm_sec}"]
             ]
        )
        
# UsersData.CheekUserId(5)