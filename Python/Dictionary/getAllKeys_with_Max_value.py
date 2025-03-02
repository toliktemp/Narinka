
# Create a dictionary of string and int
sampleDict = {
    'Ritika': 5,
    'Sam': 27,
    'John' : 10,
    'Sachin' : 14,
    'Mark' : 19
}


# Find Key with Max Value
itemMaxValue = max(sampleDict.items(), key=lambda x : x[1])

print('Max value in Dict: ', itemMaxValue[1])
print('Key With Max value in Dict: ', itemMaxValue[0])


listOfKeys = list()
# Iterate over all the items in dictionary to find keys with max value
for key, value in sampleDict.items():
    if value == itemMaxValue[1]:
        listOfKeys.append(key)

print('Keys with maximum Value in Dictionary : ', listOfKeys)
