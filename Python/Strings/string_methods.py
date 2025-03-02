str = "Hello, World!"

# first char 
print(str[0])       # H

# second char
print(str[1])       # e

# last char
print(str[-1])      # !

print(str[-2])      # d
print(str[:3])      # Hel
print(str[3:])      # lo, World!
print(str[:])       # Hello, World!
print(str[::2])     # Hlo ol!

# reverse string
print(str[::-1])    # !dlroW ,olleH

txt = "Hello World!"[::-1]
print(txt)          # !dlroW olleH

# an example of how to use the len() function to get the last character in a string:
string = "Hello, World!"
last_char = string[len(string) - 1]
print(last_char)


# Slicing
str = 'Hello, World!'

# Grab everything past the first term all the way to the length of s which is len(s)
print(str[1:])

# Grab everything UP TO the 3rd index
print(str[:3])

#Everything
str[:]

# Last letter (one index behind 0 so it loops back around)
str[-1]

# Grab everything but the last letter
str[:-1]

# Grab everything, but go in steps size of 1
str[::1]

# Grab everything, but go in step sizes of 2
str[::2]

# We can use this to print a string backwards
str[::-1]




# Concatenation two strings
str = "Hello "
str1 = "Python"
str3 = str + str1
print(str3)         # Hello Python

a = "Hello"
b ="Python"
print(a+b)          # HelloPython

c = '3'
d = '45'
print(c + d)        # 345


# Repetition : concatenating multiple copies of the same string
str = 'Hello'
print(str * 5)      # HelloHelloHelloHelloHello


# index()
str = "green ideas"
print(str.count('d'))       # 1
print(str.count('id'))      # 1
print(str.count('e'))       # 3

# replace()
str1 = " Hello Pyton "
b = str1.replace("H", "J")      #  Jello Pyton

str2 = "Colorless green ides sleep furiously"
c = str2.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '')
print(c)            # Clrlss grn ds slp frsly


# split()
str2 = "Hello, Pyton!"
c = str2.split(",")
print(c)            # ['Hello', ' Pyton!']
print(c[0])         # Hello

# Split a string by blank space (this is the default)
print(s.split())

# Split by a specific element (doesn't include the element that was split on)
s.split('W')



# join
'''
    The method join() returns a string in which the string elements
    of sequence have been joined by str separator.
    '''
s = " - "
seq = ('a','b','c')
print(s.join(seq))      # a - b - c


# len()
print(len(str2))       # 13


# lower()
print(str.lower())      # hello, world!


# upper()               # HELLO, WORLD!
print(str.upper())


# startswith()
str = "school"
print(str.startswith('s'))      # True
print(str.startswith('scho]'))
print(str.startswith('k'))      # False


# endswith()
str = "school"
print(str.endswith('l'))        # True
print(str.endswith('ll'))       # False
print(str.endswith('ol'))       # True


# count()
str = "colorless green ideas sleep furiously"
print(str.count('s'))       # 5
print(str.count('ee'))      # 2


# capitalize()
print(str.capitalize())     # Colorless green ideas sleep furiously


# title()
print(str.title())          # Colorless Green Ideas Sleep Furiously


# strip()
str = "\thello world\n \n"
print(str.strip())          # hello world

str1 = "  Hello World!   "
print(str1.strip())         # Hello World!


# find()
str = " green ideas"
print(str.find('e'))        # 3
print(str.find('th'))       # -1
'''
    if the substring is not found,
    pyton return -1 instead of producing an error.
    '''
txt = "Hello, welcome to my world."
x = txt.index("welcome")


# isalpha() alphabetic (A-Z, a-z)
str = 'iPad'
print(str.isalpha())        # True


# isalnum() alpha-numeric (A-Z, a-z, 0-9)
str = 'Homework3'
print(str.isalnum())        # True


# isdigit() numeric (0-9)
str = "2014"
print(str.isdigit())        # True

str = '9:30'
print(str.isdigit())       # False


# islower() lowercase (a-z)
str = 'apple'
print(str.islower())        # True


# .isupper()    uppercase (A-Z)
str = "HELLO"
print(str.isupper())        # True

str = "Hello"
print(str.isupper())        # False


# .isspace()    whitespace character:     ' ', '\n', '\t', '\r'
str = "\t \r \n"
print(str.isspace())        # True

str = "A b c1 12"           # False
print(str.isspace())


'''
    strings do not have a designated method : < IN >,
    but the versatile in operator can be used.
    Because in is not a string METHOD, it uses a different syntax of y in x:
    '''

str = "school"
if 'oo' in str:
    print("Yes, 'oo' in string ")   # Yes, 'oo' in string

if 'h' in str:
    print("Yes, 'h' in string")     # Yes, 'h' in string

if 'school' in str:
    print("Yes, 'school' in string")    # Yes, 'school' in string

if 'k' in str:
    print("Yes 'k' in string")
else:
    print("No 'k' not in string")   # No 'k' not in string


if 'j' not in str:
    print("Yes 'j' not in string <school>")
else:
    print("No j in string")


# zfill()
# The method zfill() pads string on the left with zeros to fill width.
str = "this is string example!!!";
print(len(str))     # 25

a = str.zfill(40)
print(len(a))       # 40


# center()
'''
    returns centered in a string of length width.
    Padding is done using the specified fillchar.
    Default filler is a space.
    Syntax
    str.center(width[, fillchar])
    '''

str = "this is string example....wow!!!"
print("str.center(40, 'a') : ", str.center(40, 'a'))
# str.center(40, 'a') :  aaaathis is string example....wow!!!aaaa

