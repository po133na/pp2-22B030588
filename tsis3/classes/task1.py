class Strings:
    def __init__(self, getString):
        self.getString = getString
    def printString(self):
        return self.getString.upper()
        
s = Strings(input())
print(s.printString())