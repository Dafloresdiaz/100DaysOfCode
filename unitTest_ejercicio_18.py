from ejercicio_18 import majorityOfElements

def testMajority1():
    listElements = [1, 2, 1, 1, 3, 4, 0]
    result = majorityOfElements(listElements)
    assert result == 1

def testMajority2():
    listElements = [3,4,52,1,4,1,4,21,4,6,4]
    result = majorityOfElements(listElements)
    assert result == 4
