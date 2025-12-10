# taking inputs from the user
n = int(input("Enter the number: "))
 
# to print fibonacci series upto n.

# a = 0
# b = 1
# print(a)
# print(b)
# for i in range(n-2):
#     c = a + b
#     a = b
#     b = c
#     print(c)

# using recursion 
def fibo(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    return fibo(x-1) + fibo(x-2)
print(fibo(n-1))
