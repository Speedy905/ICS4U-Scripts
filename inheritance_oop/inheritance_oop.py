#Antonio Karlo Mijares

class BaseCharacter (object):
    def __init__(self):
        self.health = 100
    def printName (self):
        print (self.name)

class NonPlayable (BaseCharacter):
    pass

class Enemy (NonPlayable):
    def __init__(self):
        self.attack -= 5

class Friend (NonPlayable):
    pass

class Playable (BaseCharacter):
    def __init__ (self):
        self.weapon = Weapon()

class Archer (Playable):
    pass

class Green_Lantern (Playable):
    pass

class Buther (Playable):
    pass

class Weapon (object):
    pass