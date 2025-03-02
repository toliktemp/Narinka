'''
List Functions:
len(), list([iterable]), max(), min(), range(), enumerate(), filter()
iter(), len(), map(), reversed(), slice(), sorted(), sum(), zip()
'''


'''
enumerate()	Returns an Enumerate Object

The enumerate() method takes two parameters:

iterable - a sequence, an iterator, or objects that supports iteration
start (optional) - enumerate() starts counting from this number. 
If start is omitted, 0 is taken as start.
'''
grocery = ['bread', 'milk', 'butter']
enumerateGrocery = enumerate(grocery)

print(type(enumerateGrocery))       #<class 'enumerate'>

# converting to list
print(list(enumerateGrocery))       # [(0, 'bread'), (1, 'milk'), (2, 'butter')]

# changing the default counter
enumerateGrocery = enumerate(grocery, 10)
print(list(enumerateGrocery))       # [(10, 'bread'), (11, 'milk'), (12, 'butter')]



# Looping Over an Enumerate object

grocery = ['bread', 'milk', 'butter']

for item in enumerate(grocery):
  print(item)

print('\n')
for count, item in enumerate(grocery):
  print(count, item)

print('\n')
# changing default start value
for count, item in enumerate(grocery, 100):
  print(count, item)



fruits = ['apple', 'banana', 'mango']

for i, fruit in enumerate(fruits):
    print(i, fruit)


fruits = ['apple', 'banana', 'mango']

for i, fruit in enumerate(fruits, start=1):
    print(i, fruit)

"""
filter()	constructs iterator from elements which are true
syntax: filter(function, iterable)

filter() Parameters
The filter() method takes two parameters:

function - function that tests if elements of an iterable returns true or false
If None, the function defaults to Identity function - which returns false if any elements are false
iterable - iterable which is to be filtered, could be sets, lists, tuples, or containers of any iterators
"""
# list of alphabets
alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# function that filters vowels
def filterVowels(alphabet):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if(alphabet in vowels):
        return True
    else:
        return False

filteredVowels = filter(filterVowels, alphabets)

print('The filtered vowels are:')
for vowel in filteredVowels:
    print(vowel, end=', ')      # a, e, i, o,



# 2 filter() method works without the filter function
# random list
randomList = [1, 'a', 0, False, True, '0']

filteredList = filter(None, randomList)

print('The filtered elements are:')
for element in filteredList:
    print(element)              # 1, a, True, 0



'''
iter()	returns iterator for an object
'''
# list of vowels
vowels = ['a', 'e', 'i', 'o', 'u']

vowelsIter = iter(vowels)

# prints 'a'
print(next(vowelsIter))

# prints 'e'
print(next(vowelsIter))

# prints 'i'
print(next(vowelsIter))

# prints 'o'
print(next(vowelsIter))

# prints 'u'
print(next(vowelsIter))



# 2
'''
class PrintNumber:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if(self.num >= self.max):
            raise StopIteration
        self.num += 1
        return self.num

printNum = PrintNumber(3)

printNumIter = iter(printNum)

# prints '1'
print(next(printNumIter))

# prints '2'
print(next(printNumIter))

# prints '3'
print(next(printNumIter))

# raises StopIteration
print(next(printNumIter))
'''


'''
list() constructor creates a list in Python
'''

# empty list
print(list())

# vowel string
vowelString = 'aeiou'
print(list(vowelString))

# vowel tuple
vowelTuple = ('a', 'e', 'i', 'o', 'u')
print(list(vowelTuple))

# vowel list
vowelList = ['a', 'e', 'i', 'o', 'u']
print(list(vowelList))


# vowel set
vowelSet = {'a', 'e', 'i', 'o', 'u'}
print(list(vowelSet))                   # ['i', 'e', 'u', 'o', 'a']

# vowel dictionary
vowelDictionary = {'a': 1, 'e': 2, 'i': 3, 'o':4, 'u':5}
print(list(vowelDictionary))            # ['a', 'e', 'i', 'o', 'u']


#  You can also use the list function to create a new list from a range:

number_range = range(1,6)
number_list = list(number_range)
print(number_list)

# an example of how to use the list function to create a new list from a tuple:

numbers = (1, 2, 3)
number_list = list(numbers)
print(number_list)

'''
len()	Returns Length of an Object
'''
testString = ''
print(f"Length of testString is {len(testString)}")

testString = 'Python'
print(f"Length of testString is {len(testString)}")

#byte object
testByte = b'Python'
print(f"Length of testByte is {len(testByte)}")

testList = [1,2,3]
#converting to bytes object

testByte = bytes(testList)
print(f"Length of testByte is {len(testByte)}")

testSet = {1,2,3}
print(f"testSet length is {len(testSet)}")


testDict = {1:'one', 2:'two'}
print(f"testDict length is {len(testDict)}")



'''
max()	returns largest element
'''
# using max(arg1, arg2, *args)
print('Maximum is:', max(1, 3, 2, 5, 4))

# using max(iterable)
num = [1, 3, 2, 8, 5, 10, 6]
print('Maximum is:', max(num))


def sumDigit(num):
    sum = 0
    while(num):
        sum += num % 10
        num = int(num / 10)
    return sum

# using max(arg1, arg2, *args, key)
print('Maximum is:', max(100, 321, 267, 59, 40, key=sumDigit))

# using max(iterable, key)
num = [15, 300, 2700, 821, 52, 10, 6]
print('Maximum is:', max(num, key=sumDigit))


num = [15, 300, 2700, 821]
num1 = [12, 2]
num2 = [34, 567, 78]

# using max(iterable, *iterables, key)
print('Maximum is:', max(num, num1, num2, key=len))



You can also use the max() function with a key function to specify how the elements should be compared. For example:


words = ['cat', 'apple', 'zoo', 'good']
longest_word = max(words, key=len)
print(longest_word)  # Output: 'apple'

√   √  √.  √.  √

def myMax(list1):
 
    # Assume first number in list is largest
    # initially and assign it to variable "max"
    max = list1[0]
# Now traverse through the list and compare
    # each number with "max" value. Whichever is
    # largest assign that value to "max'.
    for x in list1:
        if x > max:
            max = x
 
    # after complete traversing the list
    # return the "max" value
    return max
 
 
# Driver code
list1 = [10, 20, 4, 45, 99]
print("Largest element is:", myMax(list1))



'''
min()	returns smallest element
'''
# using min(arg1, arg2, *args)
print('Minimum is:', min(1, 3, 2, 5, 4))

# using min(iterable)
num = [3, 2, 8, 5, 10, 6]
print('Minimum is:', min(num))


def sumDigit(num):
    sum = 0
    while(num):
        sum += num % 10
        num = int(num / 10)
    return sum


def myMin(list):
min = list[0]

for x in list:
	if x < min:
		min = x
return min

# using min(arg1, arg2, *args, key)
print('Minimum is:', min(100, 321, 267, 59, 40, key=sumDigit))

# using min(iterable, key)
num = [15, 300, 2700, 821, 52, 10, 6]
print('Minimum is:', min(num, key=sumDigit))

num = [15, 300, 2700, 821]
num1 = [12, 2]
num2 = [34, 567, 78]

# using min(iterable, *iterables, key)
print('Minimum is:', min(num, num1, num2, key=len))



'''
map()	Applies Function and Returns a List
'''
def calculateSquare(n):
  return n*n

numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
print(result)

# converting map object to set
numbersSquare = set(result)
print(numbersSquare)


# use lambda function with map()
numbers = (1, 2, 3, 4)
result = map(lambda x: x*x, numbers)
print(result)

# converting map object to set
numbersSquare = set(result)
print(numbersSquare)


# Passing Multiple Iterators to map() Using Lambda
num1 = [4, 5, 6]
num2 = [5, 6, 7]

result = map(lambda n1, n2: n1+n2, num1, num2)
print(list(result))

***

def multiply(x, y):
    return x * y


numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
results = map(multiply, numbers1, numbers2)
print(list(results))  # Output: [4, 10, 18]


numbers = [1, 2, 3]
squares = map(lambda x: x ** 2, numbers)
print(list(squares))  # Output: [1, 4, 9]


'''
reversed()	returns reversed iterator of a sequence
'''
# for string
seqString = 'Python'
print(list(reversed(seqString)))

# for tuple
seqTuple = ('P', 'y', 't', 'h', 'o', 'n')
print(list(reversed(seqTuple)))

# for range
seqRange = range(5, 9)
print(list(reversed(seqRange)))

# for list
seqList = [1, 2, 4, 3, 5]
print(list(reversed(seqList)))

class Vowels:
    vowels = ['a', 'e', 'i', 'o', 'u']

    def __reversed__(self):
        return reversed(self.vowels)

v = Vowels()
print(list(reversed(v)))



'''
slice()	creates a slice object specified by range()

slice() mainly takes three parameters which have the same meaning in both constructs:

start - starting integer where the slicing of the object starts
stop - integer until which the slicing takes place. The slicing stops at index stop - 1.
step - integer value which determines the increment between each index for slicing
If a single parameter is passed, start and step are set to None.


'''

#1  Get substring from a given string by extending indexing syntax

pyString = 'Python'

# contains indices (0, 1, 2)
print(pyString[0:3])        # Pyt

# contains indices (1, 3)
print(pyString[1:5:2])      # yh


#2  Create a slice object for slicing
pyString = 'Python'

sObject = slice(3)
print(pyString[sObject])        # Pyt

sObject1 = slice(1,5,2)
print(pyString[sObject1])       # yh


#3 Get substring from a given string using negative index
pyString = 'Python'

sObject = slice(-1, -4, -1)
print(pyString[sObject])            # noh



#4 Get sublist and sub-tuple from a given list and tuple respectively

pyList = ['P', 'y', 't', 'h', 'o', 'n']
pyTuple = ('P', 'y', 't', 'h', 'o', 'n')

sObject = slice(3)
sObject1 = slice(1,5,2)

print(pyList[sObject])      # ['P', 'y', 't']
print(pyTuple[sObject1])    # ('y', 'h')


# 5
elements=[1,2,3,4,5]
print( elements[:] ) 			# all members in list


'''
sorted()	returns sorted list from a given iterable

Note: A list also has sort() method which performs the same way as sorted(). 
Only difference being, sort() method doesn't return any value and changes the original list itself.
'''
# vowels list
pyList = ['e', 'a', 'u', 'o', 'i']
print(sorted(pyList))           # ['a', 'e', 'i', 'o', 'u']

# string
pyString = 'Python'
print(sorted(pyString))         # ['P', 'h', 'n', 'o', 't', 'y']

# vowels tuple
pyTuple = ('e', 'a', 'u', 'o', 'i')
print(sorted(pyTuple))          # ['a', 'e', 'i', 'o', 'u']


# set
pySet = {'e', 'a', 'u', 'o', 'i'}
print(sorted(pySet, reverse=True))      # ['u', 'o', 'i', 'e', 'a']

# dictionary
pyDict = {'e': 1, 'a': 2, 'u': 3, 'o': 4, 'i': 5}
print(sorted(pyDict, reverse=True))     # ['u', 'o', 'i', 'e', 'a']

# frozen set
pyFSet = frozenset(('e', 'a', 'u', 'o', 'i'))
print(sorted(pyFSet, reverse=True))     # ['u', 'o', 'i', 'e', 'a']


# take second element for sort
def takeSecond(elem):
    return elem[1]

# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# sort list with key
sortedList = sorted(random, key=takeSecond)

# print list
print('Sorted list:', sortedList)       # Sorted list: [(4, 1), (2, 2), (1, 3), (3, 4)]



'''
sum()	Add items of an Iterable
'''
numbers = [2.5, 3, 4, -5]

# start parameter is not provided
numbersSum = sum(numbers)
print(numbersSum)               # 4.5

# start = 10
numbersSum = sum(numbers, 10)
print(numbersSum)               # 14.5



'''
zip()	Returns an Iterator of Tuples
'''
numberList = [1, 2, 3]
strList = ['one', 'two', 'three']

# No iterables are passed
result = zip()

# Converting itertor to list
resultList = list(result)
print(resultList)               # []

# Two iterables are passed
result = zip(numberList, strList)

# Converting itertor to set
resultSet = set(result)
print(resultSet)                # {(3, 'three'), (2, 'two'), (1, 'one')}


# 2
numbersList = [1, 2, 3]
strList = ['one', 'two']
numbersTuple = ('ONE', 'TWO', 'THREE', 'FOUR')

result = zip(numbersList, numbersTuple)

# Converting to set
resultSet = set(result)
print(resultSet)                # {(2, 'TWO'), (3, 'THREE'), (1, 'ONE')}

result = zip(numbersList, strList, numbersTuple)

# Converting to set
resultSet = set(result)
print(resultSet)                # {(2, 'two', 'TWO'), (1, 'one', 'ONE')}



# 3     Unzipping the Value Using zip()
coordinate = ['x', 'y', 'z']
value = [3, 4, 5, 0, 9]

result = zip(coordinate, value)
resultList = list(result)
print(resultList)               # [('x', 3), ('y', 4), ('z', 5)]

c, v =  zip(*resultList)
print('c =', c)                 # c = ('x', 'y', 'z')
print('v =', v)                 # v = (3, 4, 5)




'''
The count() method of a string or a list returns the number of occurrences
of a specified element in the string or list.
'''

s = 'hello world'
s.count('l')


numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
numbers.count(4)


lst = ['Cat', 'Bat', 'Sat', 'Cat', 'Mat', 'Cat', 'Sat']

# To get the number of occurrences
# of each item in a list
print([[el, lst.count(el)] for el in set(lst)])

# To get the number of occurrences
# of each item in a dictionary
print(dict((el, lst.count(el)) for el in set(lst)))




'''
range() is a built-in function in Python that returns an object
that generates a sequence of integers. It is commonly used in a
for loop to repeat a block of code a certain number of times.

The basic syntax of range() is range(stop), which generates a sequence
of integers from 0 to stop-1. You can also specify the starting value
of the sequence by using the syntax range(start, stop),
which generates a sequence of integers from start to stop-1.

'''

# Print the numbers 0 to 9
for i in range(10):
    print(i)

# Print the numbers 5 to 9
for i in range(5, 10):
    print(i)


# Print the even numbers between 0 and 10
for i in range(0, 11, 2):
    print(i)

# Create a list of integers from 0 to 9
numbers = list(range(10))
print(numbers)

'''
Note that range() generates a sequence of integers in a lazy manner, 
meaning that it does not create the entire sequence in memory at once. 

This makes it efficient for generating large sequences of numbers.
 
However, it does not support indexing or slicing, and the elements 
of the sequence cannot be modified. To create a list of integers, 
you can use the list() function:
'''

********************************

'''
index() is a built-in function of Python that returns the index of an element in a list.
It takes a list and an element as arguments and returns the index of the first
occurrence of the element in the list. If the element is not found in the list,
it raises a ValueError exception.
'''

fruits = ['apple', 'banana', 'mango']
index = fruits.index('banana')
print(index)


# You can also specify a start and end index for the search by using the
# optional arguments start and end:

fruits = ['apple', 'banana', 'mango', 'banana', 'pear']
index = fruits.index('banana', 1, 4)
print(index)

'''
Note that index() returns the index of the first occurrence of the element 
in the list. If the element appears more than once in the list, you can 
use a loop or the count() function to find the other occurrences.
'''

fruits = ['apple', 'banana', 'mango', 'banana', 'pear']
count = fruits.count('banana')
print(count)
