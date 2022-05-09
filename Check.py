from pprint import pp, pprint
from warnings import catch_warnings
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
    groupName = ''
    #  Возврашает список id пользователей
    def GetUsersId():
        return Sheets.GetUsersData('A:A')['values'][0]
    #  возврашает список id  пользователей и имя группы пользователей
          
    def GetUsersData():
        return Sheets.GetUsersData('A:B')['values']
    
    def GetUserIdAndWeekType():
        return [Sheets.GetUsersData('A:A')['values'][0],Sheets.GetUsersData('I:I')['values'][0]]
    
    def GetUserIdUserGroupAndNotification():
        return [
            Sheets.GetUsersData('A:A')['values'][0],
            Sheets.GetUsersData('B:B')['values'][0],
            Sheets.GetUsersData('J:J')['values'][0]
            ]
    
    def SetUsersData(range,values):
        Sheets.SetUsersData(range, values)
        
    def CheekUserId(message, chatId):
        UsersId = UsersData.GetUsersId()
        containsId = False
        for id in range(len(UsersId)):
            if UsersId[id] == str(chatId) :
                containsId = True
                break
        if containsId == False:
            UsersData.AddUserId(message,chatId,len(UsersId))
              
    def CheckGroupType(chatId, groupType):
        UsersData1 = UsersData.GetUsersData()
        for id in range(len(UsersData1[0])):
            if id == 0:
                continue
            if UsersData1[0][id] == str(chatId) :
                try:
                    if UsersData1[1][id]==groupType:
                        break 
                    else:
                        UsersData.AddGroupType(groupType, id+1)
                except IndexError:
                    UsersData.AddGroupType(groupType, id+1)
    
    def CheckWeekType(chatId,weekType):
        usersData = UsersData.GetUserIdAndWeekType()
        for id in range(len(usersData[0])):
            if id == 0:
                continue
            if usersData[0][id] == str(chatId) :
                try:
                    if usersData[1][id]==weekType:
                        break 
                    else:
                        UsersData.AddWeekType(weekType, id+1)
                except IndexError:
                    UsersData.AddWeekType(weekType, id+1)
    
    def SetNotificationAccept(chatId, notififcation):
        UsersId = UsersData.GetUsersId()
        for id in range(len(UsersId)):
            if UsersId[id] == str(chatId) :
                UsersData.AddNotificationValue(notififcation, id+1)
                break
    def GetNotificationAccept(chatId):
        UsersId = UsersData.GetUsersId()
        for id in range(len(UsersId)):
            if UsersId[id] == str(chatId) :
                return Sheets.GetUsersData(F'J{id+1}')['values'][0][0]
    
    def GetUserChousedWeekType(chatId):
        UsersData1 = UsersData.GetUserIdAndWeekType()
        for id in range(len(UsersData1[0])):
                if UsersData1[0][id] == str(chatId) :
                    return UsersData1[1][id]
                
    def GetUserChousedGroupType(chatId):
        UsersData1 = UsersData.GetUsersData()
        for id in range(len(UsersData1[0])):
                if UsersData1[0][id] == str(chatId) :
                    return UsersData1[1][id] 
                          
    def AddNotificationValue(notification, idRange):
            UsersData.SetUsersData(
            F'J{idRange}', [[notification]]
        )
    def AddWeekType(weekType, idRange):
            UsersData.SetUsersData(
            F'I{idRange}', [[weekType]]
        )                   
    def AddGroupType(groupType, idRange):
        UsersData.SetUsersData(
            F'B{idRange}', [[groupType]]
        )
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
