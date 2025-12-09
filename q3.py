# for taking input from user
n = int(input("Enter a year: "))
# for checking if the year is leap or not.
if (n%4==0 and n%100 != 0) or ( n%400 ==0):
    print("The year is a leap year.")
else:
    print("The year is not a leap year.")   
