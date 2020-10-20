from ejercicio_3 import erastosthenesAlgorith as algorithm
from ejercicio_3 import createAList as listToNumber

def testcheckPrimeListWhenIsTen():
    correctList = [2, 3, 5, 7]
    testList = algorithm(listToNumber(10), 10)
    result = correctList == testList
    assert result == True

def testcCheckPrimeListWhenuIsThirty():
    correctList = [2,3,5,7,11,13,17,19,23,29]
    testList = algorithm(listToNumber(30),30)
    result = correctList == testList
    assert result == True

def testCheckPrimeListWhenIsOneHundred():
    correcList = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
    testList = algorithm(listToNumber(100),100)
    result = correcList == testList
    assert result == True

def testCheckPrimeListIsWrong():
    wrongList = [2,3,5,7,11,12,13,17,19,23,29]
    testList = algorithm(listToNumber(30), 30)
    result = wrongList == testList
    assert result == False

