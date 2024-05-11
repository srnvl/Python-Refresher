##### Dictionary in Python #####

di = {}

print("Original (Empty) Dictionary: ")
print(di)
print('\n')

di.update({211 : 27, 22 : 95, 1309 : 78})

print("Updated Dictionary: ")
print(di)
print('\n')

# Alternate Syntax: 
for key, value in di.items():
    print(key, ":", value)
print('\n')

# Get a key value from Dictionary:
print("Get me the value for key 22: ")
# print(di[2])
print("Here it is: ", di.get(22))
print('\n')

# Delete a key in Dictionary:
del(di[211])
print("Modified Dictionary: ")
print(di)

print('\n')

# Reverse a dictionary:
reversed_di = {value : key for key, value in di.items()}
print("Reversed Dictionary: ")
print(reversed_di)

print('\n')

# Sort a dictionary based on key:
sort_by_key_di = {key : value for key, value in sorted(di.items(), key = lambda item : item[0])}
print("Dictionary sorted by keys: ")
print(sort_by_key_di)

print('\n')

# Sort a dictionary based on value:
sort_by_value_di = {key : value for key, value in sorted(di.items(), key = lambda item: item[1])}
print("Dictionary sorted by values: ")
print(sort_by_value_di)

# Length of a Dictionary:
print('\n')
print("Length of the Modified Dictionary is: ", len(di))
