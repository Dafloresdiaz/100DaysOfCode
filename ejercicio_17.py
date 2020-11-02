def commonDenominator(listNumbers):
    listNumbers.sort(reverse=True)
    a = listNumbers[0]
    for number in listNumbers[1:]:
        a = euclAlgorithm(a, number)
    return a

def euclAlgorithm(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        reminder = a % b
        return (euclAlgorithm(b, reminder))


