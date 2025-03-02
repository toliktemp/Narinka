
# Dictionary of string and int
wordFreqDic = {
    "Hello": 56,
    "at"   : 23,
    "test" : 43,
    "this" : 2,
    "here" : 23,
    "city" : 2,
    }


# Create a new list from the view object returned by values()
dictValues = list (wordFreqDic.values())

print("List of values in Dictionary : ", dictValues)



'''
*************************************************
Creating a list of dulicate values in dictionary
*************************************************
'''
uniqueValues = list()
duplicateValues = list()

# Creating a list of all duplicate values in dictionary
for x in wordFreqDic.values() :
    if x not in uniqueValues :
        uniqueValues.append(x)
    else:
        duplicateValues.append(x)

print("List of Duplicate values in Dictionary" , duplicateValues)
