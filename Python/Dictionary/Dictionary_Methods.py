'''
Python Dictionary Methods:
clear(), copy(), fromkeys(), get(), items(), keys(), pop(), popitem(),
setdefult(), update(), values()

'''

'''
*********************
Create a dictionary
*********************
'''
# empty dictionary
empty_dictionary = {}

# dictionary with integer keys
my_dict = {
    1: 'apple',
    2: 'banana',
    3: 'walnut'
}

# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}


# using dict()
thisdict =	dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment

print(thisdict)     # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}


builtIn_dict = dict({1:'apple',2:'strawberry',3:'berry'})


# from sequence having each item as a pair
sequence_dict = dict([(1,'apple'),(2,'red berry'),(3,'blueberry')])


# Dictionary containing Lists & Tuples
food = {"Fruit": ["Apple", "Orange", "Banana"], "Vegetables": ("Eat", "Your", "Greens")}



# fromkeys() method returns a dictionary with the specified keys and values.
x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)      # ['key1': 0, 'key2': 0, 'key3': 0]


keys = {'a', 'e', 'i', 'o', 'u' }
value = [1]

vowels = dict.fromkeys(keys, value)

#  updating the value
value.append(2)
print(vowels)       # {'e': [1, 2], 'a': [1, 2], 'o': [1, 2], 'u': [1, 2], 'i': [1, 2]}



'''
*****************************************
How to access elements from a dictionary
*****************************************
'''
my_dict = {
    'key1':123,
    'key2':[12, 23, 33],
    'key3':['item0','item1','item2']
}

print(my_dict['key3'])          # ['item0', 'item1', 'item2']

for item in my_dict['key3']:
    print(item, end=', ')       # item0, item1, item2


# Can call an index on that value
my_dict['key3'][0]	            # output: 'item0'


#Can then even call methods on that value
my_dict['key3'][0].upper()	    # output: 'ITEM0'


# Dictionary nested inside a dictionary nested in side a dictionary
d = {'key1':{'nestkey':{'subnestkey':'value'}}}

# Keep calling the keys
d['key1']['nestkey']['subnestkey']



# Create the dictionary
food = {"Fruit": ["Apple", "Orange", "Banana"], "Vegetables": ("Eat", "Your", "Greens")}


print(food["Fruit"][1])             # Orange

print(food['Vegetables'])           # ('Eat', 'Your', 'Greens')

print(food['Vegetables'][1])        # Your



playlist = {
    'title': 'patagonia bus',
    'author': 'colt steele',
    'songs': [
        {'title': 'kitty', 'artist': ['blue','sky'], 'duration': 2.5},
        {'title': 'pussy_cat', 'artist': ['kitty', 'djcat'], 'duration': 5.25},
        {'title': 'meowmeow', 'artist': ['garfield','sons'], 'duration': 2.0}
        ]
}

print(playlist.keys())  # dict_keys(['title', 'author', 'songs'])

print(playlist.values())
# dict_values(['patagonia bus', 'colt steele', [{'title': 'kitty', 'artist': ['blue', 'sky'], 'duration': 2.5}, {'title': 'pussy_cat', 'artist': ['kitty', 'djcat'], 'duration': 5.25}, {'title': 'meowmeow', 'artist': ['garfield', 'sons'], 'duration': 2.0}]])

print(playlist.items())
# dict_items([('title', 'patagonia bus'), ('author', 'colt steele'), ('songs', [{'title': 'kitty', 'artist': ['blue', 'sky'], 'duration': 2.5}, {'title': 'pussy', 'artist': ['kitty', 'djcat'], 'duration': 5.25}, {'title': 'meowmeow', 'artist': ['garfield', 'sons'], 'duration': 2.0}])])



print(playlist['songs'][0]['duration'])

print(playlist['songs'][2]['title'])

print(f"Artist: {playlist['songs'][1]['artist']}")

print(playlist['songs'][2]['title'].upper())



for item in playlist['songs']:
	print(item['artist'])


total_length = 0
for song in playlist['songs']:
    total_length += song['duration']

print(total_length)


'''
dictionary uses keys. Key can be used either inside square brackets 
or with the get() method.

The difference while using get() is that it returns None 
instead of KeyError, if the key is not found.
'''
me = {'name':'James', 'age': 28}

print(me['name'])

print(me.get('age'))

print(me.get('address'))            # None


# use the get() function twice, but we only provide a default value
# for the second one.
planet_size = {"Earth": 40075, "Saturn": 378675, "Jupiter": 439264}

# get() function without a default value
print(planet_size.get("Arrakis"))

# get() function with a default value
print(planet_size.get("Arrakis", "Huh?"))



'''
****************
Change Values
****************
'''
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
thisdict["brand"] = "Dodge"



'''
*************
Adding Items
*************
'''
thisdict["color"] = "Red"
# {'brand': 'Dodge', 'model': 'Mustang', 'year': 2018, 'color': 'Red'}


# update() method overwrites the value for a key if it already exists in the dictionary.
 If the key does not exist, it is added to the dictionary.

You can also use the update() method with keyword arguments to update the dictionary with multiple key-value pairs:

dict1 = {'a': 1, 'b': 2}

# Update dict1 with multiple key-value pairs
dict1.update(b=3, c=4)
print(dict1)  # Output: {'a': 1, 'b': 3, 'c': 4}


dict1 = {'a': 1, 'b': 2}
pairs = [('b', 3), ('c', 4)]

# Update dict1 with the key-value pairs from the iterable
dict1.update(pairs)
print(dict1)  # Output: {'a': 1, 'b': 3, 'c': 4}



'''
**************************
Loop Through a Dictionary
**************************
'''
# Iterate over the dictionary using for loop
for key in thisdict:
    value = thisdict[key]
    print(key, " :: ", value)


# Print all key names in the dictionary, one by one:
for key in thisdict:
  print(key)


# Print all values in the dictionary, one by one:
for x in thisdict:
    print(thisdict[x])


#  the values() function to return values of a dictionary:
for val in thisdict.values():
    print(val)


# Loop through both keys and values, by using the items() function:
for key, val in thisdict.items():
    print(key, " :: ", val)


# Check if Key Exists
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")



# Dictionary Length
print(len(thisdict))



'''
***************
Removing Items
***************
'''
# pop() method removes the item with the specified key name:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict.pop("model")


# popitem() method removes the last inserted item
thisdict.popitem()


# del keyword removes the item with the specified key name:
del thisdict["model"]


# del keyword can also delete the dictionary completely:
del thisdict


# clear() keyword empties the dictionary:
thisdict.clear()



# copy()
mydict = thisdict.copy()


# Another way to make a copy is to use the built-in method dict().
mydict = dict(thisdict)



'''
*****************************************
Printable String format
*****************************************
'''
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
print(f"Printable string format: {str(Dict)}")
# Printable string format: {'Tim': 18, 'Charlie': 12, 'Tiffany': 22, 'Robert': 25}



'''
*****************************************
Sorting Dictionary
*****************************************
'''
mydict = {
    "carl": 40,
    "alan": 2,
    "bob": 1,
    "danny": 3,
}

# 1
# sort a dict by key
print("Sort by Keys: ")
for key in sorted(mydict.keys()):
    print(f"{key} : {mydict[key]}")

'''
alan : 2
bob : 1
carl : 40
danny : 3
'''
# 2
numbers = {'first': 1, 'second': 2, 'third': 3, 'Fourth': 4}
print(list(sorted(numbers)))    # ['Fourth', 'first', 'second', 'third']

# 2a
print(list(sorted(numbers.keys())))

# 3
[key for (key, val) in sorted(numbers.items())]

# sort a dict by value
print("Sort by Values: ")
for key, value in sorted(mydict.items(), key=lambda item: item[1]):
    print(f"{key}  {value}")

'''
bob  1
alan  2
danny  3
carl  40

'''
# 2
print(list(sorted(numbers.values())))   # [1, 2, 3, 4]

# 3
[val for (key, val) in sorted(numbers.items())]




****************** ***************************

A list of some common methods for dictionaries in Python:

🔹 dictionary.clear(): Removes all items from the dictionary.

🔹 dictionary.copy(): Returns a shallow copy of the dictionary.
dictionary.fromkeys(iterable, value): Returns a new dictionary with keys from iterable and all values set to value.

🔹 dictionary.keys(): Returns a view object that displays a list of all the keys in the dictionary.

🔹 dictionary.get(key[, default]): Returns the value for key if key is in the dictionary, else default. If default is not provided, it defaults to None.

🔹 dictionary.values(): Returns a view object that displays a list of all the values in the dictionary.

🔹 dictionary.items(): Returns a view object that displays a list of dictionary's (key, value) pairs.


🔹 dictionary.pop(key[, default]): Removes and returns the value for key if key is in the dictionary, else default. If default is not provided and key is not in the dictionary, a KeyError is raised.

🔹 dictionary.popitem(): Removes and returns an arbitrary (key, value) pair from the dictionary. If the dictionary is empty, a KeyError is raised.

🔹 dictionary.setdefault(key[, default]): If key is in the dictionary, returns its value. If not, inserts key with a value of default and returns default. default defaults to None if not provided.

🔹 dictionary.update(other_dictionary): Updates the dictionary with the key-value pairs from other_dictionary, overwriting existing keys.




****************** ***************************

🔷 '''
The clear() method is used to remove all items from a dictionary.
It does not take any arguments and does not return a value.
'''

colors = {'red': '#ff0000', 'green': '#00ff00', 'blue': '#0000ff'}
colors.clear()
colors      # {}


'''
Note that the clear() method modifies the dictionary in place, 
rather than creating a new, empty dictionary. If you want to create a new, 
empty dictionary, you can simply use the {} notation or the dict() function.
'''

***

🔷'''
The deepcopy() function is a function in the copy module of the Python
standard library that returns a deep copy of an object.
A deep copy is a new object that has a copy of the values in the original object,
rather than references to the values in the original object.
'''


import copy

colors = {'red': ['#ff0000', '#FF0000'], 'green': ['#00ff00', '#00FF00'], 'blue': ['#0000ff', '#0000FF']}
colors_copy = copy.deepcopy(colors)


# You can modify the values in the new dictionary without affecting the original:

colors_copy['red'][1] = '#f00'
print(colors_copy)
# {'red': ['#ff0000', '#f00'], 'green': ['#00ff00', '#00FF00'], 'blue': ['#0000ff', '#0000FF']}

print(colors)
# {'red': ['#ff0000', '#FF0000'], 'green': ['#00ff00', '#00FF00'], 'blue': ['#0000ff', '#0000FF']}


'''
In contrast, if you use the copy() method of a dictionary to create a shallow copy, 
the changes to mutable objects will be reflected in both the original and the copy.
'''

colors_copy = colors.copy()
colors_copy['red'][1] = '#f00'
print(colors_copy)
# {'red': ['#ff0000', '#f00'], 'green': ['#00ff00', '#00FF00'], 'blue': ['#0000ff', '#0000FF']}

print(colors)
# {'red': ['#ff0000', '#f00'], 'green': ['#00ff00', '#00FF00'], 'blue': ['#0000ff', '#0000FF']}


'''
The deepcopy() function is useful when you want to create a completely independent copy of an object, including all of its nested objects. 

It is especially useful for making copies of objects that contain mutable  objects, such as lists or dictionaries, as the changes to the mutable objects in the copy will not be reflected in the original.
'''

***

'''
🔷 The copy() method returns a shallow copy of a dictionary.
A shallow copy is a new dictionary that has the same keys as
the original, but the values in the new dictionary are references
to the values in the original dictionary.
'''

colors = {'red': '#ff0000', 'green': '#00ff00', 'blue': '#0000ff'}
colors_copy = colors.copy()
colors_copy
# output: {'red': '#ff0000', 'green': '#00ff00', 'blue': '#0000ff'}


'''
You can modify the values in the new dictionary without affecting the original:

>>> colors_copy['red'] = '#FF0000'
>>> colors_copy
{'red': '#FF0000', 'green': '#00ff00', 'blue': '#0000ff'}
>>> colors
{'red': '#ff0000', 'green': '#00ff00', 'blue': '#0000ff'}


However, if you modify a mutable object (such as a list or a dictionary) that is used as a value in the original dictionary, the changes will be reflected in both the original and the copy:
'''

colors = {'red': ['#ff0000', '#FF0000'], 'green': ['#00ff00', '#00FF00'], 'blue': ['#0000ff', '#0000FF']}
colors_copy = colors.copy()

colors_copy['red'][1] = '#f00'
colors_copy
{'red': ['#ff0000', '#f00'], 'green': ['#00ff00', '#00FF00'], 'blue': ['#0000ff', '#0000FF']}

colors
{'red': ['#ff0000', '#f00'], 'green': ['#00ff00', '#00FF00'], 'blue': ['#0000ff', '#0000FF']}


'''
This behavior is known as aliasing, and it occurs because the values in the new dictionary are references to the values in the original dictionary, rather than copies of the values. To create a deep copy, which is a new dictionary with copies of the values in the original dictionary, you can use the deepcopy() function from the copy module 
in the Python standard library.
'''


***

'''
🔷 The keys() method returns a view object that displays a list of all the keys
in a dictionary. The view object is dynamic and reflects any changes made
to the dictionary.
'''

colors = {'red': '#ff0000', 'green': '#00ff00', 'blue': '#0000ff'}
keys = colors.keys()
print(keys)  # dict_keys(['red', 'green', 'blue'])

'''
The view object returned by keys() is an iterable, so you can use it in a 
loop or pass it to a function that expects an iterable, such as list() or 
sorted().
'''

# print the keys in sorted order
for key in sorted(colors.keys()):
    print(key)

# create a list of keys
key_list = list(colors.keys())
print(key_list)  # ['red', 'green', 'blue']


'''
Note that the keys() method does not return a list, but rather a view 
object that displays the keys of the dictionary. If you want to create 
a list of the keys, you can pass the view object to the list() function.

The view object returned by keys() is dynamic, which means that it 
reflects any changes made to the dictionary. For example, if you 
add or remove a key-value pair from the dictionary, the view 
object will be updated to reflect the change.
'''

# add a key-value pair to the dictionary
colors['black'] = '#000000'
keys = colors.keys()
print(keys)  # dict_keys(['red', 'green', 'blue', 'black'])

# remove a key-value pair from the dictionary
del colors['red']
keys = colors.keys()
print(keys)  # dict_keys(['green', 'blue', 'black'])


'''
If you want a snapshot of the keys in the dictionary at a particular point in 
time, you can use the dict.keys() method to create a list of the keys.
'''

key_list = list(colors.keys())
print(key_list)  # ['green', 'blue', 'black']



***

🔷 '''
The values() method of a dictionary returns a view object that displays a
list of all the values in the dictionary. You can access the values of
the dictionary by iterating over the view, or by converting the view into a list.
'''


my_dict = {'a': 1, 'b': 2, 'c': 3}

for value in my_dict.values():
    print(value)

# Output:
# 1
# 2
# 3

# You can also convert the view into a list using the list() function:


values = list(my_dict.values())
print(values)  # [1, 2, 3]

'''
Note that the order of the values in the view is not guaranteed to be 
the same as the order they were added to the dictionary. 
If you need to preserve the order of the values, you can use an OrderedDict instead.
'''



***

🔷 '''
The items() method returns a view object that displays a list of the
key-value pairs in a dictionary. The view object is dynamic and
reflects any changes made to the dictionary.
'''

colors = {'red': '#ff0000', 'green': '#00ff00', 'blue': '#0000ff'}
items = colors.items()
print(items)
# dict_items([('red', '#ff0000'), ('green', '#00ff00'), ('blue', '#0000ff')])

'''
The view object returned by items() is an iterable, so you can use it in a 
loop or pass it to a function that expects an iterable, such as list() or sorted().
'''

# print the key-value pairs in sorted order
for key, value in sorted(colors.items()):
    print(f"key: {key} => value: {value}")

# create a list of key-value pairs
item_list = list(colors.items())

print(item_list)
# [('red', '#ff0000'), ('green', '#00ff00'), ('blue', '#0000ff')]


'''
Note that the items() method does not return a list, but rather a view 
object that displays the key-value pairs of the dictionary. If you want 
to create a list of the key-value pairs, you can pass the view object 
to the list() function.

The view object returned by items() is dynamic, which means that it 
reflects any changes made to the dictionary. For example, if you add 
or remove a key-value pair from the dictionary, the view object will 
be updated to reflect the change.
'''


# add a key-value pair to the dictionary
colors['black'] = '#000000'
items = colors.items()
print(items)  # dict_items([('red', '#ff0000'), ('green', '#00ff00'), ('blue', '#0000ff'), ('black', '#000000')])

# remove a key-value pair from the dictionary
del colors['red']
items = colors.items()
print(items)  # dict_items([('green', '#00ff00'), ('blue', '#0000ff'), ('black', '#000000')])


'''
If you want a snapshot of the key-value pairs in the dictionary at a 
particular point in time, you can use the dict.items() method to 
create a list of the key-value pairs.
'''

item_list = list(colors.items())
print(item_list)  # [('green', '#00ff00'), ('blue', '#0000ff'), ('black', '#000000')]





***

🔷 

