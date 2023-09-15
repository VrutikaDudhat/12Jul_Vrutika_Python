# Write a Python function that takes a list of words and returns the length of the longest one.

s=input("Enter String :")
longest=0

for  i in s.split():
    if len(i)>longest:
        longest=len(i)
        longest_word=i

print("Longest Word is :",longest_word,",This Length is :",len(longest_word))
#print("This Length is :",len(longest_word))

 
