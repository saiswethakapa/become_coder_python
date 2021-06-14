#shuffle the array--leetcode
def sa(n,data):
    c=[]
    w=len(data)
    f=data[0:n:1]
    l=data[n:w+1:1]
    i=0
    while i<=n-1:
        c.append(f[i])
        c.append(l[i])
        i=i+1
    return c
n=int(input())
data=list(map(int,input().split()))
print(sa(n,data))
