from ejercicio_6 import totalOverlaps as TL

def testOverLap1():
    listOfIntervals = [[1,2],[2,3],[3,5]]
    result = TL(listOfIntervals)
    assert result == 0

def testOverlap2():
    listOfIntervals = [[7,9], [2,4], [5,8]]
    result = TL(listOfIntervals)
    assert result == 0

def testOverlap3():
    listOfIntervals = [[1,2], [2,3], [3,4], [1,3]]
    result = TL(listOfIntervals)
    assert result == 1
