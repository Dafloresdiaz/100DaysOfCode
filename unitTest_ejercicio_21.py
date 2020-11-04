from ejercicio_21 import ejercicio21

exercise = ejercicio21()
def testBits():
    bitList = [1,0,1,0,1,0,1,0]
    result = exercise.swapBits(bitList)
    assert result == [0,1,0,1,0,1,0,1]

def testBits2():
    bitList = [1,1,1,0,0,0,1,0]
    result = exercise.swapBits(bitList)
    assert result == [1,1,0,1,0,0,0,1]

