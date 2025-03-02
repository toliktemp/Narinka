
# Dictionary of strings and int
dictOfWords = {
    "hello": 56,
    "at" : 23 ,
    "test" : 43,
    "this" : 97,
    "here" : 43,
    "now" : 97
    }


'''
*******************************************************
Get list of keys with value 43 using list comprehension
*******************************************************
'''
listOfKeys = [key  for (key, value) in dictOfWords.items() if value == 43]




def getKyesByValue(dictOfElements, valueToFind):
    listOfKeys = list()
    listOfItems = dictOfElements.items()

    for item in listOfItems:
        if item[1] == valueToFind:
            listOfKeys.append(item[0])
    return listOfKeys

# Get list of keys with value 43

listOfKeys = getKyesByValue(dictOfWords, 43)
print("Keys with value equal to 43")

for key in listOfKeys:
    print(key)


'''
*******************************************************
Get a list of keys from dictionary which has value that 
matches with any value in given list of values
*******************************************************
'''


def getKeysByValues(dictOfElements, listOfValues):
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[1] in listOfValues:
            listOfKeys.append(item[0])
    return  listOfKeys


print("Keys with value equal to any one from the list [43, 97] ")

listOfKeys = getKeysByValues(dictOfWords, [43, 97] )
#Iterate over the list of values
for key  in listOfKeys:
    print(key)

