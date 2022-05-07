from pprint import *
import Range 
import Sheets 
import week 
# сегдняшный день
todaysWeekName = week.Name.Today()
# координации начало и конец "Начало"
StartTimeRange = F'{Range._startTimeColName}{Range.startRangeId}:{Range._startTimeColName}{Range.endRangeNum}'
# координации начало и конец "Конец"
EndTimeRange = F'{Range._endTimeColName}{Range.startRangeId}:{Range._endTimeColName}{Range.endRangeNum}'

# массив всех время начало урока
class listOfTimes:
    Start = []
    End =  []
    StartTimesArray = [[3,27], [3, 28], [3, 29], [3, 30], [3, 31], [3, 35]]
    def GetValues():
      listOfTimes.Start = Sheets.GetTimesBySheetName('Понедельник',StartTimeRange,"ROWS")
      listOfTimes.End = Sheets.GetTimesBySheetName('Понедельник',EndTimeRange,"ROWS")
      # for time in range(len(listOfTimes.Start['values'])):
      #     time_temp =  listOfTimes.Start['values'][time][0].split('.')
      #     listOfTimes.StartTimesArray.append([int(time_temp[0]),int(time_temp[1])])
  
