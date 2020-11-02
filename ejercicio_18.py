def majorityOfElements(listElements):
    dic = {}
    element = 0
    #Eliminate the duplicates in the original list
    listNoDupli = []
    [listNoDupli.append(x) for x in listElements if x not in listNoDupli]
    
    for i in listNoDupli:
        dic[i] = listElements.count(i)
        countEle = listElements.count(i)
        if countEle >= (len(listElements)//2):
            element = i

    print(dic)
    return element
