import random

def minSwaps(n):
    normalList = [i for i in range(1, n+1)]
    randomList = normalList[:]
    random.shuffle(randomList)

    swap = 0

    for i in range(n):
        if normalList[i] == randomList[i]:
            continue
        else:
            indexChange = randomList.index(normalList[i])
            new = randomList[i]

            randomList[i] = randomList[indexChange]
            randomList[indexChange] = new
            swap += 1

    return swap

