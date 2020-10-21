def findValue(listOfNumbers,n):
    listOfNumbers.sort()
    print(listOfNumbers)
    size = len(listOfNumbers)
    minValue = 0
    highValue = size - 1

    position = (minValue+highValue)//2
    foundIt = False

    while listOfNumbers[position] != n:

        if listOfNumbers[position] < n:
            minValue = position + 1
        else:
            highValue = position - 1
            
        position = ((minValue+highValue)//2)

    return position

def findMinValue(listOfNumbers):
    minValue = listOfNumbers[0]
    for i in listOfNumbers:
        if i < minValue:
            minValue = i

    print(minValue)
    return minValue
    


