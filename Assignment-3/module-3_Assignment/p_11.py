# Write a Python program to get unique values from a list

def get_unique_values(lst):
    unique_values = []
    for item in lst:
        if item not in unique_values:
            unique_values.append(item)
    return unique_values

# Example usage
my_list = [1, 2, 3, 4, 2, 3, 5, 6, 1, 4]
unique_values = get_unique_values(my_list)
print(unique_values)
