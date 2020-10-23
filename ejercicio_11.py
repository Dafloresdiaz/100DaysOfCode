def linkedListSwap(linkedList):
    n =len(linkedList)
    for i in range(n):
        if (i%2) != 0:
            linkedList[i], linkedList[i-1]= linkedList[i-1], linkedList[i]

    return linkedList
