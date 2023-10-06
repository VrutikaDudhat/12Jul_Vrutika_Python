# Write a Python program to reverse a tuple.

def tuple(t):
    if len(t) == 0:
        return t
    else:
        return(t[-1],)+tuple(t[:-1])
    
original_tuple = ('z','a','d','f','g','e','e','k')
reversed_tuple = tuple(original_tuple)

print("Original Tuple: ", original_tuple)
print("Reversed Tuple: ", reversed_tuple)


# ------------------------------------- #

"""values = (1, 2, 'Python', 'Java', 23.4, 77, 10)  
print("The original tuple is : ", values)  
  
values = values[::-1]  
print("The reversed tuple is : ", values)""" 