# taking user inputs
# to check the number is perfect is or not
n = int(input("Enter the number"))
c = 0
for i in range(1,n):
    if n % i ==0:
        c += i
if c == n:
    print("Perfect number")
else:
    print("Not perfect")