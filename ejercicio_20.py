
class exercise20:

    def findNumbers(self, listNumbers):
        resultList = []
        for i in range(len(listNumbers)):
            #First  position
            if i == 0:
                if listNumbers[i]%listNumbers[i+1] == 0:
                    resultList.append(listNumbers[i+1])
            #Last Position
            elif i == (len(listNumbers)-1):
                if listNumbers[i]%listNumbers[i-1] == 0:
                    resultList.append(listNumbers[i-1])
            else:
                if listNumbers[i]%listNumbers[i+1] == 0:
                    resultList.append(listNumbers[i+1])
                if listNumbers[i]%listNumbers[i-1] == 0:
                    resultList.append(listNumbers[i-1])
        return resultList
                
