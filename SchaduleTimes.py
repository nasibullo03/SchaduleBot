from pprint import *
import Range 
import GetData 
import week 
# сегдняшный день
todaysWeekName = week.GetTodaysWeekName()
# координации начало и конец "Начало"
StartTimeRange = F'{Range.startTimeColumn}{Range.startRangeNum}:{Range.startTimeColumn}{Range.endRangeNum}'
# координации начало и конец "Конец"
EndTimeRange = F'{Range.endTimeColumn}{Range.startRangeNum}:{Range.endTimeColumn}{Range.endRangeNum}'

# массив всех время начало урока
# class listOfTimes:
Start = GetData.GetTimesBySheetName(todaysWeekName,StartTimeRange,"ROWS")
End =  GetData.GetTimesBySheetName(todaysWeekName,EndTimeRange,"ROWS")

pprint(Start)