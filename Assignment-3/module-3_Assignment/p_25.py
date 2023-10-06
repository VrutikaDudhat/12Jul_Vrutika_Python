# Write a Python program to convert a list of tuples into a dictionary.

def convert_to_dictionary(lst):
    dictionary = dict(lst)
    return dictionary

# Example usage:
list_of_tuples = [("a", 1), ("b", 2), ("c", 3)]
result_dict = convert_to_dictionary(list_of_tuples)
print(result_dict)
