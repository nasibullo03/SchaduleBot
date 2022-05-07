
startRangeId = 4
endRangeNum = 13

_startTimeColName = 'A'
_endTimeColName = 'B'

def makeRange(col):
    return F'{col}{startRangeId}:{col}{endRangeNum}'

# четная неделя
class EvenWeek:
    _fistGroupColName = 'C'
    _secGroupColName = 'D'

    class FirstGroup:
    
        def Range():
            return makeRange(EvenWeek._fistGroupColName)
        def HoursRange(hour):
            return F'{EvenWeek._fistGroupColName}{HoursColumn.Id(hour)}'

    class SecondGroup:
        def Range():
            return makeRange(EvenWeek._secGroupColName)
        def HoursRange(hour):
            return F'{EvenWeek._secGroupColName}{HoursColumn.Id(hour)}'
    

# нечетная неделя
class OddWeek:
    _fistGroupColName = 'E'
    _secGroupColName = 'F'
    
    class FirstGroup:
        
        def Range():
            return makeRange(OddWeek._fistGroupColName)
        def HoursRange(hour):
            return F'{OddWeek._fistGroupColName}{HoursColumn.Id(hour)}'

    class SecondGroup:
        def Range():
            return makeRange(OddWeek._secGroupColName)
        def HoursRange(hour):
            return F'{OddWeek._secGroupColName}{HoursColumn.Id(hour)}'


class HoursColumn:
    def Id(hour):
        return hour + startRangeId

