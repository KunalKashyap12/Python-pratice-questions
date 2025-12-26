# assume 
n = [10, 30]
l=[]
for i in range(n[0],n[1]):
    flag = True
    for j in range(2,int(i**0.5)+1):
        if i%j == 0:
            flag = False
            break
    if flag:
        l.append(i)
print(l)