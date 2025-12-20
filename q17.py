# assume 
ranges = [1, 500]
l=[]
for i in range(ranges[0],ranges[1]):
    rev = 0
    f = i
    while(i != 0):
        s = i%10
        rev = rev + s**3
        i = i//10
    if f == rev:
        l.append(i)
print(l