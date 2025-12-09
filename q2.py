#  for taking input from user
n = int(input("Enter a number: "))
# for checking if the number is prime or not.
if n == 0 or n == 1:
    print("The number is not prime.")
else:
    for i in range(2, n):
        if n % i == 0:
            print("The number is not prime.")
            break
    else:
        print("The number is prime.")