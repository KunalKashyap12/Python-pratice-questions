# for taking the input from user.
n = int(input("Enter the numbers: "))

# for checking the number is armstrong is not
f=n
rev = 0
s = len(str(n))
while ( n !=0):
    rem = n % 10
    rev = rev + rem**s #  <= Math.pow(rem,3)
    n = n//10
# if f == rev:
#     print("Number is Armstrong")
# else:
#     print("Number is not Armstrong ")
print("Number is Armstrong" if f == rev else "Number is not Armstrong " )