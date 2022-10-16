# DO NOT CHANGE any part of this script between the beginning
# of the file and point A (below)
# ----------------------------------------------------------------------------------------------------------------------------


def Main () :
    # 'Top-level' function (main program)
    theList = []   # Start with an empty list of theList
                   # because the user hasn't entered a list yet
    # Main loop - repeatedly displays the menu,
    #             gets the user to choose an operation
    #             and carries out that operation
    while True :
        ShowMenu ()
        chosen = GetMenuChoice ()
        if chosen == "0" :        # option 0 is 'quit the program'
            break
        else :
            theList = ExecuteChoice (chosen, theList)
    print ("Thanks for using the program: goodbye")



def ShowMenu () :
    print ("Menu options")
    print ("0 Quit the program")
    print ("1 Enter a new list of numbers")
    print ("2 Display the current list of numbers")
    print ("3 Find the sum of all the negative numbers in the list")
    print ("4 Create a list containing the trebles of the numbers in the list")
    print ("5 Create a list of the indexes of the positive numbers in the list")
    print ("6 Find the even number in the list that has the largest magnitude")
    print ("7 Remove all negative numbers from the list")
    print ("8 Show the first positive and first negative number in the list")
    


def GetMenuChoice () :
    choice = input ("Please enter a number between 0 and 8: ")
    print()
    return choice



def ExecuteChoice (c,theList) :
    # performs the operation specified by c on the list theList
    if c == "1" :
        theList = GetTheNumbers ()
    if c == "2" :
        showNums (theList)
    if c == "3" :
        negSum = SumOfNegatives (theList)
        print ("The sum of negative numbers in the list is",negSum)
    if c == "4" :
        trebleList = ListOfTrebles (theList)
        print ("The trebles of all numbers in the list are")
        print (trebleList)
    if c == "5" :
        indexes = IndexesOfPositives (theList)
        print ("The indexes of all positive numbers in the list are")
        print(indexes)
    if c == "6" :
        largest = LargestMagnitudeEven (theList)
        if largest == 999 :
            print ("Thre are no even numbers in the list")
        else :
            print ("The even number with the largest magnitude is",largest)
    if c == "7" :
        theList = RemoveNegatives (theList)
        print ("All negative numbers have been removed from the list, leaving")
        print (theList)
    if c == "8" :
        firstNums = FirstPosNeg (theList)
        if firstNums[0] == -1 :
            print ("There are no positive numbers in the list")
        else :
            print ("The first positive number in the list is",firstNums[0])
        if firstNums[1] == 1 :
            print ("There are no negative numbers in the list")
        else :
            print ("The first negative number in the list is",firstNums[1])     
        
    return theList



def GetTheNumbers () :
    # obtains a new list of numbers from the user
    theNumbers = []
    while True :
        numstr = input("Please type in a whole number, or q to quit: ")
        if numstr == 'q' :
            break
        number = int(numstr)
        theNumbers.append(number)
    return theNumbers
  
 
 
def showNums (theNumbers) :
    # shows the contents of theNumbers on screen
    print ("The current list of numbers is")
    print (theNumbers)
    print ()


# DO NOT CHANGE any part of this script between the beginning
# of the file and point A (below)
# ----------------------------------------------------------------------------------------------------------------------------
# POINT A
# ----------------------------------------------------------------------------------------------------------------------------

# Insert your Student Registration Number (SRN) between the
# quotation marks in the assignment statement below:

SRN = "20034089"

# For example, if your SRN is 01234567 the assignment statement
# should read  SRN = "01234567"

# ----------------------------------------------------------------------------------------------------------------------------
# Provide correct implementations of the functions below,
# each of which currently contains a code stub
#
# Do not change the name, the number of parameters, or
# the number of return values of any of these functions
#
# You are not allowed to use any external modules
# in the solution of these problems (no imports)
# ----------------------------------------------------------------------------------------------------------------------------
    


def SumOfNegatives (theNumbers) :
    # Returns the sum of all the negative numbers in theNumbers
    negSum = 0
    for number in theNumbers:
        if number<0:
            negSum = negSum + number
    return negSum



def ListOfTrebles (theNumbers) :
    # Returns a list, each member of which is three times the
    # corresponding member of theNumbers
    trebleList = []
    for number in theNumbers:
        trebleList.append(number*3)

    

    return trebleList



def IndexesOfPositives (theNumbers) :
    # Returns a list containing the indexes of all the
    # positive numbers in theNumbers
    indexes = []
    for number in theNumbers:
        if number>0:
            indexes.append(theNumbers.index(number))    
    
            
    return indexes



def LargestMagnitudeEven (theNumbers) :
    # Returns the even number in theNumbers that has the 
    # largest magnitude (the even number that is furthest
    # from zero), or the number 999 when theNumbers contains
    # no even numbers
    evenNums = []
    for i in range(len(theNumbers)):
        if theNumbers[i] % 2 == 0:
            evenNums.append(theNumbers[i])

    if len(evenNums) == 0:
        return 999

    minNum = min(evenNums)
    maxNum = max(evenNums)

    scan1 = abs(0-minNum)
    scan2 = abs(0-maxNum)

    if scan1 > scan2:
        return scan1
    if scan2 > scan1:
        return scan2
    if scan1 == scan2:
        return scan1
    
                   
    
    return 999



def RemoveNegatives (theNumbers) :
    # Returns a list that is the same as theNumbers with all of
    # the negative numbers removed
    for n in theNumbers:
        if (n < 0):
            theNumbers.remove(n)
    return theNumbers
    

1



def FirstPosNeg (theNumbers) :
    # Returns a two-element list, firstNums, containing the first positive
    # number from theNumbers followed by the first negative number
    # If theNumbers contains no positive numbers the first element
    # of firstNums should be -1
    # If theNumbers contains no negative numbers the second element
    # of firstNums should be 1
    firstNums = []

    inPlace = True

    while inPlace:
        for i in range(len(theNumbers)):
            if theNumbers[i] > 0:
                firstNums.append(theNumbers[i])
                break
        break

    if len(firstNums) == 0:
        firstNums.append(-1)

    while inPlace:
        for i in range(len(theNumbers)):
            if theNumbers[i] < 0:
                firstNums.append(theNumbers[i])
                break
        break

    if len(firstNums) == 1:
        firstNums.append(1)

       
    
    return firstNums
Main()
