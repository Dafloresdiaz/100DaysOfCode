def sumTotal(listOfNumbers):
    sumTotal = 0
    if listOfNumbers:
        for number in listOfNumbers:
            if number > 0:
                sumTotal += number
    return sumTotal
