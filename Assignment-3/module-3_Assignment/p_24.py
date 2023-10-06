# Write a Python program to unzip a list of tuples into individual lists.

def unzip_tuples(tuples):
    unzipped_lists = list(zip(*tuples))
    return unzipped_lists

# Example usage
tuples_list = [(1, 'a'), (2, 'b'), (3, 'c')]
result = unzip_tuples(tuples_list)

print(result)