from pprint import pprint
from array import *

from Range import EvenWeek
from Range import OddWeek
 
import Sheets
import week



class Schadule:
    # расписание на четной неделе
    class EvenWeek:

        class FirstGroup:
            def GetTodaysSchadule():
                return Sheets.GetSchadule(week.Name.Today(
                ), EvenWeek.FirstGroup.Range(), 'ROWS')

            def GetTomorrowsSchadule():
                return Sheets.GetSchadule(week.Name.Tomorrow(
                ), EvenWeek.FirstGroup.Range(), 'ROWS')
            
            def GetSchaduleByWeekName(weekname):
                return Sheets.GetSchadule(weekname, EvenWeek.FirstGroup.Range(), 'ROWS')
            
            def SchaduleByHours(sheetName, hour):
                return Sheets.GetSchadule(sheetName, EvenWeek.FirstGroup.HoursRange(hour), 'ROWS') 
        class SecondGroup:
            def GetTodaysSchadule():
                return Sheets.GetSchadule(week.Name.Today(
                ), EvenWeek.SecondGroup.Range(), 'ROWS')

            def GetTomorrowsSchadule():
                return Sheets.GetSchadule(week.Name.Tomorrow(
                ), EvenWeek.SecondGroup.Range(), 'ROWS')
            
            def GetSchaduleByWeekName(weekname):
                return Sheets.GetSchadule(weekname, EvenWeek.SecondGroup.Range(), 'ROWS')
            
            def SchaduleByHours(sheetName, hour):
                return Sheets.GetSchadule(sheetName, EvenWeek.SecondGroup.HoursRange(hour), 'ROWS')
            
# расписание на нечетной неделе
    class OddWeek:
        class FirstGroup:
            def GetTodaysSchadule():
                return Sheets.GetSchadule(week.Name.Today(
                ), OddWeek.FirstGroup.Range(), 'ROWS')

            def GetTomorrowsSchadule():
                return Sheets.GetSchadule(week.Name.Tomorrow(
                ), OddWeek.FirstGroup.Range(), 'ROWS')
            
            def GetSchaduleByWeekName(weekname):
                return Sheets.GetSchadule(weekname, OddWeek.FirstGroup.Range(), 'ROWS')
            
            def SchaduleByHours(sheetName, hour):
                return Sheets.GetSchadule(sheetName, OddWeek.FirstGroup.HoursRange(hour), 'ROWS')
                
        class SecondGroup:
            def GetTodaysSchadule():
                return Sheets.GetSchadule(week.Name.Today(
                ), OddWeek.SecondGroup.Range(), 'ROWS')

            def GetTomorrowsSchadule():
                return Sheets.GetSchadule(week.Name.Tomorrow(
                ), OddWeek.SecondGroup.Range(), 'ROWS')
            
            def GetSchaduleByWeekName(weekname):
                return Sheets.GetSchadule(weekname, OddWeek.SecondGroup.Range(), 'ROWS')
            
            def SchaduleByHours(sheetName, hour):
                return Sheets.GetSchadule(sheetName, OddWeek.SecondGroup.HoursRange(hour), 'ROWS')
            



