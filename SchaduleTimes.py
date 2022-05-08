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
    StartTimesArray = []
    def GetValues():
      listOfTimes.Start = Sheets.GetTimesBySheetName('Понедельник',StartTimeRange,"ROWS")
      listOfTimes.End = Sheets.GetTimesBySheetName('Понедельник',EndTimeRange,"ROWS")
      listOfTimes.StartTimesArray = []
      for time in range(len(listOfTimes.Start['values'])):
          time_temp =  listOfTimes.Start['values'][time][0].split('.')
          listOfTimes.StartTimesArray.append([int(time_temp[0]),int(time_temp[1])])
      # pprint(listOfTimes.StartTimesArray)
  


