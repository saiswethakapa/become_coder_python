def sod(data):
    s=0
    a=[]
    for i in data:
        while i:
            r=i%10
            i//=10
            s=s+r
        a.append(s)
        s=0
    return a
n=int(input())
data=list(map(int,input().split()))
print(*sod(data))
