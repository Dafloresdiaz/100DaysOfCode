from ejercicio_23 import ejercicio23

exercise = ejercicio23()

def testPalindrome():
    text = "ababas"
    result = exercise.wordPalindrome(text)
    assert result == False

def testPalindrome2():
    text = "ababa"
    result = exercise.wordPalindrome(text)
    assert result == True

def testPalindrome3():
    text = "anita lava la tina"
    result = exercise.wordPalindrome(text)
    assert result == True
