# taking input from user
n = input("Enter String: ")

# to check the string is palindrome or not

# using slicing operations

# print("Palindrome") if n == n[-1::-1] else print("Not Palindrome")

# using for loop

s=""
for i in range(len(n)-1,-1,-1):
    s += n[i]

print("Palindrome") if n == s else print("Not Palindrome")

