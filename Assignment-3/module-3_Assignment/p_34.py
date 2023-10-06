# Write a Python program to print all unique values in a dictionary. 

my_dict = {"a": 1, "b": 2, "c": 3, "d": 2, "e": 4, "f": 1}
unique_values = set()

for value in my_dict.values():
    unique_values.add(value)
print("The unique values in the dictionary are:")

for value in unique_values:
    print(value)
print("The number of unique values is:", len(unique_values))