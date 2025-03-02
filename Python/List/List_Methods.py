'''
List Methods: append(), extend(), insert(), remove(), pop([i]), clear(), index(),
              count(), sort(), reverse(), copy()
'''



'''
Creating Empty list
'''
lst = []



'''
List with mixed datatypes
'''
mixed_list = [1, 'Hello', 3.4, True]



'''
Nested list
'''
nested_list = ['mouse', [2,3,4,5], ['a']]



'''
How to access elements from a list
'''
lst = ['p','r','o','b','e']

print(lst[0]) 	    # output: p
print(lst[4])	    # output: e
print(lst[-1])	    # output e
print(lst[-3])	    # output o
print(lst[:])       # output: ['p', 'r', 'o', 'b', 'e']
print(lst[2:5])	    # output: ['o', 'b', 'e']
print(lst[-5])      # output: p
print(lst[-5:])     # output: ['p', 'r', 'o', 'b', 'e']
print(lst[:-1])         # output: ['p', 'r', 'o', 'b']


nested_list=['Happy', [2,1,3,4,5], 3.0]

print(nested_list[0][0])	# output: H
print(nested_list[1][2])	# output: 3



'''
Change Item Value
'''
thislist = ["apple", "banana", "cherry"]

thislist[1] = "blackcurrant"        # ['apple', 'blackcurrant', 'cherry']
thislist[0] = "watermelon"          # ['watermelon', 'blackcurrant', 'cherry']



'''
Return the Number of items in a List
'''
planets = ["Earth", "Mars", "Saturn", "Jupiter"]

print(len(planets))     # output: 4
print(f"Length of list: {len(planets)}")



'''
append()  Adds an element at the end of the list
'''
planets.append("Mercury")    # ['Earth', 'Mercury', 'Saturn', 'Jupiter', 'Mercury']
print(f"Length of list: {len(planets)} items")


'''
clear()  Removes all the elements from the list
'''
fruits = ['apple', 'banana', 'cherry', 'orange']

fruits.clear()



'''
copy()  Returns a copy of the list
'''
fruits = ['apple', 'banana', 'cherry', 'orange']

#1
x = fruits.copy()       # ['apple', 'banana', 'cherry']

# 2 copying a list using slicing
new_list = list[:]



'''
count()  Returns the number of elements with the specified value
'''
fruits = ['apple', 'banana', 'cherry']

x = fruits.count("cherry")      # 1



'''
extend()  Add the elements of a list to the end of the current list
'''
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
points = (1, 4, 5, 9)

fruits.extend(cars)     # ['apple', 'banana', 'cherry', 'Ford', 'BMW', 'Volvo']
fruits.extend(points)   # ['apple', 'banana', 'cherry', 1, 4, 5, 9]



'''
index()  Returns the index of the first element with the specified value
'''
fruits = ['apple', 'banana', 'cherry']

x = fruits.index("cherry")



'''
insert()	Adds an element at the specified position
'''
fruits = ['apple', 'banana', 'cherry']

fruits.insert(1, "orange")      # ['apple', 'orange', 'banana', 'cherry']



'''
pop()	Removes the element at the specified position
'''
fruits = ['apple', 'banana', 'cherry']

fruits.pop(1)       # ['apple', 'cherry']



'''
remove()	Removes the first item with the specified value
'''
fruits = ['apple', 'banana', 'cherry']

fruits.remove("banana")     # ['apple', 'cherry']



'''
Delete a List Item
'''
my_list = ['p','r','o','b','l','e','m']

#1  del keyword removes the specified index:
del my_list[2]	    # output: ['p', 'r', 'b', 'l', 'e', 'm']

#2
del my_list[1:5]	# output: ['p', 'm']

#3 # delete entire list
del my_list



'''
sort()	Sorts the list
'''
#Sort the list alphabetically:
cars = ['Ford', 'BMW', 'Volvo']

cars.sort()
print(cars)                 # ['BMW', 'Ford', 'Volvo']

# You can also make a function to decide the sorting criteria(s).
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key=myFunc)       # ['VW', 'BMW', 'Ford', 'Mitsubishi']
cars.sort(reverse=True, key=myFunc)     # ['Mitsubishi', 'Ford'', 'BMW', 'VW']



'''
reverse()	Reverses the order of the list
'''
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()        # ['cherry', 'banana', 'apple']

os = ['Windows', 'macOS', 'Linux']

#1
rev_list = list(reversed(os))       # output: ['Linux', 'macOS', 'Windows']

#2
reversed_list = os[::-1]

#3
print(os[1][::-1])



'''
list() constructor to make a new list
'''
thislist = list(("apple", "banana", "cherry"))  # note the double round-brackets
print(thislist)         # ['apple', 'banana', 'cherry']



'''
Check if Item Exists
'''
thislist = ["apple", "banana", "cherry"]

my_list = ['p','r','o','b','l','e','m']

int_list = [1,2,3,4,5]


#1
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


if 'p' in my_list:
    print("Yes, 'p' in your list")
else:
    print("No")


#2
if 1 in int_list:
    print("Yes, number <1> in your list")
else:
    print("NO")


********


There are several ways to duplicate a list in Python.

One way is to use the * operator to create a new list that contains multiple copies of the original list:

original_list = [1, 2, 3]
duplicate_list = original_list * 3
print(duplicate_list)


Another way to duplicate a list is to use the copy module from the copy library:

import copy
original_list = [1, 2, 3]
duplicate_list = copy.copy(original_list)
print(duplicate_list)


This would also create a new list that contains the same elements as the original list.

You can also use the list function to create a new list that contains the elements of the original list:

original_list = [1, 2, 3]
duplicate_list = list(original_list)
print(duplicate_list)


Finally, you can use the slicing operator to create a new list that contains the elements of the original list:

original_list = [1, 2, 3]
duplicate_list = original_list[:]
print(duplicate_list)

*****

The sorted function returns a new sorted list, without modifying the original iterable.

Here is the syntax for the sorted function:


sorted(iterable, key=None, reverse=False)

The iterable argument is the sequence that you want to sort. The key argument is an optional function that takes an element and returns a value that is used to determine the sort order. The reverse argument is a Boolean value that specifies whether the sort order is ascending (False) or descending (True).

Here is an example of how to use the sorted function to sort a list of integers in ascending order:


numbers = [3, 1, 4, 2]
sorted_numbers = sorted(numbers)
print(sorted_numbers)

This would output the following sorted list:


[1, 2, 3, 4]
You can also use the sorted function to sort a list of strings in descending order:


words = ['cat', 'window', 'defenestrate']
sorted_words = sorted(words, reverse=True)
print(sorted_words)
This would output the following sorted list:


['window', 'defenestrate', 'cat']
You can also use the sorted function to sort a list of dictionaries by a specific key. For example, you can sort a list of dictionaries by the 'age' key:


people = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]
sorted_people = sorted(people, key=lambda x: x['age'])
print(sorted_people)
This would output the following sorted list:


[{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]

≥ ≤ ÷ ¡™ £ ¢ ∞ § ¶ • ª º – ≠ « 