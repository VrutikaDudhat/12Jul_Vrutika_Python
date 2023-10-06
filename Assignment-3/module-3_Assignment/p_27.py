# Write a Python script to concatenate following dictionaries to create a new one.

def concatenate_dictionaries(*dictionaries):
    dict = {}
    for i in dictionaries:
        dict.update(i)
    return dict

# Example dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}

# Concatenate dictionaries
dict = concatenate_dictionaries(dict1, dict2, dict3)

# Print the concatenated dictionary
print(dict)