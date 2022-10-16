# Insert your Student Registration Number (SRN) between the
# quotation marks in the assignment statement below:

SRN = "20034089"

# For example, if your SRN is 01234567 the assignment statement
# should read  SRN = "01234567"

# ----------------------------------------------------------------------------------------------------------------------------
# WHAT YOU HAVE TO DO
#
# Modify this script to provide correct implementations of the
# functions below, each of which currently contains a code stub
#
# When you have finished, submit the modified version of this script
#
# Do not change the names or parameters of any of these functions
# Make sure you read the function descriptions carefully
#
# You are not allowed to use any external modules
# in the solution of these problems (no imports)
# ----------------------------------------------------------------------------------------------------------------------------
#
# The script contains a test plan and code to test the functions
# and display the results of the tests
#
# To run the tests type  runtests()  at the command line in the
# Python shell
#
# ----------------------------------------------------------------------------------------------------------------------------

##########################
# Function 1 (2 marks)
##########################

def venn (X,Y,Z) :
    test = (Y|(Z&X))
# Parameters: three sets X, Y, Z
# Returns:
#  A single set that combines sets X, Y and Z in the manner
#  shown as a shaded area on the Venn diagram in the document
#  venn_diagram_function1.pdf that accompanies this file
#  on Canvas

    return test    # code stub




##########################
# Function 2 (3 marks)
##########################

def lookup(listX,listY) :
    dict1 = {}
    for i in range(len(listX)):
        dict1[listX[i]] = listY[i]
    
# Parameters: two lists listX, listY of equal length
#  listX must contain only hashable data items as it
#  is going to supply the keys for a dictionary
# Returns:
#  A dictionary in which each entry is made up of
#  a key from listX and a data item from listY, such that
#  listX[i] is the key to listY[i] for all i
   
    return dict1    # code stub




##########################
# Function 3 (3 marks)
##########################

def string_lengths (strlist) :
    dict1 = {}
    for s in strlist:
        strlen = len(s)
        if strlen not in dict1:
            dict1[strlen] = 0
        dict1[strlen] = 1
            
        
            
# Parameter: a list of strings, strlist
# Returns:
#  A dictionary in which each entry is made up of
#  * a key that is a whole number representing the length of one of
#    the strings in strlist
#  * mapped to a data item that is the number of strings in strlist
#    which are of that length

    return dict1   # code stub




##########################
# Function 4 (3 marks)
##########################

def stuff_bits (bit_str) :
    bitstring = ""
    for s in bit_str:
        if s == '0':
            bitstring += "10"
        else:
            bitstring += "01"
    
# A function that stuffs bits into a bit-string in order to balance
# the number of 0s and 1s it contains, whilst still carrying the
# same information
# Parameter: a character string bit_str
#   bit_str contains a sequence of '0' and '1' characters each of
#   which represents a single bit in a bit-string.
#   For example
#   The character string '0010111' represents the bit-string 0010111
# Returns: a character string out_str derived from bit_str as follows
#   All bits from bit_string are in out_str in the same order, but
#   every '0' from bit_str is preceded immediately by a '1' and
#   every '1' from bit_str is preceded immediately by a '0'
#   so out_str is twice the length of bit_str
# For example
# stuff_bits ('0') returns '10'
# stuff_bits ('1') returns '01'
# stuff_bits ('00') returns '1010'
# stuff_bits ('001') returns '101001'
# stuff_bits ('100') returns '011010'
# stuff_bits ('110') returns '010110'
# and so on, so that
# stuff_bits ('0010111') returns '10100110010101'

    return bitstring    # code stub




##########################
# Function 5 (3 marks)
##########################

def strip_bits (bit_str) :
    bitstring = ""
    for i in range(0,len(bit_str),2):
        if bit_str[i] == '0' and bit_str[i+1] == '1':
            bitstring += "1"
        if bit_str[i] == '1' and bit_str[i+1] == '0':
            bitstring += "0"
    return bitstring
            
# A function that extracts the original bit-string from the
# stuffed version produced by stuff_bits (see function 4)
# so that after executing the following sequence of instructions
#   mystr = '0010'
#   stuffed = stuff_bits(mystr)
#   stripped = strip_bits(stuffed)
# stuffed is  '10100110'  and stripped is  '0010'

    return None    # code stub




##########################
# Function 6 (3 marks)    USE RECURSION
##########################

def all_negatives (numlist) :
    if len(numlist) == 0:
        return True
    else:
# A function that determines whether or not all elements in a list
# of numbers are negative.
# You are required to USE RECURSION when implementing this function

# Parameter: a non-empty list of numbers, numlist
# Returns: a truth value
#   True when the numbers in numlist are all negative
#   False when they are not

        return all_negatives (numlist[1:])    # code stub



##########################
# Function 7 (3 marks)    USE RECURSION
##########################

def in_descending_order (numlist) :
    if len(numlist) == 1:
        return True
    elif numlist[] < numlist[]:
        return False
    else:
        
# A function that determines whether or not the elements in a list
# of numbers are arranged in descending order.
# You are required to USE RECURSION when implementing this function

# Parameter: a list of numbers, numlist
# Returns: a truth value
#   True when the numbers in numlist are in descending order
#   False when they are not

        return in_descending_order (numlist[0:])     # code stub




# ----------------------------------------------------------------------------------------------------------------------------
# Do not change any part of this script between here and
# the end of the file
# ----------------------------------------------------------------------------------------------------------------------------

###########################################################################

#                           TEST PLAN

############################################################################

test_plan = dict ()

fn = "venn"
test_plan [fn] = dict()
test_plan [fn] [1] = [[set(),set(),set()],set()]
test_plan [fn] [2] = [[{1},{2},{3}],{2}]
test_plan [fn] [4] = [[{1,2,3,4,5},{6,5,4,7,9},{1,5,6,2}],{6,5,4,7,9,1,2}]
test_plan [fn] [3] = [[{8,9,7},{6,5,3},{}],{6,5,3}]


fn = "lookup"
test_plan [fn] = dict()
test_plan [fn] [1] = [[[],[]],dict()]
test_plan [fn] [2] = [[[10],[-8]],{10:-8}]
test_plan [fn] [3] = [[[2,4,6],[18,20,22]],{2:18,4:20,6:22}]
test_plan [fn] [4] = [[[-5,4,9,7],[4,11,21,6]],{-5:4,4:11,9:21,7:6}]
test_plan [fn] [5] = [[[1,2,13],['a','b','m']],{1:'a',2:'b',13:'m'}]


fn = "string_lengths"
test_plan [fn] = dict()
test_plan [fn] [1] = [[list()],{}]
test_plan [fn] [2] = [[['hello','fred','pete','']],{5:1,4:2,0:1}]
test_plan [fn] [3] = [[['a','pot','v','l','uui','goherts']],{1:3,3:2,7:1}]
test_plan [fn] [4] = [[['','k','pp','ooo']],{0:1,1:1,2:1,3:1}]


fn = "stuff_bits"
test_plan [fn] = dict()
test_plan [fn] [1] = [[''],'']
test_plan [fn] [2] = [['1'],'01']
test_plan [fn] [3] = [['01'],'1001']
test_plan [fn] [4] = [['0011'],'10100101']
test_plan [fn] [5] = [['11100110'],'0101011010010110']


fn = "strip_bits"
test_plan [fn] = dict()
test_plan [fn] [1] = [[''],'']
test_plan [fn] [2] = [['01'],'1']
test_plan [fn] [3] = [['1001'],'01']
test_plan [fn] [4] = [['10100101'],'0011']
test_plan [fn] [5] = [['0101011010010110'],'11100110']


fn = "all_negatives"
test_plan [fn] = dict()
test_plan [fn] [1] = [[[-2]],True]
test_plan [fn] [2] = [[[1,3,5,7]],False]
test_plan [fn] [3] = [[[0,-11]],False]
test_plan [fn] [4] = [[[1,2,4,-1]],False]
test_plan [fn] [5] = [[[-9,-8]],True]


fn = "in_descending_order"
test_plan [fn] = dict()
test_plan [fn] [1] = [[[2]],True]
test_plan [fn] [2] = [[[1,3,5,7]],False]
test_plan [fn] [3] = [[[3,1]],True]
test_plan [fn] [4] = [[[1,2,4,-1]],False]
test_plan [fn] [5] = [[[-8,-9]],True]


###########################################################################

#                           TEST DRIVER

############################################################################

def tester (ms) :
    results = dict()
    totalmark = 0
    for funcname in ms :
        results[funcname] = dict()
        totalfunc = 0
        tests = ms[funcname].copy()
        for case in tests :
            test      = tests [case]
            args      = test[0]
            arg0      = args[0]
            if isinstance (arg0,str) :
                arg0 = "'" + arg0 + "'"
            else :
                arg0 = str(args[0])
            strargs = "(" + arg0
            for arg in args[1:] :
                if isinstance (arg,str) :
                    arg = "'" + arg + "'"
                else :
                    arg = str(arg)
                strargs = strargs + "," + arg
            strargs   = strargs + ")"
            target    = test[1]
            if isinstance (target,str) :
                strtarget = "'" + target + "'"
            else :
                strtarget = str(target)
            try :
                call = funcname + strargs
                actual = eval(call)
                if isinstance (actual,str) :
                    stractual = "'" + actual + "'"
                else :
                    stractual = str(actual)

            except NameError :
                result = "Name error"
                results[funcname][case] = [strargs,strtarget,"no result",result]
                continue
            except RecursionError :
                result = "Recursion error (too many recursive calls)"
                results[funcname][case] = [strargs,strtarget,"no result",result]
                continue
            except :
                result = funcname + " crashed"
                results[funcname][case] = [strargs,strtarget,"no result",result]
                continue

            if type(actual) != type(target) :
                result = "wrong type returned"
                
            else :
                if target == actual :
                    result = "pass"
                else :
                    result = "FAIL"

            results[funcname][case] = [strargs,strtarget,stractual,result]

    return results



def DisplayTestResults (results) :    
    display = "Test results\n"
    display += "Each function listed in the order tested\n\n"
    
    for fn in results :
        display += "\nTesting " + fn + "\n=========================="
        testres = results[fn]
        for test in testres :
            t = testres[test]
            #display += "\nTest " + str(test)
            display += "\nParameters:    " + t[0]
            display += "\nShould return: " + t[1]
            display += "\nActual return: " + t[2]
            display += "\nTest result:   " + t[3]
            display += "\n"
        display += "\n"
    return display




def run_tests () :
    global test_plan
    
    results = tester(test_plan)
    message = DisplayTestResults (results)
    print (message)

