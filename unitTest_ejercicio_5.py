from ejercicio_5 import sortString
from ejercicio_5 import stringToList as stl

def testSortList():
    text = "aab"
    result = sortString(stl(text))
    assert result == "aba"

def testSortString2():
    text = "abbdaac"
    result = sortString(stl(text))
    assert result == "ababacd"
