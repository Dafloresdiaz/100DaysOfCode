def obtainTheGreaterValue(listOfElements):
    newList = []
    
    #Loop to detect each element in the list and eliminate duplicate with the next condition
    for i in listOfElements:
        if i not in newList:
            newList.append(i)
    newList.sort(reverse=True)
    print(newList)
    return (newList[0])
