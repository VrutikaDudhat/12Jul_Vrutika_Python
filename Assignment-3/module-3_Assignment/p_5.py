# Write a Python function that takes two lists and returns true if they have at least one common member. 

def common_member(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
print(common_member(list1, list2))  # False

list3 = [4, 5, 6, 7, 8]
print(common_member(list1, list3))  # True

