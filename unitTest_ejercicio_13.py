from ejercicio_13 import sumTotal as ST

def testSumTotal1():
    listOfNumbers = [8,-1,3,4,0]
    result = ST(listOfNumbers)
    assert result == 15

def testSumTatal2():
    listOfNumbers = []
    result = ST(listOfNumbers)
    assert result == 0

def testSumTotal3():
    listOfNumbers = [-4,5,1,0]
    result = ST(listOfNumbers)
    assert result == 6
