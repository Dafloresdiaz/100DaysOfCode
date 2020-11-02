from ejercicio_18 import majorityOfElements

def testMajority1():
    listElements = [1, 2, 1, 1, 3, 4, 0]
    result = majorityOfElements(listElements)
    assert result == 1
