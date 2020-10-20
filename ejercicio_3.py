def createAList(number):
    listOfNumbers = [i for i in range(2, number+1)]
    return (listOfNumbers)

def removeNotPrimeNumbers(completeList,listOfRemoveNumbers):
    for i in listOfRemoveNumbers:
        if i in completeList:
            completeList.remove(i)
    return completeList

def erastosthenesAlgorith(listNumbers, number):
    newList =[ ]
    count = 2
    while count < number:
        for i in range(len(listNumbers)):
            if (listNumbers[i]%count == 0) and (listNumbers[i] >= count**2):
                newList.append(listNumbers[i])
        count += 1
    primeList = removeNotPrimeNumbers(listNumbers,sorted(newList))
    return primeList
