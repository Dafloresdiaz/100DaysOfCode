from ejercicio_17 import commonDenominator

def testfindDenominator1():
    listNumbers = [ 192, 270]
    result = commonDenominator(listNumbers)
    print(result)
    assert result == 6

def testfindDenominator2():
    listNumbers = [20,50,120]
    result = commonDenominator(listNumbers)
    print(result)
    assert result == 10

def testfindDenominator():
    listNumbers = [42,56,14]
    result = commonDenominator(listNumbers)
    print(result)
    assert result == 14
