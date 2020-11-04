from ejercicio_20 import exercise20

exercise = exercise20()

def testList():
    listNumbers=[1,3,6,24]
    result = exercise.findNumbers(listNumbers)
    print(result)
    assert result == [1,3,6] 
    
def testList2():
    listNUmbers = [3,5,10,20,21]
    result = exercise.findNumbers(listNUmbers)
    print(result)
    assert result == [5,10]

