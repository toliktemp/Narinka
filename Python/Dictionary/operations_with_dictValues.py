dict = {
    'a' : 1,
    'b' : 2,
    'c' : 3,
    'd' : 4,
    'e' : 5,
}

# addition
print(dict['a'] + dict['b'], ": addition of a + c")     # 3 : addition of a + c


# sum of all values
sumOfAll_Values = [sum(dict[i] for i in dict)]
print(sumOfAll_Values)          # [15]


sum_values = sum(dict.values())
print(sum_values)               # 15



#print("Calculating sum of duration")
playlist = {
    'title': 'patagonia bus',
    'author': 'colt steele',
    'songs': [
        {'title': 'kitty', 'artist': ['blue','sky'], 'duration': 2.5},
        {'title': 'pussy_cat', 'artist': ['kitty', 'djcat'], 'duration': 5.25},
        {'title': 'meowmeow', 'artist': ['garfield','sons'], 'duration': 2.0}
        ]
}

total = 0
for i in playlist['songs']:
    total = total + i['duration']
print(total)
