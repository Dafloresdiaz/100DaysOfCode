from ejercicio_1 import sumOfElements as SE

def testWhenIsFalse():
    listOfElements = [10,15,3,7]
    number = 100
    assert (SE(listOfElements, number)) == False

def testWhenIsTrue():
    listOfElements = [1,4,9,15,10,16,17,20]
    number = 37
    assert (SE(listOfElements, number)) == True

def testWhenTheSumIsTwoTimes():
    listOfElements = [1,5,3,10,11,15,-2]
    number = 8
    assert (SE(listOfElements,number)) == True
