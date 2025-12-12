# taking input from the user 
n = int(input("Enter the number: "))

# to find the sum of digits of a number 
sum =0
while(n != 0):
    s = n%10
    sum += s
    n //= 10
print("Sum of digits is: ",sum)
