# taking input from user
# returing the max and min of an array
x = int(input("Enter the size of array"))
list = []
for i in range(x):
    n = int(input())
    list.append(n)
max = list[0]
min = list[0]
for i in list:
    if max<i:
        max = i
    if min>i:
        min = i
print("Max is: ",max)
print("Min is: ",min)