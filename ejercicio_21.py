class ejercicio21:
    
    def swapBits(self, bitList):
        if len(bitList) == 8:
            for i in range(len(bitList)):
                if (i % 2) != 0:
                    bitList[i], bitList[i-1] = bitList[i-1], bitList[i]
        return bitList


