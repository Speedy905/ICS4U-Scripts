#Antonio Karlo Mijares

class BaseClass (object):
    def __init__ (self):
        self.x = 5
    def printWord (self):
        print("Word")
        
class Interger (BaseClass):
    def __init__ (self):
        super (Interger,self).__init__()
        self.x = 17
        
class Word (BaseClass):
    def printWord(self):
        print("Another One")

class Replacement (Word):
    def printX (self):
        print('x')


a = Interger()
b = Word()
c = Replacement()
print (a.x)
b.printWord()
c.printX()
