def sumOfElements(listOfElements, n):
    sumNum = 0
    for i in listOfElements:
        for y in listOfElements:
            if (i != y) and (i + y == n):
                print("Numbers:" + str(i) +"+"+ str(y)+"="+str(i+y))
                return True
    return False
