from ejercicio_11 import linkedListSwap

def testLinkedList():
    linkedList = [1,2,3,4,5]
    result = linkedListSwap(linkedList)
    assert result == [2,1,4,3,5]

def testLinkedList2():
    linkedList = [3,6,5,4,3,1,6,7,8,1]
    result = linkedListSwap(linkedList)
    assert result == [6,3,4,5,1,3,7,6,1,8]

def testLinkedList3():
    linkedList = [4,3,1,4,57,5,3,7,8,9,100]
    result = linkedListSwap(linkedList)
    assert result == [3,4,4,1,5,57,7,3,9,8,100]
