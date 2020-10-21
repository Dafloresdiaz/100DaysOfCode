from ejercicio_10 import findValue
from ejercicio_10 import findMinValue

def testWhenIsTen():
    listOfNumbers = [5,3,1,9,10,3,4,7,8]
    result = findValue(listOfNumbers,10)
    assert result == 8

def testWhenIsTwenty():
    listOfNumbers = [10,11,13,1,5,9,64,20,19,17,32,23,90,100,43,12,45,78,21]
    result = findValue(listOfNumbers, 20)
    assert result == 9

def testMinValue1():
    listOfNumbers = [5,3,1,9,10,3,4,7,8]
    result = findMinValue(listOfNumbers)
    assert result == 1

def testMinValue2():
    listOfNumbers = [1000,11,13,111,55,99,64,20,19,17,32,23,90,100,43,12,45,78,21]
    result = findMinValue(listOfNumbers)
    assert result == 11
