# Write a Python program to check whether a list contains a sub list

def is_sublist(list1, sublist):
    n = len(sublist)
    return any(sublist == list1[i:i+n] for i in range(len(list1) - n + 1))

# Example usage
main_list = [1, 2, 3, 4, 5, 6, 7]
sub_list = [2,3,4]

if is_sublist(main_list, sub_list):
    print("The sublist is present in the main list.")
else:
    print("The sublist is not present in the main list.")
