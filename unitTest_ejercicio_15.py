from ejercicio_15 import listPrefix

def testList1():
    listWord = ['perro', 'abeja', 'caballo']
    result = listPrefix(listWord)
    assert result == ['p','a','c']

def testList2():
    listWord = ['perro', 'pato', 'pollo']
    result = listPrefix(listWord)
    print(result)
    assert result == ['p', 'pa', 'po']

def testList3():
    listWord = ['dog', 'cat', 'apple', 'apricot','aperitive', 'fish']
    result = listPrefix(listWord)
    print(result)
    assert result == ['d','c','a','ap','ape','f']
