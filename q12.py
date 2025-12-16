# taking input from user 
# ! string not containg any special character
# to count the number of vowels and consonants
n = input("Enter the string")
countV = 0
countC = 0
for i in n.split():
    for j in i:
        if j in "aeiouAEIOU":
           countV += 1
        else:
           countC += 1
print("Vowels : ",countV)
print("Consonant : ",countC)
