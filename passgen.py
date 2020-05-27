import string
import random

class PasswordGenerator:
    allowedCharacters = string.ascii_letters
    allowedSpecialChars = "!@#$%^&*_()"
    allowedNumbers = string.digits
    passLength = 0
    charCount = 4
    specialCharCount = 3
    numCount = 3
    charMix = ""
    resultPassword = ""

    def getTenCharacterPassword(self):
        # length = self.passLength
        result = ""
        for count in range(self.charCount):
            self.charMix += random.choice(self.allowedCharacters)
        for count in range(self.specialCharCount):
            self.charMix += random.choice(self.allowedSpecialChars)
        for count in range(self.numCount):
            self.charMix += random.choice(self.allowedNumbers)
        mixList = [char for char in self.charMix]
        # print(str(mixList))
        finalList = random.sample(mixList,len(mixList))
        # print(str(finalList))
        for char in finalList:
            self.resultPassword += str(char)
        # print(self.resultPassword)
        return self.resultPassword
