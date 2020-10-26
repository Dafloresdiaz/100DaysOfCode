from ejercicio_14 import pushItem
from ejercicio_14 import popItem
def testPushItem():
    result = pushItem(1)
    assert result == [1]

def testPushItem2():
    result = pushItem(2)
    assert result == [1,2]

def testPopItem():
    result = popItem()
    assert result == [1]

def testPopItem2():
    result = popItem()
    assert result == []

def testPopItem3():
    result = popItem()
    assert result == []

def testPushItem3():
    result = pushItem("Hola")
    assert result == ["Hola"]

def testPusItem4():
    result = pushItem(100)
    print(result)
    assert result == ["Hola", 100]
    

