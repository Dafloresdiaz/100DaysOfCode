def stringToList(text):
    listOfChar = list(text.strip())
    return listOfChar

def sortString(listOfChar):
    n = len(listOfChar)
    final = ""
    print(n)
    listOfChar.sort()
    for i in range(0, n-1):
        if listOfChar[i] != listOfChar[i+1]:
            continue
        else:
            if i + 2 == n:
                return None
            else:
                for y in range(i+2, n):
                    if listOfChar[y] != listOfChar[i+1]:
                        listOfChar[i+1], listOfChar[y] = listOfChar[y], listOfChar[i+1]
                        break
    return final.join(listOfChar)





