def listPrefix(listWords):
    prefixes = []
    for word in listWords:
        if word[0] in prefixes:
            prefix = ""
            i = 2
            notInList = True
            while notInList:
                prefix = word[0:i]
                if prefix in prefixes:
                    i += 1
                else:
                    prefixes.append(prefix)
                    notInList = False
        else:
            prefixes.append(word[0])
    return prefixes



