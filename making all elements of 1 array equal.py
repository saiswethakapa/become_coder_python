#challenge    
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
cnt=0
s=min(a)
for i in range(n):
    if a[i]==s:
        c.append(a[i])
    elif a[i]>s:
        while a[i]>=s:
            a[i]=a[i]-b[i]
            cnt=cnt+1
            if a[i]==s:
                break
        c.append(a[i])
print(c)
d=0
for i in range(n-1):
    if c[i]==c[i+1]:
        d=d+1
if d==n-1:
    print(cnt)
else:
    print(-1)
