#Antonio Karlo Mijares
#ICS4U-01
#November 24 2016
#1D_2D_arrays.py

#Creates 1D arrays, for the variables to be placed in
characteristics = []
num = []

#Creates a percentage value for the numbers to be calculated with
base = 20
percentage = 100

#2d Arrays

#Ugly Arrays
ugly_one_D = []
ugly_one_D_two = []
ugly_two_D = []
#Nice Array
nice_two_D = []

#Sets the default file name to be open
filename = ('character')

#Strength function that will write to a 1D Array
def strength():
    #Opens the file
    with open(str(filename)+'.txt','r') as s:
        #Reads the file into a list
        line = s.read().splitlines()
        #Strips a part from the selected section
        name = line[3].strip(': 17')
        number = line[3].strip('Strength: ')
        
        #Appends the info to the 1D Arrays
        characteristics.append(name)
        num.append(number)

#Constitution function that will write to a 1D Array
def constitution():
    #Opens the file
    with open(str(filename)+'.txt','r') as s:
        #Reads the file into a list
        line = s.read().splitlines()
        #Strips a part from the selected section
        name = line[4].strip(': 10')
        number = line[4].strip('Constitution: ')
        
        #Appends the info to the 1D Arrays
        characteristics.append(name)
        num.append(number)

#Dexerity function that will write to a 1D Array
def dexerity():
    with open(str(filename)+'.txt','r') as s:
        #Reads the file into a list
        line = s.read().splitlines()
        #Strips a part from the selected section
        name = line[5].strip(': 8')
        number = line[5].strip('Dexerity: ')
        
        characteristics.append(name)
        num.append(number)

#Intelligence function that will write to
def intelligence():
    with open(str(filename)+'.txt','r') as s:
        #Reads the file into a list
        line = s.read().splitlines()
        #Strips a part from the selected section
        name = line[6].strip(': 19')
        number = line[6].strip('Intelligence: ')
        
        #Appends the info to the 1D Arrays
        characteristics.append(name)
        num.append(number)

#Wisdom function that will write to
def wisdom():
    with open(str(filename)+'.txt','r') as s:
        #Reads the file into a list
        line = s.read().splitlines()
        #Strips a part from the selected section
        name = line[7].strip(': 2')
        number = line[7].strip('Wisdom: ')
        
        #Appends the info to the 1D Arrays
        characteristics.append(name)
        num.append(number)

#Charisma function that will write to
def charisma():
    with open(str(filename)+'.txt','r') as s:
        #Reads the file into a list
        line = s.read().splitlines()
        #Strips a part from the selected section
        name = line[8].strip(': 9')
        number = line[8].strip('Charisma: ')
        
        #Appends the info to the 1D Arrays
        characteristics.append(name)
        num.append(number)

#2d function Array that creates the 2D Array (Nice Way)
def real_two_d(nice_two_D):
    nice_two_D = [characteristics,num]
    for row in nice_two_D:
       for element in row:
          print(element, end=" ")
       print()
    return nice_two_D

#2d function Array that creates the 2D Array (UGLY Way)
def notreal_two_d(ugly_two_D):
    ugly_two_D = [characteristics,num]
    return ugly_two_D

#Percentage function calculation that determines the 
#percentage for each stat
def percentagecalc():
    #Converts the number into a interger
    #Then divides it by base to be multiplied by 100
    strengthpercent = int(num[0]) / base * percentage
    constitutionpercent = int(num[1]) / base * percentage
    dexeritypercent = int(num[2]) / base * percentage
    intelligencepercent = int(num[3]) / base * percentage
    wisdompercent = int(num[4]) / base * percentage
    charismapercent = int(num[5]) / base * percentage
    
    #Displays the percentage results
    print('')
    print('Strength: '+ str(strengthpercent)+'%')
    print('Constitution: '+ str(constitutionpercent)+'%')
    print('Dexerity: '+ str(dexeritypercent)+'%')
    print('Intelligence: '+ str(intelligencepercent)+'%')
    print('Wisdom: '+ str(wisdompercent)+'%')
    print('Charisma: '+ str(charismapercent)+'%')
           
menu = True
#Runs the menu loop
while menu:
    #Menu Screen
    print('')
    print('Welcome to the 2D Array Creation!')
    print('Press:')
    print('S to start')
    print('H for help')
    print('Q to quit')
    #Waits for player input
    menuinput = input('Response: ')
    #States if user inputs s
    if (menuinput == 's') or (menuinput == 'S'):
        #Runs the 1D array functions
        strength()
        constitution()
        dexerity()
        intelligence()
        wisdom()
        charisma()
        #Runs the percentage function
        percentagecalc()
        #Runs the ugly 2d function
        uglytwo_d= notreal_two_d(ugly_two_D)
        #Displays the ugly 2d function
        print('')
        print('Ugly Two D Array:')
        print(uglytwo_d)
        print('')
        print('Nice Two D Array: ') 
        #Runs the nice 2d function
        nice_two_D2= real_two_d(nice_two_D)
        #Displays the nice 2d function
        #print('Nice Two D Array:')
        #print(nice_two_D2)
        
     #States if user inputs h
    elif (menuinput == 'h') or (menuinput == 'H'):
        print('')
        print('This program creates a 2D array')
        print('')
        helpinput = input('Press Enter to continue.')
        
    #States if user inputs q
    elif (menuinput == 'q') or (menuinput == 'Q'):
        #Quits the program
        print('')
        print('You hage quit the program')
        print('Have a nice day!')
        menu = False
    #States if user inputs anything else
    else:
        #Error screen
        print("Sorry, that's an invalid input!")
        