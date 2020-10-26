listOfElements = []
def pushItem(item):
    listOfElements.append(item)
    return listOfElements

def popItem():
    if len(listOfElements) > 0:
        listOfElements.pop(len(listOfElements) - 1)
    else:
        print("The list is empty")
    return listOfElements


