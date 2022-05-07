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
    Start = Sheets.GetTimesBySheetName(todaysWeekName,StartTimeRange,"ROWS")
    End =  Sheets.GetTimesBySheetName(todaysWeekName,EndTimeRange,"ROWS")
        