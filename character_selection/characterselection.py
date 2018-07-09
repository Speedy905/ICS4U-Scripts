#Antonio Karlo Mijares
#ICS4U-01
#November 10 2016
#characterselection.py

#Imports the random module
import random

#Sets the default file name
filename = ('character')


#Creates a dictionary of the chracter information
Swords = ['small','medium','large']
Axes = ['small','medium','large']
MagicalPotions = ['red','blue','green']
Bows = ['cross','short','long']
Loot = ['gems','coins','artifact']
StuffAlive = ['food','healing potions']
MagicalItems = ['wand','scroll','ring','empty/none']
Classes = ['Fighter','Wizard','Thief','Healer','Ranger']
Races = ['Human','Elf','Dwarf','Halfling','Gnome']
MiscellaneousItems = ['torch','lamp','key','map','empty / none']

#A function to change the file name
def changefilename(newfilename):
    newfilename = input('Type in the new file name: ')
    filename = newfilename
    with open(str(filename)+'.txt','a') as c:
        c.write('\n')
    return filename
    return newfilename

#A function to create your character name
def createCharacter():
    firstname = input ('Type in your first name: ')
    lastname = input ('Type in your last name: ')
    with open(str(filename)+'.txt', 'w') as c:
        c.write('Character: ')
        c.write(str(firstname) + ' ') #Adds in the first name
        c.write(str(lastname)) #Adds in the last name
        c.write('\n') #Concantenate a new line

#A function to randomize the character's class
def randomClass():
    newClass = random.randint(0,4) #Selects a number to determine the position
    #Writes the items onto the text file
    with open(str(filename)+'.txt', 'a') as c:
        c.write('Class: ')
        c.write(Classes[newClass])
        c.write('\n')

#A function to randomize the character's race
def randomRace():
    newRace = random.randint(0,4)
    #Writes the items onto the text file
    with open(str(filename)+'.txt','a') as c:
        c.write('Race: ')
        c.write(Races[newRace])
        c.write('\n')

#A function to randomize the character's Strength
def randomStrength():
    newStrength = random.randint(0,20)
    #Writes the items onto the text file
    with open(str(filename)+'.txt','a') as c:
        c.write('Strength: ')
        c.write(str(newStrength))
        c.write('\n')

#A function to randomize the character's Constitution
def randomConstitution():
    newConstitution = random.randint(0,20)
    #Writes the items onto the text file
    with open(str(filename)+'.txt','a') as c:
        c.write('Constitution: ')
        c.write(str(newConstitution))
        c.write('\n')

#A function to randomize the character's Dexterity
def randomDexterity():
    newDexterity = random.randint(0,20)
    #Writes the items onto the text file
    with open(str(filename)+'.txt','a') as c:
        c.write('Dexterity: ')
        c.write(str(newDexterity))
        c.write('\n')

#A function to randomize the character's Intelligence
def randomIntelligence():
    newIntelligence = random.randint(0,20)
    #Writes the items onto the text file
    with open(str(filename)+'.txt','a') as c:
        c.write('Intelligence: ')
        c.write(str(newIntelligence))
        c.write('\n')

#A function to randomize the character's Wisdom
def randomWisdom():
    newWisdom = random.randint(0,20)
    #Writes the items onto the text file
    with open(str(filename)+'.txt','a') as c:
        c.write('Wisdom: ')
        c.write(str(newWisdom))
        c.write('\n')

#A function to randomize the character's Charisma
def randomCharisma():
    newCharisma = random.randint(0,20)
    #Writes the items onto the text file
    with open(str(filename)+'.txt','a') as c:
        c.write('Charisma: ')
        c.write(str(newCharisma))
        c.write('\n')

#A function to randomize the character's weapon
def backWeapon():
    randomback = random.randint(1,3)
    if randomback == 1:
        swordsize = random.randint(0,2)
        #Writes the items onto the text file
        with open(str(filename)+'.txt','a') as c:
            c.write('Back Slot: ')
            c.write(Swords[swordsize]+' ')
            c.write('sword')
            c.write('\n')
    elif randomback == 2:
        axesize = random.randint(0,2)
        #Writes the items onto the text file
        with open(str(filename)+'.txt','a') as c:
            c.write('Back Slot: ')
            c.write(Axes[axesize]+' ')
            c.write('axe')
            c.write('\n')
    elif randomback == 3:
        bowsize = random.randint(0,2)
        #Writes the items onto the text file
        with open(str(filename)+'.txt','a') as c:
            c.write('Back Slot: ')
            c.write(Bows[bowsize]+' ')
            c.write('bow')
            c.write('\n')

#A function to randomize the belt's weapon
def beltWeapon():
    randombelt = random.randint(1,3)
    if randombelt == 1:
        swordsize2 = random.randint(0,2) - 1 #Subtracts by one to prevent identification
        #Writes the items onto the text file
        with open(str(filename)+'.txt','a') as c:
            c.write('Belt Slot: ')
            c.write(Swords[swordsize2]+' ')
            c.write('sword')
            c.write('\n')
    elif randombelt == 2:
        axesize2 = random.randint(0,2) - 1
        #Writes the items onto the text file
        with open(str(filename)+'.txt','a') as c:
            c.write('Belt Slot: ')
            c.write(Axes[axesize2]+' ')
            c.write('axe')
            c.write('\n')
    elif randombelt == 3:
        bowsize2 = random.randint(0,2) - 1
        #Writes the items onto the text file
        with open(str(filename)+'.txt','a') as c:
            c.write('Belt Slot: ')
            c.write(Bows[bowsize2]+' ')
            c.write('bow')
            c.write('\n')

#A function that randomizes the left hand item
def leftHand():
    leftitem = random.randint(0,4)
    #Writes the items onto the text file
    with open(str(filename)+'.txt','a') as c:
        c.write('Left Hand: ')
        c.write(MiscellaneousItems[leftitem])
        c.write('\n')

#A function that randomizes the right hand item
def rightHand():
    rightitem = random.randint(0,4) - 1 #Subtracts by one to prevent identification
    #Writes the items onto the text file
    with open(str(filename)+'.txt','a') as c:
        c.write('Right Hand: ')
        c.write(MiscellaneousItems[rightitem])
        c.write('\n')

#A function that randomizes the pack
def pack():
    #Randomizes items for the backpack
    potionitems = random.randint(0,2)
    lootitems = random.randint(0,2)
    aliveitems = random.randint(0,1)
    magicitems = random.randint(0,3)
    otheritems = random.randint(0,4)
    potionitems1 = random.randint(0,2)
    lootitems1 = random.randint(0,2)
    aliveitems1 = random.randint(0,1)
    magicitems1 = random.randint(0,3)
    otheritems1 = random.randint(0,4)
    #Writes the items onto the text file
    with open(str(filename)+'.txt','a') as c:
        c.write('Pack: ')
        c.write(StuffAlive[aliveitems]+ ', ')
        c.write(Loot[lootitems]+ ', ')
        c.write(MagicalPotions[potionitems]+' potion, ')
        c.write(MiscellaneousItems[otheritems]+ ', ')
        c.write(MagicalItems[magicitems]+ ', ')
        c.write('\n')
        c.write('      ')
        #Creates a new line to prevent horizontal extenstion
        c.write(StuffAlive[aliveitems1]+ ', ')
        c.write(Loot[lootitems1]+ ', ')
        c.write(MagicalPotions[potionitems1]+' potion, ')
        c.write(MiscellaneousItems[otheritems1]+ ', ')
        c.write(MagicalItems[magicitems1]+ ' ')
        c.write('\n')

#A function that reads the entire characteristics
def readFile():
    with open(str(filename)+'.txt','r') as c:
        for line in c:
            print(line, end='')

menu = True
#Runs the menu loop
while menu:
    #Menu Screen
    print('')
    print('Welcome to the character creation!')
    print('Press:')
    print('S to start')
    print('H for help')
    print('Q to quit')
    #Waits for player input
    menuinput = input('Response: ')
    #States if user inputs s
    if (menuinput == 's') or (menuinput == 'S'):
        charactercreation = True
        while charactercreation:
            #Runs the called functions below
            print('Your text file will be called ' +str(filename)+'.txt')
            print('Do you want to change it?')
            print('1. Yes')
            print('2. No')
            changefileinput = input('Response: ')
            if changefileinput == '1':
                filename = changefilename(filename)
                print('')
                createCharacter()
                randomClass()
                randomRace()
                randomStrength()
                randomConstitution()
                randomDexterity()
                randomIntelligence()
                randomWisdom()
                randomCharisma()
                backWeapon()
                beltWeapon()
                leftHand()
                rightHand()
                pack()
                readFile()
                print('')
                charactercreation = False
            elif changefileinput == '2':
                print('')
                createCharacter()
                print('')
                randomClass()
                randomRace()
                randomStrength()
                randomConstitution()
                randomDexterity()
                randomIntelligence()
                randomWisdom()
                randomCharisma()
                backWeapon()
                beltWeapon()
                leftHand()
                rightHand()
                pack()
                readFile()
                print('')
                charactercreation = False
    #States if user inputs h
    elif (menuinput == 'h') or (menuinput == 'H'):
        print('')
        print('This is a character creation program.')
        print('')
        print('You type in your first and last name,')
        print('and the program will generate a text file')
        print('where your randomly generated character has been made.')
        print('')
        helpinput = input('Press Enter to continue.')
    #States if user inputs q
    elif (menuinput == 'q') or (menuinput == 'Q'):
        #Quits the program
        print('')
        print('Thanks for using the character creation!')
        print('Have a nice day!')
        menu = False
    #States if user inputs anything else
    else:
        #Error screen
        print("Sorry, that's an invalid input!")
