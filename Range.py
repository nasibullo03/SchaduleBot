
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
    
        def Range(self):
            return self.makeRange(self._fistGroupColName)
        def HoursRange(self, hour):
            return F'{self._fistGroupColName}{HoursColumn.Id(hour)}'

    class SecondGroup:
        def Range(self):
            return self.makeRange(self._secGroupColName)
        def HoursRange(self, hour):
            return F'{self._secGroupColName}{HoursColumn.Id(hour)}'
    

# нечетная неделя


class OddWeek:
    fistGroupColumn = 'E'
    secondGroupColumn = 'F'
    
    class FirstGroup:
        
        def Range(self):
            return self.makeRange(self._fistGroupColName)
        def HoursRange(self, hour):
            return F'{self._fistGroupColName}{HoursColumn.Id(hour)}'

    class SecondGroup:
        def Range(self):
            return self.makeRange(self._secGroupColName)
        def HoursRange(self, hour):
            return F'{self._secGroupColName}{HoursColumn.Id(hour)}'


class HoursColumn:
    def Id(hour):
        return hour + startRangeId
