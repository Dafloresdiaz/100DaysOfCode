from ejercicio_9 import obtainTheGreaterValue as OG

def testWhenIIsSeven():
    listOfNumbers = [5,2,4,2,3,1,6,7]
    result = OG(listOfNumbers)
    assert result == 7

def testWhenIsFive():
    listOFNumbers = [5,1,3,5,2,3,4,1]
    result = OG(listOFNumbers)
    assert result == 5

def testWhenIsTwenty():
    listOfNumbers =[10,4,3,2,1,3,4,6,8,18,14,1,15,20,10,13,14,15,19,19,17]
    result = OG(listOfNumbers)
    assert result == 20
