from ejercicio_12 import stringIsomorphic as IS

def testStringIso1():
    result = IS("abc", "bcd")
    assert result == True

def testStrinIso2():
    result = IS("abc", "bbcc" )
    assert result == False

def testStringIso3():
    result = IS("aac", "cbs")
    assert result == False
