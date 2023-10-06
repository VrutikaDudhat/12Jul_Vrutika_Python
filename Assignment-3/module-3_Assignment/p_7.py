# Write a Python function that takes a list and returns a new list with unique elements of the first list. 

def unique(input_list):
    return list(set(input_list))


l = [1, 2, 2, 3, 4, 4, 5]
unique_elements = unique(l)
print(unique_elements)
