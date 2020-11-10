class ejercicio23():

    def wordPalindrome(self, text):
        #This code is to eliminate the blank spaces and treat the text normally
        text = text.replace(' ', '')
        reverseWord = text[::-1]
        if text == reverseWord:
            return True
        else:
            return False
