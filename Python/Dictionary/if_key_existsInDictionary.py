import sys

wordFreqDic = {
    "Hello": 56,
    "at" : 23 ,
    "test" : 43,
    "this" : 78
}

'''
    Check if key exists in dictionary using 'in' operator
'''
if 'test' in wordFreqDic:
    print("Yes 'test' key exists in dict ")
else:
    print("No 'test' key does not exists in dictionary")



print("**********************************")


fruits = {
    'apple':1,
    'orange':2,
    'banana':3
}

#if key 'apple' exists in fruits?
if 'apple' in fruits:
    print(fruits['apple'])


'''
    Check if key exists in dictionary using get()
'''

if wordFreqDic.get("test") != None:
    print("Yes 'test' key exists in dict ")
else:
    print("No 'test' key does not exists in dictionary")



print("**********************************")

# if key exist in another dict

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}


for key in Dict.keys():
    if key in Boys.keys():
        print(key,  " : ", end=" ")
        print (True)

    else:
        print("*" * 8)
        #print two statements in one line
        print(key, " : ", end=" ")
        print (False)
        print("*" * 8)


'''
Tim  :  True
Charlie  :  True
********
Tiffany  :  False
********
Robert  :  True
'''
