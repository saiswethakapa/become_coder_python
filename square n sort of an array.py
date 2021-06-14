#leet square of an array
data=list(map(int,input().split()))
n=len(data)
a=[]
for i in range(n):
    b=data[i]**2
    a.append(b)
print(a.sort())
