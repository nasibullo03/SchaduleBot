from importlib.metadata import PathDistribution
from select import select
import week


_weekName = "" 
class WeekType:
    
    def Get():
        return _weekName

    def Set():
        global _weekName
        _weekName = week.GetOddOrEvenWeek()

    def GetFromKemsu():
        return week.GetOddOrEvenWeek() 
    
    