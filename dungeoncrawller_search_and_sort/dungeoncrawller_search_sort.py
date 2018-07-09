#Antonio Karlo Mijares
#ICS4U-01
#November 21 2016
#dungeoncrawller_search_sort.py

#Imports the necessary modules
import random
from datetime import datetime

#Creates a dictionary for a pack
MagicalPotions = ['Red Potion','Blue Potion','Green Potion']
Loot = ['gems','coins','artifact']
StuffAlive = ['food','healing Potions']
MagicalItems = ['wand','scroll','ring','empty/none']
MiscellaneousItems = ['torch','lamp','key','map','empty / none']

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
    
    print('Pack: ')
    
    #Creates a list for the pack
    Pack = [StuffAlive[aliveitems],Loot[lootitems],MagicalPotions[potionitems],MiscellaneousItems[otheritems],MagicalItems[magicitems],
            StuffAlive[aliveitems1],Loot[lootitems1],MagicalPotions[potionitems1],MiscellaneousItems[otheritems1],MagicalItems[magicitems1]]
    
    
    #Returns the pack
    return Pack

#A function that randomizes stats
def createStats():
    #Randomises the new stats
    newStrength = random.randint(0,20)
    newConstitution = random.randint(0,20)
    newDexterity = random.randint(0,20)
    newIntelligence = random.randint(0,20)
    newWisdom = random.randint(0,20)
    newCharisma = random.randint(0,20)
    
    #Creates a list of the stats
    Stats = [newStrength,newConstitution,newDexterity,
             newIntelligence,newWisdom,newCharisma]
    return Stats

#A function that does a linear search
def linearSearch(item,list):
    found = False
    current_pos = 0
    while current_pos < len(list) and not found:
        #States if the item has been found
        if list[current_pos] == item:
            #Sets the variable to true
            found = True
        current_pos = current_pos + 1
    return found
    
#A function that does a binary search
def binarySearch(item,list):
    startTime = datetime.now()
    found = False
    bottom = 0
    top = len(list) - 1
    while bottom<=top and not found:
        middle = (bottom+top) // 2
        #Display the searching progress
        print(list[bottom])
        print(list[top])
        print(list[middle])
        
        if list[middle] == item:
            found = True
        elif list[middle] < item:
            bottom = middle + 1
        else:
            top = middle - 1
    print (datetime.now() - startTime)
    return found
    
#A function that sorts the binary number from smallest to largest (for the search)
def InsertionSortforSearch (list):
    
    for i in range(1,len(list)):

        current = list[i]
        position = i 
         
        # Check backwards through the sorted list for a proper position of the current list
        while((position > 0) and (list[position-1] > current)):
            list[position] = list[position-1]
            position = position-1
             
        if position != i:
            list[position] = current 
    return list 

#A function that sorts the binary number from smallest to largest (for ONLY sorting)
def InsertionSort (list):
    startTime = datetime.now()
    for i in range(1,len(list)):
        #Displays the sorting progress
        print(list)
        current = list[i]
        position = i 
         
        # Check backwards through the sorted list for a proper position of the current list
        while((position > 0) and (list[position-1] > current)):
            list[position] = list[position-1]
            position = position-1
        if position != i:
            list[position] = current
    print (datetime.now() - startTime)    
    return list 

#A function that sorts binary numbers from smallest to largest using the bubble
def BubbleSort (list):
    startTime = datetime.now()
    swaps = True
    while swaps:
        print(list)
        swaps = False
        for elements in range(len(list)-1):
            if list[elements]> list[elements+1]:
                swaps = True
                temporary = list[elements]
                list[elements]= list[elements+1]
                list[elements+1]=temporary
    print (datetime.now() - startTime)
    return list

menu = True
#Runs the menu loop
while menu:
    #Menu Screen
    print('')
    print('Welcome to the Dungeon Crawler Search and Sort!')
    print('Press:')
    print('S to start')
    print('H for help')
    print('Q to quit')
    #Waits for player input
    menuinput = input('Response: ')
    #States if user inputs s
    if (menuinput == 's') or (menuinput == 'S'):
        search_and_sort = True
        while search_and_sort:
            print('')
            print('Press: ')
            print('1 for a Linear Search')
            print('2 for a Binary Search')
            print('3 for an Insertion Sort')
            print('4 for a Bubble Sort')
            print('0 to go back to the menu')
            print('')
            search_and_sort_input = input('Response: ')
            #States if user selects 1
            if search_and_sort_input == '1':
                currentpack = pack()
                print(currentpack)
                itemtofind = input('Which item do you want to find: ')
                startTime = datetime.now()
                founditem = linearSearch(itemtofind, currentpack)
                #States if the item has been found
                if founditem:
                    print('The item is in your pack!')
                else:
                    print('The item is not in your pack.')
                print (datetime.now() - startTime)
            #States if user selects 2
            elif search_and_sort_input == '2':
                #Orders the stats to do a proper binary search
                stats_to_search = InsertionSortforSearch(createStats())
                print(stats_to_search)
                numtofind = int(input('Which item do you want to find: '))
                foundnum = binarySearch(numtofind, stats_to_search)
                if foundnum:
                    print('The number has been found!')
                else:
                    print('The number does not exist')
            #States if user selects 3
            elif search_and_sort_input == '3':
                stats_to_sort = InsertionSort(createStats())
                print('Final sort:')
                print(stats_to_sort)
            #States if user selects 4
            elif search_and_sort_input == '4':
                stats_to_sort_2 = BubbleSort(createStats())
                print('Final sort:')
                print(stats_to_sort_2)
            #States if user selects 0
            elif search_and_sort_input == '0':
                #Stops the loop
                search_and_sort = False
            else:
                print('Invalid input')
    #States if user inputs h
    elif (menuinput == 'h') or (menuinput == 'H'):
        print('')
        print('This is a search and sort program.')
        print('')
        helpinput = input('Press Enter to continue.')
        
    #States if user inputs q
    elif (menuinput == 'q') or (menuinput == 'Q'):
        #Quits the program
        print('')
        print('Thanks for using the search and sort program!')
        print('Have a nice day!')
        menu = False
    #States if user inputs anything else
    else:
        #Error screen
        print("Sorry, that's an invalid input!")
