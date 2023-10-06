# Write a Python program to convert a tuple to a string.

tp = ('Students', 'of', 'python')
st = ''

for item in tp:
    st = st + item

print("Given Tuple : ", tp)
print("Generated String : ", st)
print(type(st))