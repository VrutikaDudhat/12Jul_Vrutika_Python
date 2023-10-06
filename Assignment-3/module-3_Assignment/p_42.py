# Write a Python function that checks whether a passed string is palindrome or no.

def isPalindrome(s):
    return s == s[::-1]
 
s = "Rajkot"
ans = isPalindrome(s)
 
if ans:
    print("Yes...")
else:
    print("No...")

# ------------------------- #

"""s="Vrutika"

ans=s[::-1]
print(ans)

if ans==s:
    print("yes...")
else:
    print("no...")"""