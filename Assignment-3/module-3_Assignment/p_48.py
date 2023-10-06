# Write a Python program to returns sum of all divisors of a number 

def sum_div(number):
    for i in range(1,number):
        if number%i == 0:
            print(i)
    return i
print(sum_div())