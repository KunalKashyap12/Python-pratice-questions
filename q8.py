# taking input from the user 
n = int(input("Enter the number: "))

# to find the factorial of n. => by using loop
# fact = 1
# for i in range(n,0,-1):
#     fact *= i
# print("Factorial of ",n,"=",fact)

def fact(x):
    if x == 0:
        return 1
    return x * fact(x-1)

print("Factorial of ",n,"=",fact(n))