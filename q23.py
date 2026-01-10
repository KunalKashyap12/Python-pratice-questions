# taking user inputs
x = int(input("Enter Position"))
# function to return fibonacci number at a specific position
def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)

print(fibo(x-1))